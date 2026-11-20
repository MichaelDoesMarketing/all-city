# Hand

A graffiti writer's tag is identical on every surface. Thousands of reps, same letterforms, same proportions, recognizable from a moving car. That consistency is the entire point. It is how one name, in forty places, reads as one person instead of forty.

Almost nobody's professional presence works this way. Most people have a different answer to "what do you do" on every surface they own. Written at a different time, for a different reason, and never compared.

## Why it costs more than it looks like it should

A reader sees one surface. Not the set. Whichever one they land on is the whole of what they know.

So the question is never "is this bio good." It is "is this bio good enough to be the only one." Most people have two or three surfaces they would be happy to be judged on, and six they have not read in years. A stranger has no way to tell which is which.

The second cost is compounding. Forty mentions of one consistent claim builds a position. Forty mentions of eleven different claims builds nothing, because nothing repeats enough to stick. The work gets done and the position never arrives.

## What has to match

**The category.** What kind of thing this is. A consultant, a product, an agency, a tool. If one surface says consultant and another says agency, every downstream decision a reader makes is different.

**The subject.** Who it is for. Named specifically enough to exclude someone.

**The claim.** What is different about it, in the same words. Not the same idea in fresh phrasing each time. The same words. Reuse is the mechanism. A writer bored of their own line is usually about one tenth of the way to anyone else having heard it.

**The name.** Including capitalization, spacing, and whether a middle initial or a stage name appears. Two spellings split a search result between them.

**The proof.** The same one or two credentials everywhere, rather than a different flex per platform.

## What is allowed to vary

Length, obviously. A platform with a 160-character limit gets a compressed version, not a different claim.

Register. More formal on a professional network, looser on a personal site. The words that carry the claim stay fixed; the words around them can move.

Emphasis for a known audience. A surface built for one group can lead with the part that group cares about, as long as it does not contradict.

Format. Fragments on a profile, full sentences in a bio, a list on a landing page.

The test: could a reader who saw two versions tell they were describing the same thing, and would they come away with the same understanding of what it is. If yes, the variation is fine.

## Running the check

`scripts/surfacecheck.py --hand` prints every surface's self-description in one block, pulled from the meta description, og:description, h1 or title.

Read them as a stack. Do not evaluate them one at a time, because individually most of them are fine. The failure is only visible as a set, which is exactly why it survives for years.

Then count distinct answers. More than two is a problem. More than four means nobody has a clear idea of what this person does, including the person.

## Settling it

Pick one claim. Not a new one written for the occasion. That is the standard mistake, and it produces a ninth version nobody adopts.

Pick from what is already there. Usually one of the existing descriptions is clearly the best, it is just not on the surfaces that matter. Promote it rather than writing something fresh.

Then push it everywhere in one pass. Partial rollout is worse than none. The contradiction is now current rather than historical, so the reader cannot even use recency to work out which to believe.

Write the chosen claim down somewhere the user will find it again, because every new surface created after this needs to inherit it. `assets/surface-sheet.md` has a field for it.
