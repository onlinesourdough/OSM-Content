# One working method per channel

OSM Content is a backbone: general requirements, best practices and adaptable templates. The owner builds a setup that fits their energy, tools and goals. Notion is the default runtime; equivalent records, editable originals and review evidence can live in another selected system.

## Two skill axes

The five responsibilities describe the work across its life. A channel working method (arbejdsform) describes how a piece is assembled to fit that channel, the owner's vision and the channel goal. Keep one small working method for each active channel. Reuse an existing useful method before adding a skill.

| Responsibility | How it uses the channel method |
| --- | --- |
| Setup | Inspect existing records and methods, resolve only relevant gaps, and adapt the selected channel skills |
| Intake | Capture the idea or permitted reference and why it matters |
| Prepare | Gather the evidence, brief and accessible material the channel needs |
| Produce / Distribute | Assemble the piece with its channel method, run the quality gate, request owner review, then deliver only under actual authority |
| Learn | Keep useful feedback with the piece; revise a lasting choice on its owning record |

The five [v0.10.0 responsibility packets](../README.md#adapt-the-useful-templates) remain frozen imports. Use this guide and [configuration](configuration.md) beside them when adapting a personal method; old packets cannot override the current plugin binding, retention or publication rules.

## Work with the existing base records

Reuse the base records selected by OSM-plugin. These are kinds of information to find, not a compulsory title list or a request for blank pages.

| Information needed | Where to look |
| --- | --- |
| Profile/soul, brand, priorities/tasks, offers, voice, audience, positioning and operating policy | Existing Knowledge records and their linked authoritative sources |
| Content vision and channel strategy | Existing Knowledge direction, channel and working-preference records; link the relevant contribution of content |
| Cadence, formats and reusable editorial templates | Existing working-preference records in Knowledge, production templates/material in Content, or their selected external equivalents |
| Sources, production material, drafts, editions and feedback | The plugin's selected Content route; preserve its minimum schema and existing field equivalents |
| Working steps | The owner's adapted personal Skills, pointing to the relevant records |
| Lasting decisions and reasons | Memory when useful; routine production stays with its record |

A Content-side Fundament view can collect production templates and material used as building blocks, while linking to vision, strategy, cadence or format guidance already owned in Knowledge. Do not move or duplicate those records just to fill a view. [Setup](setup.md#fundament--byggesten-views) explains the optional filters and status meanings.

The [entry forms](../templates/knowledge-entries) are prompts to fill a real gap on an existing owner record. They do not establish a second brand, voice, priorities or strategy system. A red thread is optional coherence guidance; existing vision, voice and policy can already cover it.

## A short channel guideline

Start with [content-channel](../templates/content-channel/SKILL.md), the generic new-channel skeleton, or a channel example:

| Channel | Skeleton |
| --- | --- |
| Newsletter | [channel-newsletter](../templates/channel-newsletter/SKILL.md) |
| LinkedIn | [channel-linkedin-post](../templates/channel-linkedin-post/SKILL.md) |
| X | [channel-x-post](../templates/channel-x-post/SKILL.md) |
| YouTube | [channel-youtube](../templates/channel-youtube/SKILL.md) |

Each guideline links to vision, channel goal, audience, voice, policy and the chosen format. Its steps explain how to select the point, assemble the piece, check channel fit and hand it to review. It may refer to a reusable format without copying its facts. Owner-specific language, offers, voice and editorial choices stay at their existing owners.

One production record can cover one or more channels. Keep one editable original for each independently maintained version and unambiguous review/delivery evidence per destination; a separate Edition is useful when editing, review or delivery needs its own identity. The owner selects record grouping and reuse policy in their setup.

The [newsletter-to-posts helper](../templates/channel-newsletter-to-posts/SKILL.md) is an optional handoff to selected channel methods. A newsletter is one possible original. No channel is a mandatory upstream source.

## A schedule helps; the owner chooses it

A documented cadence makes workload, upcoming review and gaps visible. The [content-schedule skeleton](../templates/content-schedule/SKILL.md) reads an existing [cadence entry](../templates/knowledge-entries/cadence.md) in Knowledge or its equivalent and proposes a plan. It prescribes no frequency, posting time or daily workflow. The owner may leave cadence unselected; that does not block an ordinary draft.

Record only actual choices: selected channels, rhythm or on-demand use, timezone where times matter, optional planning horizon, review route, and limits when wanted. A planning entry is distinct from a live scheduler job. Installing or adopting the skill creates no automation.

Optional patterns include a short daily owner approval window for work due soon, backed by a bank replenished on a chosen cycle; and owner-named value categories with caps to keep one theme or selling from dominating. Neither pattern is a prerequisite. Approval before publication remains required for each final version and destination.

## Quality gate, comments and owner approval

The shared [quality-gate skill](../templates/channel-quality-gate/SKILL.md) checks the actual text or media before requesting owner review and again before delivery when the version or conditions have changed. Check meaning, evidence, attribution, vision, channel goal, voice, format, privacy and rights. Apply cadence or category limits only when selected. Partial voice evidence stays explicit; a first draft does not require complete style calibration.

Apply review comments to the editable original and check that the resulting piece makes sense. Resolve comments whose requested changes are addressed. A contradictory or unresolved comment holds the review handoff; record the precise blocker rather than marking it resolved. An owner decision can be requested without presenting an unfinished draft as ready.

In Notion, keep the draft in ordinary editable text that the owner can comment on, with review notes beside it. For video, link the actual revision and use timecoded review notes. A code block may hold code examples, but should not be the only editable copy of a prose draft.

Use the existing review section (or a sufficient existing field) for gate result/date, version, destinations, open issues and owner approval. No new approval Select is required. Only the owner marks approval. Preserve prior approval evidence; a changed version needs renewed approval. A gate pass, Ready, or a voice exemplar selection is not publication approval. Publishing or activating a delivery job also needs applicable destination authority and verified outcomes under the [release contract](../templates/content-produce/references/release-contract.md).

A second-model review is an optional switch on the owner's review policy, with no required model. Record findings and unresolved disagreements with the version reviewed; the switch grants no extra data-sharing permission.

## Build and check an owner's setup

1. Inspect the selected plugin routes, existing base records, editorial original and useful skills. Respect an external route or deferred Content setup.
2. Use the [setup prompts](../templates/knowledge-entries/setup-interview.md) only for gaps affecting the selected task. Save a supported choice once, at its existing owner. Do not repeat a complete interview on normal use.
3. Adapt one channel guideline through the available skill-management method. Record template provenance and local changes; verify its pointers and actual discovery/invocation separately.
4. Exercise a real, bounded draft in a verified non-publishing state, run the gate and request owner review. Structure alone does not prove useful work or complete calibration.
5. Add cadence, another channel, recurring planning or delivery only when selected and authorized. Keep superseded guidance as linked history rather than deleting it.

Channel, schedule and gate skeletons remain Git sources, outside the eight synced Notion catalogue pages. The public guide links to them. Adopting a private skill and publishing a method release are separate authorized actions.
