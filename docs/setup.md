> Build your editorial workflow on the completed, selected OSM foundation. Reuse the owner's home, business context and Content route; keep originals, identities and useful integrations. Content adapts working methods, channels and formats above that foundation.

## Check the core handoff

Read the owner's exact AI operating model home (or existing Data & Context entry) and selected operating policy. Find their existing Knowledge, Memory and personal Skills routes. Locate the current goals, audience, offers, voice and working preferences. These remain business context in Knowledge; this extension does not create a second strategy or Goals database.

Read the actual selected Content binding: existing Notion, external workflow, genuinely deferred, or a new empty store prepared by core Setup. A completed Content-ready handoff has a working selected route and its required foundation; installation alone does not prove that. A deferred route is a valid owner choice, not a ready production destination. If a selected foundation is incomplete, resume core Setup on the same identities before dependent editorial work. Do not repeat database onboarding or create a second store here.

An explicit request to adapt the editorial workflow normally covers ordinary chosen editorial configuration inside the authorized home. Reuse standing authority, the core minimum schema and sufficient existing field equivalents; add only useful selected editorial details. Inspect both schema dependencies and row-level triggers before writing: a new row, Type/Status choice or checkbox can publish to a website, send mail or trigger another system. Do not use an integrated destination for a sample until the chosen draft state is confirmed non-publishing. Unknown destinations, consequential changes to an integration or new external access need a concrete resolution; they are not permission to create another account or content mirror.

The personal configuration should link the owner's direction/goals, audience and perspective, voice/style and actual working choices. Reuse existing Knowledge records; these are responsibilities, not mandatory <code>vision.md</code> files or new databases. Choose a purpose for each active channel, including newsletter/email as its own channel. The configuration guide provides adaptable channel-role examples. Use the [setup prompts](../templates/knowledge-entries/setup-interview.md) only to resolve relevant missing input. Save each supported answer at its existing owner; do not add empty mandatory pages.

## One collection, three record types

| Type | What it owns | Example |
| --- | --- | --- |
| Source | A reference, raw observation, transcript or inspiration and our annotation | A saved article or recording reference |
| Content | An idea growing into a production, with one stable identity | An explanation based on real work |
| Edition | An independently edited version for a format or destination | A LinkedIn post or newsletter derived from that production |

An idea can become a production on the same Content record. One production record can cover one or more channels; grouping is an owner choice. Keep a single editable original per independently maintained version and review/delivery evidence per destination. Create an Edition when independent editing, packaging, review or delivery benefits from its own identity. One newsletter may use several sources or productions. A Source keeps its own state when something derived from it is published.

## Reuse the core Content foundation

Core OSM 0.35.0 introduces a Content proposal during authorised new-home Setup: reuse an existing Notion store, register an external workflow, record a deferral, or create one empty Notion store within the accepted plan. Installing a package or resuming an established home does not create a collection. The editorial methods remain optional. On an older core release, use this extension only under the owner's explicit selected setup scope; do not claim the new core default.

The core's [database field definitions](https://github.com/onlinesourdough/OSM-plugin/blob/v0.35.0/skills/osm-data-context/assets/database-fields.md) are the single minimum field/type list. Read the selected Definition and its actual binding; reuse sufficient field equivalents, existing identities and external owners. Keep that binding in the Definition or its linked source agreement, rather than maintaining another editable field map here. A personal configuration links it and owns only chosen editorial details.

When resuming an incomplete core foundation, ordinary fields and verified database/data-source identity come before its self-relations; this remains core Setup work. If interrupted, resume the same binding and add only missing fields; an uncertain write needs reconciliation before retry. An empty store can be structurally ready without a post, sample, personal method or publishing action. An unknown trigger holds only the dependent writes. Frozen older template packets are references, not authority to create a second store or override the current binding, retention or trigger agreement.

Notion does not enforce Key uniqueness. Record the owner's key convention in configuration; query the key/origin and semantic overlap before creating. For a URL source use the verified canonical origin without stripping meaningful query parameters. For another new record choose a durable generated key before the first create, retain that key through the attempt and reuse it on retry. A source URL does not identify an independently edited edition. Serialize a shared writer where needed. After an uncertain create, inspect that key and actual service result before any retry; never mint a new key just because the response was lost.

## Add metadata where the workflow uses it

| Property | Suggested type | Meaning |
| --- | --- | --- |
| Kind | Existing Select or body note | Source authorship, such as Own writing or Inspiration; record mixed authorship explicitly |
| Review | Existing Select or body note | Inspected or explicitly Voice approved; separate from production/delivery Status |
| Medium | Select | Text, video, audio or mixed; independent of platform |
| Format | Rich text or existing Select | How-to, reflection, showcase, interview or another useful form |
| Channels | Multi-select | Only the owner's selected destinations; do not activate every platform |
| Revised | Date, optional | A substantive record, method or editorial-annotation change; not blanket reverification |
| Review due | Date, optional | A justified reconsideration point; keep the reason beside the affected claim |
| Publish date | Date | Verified time for the primary delivery, or omitted when ambiguous; the per-destination section remains authoritative |
| Public URL | URL | Actual primary output when available; multiple deliveries retain their own URLs in the delivery section |
| Last updated by | Native last-edited-by, or an existing explicit client field | Preserve the distinction between the API actor and a known editing client; do not invent an author |
| Created / Last edited | Native system fields, if useful | Technical record times, never evidence freshness |

Reuse source/import/processing fields already present. Do not overwrite them with Revised, backfill unknown dates with today, or add a universal recency score. Reads, imports, formatting and unchanged runs do not bump Revised. Review due is a review signal, not expiry or falsehood. On a Source, Revised dates our annotation; the external original retains its own date. Personal skill source/version remains separate from its record revision.

## Practical starter states and views

Use one Select with only the values needed by the chosen workflow; map existing values deliberately. These type-specific transitions are a starter:

| Type | Normal progression | What allows the transition |
| --- | --- | --- |
| Source | Inbox → Reviewed, or Archived | The source/coverage was actually inspected; Reviewed does not mean every external claim was verified. A derivative's publication never publishes the Source. |
| Content | Inbox → Selected → Preparing → Material ready → Producing → Ready → Scheduled / Published only for direct delivery | The owner or configured selection policy selects it. Material ready requires actual accessible text/media and a known revision. Ready requires the configured review of the finished original. |
| Edition | Preparing / Producing → Ready → Scheduled / Published | Ready requires the configured review; publication approval is still an owner decision. Scheduled needs the service's real job ID; Published needs verified delivery evidence. |

Paused, Needs review and Archived are optional production states. Do not confuse these with Knowledge's selection/quality statuses below. Run the shared quality gate before owner review, while the piece is still being produced. Record its result in the review section. Apply corrections, resolve addressed comments and check that the text itself makes sense; unresolved issues hold the review handoff. In Notion, keep draft prose directly commentable rather than only in a code block.

Only the owner marks approval of the final version and destinations. Use the existing review section or a sufficient existing field; no new approval Select is required. Preserve earlier approval evidence, and require renewed approval when material changes. Ready, a gate pass and voice approval are separate from publication approval. Scheduled/Published also require actual delivery authority and verified service evidence. A directly delivered original can keep its review and delivery section on the Content record without a duplicate editable body.

For each selected destination retain its delivery state, actual revision, account, date/URL or send/job ID in a delivery section. One edition may have several deliveries. Failed and Outcome unknown describe real delivery results; if some destinations succeeded, retain Partially published until the others are reconciled. Do not let one public URL erase a failed email. Add those Select values only when used; the delivery section is authoritative for the individual results.

Start with a few views of the same records: Inbox; Ideas (Type Content); In production; Editions (Type Edition); Sources/library (Type Source); Follow-up (Needs review, failed/unknown delivery or Review due, where selected). A due view does not replace useful new evidence or route drift. Do not add another measurements database or dashboard until its scale warrants one.

## Keep bodies useful

Use only the sections a record needs:

- Source: original location/attribution, why saved, permitted excerpt or supported annotation, source date/coverage and uncertainty. For creative references, record the specific technique and relevant time range; follow the [reference-library workflow](reference-library.md) when it informs reusable guidance.
- Content: angle, chosen goal and its Knowledge reference/revision, audience, evidence, brief/script, actual material links, and next useful action. A goal revision is its owning record link plus Revised/version, or an explicit selected statement/date when no semantic revision exists; preserve that selection rather than inventing a date.
- Edition: parent/source links, editable body or media-project reference, destination, review section, delivery evidence and dated feedback. The review section holds the quality-gate result, the gate date, any failed checks, the checked version/destinations, open comments/issues, and separately the owner's approval evidence. Use the existing review policy; the [gate prompts](../templates/knowledge-entries/quality-gate.md) can fill a real gap. The agent records the gate result, never owner approval.

A brief is not footage. A Source summary is not the full transcript. Separate original words, our annotation and a proposed angle. Preserve human writing and useful prior reasons while revising the affected current section instead of appending a contradictory history.

## Video and other large files

Notion is the editorial index and context home, not mandatory storage for large footage or project files. Keep media in an owner-selected local or cloud location and the actual editor project in its chosen workspace. Record the original's location, meaningful revision, relevant assets and access route on its production; keep real clip time ranges when excerpts exist.

Record who owns storage/backup and what the agent can actually access. A link is not a backup. A local path is scoped to its host, not a universal data location. Do not upload private footage to a cloud service to bypass a missing route. Existing editors, external editorial originals and analog material can stay; map one editable original and its handoff rather than making a competing copy.

## Reuse base records and editorial building blocks

Find the relevant profile/soul, brand, priorities/tasks, offers, audience, voice, positioning and operating-policy records in the plugin's existing Knowledge route. These are kinds of information, not compulsory titles. Content vision and channel strategy link that direction to production. Cadence and formats are working preferences in Knowledge or their existing equivalent; reusable production templates/material belong in Content. Do not move existing records or duplicate their facts to impose this split.

Use the [entry forms](../templates/knowledge-entries) only to fill real gaps. A red thread, separate format page or dedicated gate page is optional when existing guidance already serves the task. Adapted Skills hold short procedures and references, rather than another profile/brand/priority system. The [channel-skills guide](channel-skills.md) explains the responsibility axis plus one assembly guideline per selected channel. An agent replicates [content-channel](../templates/content-channel/SKILL.md); the existing channel files are thin example copies. The five frozen responsibility packets remain unchanged.

A documented [cadence](../templates/knowledge-entries/cadence.md) and [schedule skeleton](../templates/content-schedule/SKILL.md) help plan workload and review. The owner chooses whether and how to use them; no rhythm, horizon or daily workflow is required. A planning choice creates no automation.

## Foundation views

Before ideas and production accumulate, make the base records the module and agent get most value from easy to find. Use **Foundation** as the recommended English view name. Start with the small set of kinds below; names are inspiration, not compulsory pages or a new classification. Reuse existing records even when they combine several kinds.

| Kind | Simple name inspiration | What Content uses |
| --- | --- | --- |
| Owner and audience | About / Soul | Profile, brand, audience and point of view |
| Direction | Vision | Goals, priorities, offers and channel strategy |
| Expression and boundaries | Voice / Policy | Voice, operating rules and review authority |
| Working choices | Plan | Selected cadence and formats |
| Production building blocks | Templates | Reusable production templates and material |

A best-practice Foundation view in Knowledge selects the relevant existing owners of direction, voice, audience, policy and working choices. In Content, select reusable templates or production building blocks and link the Knowledge owners where appropriate. A thin view is valid; create no empty mandatory pages, parallel stores or copies just to fill it. Memory needs few or no such files.

Filter using sufficient existing Kind/tags, explicit record selection or suitable existing metadata. Add an optional foundation marker only when a useful view needs it and schema changes are authorized; the method adds no required column. Exclude Superseded records from the working foundation view and retain them in All/history. Verify actual view membership; a view is not an access boundary.

Knowledge status meanings follow the plugin: **Current** = selected for use; **Needs review** = useful uncertainty, never age alone; **Superseded** = replaced and retained history. Historical temporal scope is separate, so a historical record can still be Current. Keep Current and All views, with optional Attention (also called **Needs attention**) for flagged records or justified review dates. Needs attention is a view, not a topic or niche. Do not apply these selection meanings to Content delivery states.

Reuse one current owner per fact; mark genuinely replaced guidance Superseded with its replacement link, rather than deleting it. Do not mark it obsolete just for being old.

## Register and verify

1. Reuse or save the verified Content binding in the existing Definition or its source agreement. Link it from personal configuration; keep selected editorial fields/views there and preserve general goals and policy ownership.
2. Adapt only the useful skill templates into the owner's personal Skills through the available skill-management method. Check existing methods and collisions first; keep their selected versions/references and human originals. Responsibility templates and channel-skill templates stay distinct. A channel skill links the relevant base records and production building blocks above.
3. When the owner selects the editorial workflow, exercise one bounded authorized example in a verified non-publishing state: capture a source/idea, prepare the needed material, and follow its actual next handoff. Do not publish just to prove setup. A repeat capture/setup must reuse identities. For a one-off capture without saved configuration, inspect the actual schema, key convention and integration-safe draft state, reuse standing write authority and resolve only material gaps. Full setup or a new configuration record is not a prerequisite for that isolated safe task.
4. Report separately what is mapped, created, adapted, enabled/discoverable, actually exercised and still missing. A saved skill page is not proof of native discovery or installation.

Existing OSM upkeep can maintain this selected collection and definition under its normal policy. Setup does not create a second daily writer, a production schedule, subscriber sync or outbound publication.
