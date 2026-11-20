> Build the Content extension on an existing OSM foundation. Reuse the owner's Notion home and general business context. Create only missing content-specific structure; keep originals, identities and useful integrations.

## Before you create anything

Read the owner's exact AI operating model home (or existing Data & Context entry) and selected operating policy. Find their existing Knowledge, Memory and personal Skills routes. Locate the current goals, audience, offers, voice and working preferences. These remain business context in Knowledge; this extension does not create a second strategy or Goals database.

Inspect the existing content workflow, database schema, integrations and media locations. A ready OSM setup does not imply a Content database exists. A similar title does not identify the canonical database. Record whether you will reuse, adapt or create, and resolve only missing choices that affect this work.

An explicit request to set up this extension normally covers the missing collection and ordinary properties inside the owner's authorized home; reuse that authority. Inspect both schema dependencies and row-level triggers before writing: a new row, Type/Status choice or checkbox can publish to a website, send mail or trigger another system. Do not use an integrated destination for a sample until the chosen draft state is confirmed non-publishing. Unknown destinations, consequential changes to an integration or new external access need a concrete resolution; they are not permission to create another account or content mirror.

The personal configuration should link the owner's direction/goals, audience and perspective, voice/style and actual working choices. Reuse existing Knowledge records; these are responsibilities, not mandatory vision.md files or new databases. Choose a purpose for each active channel, including newsletter/email as its own channel. The configuration guide provides adaptable channel-role examples.

## One collection, three record types

| Type | What it owns | Example |
| --- | --- | --- |
| Source | A reference, raw observation, transcript or inspiration and our annotation | A saved article or recording reference |
| Content | An idea growing into a production, with one stable identity | An explanation based on real work |
| Edition | An independently edited version for a format or destination | A LinkedIn post or newsletter derived from that production |

An idea can become a production on the same Content record. Create an Edition when it has its own editable text, packaging, review or delivery. One newsletter may use several sources or productions. A Source keeps its own state when something derived from it is published.

## Baseline properties

These are meanings and starter names, not a migration command. Map suitable existing properties before adding columns. Record the actual property names, types and canonical database/data-source IDs in the owner's configuration.

| Property | Starter Notion type | Use |
| --- | --- | --- |
| Title | Title | Human-readable subject |
| Key | Rich text | Stable record identity; retain an existing key, otherwise create a durable origin-based or generated key |
| Type | Select: Source, Content, Edition | Record responsibility |
| Status | Select | State within that responsibility, using the transitions below |
| Summary | Rich text | Short current explanation, searchable without loading the whole body |
| Source URL | URL | External original when one exists; keep other origins in the body |
| Source date | Date | Actual origin/event date, if known; never the import date by default |
| Sources | Self-relation, multiple | Links to the actual Source records used |
| Derived from | Self-relation, multiple | Links an Edition to its Content parent(s), or a deliberate adaptation to its predecessor |

For a new collection, create the ordinary columns first, read its actual data-source ID, then add self-relations using that ID and verify both ends. Do not put a database block ID where a data-source ID is required. Prefer one-way relations unless a useful reciprocal view justifies paired properties. Never retarget a populated relation without a checked migration.

Notion does not enforce Key uniqueness. Record the owner's key convention in configuration; query the key/origin and semantic overlap before creating. For a URL source use the verified canonical origin without stripping meaningful query parameters. For another new record choose a durable generated key before the first create, retain that key through the attempt and reuse it on retry. A source URL does not identify an independently edited edition. Serialize a shared writer where needed. After an uncertain create, inspect that key and actual service result before any retry; never mint a new key just because the response was lost.

## Add metadata where the workflow uses it

| Property | Suggested type | Meaning |
| --- | --- | --- |
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
| Edition | Preparing / Producing → Ready → Scheduled / Published | Ready requires the configured review, including a human where selected. Scheduled needs the service's real job ID; Published needs verified delivery evidence. |

Paused, Needs review and Archived are optional across types. Agents may perform the configured review when the owner's policy permits it; self-review does not replace a required human/independent gate. Never infer publication authority from Ready. A directly published original can retain its delivery section on the Content record when that is the existing configured workflow; no duplicate editable body is required.

For each selected destination retain its delivery state, actual revision, account, date/URL or send/job ID in a delivery section. One edition may have several deliveries. Failed and Outcome unknown describe real delivery results; if some destinations succeeded, retain Partially published until the others are reconciled. Do not let one public URL erase a failed email. Add those Select values only when used; the delivery section is authoritative for the individual results.

Start with a few views of the same records: Inbox; Ideas (Type Content); In production; Editions (Type Edition); Sources/library (Type Source); Follow-up (Needs review, failed/unknown delivery or Review due, where selected). A due view does not replace useful new evidence or route drift. Do not add another measurements database or dashboard until its scale warrants one.

## Keep bodies useful

Use only the sections a record needs:

- Source: original location/attribution, why saved, useful excerpt or supported annotation, source date/coverage and uncertainty. For creative references, record the specific technique and relevant time range; follow the [reference-library workflow](reference-library.md) when it informs reusable guidance.
- Content: angle, chosen goal and its Knowledge reference/revision, audience, evidence, brief/script, actual material links, and next useful action. A goal revision is its owning record link plus Revised/version, or an explicit selected statement/date when no semantic revision exists; preserve that selection rather than inventing a date.
- Edition: parent/source links, editable body or media-project reference, destination, reviewed version, delivery evidence and dated feedback.

A brief is not footage. A Source summary is not the full transcript. Separate original words, our annotation and a proposed angle. Preserve human writing and useful prior reasons while revising the affected current section instead of appending a contradictory history.

## Video and other large files

Notion is the editorial index and context home, not mandatory storage for large footage or project files. Keep media in an owner-selected local or cloud location and the actual editor project in its chosen workspace. Record the original's location, meaningful revision, relevant assets and access route on its production; keep real clip time ranges when excerpts exist.

Record who owns storage/backup and what the agent can actually access. A link is not a backup. A local path is scoped to its host, not a universal data location. Do not upload private footage to a cloud service to bypass a missing route. Existing editors, external editorial originals and analog material can stay; map one editable original and its handoff rather than making a competing copy.

## Register and verify

1. Save the real Content route, field map, chosen views and configuration reference in the owner's existing definition/context. Preserve general goals and policy ownership.
2. Adapt only the useful skill templates into the owner's personal Skills through the available skill-management method. Check existing methods and collisions first; keep their selected versions/references and human originals.
3. Exercise one bounded authorized example in a verified non-publishing state: capture a source/idea, prepare the needed material, and follow its actual next handoff. Do not publish just to prove setup. A repeat capture/setup must reuse identities. For a one-off capture without saved configuration, inspect the actual schema, key convention and integration-safe draft state, reuse standing write authority and resolve only material gaps. Full setup or a new configuration record is not a prerequisite for that isolated safe task.
4. Report separately what is mapped, created, adapted, enabled/discoverable, actually exercised and still missing. A saved skill page is not proof of native discovery or installation.

Existing OSM upkeep can maintain this selected collection and definition under its normal policy. Setup does not create a second daily writer, a production schedule, subscriber sync or outbound publication.
