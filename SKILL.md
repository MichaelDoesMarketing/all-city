---
name: all-city
description: Audit everything currently published under a name, as a set, and decide what stays. Use when someone asks what comes up when you google them or their company, when old pages are still live, when bios and taglines disagree across profiles, when a site is not showing up, when a rebrand or a name change leaves things behind, when someone is job hunting or fundraising and wants their presence to hold up, or when they say their online presence is a mess and they do not know where to start.
---

# All City

Every skill that operates on one artifact assumes the artifact is what people will see. Usually it is not. People arrive through whatever they happen to land on, which is almost never the thing being maintained this week.

This works on the whole standing body of work instead. Everything live right now that carries the name. Not the plan, not the next launch. What is up.

Most people have never listed it. That is the job.

Use the logic, do not perform the frame. Nothing in the output talks about graffiti, tags, or walls unless the user asks where the method comes from.

## The rule that protects this skill

**Nothing goes on the list unverified.**

Every surface in the inventory needs a URL that was actually opened and a note on what was found there. Not "you probably have a Crunchbase page." Not "there's likely an old About page." A confident inventory of surfaces that were never checked is worse than no inventory, because the user will act on it.

Applied, that means:

- A surface that cannot be opened is recorded as unverified, with the reason, and never given a verdict
- A surface found through search is not verified until it has been opened
- When a page cannot be reached, say which one and why, rather than describing what is probably on it
- Never assert what a blocked page says. Blocked is the finding
- Never recommend burying something that has not been looked at

If most of the inventory could not be verified, say so plainly and deliver a short honest list instead of a long confident one.

## Step 1: Build the inventory

Ask for what the user knows about, then go find the rest. People consistently forget the surfaces other people put up.

Start with what they name, then work through `references/surfaces.md`, which lists the categories that get missed: syndicated copies, speaker and podcast pages, directory and data-broker listings, old subdomains, app store entries, archived campaign pages, co-authored posts, and anything a former employer still hosts.

Then search the way a stranger would. Their name, their company, their name plus the category, the thing they want to be known for. Record what comes back and in what order. That order is data, and it is the input to Step 4.

Mark each surface as **owned** (they can edit it), **claimed** (they control an account on someone else's platform) or **third-party** (they cannot change it). The verdict rules differ for each.

## Step 2: Check what each one actually does

Run the script. It is in `scripts/surfacecheck.py`, needs nothing installed, and takes a file of URLs or a list of them.

```
python3 scripts/surfacecheck.py urls.txt
python3 scripts/surfacecheck.py https://example.com https://example.com/about
python3 scripts/surfacecheck.py urls.txt --hand     # self-descriptions only
python3 scripts/surfacecheck.py urls.txt --json
```

Each line of the file can be `Label | URL` to name the surface.

It reports, per surface: whether it loads, where it actually lands after redirects, the title and description, how much text a crawler sees, whether the page needs JavaScript to say anything, and the newest year on the page. Then it lines up every surface's self-description in one block.

That last part is the one that changes minds. Eleven different answers to "what do you do," side by side, is not an argument anyone wins.

**Read the flags carefully.** `NO-RENDER` means a crawler got almost nothing, which usually means a client-rendered app. The page may look perfect in a browser and still be invisible to link previews, scrapers and some indexing. Confirm in a browser before telling someone their site is broken.

If the script cannot run, open the surfaces by hand and record the same fields. Say that the numbers were gathered by hand.

## Step 3: Score the surface

Four axes, 1 to 5. Score the body of work, not the individual pages.

- **Coverage** - when someone looks for them, or for what they do, is there something of theirs there. Gaps matter more than quality
- **Decay** - how much of what is up is stale, wrong, or contradicted by something newer
- **Hand** - how consistently the surfaces describe the same person or company. A writer's tag is identical everywhere; most people's is not
- **Order** - whether the things people hit first are the things they would choose

Score Order last, because it depends on the search results from Step 1 rather than on any single page.

`references/order.md` covers why first contact is rarely the homepage.

## Step 4: Give every surface a verdict

Three options. No fourth, and no "monitor."

- **KEEP** - it works, it is current, leave it alone. Say why, so the list is not only bad news
- **FIX** - it earns its place but says the wrong thing, is stale, or is broken. Name the specific change
- **BURY** - take it down, redirect it, or deindex it

`references/verdicts.md` has the decision rules, including what to do about third-party surfaces that cannot be buried, where the move is to outrank rather than remove.

**BURY is the one that matters.** People will rewrite a dead page forever rather than delete it. A surface with no traffic, no current claim, and no link value is costing maintenance and diluting everything else. Recommend removal and mean it.

For anything third-party, never recommend contacting a publisher to remove a true, unflattering article. That is not what this is for. The move is to publish something better and let it rank.

## Step 5: Fix the hand before making anything new

**No new work until the contradictions are resolved.**

This is deliberately unwelcome, because making a new thing is more fun than fixing the bio on a profile nobody has opened in two years. It is still correct. A new piece landing on a surface that argues with itself is wasted, and the contradiction is what the reader remembers.

Settle on one claim. Then push it to every owned and claimed surface in the same pass. `references/hand.md` covers what has to match and what is allowed to vary by platform.

## Modes

**All city** - the default. Inventory, check, score, verdict, fix the hand.

**First ten** - the fast uncomfortable one. Search the way a stranger would and report the first ten things they hit, in order, with nothing else. No recommendations. The order is the finding.

**The buff** - decay only. Everything still up that is stale, wrong, or embarrassing. Use when someone is about to be looked up, before an interview, a launch, a raise, or a press cycle.

**Hand check** - consistency only. Every surface's self-description in one block, then the one claim that should replace them.

**Going up** - forward-looking. Something new is about to be published. Where will it land, what will it collide with, and does the existing surface support it or argue with it.

## Output format

Deliver in this shape unless the user asks for something else.

```
WHAT IS UP
The inventory. Every surface, owned / claimed / third-party, with its URL
and what was found. Unverified ones listed separately, with the reason.

THE SCORE
Coverage, Decay, Hand, Order. Four numbers, one line each.

WHAT A STRANGER HITS FIRST
The first few results in order, and whether that is the intended front door.

HOW YOU DESCRIBE YOURSELF
Every self-description side by side, verbatim.

THE VERDICTS
Each surface: KEEP, FIX or BURY, with the specific action.

THE ONE CLAIM
The single description that should replace the others, and where it goes.

WHAT COULD NOT BE CHECKED
Everything unverified, and why. Never empty unless everything was opened.
```

Worksheets are in `assets/surface-sheet.md` and `assets/first-ten.md`.

## Rules of engagement

**Verified or it does not exist.** See the rule above. It is the only one here with no exceptions.

**Old is not the same as stale.** A piece from four years ago that still makes a true claim and still gets traffic is an asset. Age alone is never a reason to bury.

**Presence is not performance.** Being on a platform is not a win if nobody looks for them there. A thin profile on a network they do not use is dead weight, not coverage.

**Do not audit what they did not ask about.** Personal accounts, private profiles, and anything a reasonable person would consider separate from the work stay out unless the user puts them in scope.

**Never recommend suppressing true information.** The response to an accurate unflattering surface is better work ranking above it, never removal.

**Third-party surfaces get a different verdict set.** They cannot be fixed or buried directly, only outranked, corrected through the platform's own process, or accepted. Say which.

**Say what is working.** An output that is only a list of problems gives a false picture and will not get run twice. KEEP verdicts are part of the deliverable.
