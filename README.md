# all-city

**Everything you ever published is still up.**

You remember the thing you made this week. You don't remember the conference bio you sent in 2023, the landing page from a campaign that ended, the profile on a platform you quit, or the article someone else wrote about you that outranks your own site.

Strangers don't arrive at your front door. They arrive wherever the link they clicked went, and that link is almost never the page you maintain. Whatever they land on is the entire thing they know about you.

`all-city` takes an inventory of everything currently live under your name, scores it as a set, and makes you decide what stays.

## How it works

Four axes, scored on the body of work instead of any single page.

**Coverage.** When someone searches for you, or for the thing you want to be known for, is there anything of yours there. Gaps count for more than quality.

**Decay.** What's still up but stale, wrong, or quietly contradicted by something newer. Decay isn't age. A piece from five years ago that still makes a true claim is an asset.

**Hand.** A graffiti writer's tag is identical on every wall. Thousands of reps, same letterforms, recognizable from a moving car. Your bio probably isn't. Most people have a different answer to "what do you do" on every surface they own, written at a different time, never compared.

**Order.** What people actually hit first, versus what you'd have chosen. These are rarely the same and almost nobody has looked.

## It actually checks

There's a Python script in the folder. No dependencies, takes a file of URLs or a list of them.

Per surface it reports whether it loads, where it really lands after redirects, the title and description, how much text a crawler sees, whether the page says anything at all without JavaScript, and the newest year on the page.

Then it stacks every surface's self-description in one block. Eleven different answers to "what do you do," side by side, is not an argument anyone wins.

## The verdicts

Every surface gets one of three. **KEEP**, **FIX**, or **BURY**. There's no fourth, and specifically no "monitor," which is how a broken page survives another two years while appearing on a list.

BURY is the one that does the work. The instinct is always to rewrite rather than remove, so a dead page gets a fresh coat every eighteen months and keeps helping nobody.

Then the rule people don't want: **nothing new gets made until the contradictions are resolved.** Fixing a bio nobody has opened in two years is less fun than making a new thing. It's still correct. A new piece landing on a surface that argues with itself inherits the argument.

## The rule that keeps it honest

**Nothing goes on the list unverified.**

Every surface needs a URL that was actually opened. Not "you probably have a Crunchbase page." Not "there's likely an old About page somewhere." A confident inventory of surfaces nobody checked is worse than no inventory, because you'll act on it.

Anything that can't be opened goes in a separate section with the reason, and never gets a verdict. Blocked is a finding, not a gap to fill with a guess.

It also won't help you suppress something true. The answer to an accurate unflattering article is better work ranking above it. Never a takedown.

## Install

```bash
git clone https://github.com/MichaelDoesMarketing/all-city.git ~/.claude/skills/all-city
```

Or grab the packaged `.skill` from [releases](https://github.com/MichaelDoesMarketing/all-city/releases).

## Try it with

> "What comes up when someone googles me?"

> "I'm interviewing next week. Is anything embarrassing still live?"

> "Does my LinkedIn say the same thing as my site?"

Five modes. **All city** is the full pass. **First ten** searches you the way a stranger would and lists what they hit, in order, with no advice attached. **The buff** is decay only, for when you're about to be looked up on purpose. **Hand check** stacks your self-descriptions. **Going up** runs before you publish something new, to see what it's about to land on top of.

## Real demo: I ran it on myself

I have a personal site, a blog on it, a LinkedIn I post to, an X account, and eight public repos. I'd have told you my presence was in decent shape.

**The headline finding.** My homepage and my blog return byte-identical HTML. Same 14,057 bytes, same title, same meta description, same everything. A crawler asking for either one gets **97 characters** of text. My browser renders **10,355**.

So the long-form writing that is the entire point of the site doesn't exist to anything that doesn't run JavaScript. Every blog URL presents as the homepage. Link previews, scrapers, and anything indexing without rendering see one page where I think there are many.

**The one I'd never have found.** My own site's Twitter card credits someone else:

```
twitter:site    @Lovable
twitter:image   https://michael-does-marketing.lovable.app/og-image.png
og:url          https://www.michaeldoesmarketing.com/   (page served at the bare domain)
```

Anyone who shares my site on X credits the tool I built it with. The preview image is hosted on a different domain than the site. The canonical points at `www` while the page answers without it. Default template values nobody edited, including me, for however long it's been live.

**Three surfaces I can't audit at all.** My LinkedIn profile, a LinkedIn article, and my X profile are all disallowed to automated fetching. Not a script problem. That's the actual condition: a large share of my presence is invisible to anything that isn't a logged-in human, which means it can't be previewed, indexed normally, or checked. They're listed as unverified with the reason, and they get no verdict. That's the rule working.

**The scores.**

```
Coverage   3/5   Present on the big surfaces. Searching the position I've spent
                 months building returns nothing of mine.
Decay      4/5   Little that's stale. Most of it is recent.
Hand       3/5   Three related but different claims across site, LinkedIn and
                 GitHub. Same theme, three different sentences.
Order      3/5   The name finds me. The thing I want to be known for doesn't.
```

Decent-looking presence. The front door is invisible to machines and credits a third party, and I'd never have checked, because the site looks perfect in my browser. That's the whole argument for this one.

## License

MIT. Michael Daughters.
