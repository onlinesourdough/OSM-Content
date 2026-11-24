# OSM Content

<img src="assets/icon.png" alt="OSM Content" width="56" height="56">

Turn real work, ideas and references into content worth sharing. Keep the
author's voice, choose a purpose for each edition and learn from the response.

OSM Content is an optional operating model: general requirements, best practices,
templates and skill skeletons for
[The Onlinesourdough Method](https://github.com/onlinesourdough/OSM-plugin).
It uses the business foundation in the owner's AI operating model home.
Notion is the default runtime; equivalent records and review evidence can live
outside it. Existing editors, human workflows and useful personal skills can stay.

## Start here

For one post, use the [short-post workflow](docs/post-workflow.md).
For writing style and corrections, use [the author's voice](docs/writing-voice.md).
For one skill per channel on a shared Knowledge layer, use [channel skills](docs/channel-skills.md).
For initial setup, give your agent this repository and your private context-home
link. Ask it to read [setup](docs/setup.md) and
[configuration](docs/configuration.md), inspect what exists and adapt only what
is missing. Your own home supplies the routes and permissions.

The [Notion guide](https://gustavanderson.notion.site/40d6d2e17f5681219a81e13317a19339)
is the readable companion. [Releases](https://github.com/onlinesourdough/OSM-Content/releases)
identify the shared source. Actual goals, channels, voice, media and adapted
personal skills stay in the owner's private home.

## A small working loop

1. Save the idea or reference and why it matters.
2. Choose the reader, purpose and your own contribution.
3. Write, record or edit only the editions that help.
4. Review and deliver under the owner's selected publication authority.
5. Keep the result and one useful lesson for the next piece.

A short post can stand alone. Different channels can serve different goals.
An informative or reflective post can end with its point; a sales invitation
or external link is a choice, not a requirement.

## The foundation

Core OSM 0.35.0 owns the new-home Content proposal and the single minimum
schema. Reuse its selected Notion or external route, or respect a deferral;
installation and ordinary resume create nothing. Editorial methods stay optional.
See [setup](docs/setup.md) for the version boundary and interrupted setup.

A selected Content collection has three useful responsibilities:

| Record | Keeps |
| --- | --- |
| Source | Original attribution, why saved and observed details |
| Content | The author's idea or production, evidence and next action |
| Edition | An independently edited version, review and delivery result |

Knowledge owns goals, audience, offers and voice. Personal Skills carry the
chosen workflow. Media and editor projects use mapped storage; a link is not
a backup. [Creative references](docs/reference-library.md) can improve an
angle, explanation or treatment without becoming an imitation of the creator.

## Adapt the useful templates

Five responsibilities can be covered by existing personal methods. They do
not require five agents or five new skills.

| Responsibility | Starting template |
| --- | --- |
| Setup | [content-setup](templates/content-setup/SKILL.md) |
| Intake | [content-intake](templates/content-intake/SKILL.md) |
| Prepare | [content-prepare](templates/content-prepare/SKILL.md) |
| Produce / Distribute | [content-produce](templates/content-produce/SKILL.md) |
| Learn | [content-learn](templates/content-learn/SKILL.md) |

A second axis is one small working method (arbejdsform) per active channel:
how to assemble a piece so it fits the channel, the owner's vision and its goal.
Reuse the plugin's existing base records and keep business facts at their owners.
The primary [content-channel](templates/content-channel/SKILL.md) skeleton is
replicated and filled in by an agent for the selected channel or format. The
existing newsletter, LinkedIn, X and YouTube files are thin example copies,
not a catalogue that needs to grow. Schedule and gate are shared helpers:

| Use | Example copy or shared helper |
| --- | --- |
| Newsletter | [channel-newsletter](templates/channel-newsletter/SKILL.md) |
| LinkedIn | [channel-linkedin-post](templates/channel-linkedin-post/SKILL.md) |
| X | [channel-x-post](templates/channel-x-post/SKILL.md) |
| YouTube | [channel-youtube](templates/channel-youtube/SKILL.md) |
| Optional newsletter reuse | [channel-newsletter-to-posts](templates/channel-newsletter-to-posts/SKILL.md) |
| Check before owner review/delivery | [channel-quality-gate](templates/channel-quality-gate/SKILL.md) |
| Plan from the owner's cadence | [content-schedule](templates/content-schedule/SKILL.md) |

A schedule is useful best practice; its rhythm and optional horizon are owner
choices. The skeleton activates no jobs. The quality gate checks the coherent
text and resolved comments before owner review; only the owner marks approval
of the final version/destinations. Approval and delivery authority are separate.

[Channel skills](docs/channel-skills.md) explains the two axes and adoption.
The [entry forms](templates/knowledge-entries) fill real gaps in existing
records; they do not require a new profile, strategy or empty page list.
[Setup](docs/setup.md#foundation-views) describes optional foundation views.

## Versions and upkeep

The proposed method version is **v0.14.0**. The five retained **v0.10.0 Draft templates**
are unchanged imports of the earlier public Notion template edition 2026-11-05.1,
retained in [the initial import](https://github.com/onlinesourdough/OSM-Content/commit/b8dc567), with hashes in
[provenance.json](provenance.json). Their template versions do not become
v0.14.0 merely because the guide has changed. Adapt them with the current
configuration, short-post and reference guidance. Channel, schedule and gate skeletons and
Knowledge entry forms are a later generation at v0.14.0, revised as edition
2026-11-24.1, with channel skeleton/examples and schedule refined in edition
2026-11-24.2. Earlier proposals remain in Git history. They do not rewrite
the frozen packets.

This release distributes method source, not an installable Content plugin.
Its public guide can sync automatically after accepted main changes and method
releases through the configured public-only Notion connection. Human edits that
conflict with the source hold the update for review. This starts no personal
content production, subscriber send or social publishing. Content has its own
release lifecycle outside the OSM plugin; the archived Agentic-Content-System
remains historical.

[Documentation upkeep](docs/maintenance.md) explains the source-to-guide mapping
and verification. Run `python3 scripts/check_release.py` before release.

MIT licensed. See [LICENSE](LICENSE).
