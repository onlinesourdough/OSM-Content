## Verdict: `CHANGES_REQUIRED`

Static review of the inline public OSM Content `v0.13.0` candidate documents and the five fictional synthetic acceptance outputs only (no live Notion schema/API, native composer/publication, whole-profile, or external benchmark verification was performed or is claimed).

---

### Method Review Summary (Passed Areas)

Across `README.md`, `docs/setup.md`, `docs/configuration.md`, `docs/guide.notion.md`, `docs/post-workflow.md`, `docs/writing-voice.md`, `docs/sidebar-icons.md`, and `assets/icon.md`:
- **Interrupted setup & idempotent reuse (`docs/setup.md`):** Strong and complete—ordinary fields and verified database/data-source identity precede self-relations; interrupted setup resumes the same binding and adds only missing fields; uncertain creates reconcile before retry without minting a new key; pre-generated durable keys, canonical URLs with meaningful query params, non-publishing draft verification, unknown-trigger isolation, empty-store readiness, and frozen `v0.10.0` packet subordination are all handled cleanly.
- **Source-only privacy (`docs/writing-voice.md`, `docs/setup.md`, `docs/configuration.md`):** Clear—source-only examples stay in their original system, accessible links are not copy permission, private footage is not uploaded to bypass a missing route, and private material stays private.
- **Faithful/minimal edits & approval/provenance (`docs/writing-voice.md`, `docs/post-workflow.md`, `docs/setup.md`):** Clear separation of `Kind = Own writing` vs `Review = Voice approved`, explicit AI/mixed authorship retention, non-replacement of human calibration examples, rejection retention, engagement/publication ≠ approval, review ≠ publish authority, fixed-wording preservation, and direct future instruction accepted without extra confirmation under existing authority.
- **Destination counts & evidence limits (`docs/writing-voice.md`, `docs/post-workflow.md`, `docs/setup.md`, `docs/sidebar-icons.md`):** Properly distinguishes local vs native counts, missing analytics vs zero, saved skill pages vs native discovery/installation, and API responses vs rendered sidebar icons. The `v0.35.0` link is respected as an intentional release gate, and frozen `v0.10.0` templates/CI-owned guide bodies are respected as out of change scope.

---

### Concrete Findings

#### Required Fixes

1. **Core vs optional schema-binding conflict — `docs/configuration.md` ("A compact owner configuration") vs `docs/setup.md` ("Reuse the core Content foundation" & "Register and verify")**
   - `docs/setup.md` explicitly assigns the single minimum schema binding to the core OSM `0.35.0` Definition or its linked source agreement: *"Keep that binding in the Definition or its linked source agreement, rather than maintaining another editable field map here. A personal configuration links it and owns only chosen editorial details."*
   - `docs/configuration.md`'s `content_workflow` YAML template omits any reference key to the Definition/source agreement and retains an unscoped `field_map: {}` directly under `content_collection: null` with no editorial-only qualifier. This invites agents to duplicate the core minimum field map inside personal configuration, violating the single-owner boundary.
   - **Required fix:** Add a Definition/binding reference key (e.g., `definition_binding_ref: null`) to `content_workflow` in `docs/configuration.md`, and either remove `field_map: {}` or rename/scope it to optional editorial fields/views (e.g., `editorial_fields_and_views: {}`) with a brief note matching `docs/setup.md`.

2. **Over-promotion of a draft-failure diagnosis to an accepted standing rule — `scoped-correction` output (`standing_preference_changes[2]`)**
   - The owner's request states two direct future instructions (*"For my English X posts, crazy is a word I actually use. Don't ban the word."* and *"My Danish client emails can keep their existing restrained tone."*) plus a retrospective diagnosis of why a specific rejected draft failed (*"The problem with that draft was its promise that the tool would do all the work."*).
   - `standing_preference_changes[2]` promotes that retrospective diagnosis into an `accepted` standing rule in `voice:main` (*"Do not promise that a tool will do all the work; avoid overclaiming tool autonomy."*) and artificially narrows a general factual/meaning accuracy constraint to `language: "English", channel: "X posts", situation: "claims about tool capabilities"`.
   - Under `docs/writing-voice.md` ("Learn from the correction") and the case context (*"Update only what the evidence supports"*), the diagnosis belongs on the rejected Edition as its corrected failure reason (`record_dispositions[2]` already captures this); any generalized future-writing rule inferred from it should not be added as an `accepted` standing voice rule (compare `rejected-candidate`, which correctly kept an analogous inference as an `unconfirmed_hypothesis`).
   - **Required fix:** Remove `standing_preference_changes[2]` from accepted standing preference changes (keep the corrected failure reason on `referenced_rejected_draft_edition`, or at most record a clearly separated unconfirmed hypothesis if generalized).

#### Optional Preferences / Non-Blocking Polish

1. **`docs/writing-voice.md` ("Select evidence, not an entire archive"):** The phrase *"In the starter schema, `Kind = Own writing`... and `Review = Voice approved`..."* slightly blurs the core `0.35.0` minimum schema with the optional metadata vocabulary (`Existing Select or body note`) defined in `docs/setup.md` ("Add metadata where the workflow uses it"). Prefer *"In the optional starter metadata (or body notes)..."*.
2. **`docs/writing-voice.md` ("Learn from the correction"):** *"Keep an unconfirmed hypothesis on its Edition..."* assumes an Edition exists; as `evidence-selection` (`source:instruction-2`) shows, a pending observation can also originate on a Source. Prefer *"on its Edition or Source"*.
3. **`docs/setup.md` ("Keep bodies useful"):** Under `Source`, changing *"useful excerpt"* to *"permitted excerpt"* would reinforce `docs/writing-voice.md`'s source-only privacy rule.
4. **`minimal-edit` output (`decisions[1]`):** Minor wording nit—says *"the repeated 'og igen' reduced to 'igen'"* instead of *"'igen og igen' reduced to 'igen'"* (or *"removing 'og igen'"*). Does not affect the final text or counts.
5. **`rejected-candidate` output (`record_dispositions[0]`):** Labels `content:repair-notes` as `"Content Source / Production"`, slightly conflating the `Source` and `Content` record types from `docs/setup.md` (partially induced by the case input giving only `production_id` while mentioning "original source").

---

### Five-Case Independent Assessment

#### Character Count Verification
No inaccurate claimed character counts were found:
- **`minimal-edit`:** Verified exact — original draft is **175** characters (`60 + 1 + 33 + 1 + 80`); `final_text` is **148** Unicode NFC characters (`51 + 1 + 30 + 1 + 65`), within the `<= 150` limit.
- **`destination-length`:** Verified exact — original draft is **124** ASCII characters; `final_text` is **120** ASCII characters (`29 + 1 + 52 + 1 + 37`, `-4` from `", and it"` → `". It"`), within the `<= 120` limit.

#### Per-Case Results

| Case | Result | Assessment |
| --- | --- | --- |
| `minimal-edit` | **PASS** | Exact counts (175 → 148 ≤ 150) with local-only/NFC limitation disclosed; removes only 4 redundant tokens (`egentlig`, `så`, `en del`, `og igen`) while preserving Danish cadence, sentence order, and hedging (`bare prøvet`, `måske`, `jeg tror`); no added ending/hashtag/CTA; states limited calibration; preserves AI-assisted provenance off `Own writing`/`Voice approved` and makes no voice-profile update. (Optional wording nit in `decisions[1]`.) |
| `evidence-selection` | **PASS** | Reuses `voice:main` and existing record IDs without new databases/columns/inbox import; includes only `source:own-1` (`Own writing` + `Voice approved` + `permitted`) with narrow `da`/newsletter/personal-work-reflection scope and thin-calibration note; excludes `source:instruction-2` (dictated assistant instruction, `Reviewed` only) from voice examples and accepted rules while permitting an optional separate pending observation; excludes `edition:ai-3` (AI candidate, `Reviewed`, `published: true` ≠ approval) and keeps status/AI authorship on the Edition. |
| `rejected-candidate` | **PASS** | Reuses existing IDs; retains `edition:repair:v1` as rejected with exact failure reasons and rejects private-preview clicks as approval; retains `edition:repair:v2` as approved for this edition only (unpublished) and links it in `voice:main` as a scoped `Voice approved` example while rightly keeping `Kind` provenance separate (does not assign `Own writing` without proof); keeps inferred generalization as an `unconfirmed_hypothesis` on `edition:repair:v2` linked from `voice:main`'s pending observations; no banned-word list or publication. (Optional terminology nit in `record_dispositions[0]`.) |
| `scoped-correction` | **FAIL (Required Fix #2)** | Correctly applies the owner's direct instruction without re-asking, supersedes `"Avoid crazy in all writing."` with history/provenance preserved, accepts allowing `'crazy'` for English X posts, preserves Danish client-email restrained tone, and corrects the rejected draft's failure reason on its Edition. Fails strictly on `standing_preference_changes[2]`, which over-promotes the draft-specific failure explanation into an extrapolated `accepted` standing rule (`"avoid overclaiming tool autonomy"`) artificially scoped to English X posts. |
| `destination-length` | **PASS** | Exact counts (124 → 120 ≤ 120 ASCII) with local ASCII method and unavailable-native-composer limit clearly stated (no real-platform or native-validation claim); preserves fixed first sentence verbatim including `"I think"`; minimal `-4` edit (`", and it"` → `". It"`) keeps all facts, qualifications, authorship, and thought order; runs independent Meaning/Voice/Destination checks; marks AI-assisted draft disposition on Edition; `draft_not_sent` with no publish authority claimed. |

