## Verdict: `ACCEPT`

Static, read-only review of the three updated inline documents (`docs/configuration.md`, `docs/writing-voice.md`, `docs/setup.md`) and the independent blind rerun of `scoped-correction` (`ACTUAL_ATTEMPT2`). The core `v0.35.0` tag link remains treated strictly as a publication gate, not a release claim. The four prior `PASS` cases (`minimal-edit`, `evidence-selection`, `rejected-candidate`, `destination-length`) were **not** rerun and are not claimed as re-verified here; no live Notion/API, native composer, or external benchmark checks were performed.

---

### Resolution of Prior Required Findings

1. **Core vs. optional schema-binding conflict (`docs/configuration.md` vs. `docs/setup.md`) — RESOLVED**
   - Replacing `content_collection: null` and unscoped `field_map: {}` with `definition_binding_ref: null` and `editorial_fields_and_views: {}` eliminates minimum-schema duplication cleanly.
   - The accompanying paragraph directly mirrors `docs/setup.md`: the verified route and minimum fields stay in the Definition or source agreement, the editorial map holds only selected workflow additions and views, and `integration_triggers_and_safe_states` explicitly defers to the authoritative source agreement rather than competing with it.
   - **Substantive regressions:** None detected across `docs/configuration.md` or `docs/setup.md`. (The prior optional polish changing `"useful excerpt"` to `"permitted excerpt"` in `docs/setup.md` was also cleanly applied.)

2. **Over-promotion of candidate failure diagnosis (`docs/writing-voice.md` & `scoped-correction`) — RESOLVED**
   - **Guidance check:** The added sentences in `docs/writing-voice.md` (*"A diagnosis of why one candidate failed belongs on that candidate; it is not a standing voice rule by itself. Keep factual accuracy as a meaning check, rather than inventing a channel-specific voice preference from a factual error."*) draw a crisp, non-overfitted three-way boundary:
     1. Direct owner instructions about future writing remain accepted immediately under existing maintenance authority without re-asking (**direct-owner-instruction learning is fully preserved**).
     2. Retrospective draft-failure diagnoses stay on the rejected candidate/Edition, with factual/commitment accuracy handled as a meaning check.
     3. Inferred patterns remain unconfirmed hypotheses on their Edition or Source until confirmed or retired.
   - **Substantive regressions:** None detected in `docs/writing-voice.md`. The phrasing (*"by itself"*, *"from a factual error"*) avoids suppressing explicit future-writing rules about hype or tone when directly instructed by the owner. (Prior optional polishes clarifying `"optional starter metadata or body notes"` and `"Edition or Source"` were also cleanly applied.)

---

### Concrete Blockers

- **None.**

*(Non-blocking micro-note: in `ACTUAL_ATTEMPT2`, `standing_preference_changes[3]` logs an explicit no-op audit entry `action: "no_standing_voice_rule_added"` inside the changes array. It clearly does not add or accept a standing rule and aligns with `record_dispositions[0]`'s `"Do not store candidate production status or failure diagnosis here"`, so it is benign.)*

---

### Case Assessment

| Case | Status | Assessment |
| --- | --- | --- |
| `scoped-correction` (independent blind rerun, Attempt 2) | **PASS** | Solves prior Required Fix #2 without losing direct-owner-instruction learning. Applies the owner's direct instructions to `voice:main` without asking for re-confirmation; supersedes `"Avoid crazy in all writing."` with history and Danish-email provenance intact; accepts allowing `'crazy'` scoped strictly to English X posts; preserves restrained tone for Danish client emails; keeps the rejected draft's overpromise diagnosis on `referenced_rejected_draft_candidate` as a meaning/commitment failure rather than promoting it to a standing voice rule; avoids banned-word lists, intentional mistakes, global persona shifts, and delivery claims. |
| `minimal-edit`, `evidence-selection`, `rejected-candidate`, `destination-length` | **Not rerun** | Prior static `PASS` results stand unchanged; not re-executed against the revised text. |

---

### Quality / Value Score

**9.2 / 10** — Both required fixes are resolved cleanly at the method level with zero substantive regressions, the independent blind rerun confirms the updated guidance changes agent behavior in the intended direction without breaking direct-owner-instruction learning, and ownership/evidence boundaries are tight and operational. The remaining margin reflects static-only evidence (the four unaffected cases were not rerun, and live Notion/native-counter behavior plus the `v0.35.0` core tag gate remain outside this review).

