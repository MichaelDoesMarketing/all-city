#!/usr/bin/env python3
"""
surfacecheck.py - checks every live surface carrying your name.

Fetches each URL and reports whether it is up, where it actually lands, what it
says you do, whether it renders without JavaScript, and how old it looks. Then
it lines up every surface's self-description side by side, which is where the
contradictions become impossible to argue with.

Usage:
    python3 surfacecheck.py urls.txt
    python3 surfacecheck.py https://example.com https://example.com/about
    cat urls.txt | python3 surfacecheck.py
    python3 surfacecheck.py urls.txt --json
    python3 surfacecheck.py urls.txt --hand        (self-descriptions only)

urls.txt takes one URL per line. A line may be "Label<TAB>URL" or
"Label | URL" to name the surface. Blank lines and # comments are ignored.

No dependencies. Python 3.8+.

This reports what a crawler sees. A page that fails NO-RENDER may look perfect
in your browser and still be invisible to anything that does not run scripts,
which includes most previews, scrapers and some search indexing. Verify in a
browser before acting on that flag.
"""

import datetime
import html
import json
import re
import ssl
import sys
import urllib.error
import urllib.request
from html.parser import HTMLParser

UA = "Mozilla/5.0 (compatible; surfacecheck/1.0; +https://github.com/MichaelDoesMarketing/all-city)"
TIMEOUT = 20
MAX_BYTES = 2_000_000

# Tags whose contents are not visible text.
INVISIBLE = {"script", "style", "noscript", "template", "svg", "head"}


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = ""
        self.meta = {}
        self.h1 = []
        self.text = []
        self._stack = []
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        self._stack.append(tag)
        a = dict(attrs)
        if tag == "title":
            self._in_title = True
        elif tag == "meta":
            key = (a.get("name") or a.get("property") or "").lower()
            if key and a.get("content"):
                self.meta.setdefault(key, a["content"].strip())
        elif tag == "link" and (a.get("rel") or "").lower() == "canonical":
            self.meta.setdefault("canonical", (a.get("href") or "").strip())

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        self._stack.pop()

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        while self._stack:
            popped = self._stack.pop()
            if popped == tag:
                break

    def handle_data(self, data):
        if self._in_title:
            self.title += data
            return
        if any(t in INVISIBLE for t in self._stack):
            return
        s = data.strip()
        if not s:
            return
        self.text.append(s)
        if "h1" in self._stack:
            self.h1.append(s)


def norm(u):
    """Normalize for comparing requested vs final URL. Ignores scheme,
    www, trailing slash and case in the host."""
    u = re.sub(r"^https?://", "", u.strip(), flags=re.I)
    u = re.sub(r"^www\.", "", u, flags=re.I)
    return u.rstrip("/").lower()


def fetch(url):
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept": "text/html,application/xhtml+xml,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
    })
    ctx = ssl.create_default_context()
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx) as r:
            raw = r.read(MAX_BYTES)
            return {
                "status": r.status,
                "final": r.geturl(),
                "headers": {k.lower(): v for k, v in r.headers.items()},
                "body": raw,
                "error": None,
            }
    except urllib.error.HTTPError as e:
        try:
            raw = e.read(MAX_BYTES)
        except Exception:
            raw = b""
        return {
            "status": e.code,
            "final": e.geturl() if hasattr(e, "geturl") else url,
            "headers": {k.lower(): v for k, v in (e.headers or {}).items()},
            "body": raw,
            "error": None,
        }
    except Exception as e:
        return {"status": None, "final": url, "headers": {}, "body": b"",
                "error": f"{type(e).__name__}: {e}"}


YEAR = re.compile(r"\b(20[0-3][0-9])\b")


def analyze(label, url):
    r = fetch(url)
    out = {
        "label": label, "url": url, "final": r["final"], "status": r["status"],
        "error": r["error"], "flags": [], "title": "", "description": "",
        "h1": "", "og_title": "", "canonical": "",
        "text_chars": 0, "script_chars": 0, "newest_year": None,
        "server_date": r["headers"].get("last-modified", ""),
        "content_type": r["headers"].get("content-type", ""),
    }

    if r["error"]:
        out["flags"].append("UNREACHABLE")
        return out

    if r["status"] and r["status"] >= 400:
        out["flags"].append("BLOCKED" if r["status"] in (401, 403, 429, 999) else "DEAD")

    body = r["body"].decode("utf-8", errors="replace")
    out["script_chars"] = sum(len(m) for m in re.findall(r"<script[^>]*>(.*?)</script>", body, re.S | re.I))

    p = Page()
    try:
        p.feed(body)
    except Exception:
        pass

    out["title"] = html.unescape(" ".join(p.title.split()))[:300]
    desc = p.meta.get("description") or p.meta.get("og:description") or ""
    out["description"] = html.unescape(" ".join(desc.split()))[:400]
    out["h1"] = html.unescape(" ".join(" ".join(p.h1[:1]).split()))[:200]
    out["og_title"] = html.unescape(" ".join((p.meta.get("og:title") or "").split()))[:300]
    out["canonical"] = p.meta.get("canonical", "")

    text = " ".join(p.text)
    out["text_chars"] = len(text)

    years = [int(y) for y in YEAR.findall(text)]
    now = datetime.date.today().year
    years = [y for y in years if y <= now]
    out["newest_year"] = max(years) if years else None

    # Flags
    if norm(out["final"]) != norm(url) and "DEAD" not in out["flags"]:
        out["flags"].append("MOVED")
    if out["status"] and out["status"] < 400:
        if out["text_chars"] < 500 and out["script_chars"] > 2000:
            out["flags"].append("NO-RENDER")
        elif out["text_chars"] < 250:
            out["flags"].append("THIN")
        if not out["description"]:
            out["flags"].append("NO-DESC")
        if out["newest_year"] and out["newest_year"] < now - 1:
            out["flags"].append(f"STALE({out['newest_year']})")
    return out


# ------------------------------------------------------------------ reporting

def describe(r):
    """The one line this surface would tell a stranger."""
    return r["description"] or r["og_title"] or r["h1"] or r["title"] or ""


def report(rows, hand_only=False):
    out = []
    now = datetime.date.today().isoformat()
    out.append("ALL CITY / SURFACE CHECK")
    out.append("=" * 72)
    out.append(f"{len(rows)} surfaces checked, {now}")
    out.append("")

    if not hand_only:
        for i, r in enumerate(rows, 1):
            head = f"{i:>2}. {r['label'] or r['url']}"
            out.append(head)
            out.append("    " + r["url"])
            if norm(r["final"]) != norm(r["url"]):
                out.append(f"    -> lands on {r['final']}")
            status = r["status"] if r["status"] is not None else "no response"
            bits = [f"status {status}", f"{r['text_chars']} chars of text"]
            if r["newest_year"]:
                bits.append(f"newest year on page {r['newest_year']}")
            out.append("    " + " | ".join(bits))
            if r["error"]:
                out.append(f"    error: {r['error']}")
            if r["title"]:
                out.append(f"    title: {r['title'][:90]}")
            d = describe(r)
            out.append(f"    says:  {d[:90] if d else '(nothing)'}")
            out.append(f"    FLAGS: {' '.join(r['flags']) if r['flags'] else 'none'}")
            out.append("")

    out.append("HOW EACH SURFACE DESCRIBES YOU")
    out.append("-" * 72)
    out.append("Read these as a set. A stranger sees exactly one of them, at random.")
    out.append("")
    seen = {}
    for r in rows:
        d = describe(r).strip()
        name = r["label"] or r["url"]
        if not d:
            out.append(f"  {name}")
            out.append(f"      (says nothing about you)")
            out.append("")
            continue
        seen.setdefault(d.lower()[:120], []).append(name)
        out.append(f"  {name}")
        out.append(f"      \"{d[:160]}\"")
        out.append("")

    distinct = len(seen)
    out.append(f"  {distinct} distinct descriptions across {len(rows)} surfaces.")
    if distinct > 1:
        out.append("  Every one of these is somebody's first and only impression.")
    out.append("")

    if hand_only:
        return "\n".join(out)

    out.append("SUMMARY")
    out.append("-" * 72)
    counts = {}
    for r in rows:
        for f in r["flags"]:
            key = f.split("(")[0]
            counts[key] = counts.get(key, 0) + 1
    if counts:
        for k in sorted(counts, key=lambda x: -counts[x]):
            out.append(f"  {k:<12} {counts[k]}")
    else:
        out.append("  No flags. Everything up, rendering and described.")
    out.append("")
    out.append("  NO-RENDER means a crawler got almost no text. Check it in a browser")
    out.append("  before acting. MOVED, DEAD and BLOCKED are what a stranger hits.")
    out.append("")
    out.append("This script reports what is up. It does not decide what stays.")
    out.append("Give every surface a verdict by hand: KEEP, FIX or BURY.")
    out.append("")
    return "\n".join(out)


def read_targets(args):
    paths = [a for a in args if not a.startswith("--")]
    urls = [p for p in paths if p.startswith(("http://", "https://"))]
    files = [p for p in paths if p not in urls]

    lines = []
    if files:
        for f in files:
            try:
                with open(f, "r", encoding="utf-8") as fh:
                    lines.extend(fh.read().splitlines())
            except OSError as e:
                sys.stderr.write(f"surfacecheck: cannot read {f}: {e}\n")
                return None
    elif urls:
        lines = urls
    else:
        lines = sys.stdin.read().splitlines()

    targets = []
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        label, url = "", line
        for sep in ("\t", " | ", "|"):
            if sep in line:
                label, url = line.split(sep, 1)
                label, url = label.strip(), url.strip()
                break
        if not url.startswith(("http://", "https://")):
            url = "https://" + url
        targets.append((label, url))
    return targets


def main():
    args = sys.argv[1:]
    targets = read_targets(args)
    if targets is None:
        return 1
    if not targets:
        sys.stderr.write("surfacecheck: no URLs given.\n")
        return 1

    rows = [analyze(label, url) for label, url in targets]

    if "--json" in args:
        print(json.dumps(rows, indent=2))
    else:
        print(report(rows, hand_only="--hand" in args))
    return 0


if __name__ == "__main__":
    sys.exit(main())
