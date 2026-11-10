# A0 prepared review assets

`pages-*.json` covers all 112 actual scanned pages; page 3 is truly blank.
These are occurrence-level translations, not only a unique-word vocabulary.
`baseline.json` preserves original IDs and historical exercise definitions.
`exercise-geometry-*.json` applies visually inspected, concrete correction patches.
`verb-form-supplements.json` adds vocalized active base forms; selected passive
forms carry an explanatory note. Vocalization is retained in verb lookup keys
so nominal homographs do not receive verb paradigms.

Rebuild the reviewed worksheets and exact-width audio rectangles:

    python scripts/compile-a0-review.py
    python scripts/refine-a0-audio-rects.py

The audio refinement keeps original event timestamps from
`scripts/a0-timing-inputs/timing-intervals.json`, fixes rectangles using reviewed
words, then applies `audio-rect-overrides.json`. Three merged events are split
at their original local transcript word boundaries. Unprinted or unresolved
speech does not receive a fabricated underline. To revise timestamps, edit and
review the interval input deliberately before rebuilding.

Every recording is the source-pinned original. Timing preparation used local
speech alignment and measured waveform intervals for phonetic drills; the
whole collection has NOT been manually listened through. Review reports
record unresolved speech and remaining listening work. No paid API is used
for reader translations, analysis, word lookup, or audio timing.

Exercises are separate from vocabulary tests. Handwritten/open answers and
unverified listening keys are explicitly self-checked and never inflate
vocabulary mastery. Cover/frontmatter pages 1–7 have no activity overlays.

The source PDF/audio assets remain in the existing native R2 bucket; account
notes, saved selections and results remain in D1. The page scans and prepared
editorial content are versioned with this Site source.
