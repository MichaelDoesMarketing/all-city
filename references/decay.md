# Decay

Published work does not stay still. It stays exactly where it was while everything around it moves, which is a different thing.

Decay is not age. A piece from five years ago making a claim that is still true, still ranking, still sending people somewhere useful, is an asset and scoring it down for age is a mistake this skill should never make.

What follows is the list of ways a live surface actually goes bad.

## The kinds

**Factually wrong now.** A price, a headcount, a feature, a location, a title, a client list. The most damaging kind, because a stranger has no way to know it is old and will act on it.

**Superseded.** Two pages make different claims and the newer one is correct. The problem is that the reader has no idea which is newer, and search often prefers the older one because it has more links.

**Orphaned.** Nothing on the site links to it anymore. It is reachable only from search or an old bookmark. These are invisible to the owner and completely visible to everyone else.

**Dated by reference.** No explicit date, but it talks about something in a way that places it. A tool that no longer exists, a company that was acquired, a platform name that changed, "this year" with no year, a trend that resolved.

**Dated by absence.** The reverse, and more common. A bio listing four achievements, none from the last two years. Nothing on the page is wrong. The shape of it says the person stopped.

**Broken in form.** Images missing, embeds dead, links 404, layout collapsed on phones, a form submitting to an address nobody reads. The content is fine and the surface is unusable.

**Invisible.** It loads and shows nothing to anything that does not run JavaScript. Looks perfect to its owner, returns an empty shell to a crawler, a link preview, or a scraper. The owner is the last person who will ever notice this.

**Mis-attributed.** Metadata crediting the wrong account, the wrong author, or the platform that built it. Shows up in link preview cards, where the card credits a tool or a template rather than the person.

**Abandoned but ranking.** A profile on a platform they stopped using. Still indexed, still first page, still carrying a two-role-ago bio.

## Finding it

The mechanical part is in `scripts/surfacecheck.py`. It catches dead pages, redirects, missing descriptions, pages that render nothing without JavaScript, and the newest year appearing on a page.

The rest is reading. Specifically:

1. **Read the About and bio text on every surface, out loud.** Decay by absence is audible and invisible on a checklist
2. **Check every claim with a number in it.** Prices, counts, years of experience, client totals. Numbers are the first thing to go stale and the last thing anyone edits
3. **Paste each URL into a chat app** and look at the card. That is a surface and it fails silently
4. **Search for the brand or person and read the result text**, not the page. The snippet is what people read
5. **Sort owned pages by last edit** if that is available. The bottom of that list is where the problems are

## The buff

Graffiti has a city crew that paints over work on a schedule. Marketing has no such thing, which is the actual problem. Nothing gets removed unless somebody decides to remove it, so everything accumulates.

The mode called **the buff** is a decay-only pass. Run it when someone is about to be looked up on purpose: before an interview, a launch, a raise, a press cycle, a conference. The question is narrow. What is up right now that would be a problem if the person who matters found it first.

It is not a full audit and should not try to be. Speed is the point.

## What decay is not

**Not a reason to delete history.** Dated writing that was true when published and is clearly of its moment is fine. Blogs are allowed to be archives.

**Not a reason to rewrite a voice.** Early work sounding less polished is not decay. Leave it.

**Not an excuse to suppress something unflattering and true.** Covered in `verdicts.md`. The answer there is never removal.
