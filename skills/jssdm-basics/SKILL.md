---
name: jssdm-basics
description: JSSDM 2022 basics for Bangladesh Armed Forces service writing - Section 2 rules and conventions (classification, precedence, copy numbers, address, date/time/DTG, headings, paragraph numbering, punctuation, abbreviation rules, signature, annexes, distribution, page numbering, capitals, nicknames, units, seniority, typing layout), Section 3 service correspondence (commanded, directed, routine, formal, DO letters, memorandum, loose minute, note sheet, email, styles of address), Section 5 briefs (information, decision, personality, visit briefs, flags and side flags) with PowerPoint presentation guidelines, and Section 8 graphical presentation. Use when the user invokes /jssdm-basics or asks to write, format or review any service letter, brief, presentation, slide deck, paper or order "as per JSSDM".
---

# JSSDM 2022 basics: service writing, correspondence, briefs and presentations

While this skill is active, **every** piece of service writing you produce or review must follow all rules below and in the section files. Para numbers are JSSDM Part-II paras; cite them when you correct something (e.g. "para 0243a", "para 0508c(2)").

Source: *Joint Services Staff Duties Manual 2022* (Armed Forces Division), Sections 2, 3, 5 and 8 with their annexes. The manual is RESTRICTED: keep outputs built from it local, never publish them.

## Files

| Path | Use |
|---|---|
| this file (sections 1-6 below) | **Section 2** rules: apply to everything. |
| `reference/section3-correspondence.md` | **Section 3**: the 7 types of correspondence, when to use each, their formats, note sheet rules, email, styles of address for Army/Navy/Air Force. **Read before writing any letter, memo, LM or note sheet.** |
| `reference/section5-brief-presentation.md` | **Section 5** briefs (information/decision/personality/visit, oral vs written, flags and side flags, frameworks) + **Annex 5C PowerPoint rules** + **Section 8** graphs. **Read before any brief, briefing, presentation or slide deck.** |
| `reference/tables.md` | Annex 2C time zones, 2D D-Day/H-Hour letters, 2E units of measurement, 2F seniority lists. |
| `reference/section2-raw.txt`, `section3-raw.txt`, `section5-raw.txt`, `section8-raw.txt` | Verbatim text; check when a summarised rule is ambiguous. Bangla glyphs are legacy-font garbage; ignore them. |
| `pages/2A-*.png`, `2B1-1.png` | Standard layout and indent example as printed. |
| `pages/3B-1.png` ... `3J-4.png` | Printed examples: commanded (3B), directed (3C), routine (3D), formal (3E), DO (3F), memorandum (3G), loose minute (3H), note sheet (3J). |
| `pages/5A-*.png` ... `5E-*.png`, `8A-1.png` | Information/decision brief frameworks, PowerPoint guidelines, example decision and personality briefs, graph example. |

**Look at the matching page image before producing a full document of that type.**

### Companion skill: `jssdm-abbreviations-symbols`

Section 2 refers to Sections 16 and 17 for its details. That content lives in the `jssdm-abbreviations-symbols` skill (`~/.claude/skills/jssdm-abbreviations-symbols/`). **Invoke it (Skill tool) or read its files whenever** the work needs:

| Need | Read in `jssdm-abbreviations-symbols` |
|---|---|
| Abbreviating any word (0241a/b, 0244 unit titles, addresses, ranks, appointments, decorations) | `reference/abbreviations.md` (Annex A word→abbr, Annex B multiple meanings). Grep it; **never invent an abbreviation**. |
| Ranks/appointments, national distinguishing letters (0241e), institutions, regiments/corps, BN/BAF unit abbreviations | `reference/section16-raw.txt` (Annexes C-H) |
| Map marking, overlays, traces, sketches, writing in army symbols (0267q) | its `SKILL.md` drawing rules, `reference/symbols.md`, `symbols/pages/*.png`, `scripts/jssdm_symbols.py` |

Section 2 rules below take precedence for layout and conventions; Section 16 decides *which* abbreviation to use.

## Workflow

1. Identify the document type (operational writing/order, commanded/directed/routine/formal/DO letter, memorandum, loose minute, note sheet, email, brief, presentation, service paper, letter to civilians/allied/foreign) - several rules depend on it. Load the matching section file: letters/memos/LM/note sheets/email → `section3-correspondence.md`; briefs, presentations, slides, graphs → `section5-brief-presentation.md`.
2. Draft or check part by part: superscription → text → subscription → other rules.
   For every word you abbreviate (or leave in full), look it up in `jssdm-abbreviations-symbols` `reference/abbreviations.md`; if the document has a map, trace or sketch, follow `jssdm-abbreviations-symbols` for the symbols.
3. When reviewing, list each violation as `para XXXX: problem → fix`, then give the corrected text.

# Section 2: Rules and Conventions of Service Writing

## 1. Document parts (0203-0204)

- **Superscription**: everything above the salutation (or above the subject heading if no salutation).
- **Text**: salutation/subject heading to last word of final paragraph.
- **Subscription**: everything below the final paragraph.
- Large documents have a **prefatory part** before Chapter I (title page, acknowledgement, abstract, executive summary, foreword, table of contents).

## 2. Superscription

### Security classification (0205-0213, 0264)
- Five grades: **TOP SECRET, SECRET, CONFIDENTIAL, RESTRICTED, UNCLASSIFIED**. Avoid over-classification.
- Exercise/exam material: classification with prefix "Exercise"/"Examination" (0206).
- Typed **in capitals, in full, not underlined, centrally at top and bottom of every page**, front and back (0207).
- Loose-leaf books and bound books: top and bottom centre of front and back covers and every page, including inserted maps/sketches (0209-0210).
- Multi-section document: each page bears its section's classification; whole document at least the highest (0211).
- Minutes/directives: each item marked with its own classification at its heading; document as a whole takes the highest (0212).
- Covering letter: its own classification plus e.g. `RESTRICTED COVERING CONFIDENTIAL` at top and bottom of first page (0213).

### Privacy marking (0214, 0263)
- `IN CONFIDENCE`, optionally prefixed: `STAFF IN CONFIDENCE`, `MEDICAL IN CONFIDENCE`. For personal matters not needing security classification.
- Top and bottom centre of every page, capitals, not underlined, may be abbreviated.
- If also classified: classification **above** privacy marking at top, **below** it at bottom.

### Precedence (0215-0217)
- Only two: **IMMEDIATE** (great urgency, senior staff officers/independent unit COs authorise, use sparingly) and **PRIORITY** (ahead of routine; any commissioned officer).
- To Bangladesh government civil offices use civil precedence: Top Priority / Immediate / Urgent.
- **Capitals, top right of first page only, not underlined, not abbreviated.** Double-spaced below and to the right of classification/privacy marking (on the left for a loose minute).
- Signal message precedence: Section 15.

### Copy numbering (0218)
- Required on all **SECRET and TOP SECRET** documents and on **all operation and administrative orders, instructions and appreciations** regardless of classification.
- `Copy Number 1 of 20`, top right of cover/first page, below precedence. Single copy: `Copy Number 1 of 1`. Each annex/appendix/trace first page also copy-numbered.
- Same addressee gets the same copy number each time; allocation shown in distribution.
- Authorised reproductions: `Reproduction Copy Number ... of ...` immediately **above** the original copy number; reproduction needs written authority of originator.

### Originator's address, contact, date (0219-0221)
- Unit designation abbreviated, section in brackets after the directorate, e.g. `AHQ` / `AG's Br, PS Dte (PS-1)`; `NHQ` / `Ops Br, Dte of Naval Ops`; `Air HQ` / `Ops Br, Dte AD`.
- Then place/garrison/ship/base/post town with initial capitals (+ post box).
- Contact: telephone with extension and/or cell, and email: `Tel/Cell: XXXXXX Ext: 4338` / `Email: ...`.
- **Date under the address block: month and year abbreviated, day left blank** for the signatory to write in manuscript (e.g. `    Aug 22`). No address block (loose minute) → date under the signature block. Bangla date may precede the English date.
- Day always two figures (`01`, `06`), never `1st`/`sixth`. Month never as a number.

### Non-service address (0222)
- To government departments/civilian organisations: **unabbreviated** designations of sender and recipient, full postal address incl. street. Officially recognised abbreviations (WASA, PDB) allowed except to foreign organisations.

### Identifying reference (0223; 2B para 12b)
- Every service correspondence has one; placed **opposite the date**, left margin. In messages = originator's number. Supplementary documents (not enclosures) carry the parent's reference. May be repeated on every page of note sheets.
- Digital format `06.02.2626.121.55.003.22` = ministry/division . organisation/directorate . geographic code . section code . subject classification . originating dte/section . year.

## 3. Text

### Salutation (0224)
- Formal/DO letters: `Sir` / `Dear ...` above the subject heading. Inserted in manuscript by signatory (typed in formal letters). **No comma after it.**

### Headings (0225-0230)
- Except in operational writing, a heading **must not form part of the next sentence**. Wrong: `Plantation.   Will be discussed tomorrow.` Right: `Plantation.   The plantation programme will be discussed tomorrow.`
- **Subject heading**: simple documents/correspondence → left margin, **UNDERLINED CAPITALS, no full stop**. In annexes, appendices, maps, traces, overlays, charts, graphs → **centred**, underlined capitals, no full stop. Where main headings are used, subject heading is treated as a main heading (centred).
- **Main heading**: centred over the typed area (not the page), **UNDERLINED CAPITALS, no full stop**. Two-line: second line shorter, centred under the first.
- **Group heading**: own line at left margin, **not numbered, no full stop**, Initial Capitals for important words, underlined. Covers all paragraphs until the next main/group heading.
- **Paragraph heading**: Initial Capitals, **underlined, followed by a full stop**. Once used, every following paragraph down to the next main/group heading must have one. May stand on its own line followed by sub-paragraphs.
- **Sub-paragraph headings**: same rules as paragraph headings.
- Computer-typed headings may be bold.

### References (0231-0234)
- Under the word `Reference(s):` immediately above the text: title/identifying reference and date of each document, lettered `A.`, `B.` ...; originating authority prefixed if not self-evident. Refer in text as `Reference A`.
- Alternatives: footnote notation (0246); a single reference in DO/civilian letters may go in the text.
- Citing JSSDM: `JSSDM Part-II Para 0110` (part number before para).
- Signal messages: originator, originator's number and DTG (para 1513).
- Extracts: by chapter, article, paragraph - **never by page number**.
- Maps: (series) country/area, sheet number, (edition), scale. Charts: number and title.

### Paragraph numbering (0235-0237; 2B paras 5-6)
- Paragraphs in **Arabic numerals**; a **single paragraph is not numbered** (unless it has sub-paragraphs).
- **Never a single sub-paragraph** (exception: attachments/detachments or grouping in operational writing).
- Hierarchy: `1.` → `a.` → `(1)` → `(a)` → `i.` → `aa.` (see `pages/2B1-1.png`).
- **Never use letters `i`/`I` or `o`/`O` as sub-paragraph letters** (sequence a b c d e f g h j k l m n p q r s t u ...).
- Unnumbered list/example inside a paragraph: indented one level right of the paragraph number.
- Civilian letters: number by good taste; **condolence letters never numbered**.
- Multi-chapter documents: section number + noughts + para (`0201`); unused numbers listed at section end as `0285-0299. Reserved.`

### Punctuation, spelling, underlining (0238-0240; 2B para 15)
- Lists and sub-paragraphs introduced by a **colon** (not when directly after a paragraph heading). Each sub-paragraph **ends with a full stop** unless further subdivided.
- Full stops after: unbracketed para/sub-para numbers and letters; paragraph/sub-paragraph headings; each sub-paragraph; each reference or supplementary document listed.
- No full stops/commas in an address; no comma after salutation, complimentary ending or subscription; no full stops in familiar abbreviations; in tables, full stops only after serial numbers or between sentences; unnumbered list items take no full stop unless complete sentences.
- Spelling: latest *Concise Oxford Dictionary*, first spelling given (British: organisation, defence, metre...).
- Don't underline for emphasis; bold may be used (unit name, nom de plume, ordinals in DO letters).

### Abbreviations (0241)
- a(1) Use only Section 16 abbreviations. a(2) Others must be explained at first use, e.g. `Covering Forces (CF)`, or listed in an annex - unless in Section 16, in general use (UN, NATO), or specialist and understood by all recipients. a(3) **Once abbreviated, abbreviate throughout the document.**
- b(1) Composite words: abbreviate the authorised part (`mob`, `demob`, `minefd`), except where Section 16 lists the compound (`C attk`).
- b(2) **No full stops** in abbreviations, initials or decorations. Commas after the name and between decorations, qualifications, corps: `Lt Col Mohammad Saifur Rahman Sohel, SUP, psc, Inf`.
- b(3) Some abbreviations are already singular/plural (`rat`); units of measurement never take `s` (`m`, `l`, `hr`). Otherwise `s` goes at the end (`GOCs`), and only on nouns. Verb 1st/3rd person identical (`fol` = follow/follows).
- b(4) Verb abbreviation covers all tenses/derivatives (`sp` = support/supported/supporting/supporter/supportive); write in full if confusing. Exceptions with a specific form (`bldg`, `retd`, `addl`) apply only to that word.
- b(5) Multiple meanings (e.g. `AB`): write in full if confusion is possible.
- b(6) `&` instead of "and" in departmental/similar titles: `AA&QMG`, `R&D`, `Messrs Rahman & Sons`.
- b(7) Cardinal points **always in full, lower case**: `north`. Intermediate: `NE`, `NNE` or `north-east`, `north-north-east`.
- b(8) Keep Section 16 capitalisation everywhere (`C attk`, `Atk`).
- c. **Maximum use of abbreviations** in operational and non-operational writing and signal messages. **Exceptions (write in full)**: paragraph headings of operational and administrative orders; DO, commanded and formal letters and service papers (still abbreviate decorations, qualifications, arms/services). BAF may abbreviate in service papers on operational matters.
- d. **No Section 16 abbreviations** to allied forces and non-service authorities (officially recognised civil ones like WASA, PDB allowed, except to foreign organisations). Abbreviations allowed in operational writing addressed to para-military forces.
- e. National distinguishing letters: Section 16 Annex D (`jssdm-abbreviations-symbols` `reference/section16-raw.txt`).

### Numerals (0242)
- Fractions and whole numbers in **figures, except "one"**. Spell out a number that **starts a sentence** or that gives a **quantity of formations, units, ships, bases**.
- Figure `1` is used in dates, para/chapter numbers, serials in tables/diagrams.
- Adjacent numbers: `twelve 10-ton trucks` or `12 X 10-ton trucks`.
- Ordinals abbreviated: `6th Staff Course`, `1st World War`.

### Date and time (0243)
- Date: day month year, `01 August 2022`; abbreviated `01 Aug 22` (day always 2 figures, month first 3 letters, year last 2). Dates in text normally abbreviated **except in formal, commanded and DO letters** (2B para 22).
- Night: `Night 29/30 August`, `Night 30 August/01 September`.
- **Never "midnight"**: `0000 hours 16 August` = midnight of night 15/16 August.
- **Never am/pm** in service writing (only for civilians/social invitations).
- Time: 4 figures, 24-hour clock. Operational writing: add zone suffix, `2359F` (Bangladesh = F, -6); not needed where the order states "Time Zone Used Throughout the Order". Other service writing: `1100F` or `1100 hours` when confusion is possible.
- DTG: 6 figures (DDHHMM) + zone suffix. In orders with "Time Zone Used Throughout": `221415 Aug` (`221415 Aug 22` if ambiguous). In service writing: `221415F August 22`. Signal messages: always zone suffix + 3-letter month (para 1504d).
- Operation-relative days/hours (D Day, H Hour, etc.): `reference/tables.md`.

### Formations, units, detachments (0244)
- Identifying numbers in Arabic numerals before the description: `11 Inf Div`, `35 PCS`, `5 Sqn`.
- Quantities always in words: `one div`, `twenty-eight sqns`.
- Less a portion: `2 Inf Bde less two bns`.

### Locations and areas (0245)
- Place name: give grid reference or lat/long the first time.
- Grid reference: 4 or 6 figures **preceded by the 2-letter block**.
- GEOREF: full `ML NK 2052`, abbreviated `NK 2052`.
- Lat/long: 4-5 figures + hemisphere letter, no degree/minute symbols: `5452N 00136W`.
- Bearing and distance: state true/magnetic/grid; bearing before, distance after the reference point: `315° (T) NAB TOWER 7.9 miles`, `5600 mils (T) NAB TOWER 9.8 kilometres`.
- Place/feature names spelt exactly as on the map in use; **`River` always precedes** the name; add grid square (for a river, the square where the name appears).
- Roads/tracks/railways: word first, then places: `Road Dhaka-Tangail`.
- River banks: right/left facing **downstream** (else cardinal points); near/far for river crossings. Canals: by name, banks by cardinal points (`north bank of the GK Canal`). Channels: name + `Channel`; buoys by name, port/starboard hand, shape or position.
- Routes: with movement, points in direction of movement; without, left to right or rear to front facing the enemy.
- Areas: **northernmost point first, then clockwise.**
- Positions: left to right, front to rear, facing the enemy; prefer cardinal points for flanks.
- Boundaries: rear to front in advance; front to rear in defence/withdrawal; lateral-parallel (rear) boundaries left to right facing the enemy. Use `inclusive`/`exclusive` **before** the place and state to which unit/formation.

### Notes, cross references (0246-0247)
- Notes amplify tables/diagrams, not normally in service paper text. Numbered in Arabic numerals, restarting each chapter, under `Notes:` at the foot of the page, left margin, above the classification. Marked in text by the numeral in brackets right after the point: `(1)`.
- Cross references by paragraph only: `see Paragraph 0231`. **Never "above"/"below".**

## 4. Subscription

### Complimentary ending (0248)
- Only in formal correspondence with a salutation: `Yours faithfully`; DO letters `Yours sincerely` (or other appropriate). No comma after it.

### Signature block (0249-0251)
- All service writing except DO letters. Leave **at least 4 blank lines** after the text for the signature.
- Line 1: initials and name in **BLOCK CAPITALS**, no brackets, **no decorations/awards**.
- Line 2: rank (and service where appropriate).
- Line 3: appointment, or `For <superior's appointment>` when signing on their behalf.
  ```
  ABUL MANSUR MASUD
  Brig Gen
  For AG
  ```
- Signatory signs all action and information copies (original only if numerous). **Green ink**: Service Chiefs; formation/base commanders and commandants within their formation. **Everyone else black ink.**
- Signing over the commander's own block in their absence: write `For` and the reason (e.g. `(Absent on duty)`) in manuscript beside the block, and put your own name, rank, appointment under your signature.
- Recommendations, important requests, opinions and serious reprimands: signed by the commander. Minor censure: senior staff officer after commander's approval. **Junior staff officers never sign letters refusing a request.**

### Annexes (0252)
- Referred to in the text; **lettered A, B, C in capitals** in order of mention (a single annex is still lettered); own subject heading; copy-numbered as per 0218.
- Listed at the close of the parent, before distribution, under `Annex(es):` (colon, not underlined), wording identical to their subject headings.
- **Annex block** top right of first page only, underlined capitals, with parent reference:
  ```
  ANX A TO
  00.03.2600.005.01.008.22.001
  DT    NOV 22
  ```

### Appendices (0253)
- Amplify an annex; referred to in the annex; **numbered 1, 2, 3** (single one still numbered); own subject heading; listed at the close of the **parent annex** under `Appendix(ces):`; copy-numbered like an annex.
  ```
  APPX 1 TO
  ANX A TO
  00.03.2600.005.01.008.22.001
  DT    NOV 22
  ```

### Enclosures (0254)
- Complete documents sent with a covering document; referred to in the text; listed **numerically** under `Enclosures:` at the end, before distribution, with title, reference, date and copy number if any.

### Distribution (0255-0260)
- Recipient address as in 0219a; the action branch/directorate under the HQ/unit. Space-saving forms allowed: columns, one line, or `/`-separated: `HQ 9 Inf Div (GS Br/ AQ Br/ EME Br)`, `NHQ, Ops Br/ DNO/ DNP, Banani, Dhaka-1213`.
- `Distribution:` at left, after the signature block, or after the annex/enclosure list if any (or on a separate sheet).
- Order: **External Action → External Information → Internal** (Action/Information separately if required). External addressees by seniority of size, then of arms/services, then numerically or alphabetically. Navy: address the appointment holder, not the HQ/unit.
- Multiple copies to one addressee: number in brackets, or the copy numbers if copy-numbered.
- `(For the attention of ...)` in brackets beneath the addressee, above other address details; mark the envelope too.

### Page numbering (0261-0262)
- All pages except single-page documents numbered **bottom centre, immediately above the security/privacy marking**.
- Consecutive through the document, or section-number style: chapter `1-1`; annex `A-1`; annex after a chapter `1A-1`; appendix `A1-1`, `B1-2`.
- Copy-numbered documents additionally: single pages numbered; `Total Pages ...` below the copy number (all annexes, not enclosures); main part first page `1 of 20`; each annex/appendix first page `A-1 of 1`, `B2-1 of 3`.

## 5. Other rules

### Orders and intentions (0265-0266)
- `is to` / `are to` = direct order. Infinitive `To ...` = aim/intention (`To take up defence...`). Executive form for missions (`Capture Objective A`, `Hold river line`). `should` = leaves discretion to the commander on the spot.
- `intend` = will be done unless countermanded. `propose` = will not be done unless approved. `request` from senior to junior = courteous order. `will` = information/future tense only, never an order.

### Capitals (0267-0268)
ALL CAPITALS: subject and main headings; code words and nicknames; proper nouns in operational writing; precedence; security classification and privacy markings; `DRAFT` at top centre; paragraph headings of operational and administrative orders; Section 16 capital abbreviations; names of naval ships/establishments; annex/appendix reference blocks; postcodes; signatory's name in signature block; time zone spelt in full; message writing and writing in army symbols.

Initial Capital: proper nouns/adjectives (`Bangladeshi`); important words in group/para/sub-para headings; first word of listed items; principal words in lists of annexes/appendices/enclosures/flags and agenda items; particulars (`Paragraph 3`, `Page 2`, `Annex A`, `Thursday`, `January`); ranks/appointments of a specific individual (not collective use); column headings; `Service(s)`, `Army`, `Navy`, `Air Force` for the Bangladesh Armed Forces.

### Drafting (0269-0271; 2B para 14)
- Manuscript drafts double-spaced, same layout as final. Typed drafts: text double-spaced (normal spacing outside text); `DRAFT` in block capitals, **not underlined**, top centre of first page below classification/privacy marking.

### Code words and nicknames (0272-0274)
- Code word = one word, security cover for classified matters; taken from AFD/MOD or Service HQ lists only, issue/cancellation registered.
- Nickname = two words, no security value; for UNCLASSIFIED/RESTRICTED matters, target indication, routine exercises; e.g. `AGNI BEENA`. **Never for commanders, units or formations.** Rules: neither word a colour; first word not `OPERATION`/`EXERCISE`; second word not `ROUTE`/`ROOT`/`ROUT` or similar; words must not run together into a code-word-like word (`MATCH BOX`); no word+number series (`IRON ONE`); no series of associated words in one operation.

### Measurement, quotations, bibliography, amendments (0275-0278)
- Units: internationally agreed symbols (`reference/tables.md`); never plural `s` (`10 lb`, not `10 lbs`); no space between prefix and unit (`km`, `kilogram`). To foreign forces: their units first, ours in brackets. First use in full in the originating country's language, then abbreviated.
- Quotations acknowledged as a note (without the `Notes:` heading): `1. The Government Economic Plan from Current Affairs by M. Jalal`.
- Bibliography at the end under `BIBLIOGRAPHY`/`Bibliography`: authors, titles, publishers, dates.
- Amended/resubmitted papers: side-line amended paragraphs; keep an amendment sheet; mark amended pages `CHANGE 1` at bottom right.

### Seniority (0279-0282; Annex F)
- Services: **Army, Navy, Air Force, Inter Services Organisations**.
- Mixed address lists: originator's own Service first, then other Services in the order above, then inter-services organisations (Annex F order), then para-military/auxiliary: **BGB, Coast Guard, Police (incl. RAB), BNCC, Ansar & VDP, Fire Service & Civil Defence**.
- Corps and unit orders: `reference/tables.md`.

### Retired ranks (0283)
- `Major Mohammad Fazle Ali, OSP, psc (retd)`; `Sergeant Shakir Hossain, SUP (retd)`. **Gallantry award comes first**, right after the name: `Brigadier General Md Yousuf, BP, ndc, afwc, psc`.

### Figures and tables (0284; 2A notes 9-11; 2B para 13)
- `Figure-1: Flowers of Bangladesh` - numbered consecutively, dash, colon, name. Source bottom-left under the figure/table with year: `Source: Bangladesh Agricultural Board 2017`.
- Tables titled (`Table-1: ...`); columns lettered `(a)`, `(b)`... in brackets, rows numbered `1.`, `2.`... so items can be cited without asterisks.

## 6. Typing layout (Annex B)

- Margins: left **3 cm** (15 spaces), right ≥ 1 cm; briefs, minutes and file summaries get a 3 cm right margin with a ruled line. Transpose margins on reverse sides.
- Para number + full stop, then a tab/3 spaces; heading + full stop + 3 spaces + text. All lines of a paragraph flush to the left margin. Sub-paragraphs block-indented 5 spaces per level (points 1, 6, 11, 16...).
- Left margin: identifying reference, subject heading (unless centred), `References:`, text, `Annexes:`, `Enclosures:`, `Distribution:` and their items.
- Right-hand elements (precedence, copy number, address, telephone, date, signature block) share **one common tab stop**.
- Centred headings centred on the typed area, not the page.
- One space after all punctuation on a computer.
- Vertical: single spacing within a paragraph; **double between paragraphs, subdivisions, headings and stand-alone superscription/subscription elements**; single within a block (e.g. one address). Precedence double-spaced below classification. Leave 4 lines between reference and text when a salutation is used, and ≥ 4 lines before the signature block.
- Day of month / DTG left blank for manuscript insertion by the signatory.
- No catchwords. Annex/appendix blocks underlined in the right margin.

## Review checklist

Before returning any service writing, confirm:
- [ ] Classification (and privacy marking) top and bottom centre of every page, capitals, not underlined
- [ ] Precedence/copy number/total pages placed and formatted correctly, only where required
- [ ] Address abbreviated (service) or full (civil/foreign); contact line; date `    Mon YY` with day blank
- [ ] Identifying reference opposite the date
- [ ] Subject heading underlined capitals, no full stop, correct position
- [ ] Headings stand alone; paragraph-heading consistency; no single sub-paragraph; no `i`/`o` letters
- [ ] Colons before lists, full stops ending sub-paragraphs
- [ ] Abbreviations per 0241c/d for this document type, consistent throughout, no full stops, each one checked in `jssdm-abbreviations-symbols` abbreviations or explained at first use
- [ ] Numbers, dates (`01 Aug 22`), times (`1100F`), DTGs, no midnight/am/pm
- [ ] Locations: grid ref with 2-letter block, `River X`, `Road A-B`, areas clockwise from north, inclusive/exclusive boundaries
- [ ] Cross references by paragraph, never above/below
- [ ] Signature block: CAPS name, rank, appointment/`For`, no decorations
- [ ] Annexes lettered, appendices numbered, enclosures listed, blocks top right underlined
- [ ] Distribution order and seniority correct
- [ ] Page numbers bottom centre above classification, correct scheme
- [ ] **Letters (Section 3)**: right type chosen (commanded/directed/routine/formal/DO/memo/LM/note sheet); first vs third person; salutation/ending per Annex 3A (none on routine/LM; no commas); no abbreviations in commanded/formal/DO except decorations, qualifications, arms/services; LM never leaves the originating HQ; condolence letters unnumbered, no headings
- [ ] **Briefs (Section 5)**: correct framework (information vs decision); `Comment(s)` heading for opinion; 3 cm right margin; flags lettered A, B, C and side flags numbered 1, 2, 3 noted in the margin and listed at the end; classification at least that of the highest attached paper; decision sought after conclusion (oral) or before it (written)
- [ ] **Presentations (Annex 5C)**: no verbatim paragraphs; font 24-44, black/white/yellow on white or navy blue; slide number bottom right; no needless animation; classification on every slide if any slide is SECRET+; visuals over text; script at ~100-120 words per minute fits the time slot
- [ ] **Graphs (Section 8)**: titled, axes labelled with units, undistorted scale, source bottom left, legend if needed, ≤ 5 diagrams
