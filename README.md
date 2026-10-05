# The Beat Drop — Product Listings

Operating rules, templates, and reference data for building The Beat Drop's Shopify product listings with Claude Code.

The Beat Drop makes **rave sprouts**: 3D-printed spring-clip kandi charms for festival hats, hair, bags, and outfits. Products sell on Shopify (primary), Etsy, and TikTok Shop. This repo covers the Shopify listing workflow, plus Etsy tag selection.

Claude builds listings as **drafts only**. A human reviews and publishes every listing.

---

## Start here

1. **`the-beat-drop-brand-identity.md`**: who the brand is and why the voice sounds the way it does. Read this first.
2. **`CLAUDE.md`**: the enforceable rulebook Claude Code follows on every listing (critical rules, SEO, pricing, SKUs, variants, images, metafields, and the new-listing checklist).
3. **An intake spec**: fill one out and paste it as the build prompt.

## Files

| File | What it is |
|---|---|
| `CLAUDE.md` | Rules Claude Code follows for every listing task. Describes structure and process only; it never holds the listing copy itself. |
| `the-beat-drop-brand-identity.md` | Brand story, audience, and voice rationale. |
| `Gold_Standard_Product_Listing.docx` | **The single source of truth for Standard (single-design) listing copy.** |
| `Gold_Standard_Bundle_Listing.docx` | **The single source of truth for Bundle listing copy.** |
| `Listing_Prompt_Template.md` | Copy-and-paste build prompt for one listing, with filled-in Standard and Bundle examples. |
| `Intake_Spec_Single_Listing.md` | Fill-in form for building one listing. |
| `BATCH_LISTING.md` | Workflow for building several listings at once, with the batch intake table and the asset folder layout. |
| `Platform_Reference.xlsx` | Live catalog reference: SKU bank, product roster, category mapping. |
| `CLAUDE_md_Recommendations.md` | Review notes and suggested improvements to `CLAUDE.md` (not yet applied). |
| `Seven_Stars_*_Build_Summary.docx` | Build summaries from past Seven Stars bundle listings. |
| `IMGs/` | Product images, one subfolder per listing (see `BATCH_LISTING.md`). |

## How a listing gets built

1. Fill out `Intake_Spec_Single_Listing.md` for one listing, or the Section 1 table in `BATCH_LISTING.md` for a batch. Every required field must be filled in (Standard vs. Bundle, Product Type, Collection, and so on) so the build never stops to ask.
2. Put the listing's images in its `IMGs/` subfolder.
3. Paste the spec into Claude Code from this folder. Claude reads `CLAUDE.md` and the right gold-standard `.docx`, then creates the listing in Shopify as a **draft**.
4. Review the draft in Shopify and publish it yourself.
5. Update the Product Roster tab in `Platform_Reference.xlsx`.

## Updating listing copy

To change the wording on listings, edit the gold-standard `.docx` files only. `CLAUDE.md` should never need to change because of a copy change. If it seems to, template text has leaked into it. See "Keeping This File in Sync" in `CLAUDE.md`.

## Repo notes

- `.gitignore` excludes Office lock files (`~$*`), macOS metadata (`.DS_Store`, `__MACOSX/`), `.claude/settings.local.json` (which holds machine-specific Claude permissions), and everything inside `IMGs/`. Product photos live in Google Drive only, and `IMGs/.gitkeep` keeps the empty folder in the repo.
- This folder lives in Google Drive. Avoid editing from two machines at once, and let Drive finish syncing before you commit.
