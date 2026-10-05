# Single-Listing Intake Spec — The Beat Drop

*Fill this out completely, then paste it as your build prompt to Claude Code. Every field marked "required" has no default anywhere in `CLAUDE.md` — leaving one blank is what forces a build to stop and ask. Building more than one listing at once? Use `BATCH_LISTING.md`'s Section 1 table instead — this file is the single-listing version of the same spec.*

---

## 1. Listing Type

**Standard or Bundle:** _______________

*Required — no default (CLAUDE.md Rule 13). Standard = one design with color variants. Bundle = a themed multi-design set, no colors.*

---

## 2. Identity & Theme

- **Artist / bundle name & theme:** _______________
- **Research link(s)** *(optional — Spotify, official site, Insomniac profile, etc.):* _______________
- **Theme adaptation notes** *(Bundle only, optional):* venue-specific language swaps (e.g. a camping reference → non-camping equivalent for a city festival), non-default festival/event references for the closing paragraph.

---

## 3. Colors & Variant Structure — Standard listings only

- **Colors** *(name + Standard Color Code if you know it — flag here if a color needs a new code that isn't in the existing list yet):* _______________
- **Variant/pack structure:** leave blank for the default (1/10/20/30-Pack, all colors; Multicolor in 10/20/30 only, no 1-Pack). State here only if this listing is different — e.g. individual colors in 1-Pack only, Multicolor in 10/20/30 only.

---

## 4. Pricing

- **Standard listings:** leave blank to use the Pricing Master table ($3 / $28 / $55 / $81 for 1/10/20/30-Pack). State here only if this listing uses different pricing.
- **Bundle listings — required, no default exists:** price per pack size (e.g. 10-Pack $___ / 20-Pack $___ / 30-Pack $___, or your actual structure).

---

## 5. Shopify Fields

- **Shopify Product Type — required, no default:** `Artist Sprout` or `Festival Sprout` — pick one.
- **Collection(s) — required, no default:** _______________

*(Not needed here — fixed for every listing per CLAUDE.md: theme template, Shopify Category taxonomy, and the four standing metafields — Material, Age group, Construction, Target gender.)*

---

## 6. SKU

- **SKU code** *(optional — leave blank to auto-generate a 4-letter + versioning-digit code per the SKU Convention):* _______________
- **Duplicate / "(Bonus)" listing?** *(required if yes):* source listing being duplicated + the exact title marker to use (e.g. "(Bonus)"): _______________

---

## 7. Images

- **Image subfolder:** `IMGs/[code-or-working-name]_[ShortName]/` — per `BATCH_LISTING.md` Section 2. Standard listings: filenames should include the color (e.g. `pretty-lights_blue_1.jpg`).

---

*Once every required field above is filled in, Claude Code has everything it needs to build the listing draft end to end without stopping to ask.*
