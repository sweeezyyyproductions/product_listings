# Recommendations — Getting to Zero-Question Batch Builds

*Reviewed: `CLAUDE.md`, `the-beat-drop-brand-identity.md`, `Gold_Standard_Product_Listing.docx`, `Gold_Standard_Bundle_Listing.docx`, `Platform_Reference.xlsx` (all tabs), and the two `Product Listing Project - Instructions.docx` files, against the live `IMGs/` folder and the current Product Roster. These are recommendations, not applied edits — nothing in `CLAUDE.md` or `Platform_Reference.xlsx` has been changed by this review.*

Goal being tested against: **Claude Code should never need to stop mid-build and ask a question.** Everything below is grouped by how directly it threatens that goal.

---

## A. Instructions that explicitly tell Claude Code to stop and ask

These are the direct blockers — as written today, hitting any of them means a build halts.

1. **Rule 13, "Which Template Applies," and the Bundle Listings "Trigger" bullet** all say some version of *"if the prompt doesn't say Standard or Bundle, ask before proceeding."* Three separate places in the file encode the same blocking behavior.
   - **Fix:** don't change the rule itself — it's a reasonable safety net. Instead, make "Standard or Bundle" a **required field** on every batch's intake spec (see the new `BATCH_LISTING.md`), so the prompt never actually omits it. The rule becomes a dead-code safety net instead of a live blocker.

2. **SKU Convention → "Duplicate-for-testing SKU versioning"**: *"Confirm the generated code back to the requester before creating the product."* Read literally, this asks Claude Code to pause for a yes/no before writing anything.
   - **Fix:** reword to *"state the generated code in the build summary for owner awareness"* — informs without blocking.

---

## B. Fields with no default and no fallback

CLAUDE.md correctly refuses to guess these (new product types are actively being introduced, so a hardcoded default would go stale) — but that means if a batch prompt omits them, there's genuinely nothing for Claude Code to do except ask.

3. **Shopify Product Type & Collection(s)** (Rule 12): *"specified per prompt, not defaulted... never assume unless the prompt says so."* Correct policy, but there's no mechanism forcing the prompt to actually include them.
   - **Fix:** same as #1 — make these required fields on the intake spec, not optional prose in a chat message. This is the single highest-leverage fix in this review, since it's the field most likely to get skipped in a quick prompt.

4. **Metaobject associations** (Rule 9): *"Flag if a listing needs one; do not attempt to create."* No criteria are given for *when* a listing needs one, so Claude Code has no way to self-resolve this without asking.
   - **Fix:** until real trigger criteria exist, explicitly state the failure mode should be "assume no metaobject is needed and proceed" (never block), with a Notes-column flag if something about the build seems metaobject-shaped. Only you can define real trigger criteria when/if they exist.

5. **Product Category Mapping tab (`Platform_Reference.xlsx`) contradicts Rule 12.** That tab lists a suggested Shopify Product Type ("Rave Sprout") for every product type row — which reads as exactly the kind of default Rule 12 says never to assume.
   - **Fix:** pick one policy. Either (a) restore Category Mapping as the actual default source — fastest path to zero questions, but re-opens the door Rule 12 was written to close, or (b) keep Rule 12 as strict-per-prompt and add a one-line note to the Category Mapping tab marking it "reference only — not a default; Product Type is always specified per the intake spec." I'd lean toward (b), since (a) is exactly what Rule 12 says caused problems before.

---

## C. Stale documents that could get read by mistake

None of these are wrong on their own — they're just outdated snapshots sitting where a future session could stumble into them and follow superseded instructions.

6. **Two duplicate legacy instruction docs** in the working folder: `Product Listing Project - Instructions.docx` and `Product_Listing_Project_-_Instructions.docx`. Both predate the current rules — they reference the retired Zeds Dead tone template by name, the old festival list (EDC, Bass Canyon, Beyond Wonderland instead of the current Electric Forest, Lost Lands, Seven Stars), retired 25-/40-/50-/100-pack tiers as if they're still standard, and embed the locked template's text verbatim — which is exactly what CLAUDE.md's own "never embed template text" rule warns against. Neither is in CLAUDE.md's Reference Files table, so nothing points a session at them, but nothing stops one from finding them either.
   - **Fix:** delete both, or move them into an `/archive` subfolder so they're clearly out of scope.

7. **`Platform_Reference.xlsx` → "New Listing Checklist" tab** is a second, older checklist that actively contradicts the current one embedded in `CLAUDE.md`: it caps images at 10 (CLAUDE.md says upload everything in the subfolder), hardcodes a default collection *"Rave Sprouts & Trinkets"* (contradicts Rule 12 directly), and includes *"Listing reviewed and activated"* as a checklist item — which conflicts with Rule 1's DRAFT-only mandate. It also covers full Etsy/TikTok listing creation, which is explicitly out of scope for this workflow.
   - **Fix:** delete the tab, or mark it "SUPERSEDED — see CLAUDE.md's New Listing Checklist," matching how the SKU Convention section already treats `Platform_Reference.xlsx` as sole source of truth to avoid two copies drifting apart.

8. **`the-beat-drop-brand-identity.md`** references a file called `GOLD_STANDARDS.md` in the "Two Voice Registers" table. That file doesn't exist — the real files are `Gold_Standard_Product_Listing.docx` and `Gold_Standard_Bundle_Listing.docx`, which the same document correctly names two sections later. Small, but worth a one-line fix so there's only one filename in circulation.

---

## D. Inconsistencies inside CLAUDE.md itself

9. **SKU Convention rule #5** still lists `PCK25` and `PCK40` as valid pack-size suffixes, but the Standard Pricing table no longer offers 25-Pack or 40-Pack as buildable tiers (per the project's own instructions, those tiers "have been retired"). Right now the rule reads as if they're still an option for new builds.
   - **Fix:** add a parenthetical marking `PCK25`/`PCK40` as legacy-only — valid to match on existing live SKUs (per Rule 10), never generated on a new build.

10. **Product Roster's Notes column is gone from the live file.** The version I delivered had a 9th column carrying data-quality flags (a duplicate-SKU collision, several "no live SKU yet" items, off-convention listings, etc.) — the current `Platform_Reference.xlsx` on your machine is down to 8 columns, and that column's gone. That's exactly where a build should record "I made an assumption here" instead of asking, so losing it works against the zero-questions goal.
    - **Fix:** restore the Notes column and treat it as append-only — each batch adds to it, nothing gets cleared without you saying so.

---

## E. A live example of the gap, right now

11. **`IMGs/` currently holds 6 flat, unlabeled photos** (`Pretty-Lights_2836.jpg` … `Pretty-Lights_2843.jpg`), while the Product Roster already lists **two** in-flight Pretty Lights products — a Standard listing (`PLML1`) and a Bundle (`PLYD1`). Nothing in the filenames or folder layout says which photos belong to which product, or which color each one shows for the Standard listing's three-color variant set. This is exactly the situation that forces a build to stop and ask.
    - **Fix:** see `BATCH_LISTING.md`, Section 2 — per-product subfolders under `IMGs/`, with color named in the filename for Standard listings.

---

## Suggested priority order

If you only act on a few of these: **#1/#3 (intake spec required fields) first** — that alone closes most of the "ask before proceeding" paths. **#6/#7 next** (delete the stale docs) since they're pure downside with no upside to keeping them around. Everything else is lower-stakes cleanup.
