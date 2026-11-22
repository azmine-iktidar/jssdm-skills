---
name: jssdm-abbreviations-symbols
description: JSSDM abbreviations and military symbols - Bangladesh Armed Forces Joint Services Staff Duties Manual (JSSDM) 2022 authorised abbreviations (Section 16, Annexes A/B) with the para 0241 rules, and army map symbols (Section 17) with original page images and an SVG drawing library. Use for any military service writing, operation orders, abbreviating text "as per JSSDM", map marking, overlays, sketches or tactical diagrams.
---

# JSSDM 2022: abbreviations and military symbols

Source: *Joint Services Staff Duties Manual 2022, Service Writing* (JSP-001, Armed Forces Division). The document is marked RESTRICTED: keep outputs built from it local and never publish them.

This skill covers only Sections 16 and 17. For the general rules of service writing (Section 2 layout and conventions, Section 3 correspondence, Section 5 briefs and PowerPoint presentations, Section 8 graphs) use the `jssdm-basics` skill.

## What is here

| Path | Contents |
|---|---|
| `reference/abbreviations.md` | Section 16 Annex A (word → abbr, ~1,570 entries) and Annex B (multiple meanings, ~210). Search it; never guess an abbreviation. |
| `reference/section16-raw.txt` | Verbatim text of all of Section 16 (incl. Annex C ranks/appointments, D national letters, E institutions, F regiments and corps, G/H BN and BAF units). Fallback when a parsed row looks wrong. |
| `reference/rules-0241-raw.txt` | Verbatim para 0241 (abbreviation rules) and the following paras. |
| `reference/symbols.md` | Section 17 quick reference: colours, basic rules, role indicators, tactical symbols, each with para and page. |
| `reference/section17-raw.txt` | Verbatim text of Section 17. |
| `symbols/pages/17*.png` | Every Section 17 page as an image (17-1 … 17H-2). **Look at the page before drawing a symbol you have not drawn before.** |
| `symbols/svg/key-*.svg` | Ready-made symbol SVGs (unit types, HQ, goose egg, OBJ, strong point, front line, axis, main effort, repulsed, road block, demolition, minefield, tank obstacle, fire planning, OP). |
| `scripts/jssdm_symbols.py` | Python SVG drawing library for the symbols above (`unit()`, `hq()`, `goose()`, `front_line()`, `axis()`, `roadblock()`, `demolition_fired()`, `minefield()`, …) plus six worked doctrinal diagrams. Import it; running it writes `svg/` next to itself. |

## Abbreviation rules (para 0241, summary; verbatim text in `rules-0241-raw.txt`)

- Use only Section 16 abbreviations (a1). Others must be explained at first use (e.g. "Covering Forces (CF)") unless in general use (UN, NATO) or well understood by all recipients (a2).
- Once a word is abbreviated, abbreviate it throughout the same document (a3).
- No full stops in abbreviations (b2). Plurals take "s" at the end, only on nouns (b3).
- Composite words: abbreviate the part that has an authorised form, e.g. minefd, demob; exceptions listed in Section 16, e.g. C attk (b1).
- Verbs: the present-tense abbreviation covers all tenses and derivatives (sp = support/supported/supporting), unless Section 16 lists a specific form (bldg, retd, addl) (b4).
- Multiple meanings (Annex B): make the meaning clear from context or write it in full (b5).
- Cardinal compass points always in full lowercase (north); intermediate points NE or north-east (b7).
- Keep Section 16 capitalisation everywhere (HQ, OP, C attk) (b8).
- Operational writing and signal messages: **maximum use of abbreviations** (0241c; Section 11 annex A note 6b). Exceptions: operation-order paragraph headings (SITUATION, MISSION, EXECUTION, SERVICE SUPPORT, COMMAND AND SIGNAL) in full block capitals (1106-1107); DO, commanded and formal letters and service papers.
- No Section 16 abbreviations when writing to allied forces or non-service authorities (0241d).
- On maps and overlays, all writing is in block capitals in the symbol's colour (1704e).

Words with no authorised abbreviation stay in full (e.g. troops, bridge, route, mobile, main effort, force). Quotations from a source stay verbatim. "MOB" is Main Operating Base, not "mobile".

## Drawing rules that are easy to get wrong

- Front line curves: convex side towards the opposing force (17F 3a).
- Defence must show which way it faces, oriented on the actual threat axis in that scenario (never page-up or north-up; rotate for a flank or rear threat; all elements of one force face the same threat). For every def loc (goose egg, 1709a), put the size indicator on the line at the side facing its opposing force and rotate the symbol to suit: an own coy faces the en (all-round where the threat surrounds it, the rear coy facing the rear threat); an en FB/perimeter coy faces the obj it covers, i.e. towards own tps; a coy on a riv line faces the riv. Never leave every tick pointing page-up (user correction). In `tm.py` use `coy_area(..., face=(x, y))` / `away=(x, y)`. Then, where it helps, add the Section 17 signs that carry direction:
  - front line drawn in front of the position, curved lines with the convex side towards the opposing force (17F 3a(2), page 17F-2/3);
  - firing position bracket attached to the unit or equipment symbol, "oriented in the direction of firing" (17F 6b, page 17F-5);
  - arc of fire from the sides of the firing position, fixed line as an arrow in front of the weapon (17F 10a, page 17F-6).
  Obstacles (minefields, wire) sit on the threat side of the position they protect. In `jssdm_symbols.py` use `front_line()`, `firing_position()` and `arc_of_fire()`.
- Projected or future anything: broken line (1714). Planned route: broken line (17F 14c(3)).
- "Attack repulsed" (17F 14e) is enemy red arrow + own blue X; 17F 14f only defines *own* attack halted by enemy (blue arrow, red bar). Do not invent the reverse.
- HQ location point is the foot of the staff (1719a).
- Labels must sit beside the symbol they describe, never on an arrow or road; give text a background halo where roads pass under it.
- Non-standard signs need a legend (1703).

Related project with these used end to end (study PDF + narrated motion-graphics lesson): `~/Desktop/Projects/test/manoeuvre-terms/`.
