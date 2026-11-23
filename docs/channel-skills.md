# One skill per channel

OSM Content keeps five responsibility skills: Setup, Intake, Prepare, Produce, and Learn. Those say **when** the work happens. This guide adds a second axis: **one skill per channel**, which says **what piece** is being made.

A channel is one destination the owner actually uses: the newsletter, LinkedIn, X, Instagram, TikTok, YouTube, or a later one. Each active channel has one skill. The skill holds the procedure for that piece and pointers to the shared records. Voice, the red thread, format, cadence, boundaries, and the quality-gate checks live once in the owner's Knowledge home.

The five frozen v0.10.0 packets stay unchanged. Channel skills are a later template generation. Adopting one does not install a plugin, start a schedule, or publish.

## No redundant data

Each fact has one owner in the Notion foundation. Skills, the owner configuration, and other pages link to that owner. They do not repeat the fact.

| Fact | Single owner |
| --- | --- |
| Measured voice for a channel: traits, openers, closers, the author's words, voice-level never-do, exemplar links | [Voice profile](../templates/knowledge-entries/voice-profile.md) |
| Themes, a link to existing positioning, cross-platform signature and formatting rules, private boundaries, the rawness line, inspiration links | [Red thread](../templates/knowledge-entries/red-thread.md) |
| One channel's purpose, audience, language, skeleton, length, and visuals | [Channel format](../templates/knowledge-entries/channel-format.md) for that channel |
| Caps and any slot the owner has chosen | [Cadence](../templates/knowledge-entries/cadence.md) |
| First-draft checks, the second-model switch, and the approval rule | [Quality gate](../templates/knowledge-entries/quality-gate.md) |
| Questions asked at setup | [Setup interview](../templates/knowledge-entries/setup-interview.md). Answers are written only to the owners above |
| Gate result and human approval for one piece | The Edition review section in [setup](setup.md) |
| The broad piece for a period | The newsletter Edition in Content |
| Possible channel roles | The examples in [configuration](configuration.md). The chosen purpose is stored on the channel format page |

The repo forms are blank method sources. The owner's Knowledge page, filled from the form, is the runtime source. A channel skill points at the owner's page.

## How the two axes work together

A task uses one responsibility skill. When the task produces an edition, it also uses that edition's channel skill. The quality-gate skill is shared by every channel. It is not a sixth responsibility and not a channel.

| Responsibility | Use of the channel axis |
| --- | --- |
| [Setup](../templates/content-setup/SKILL.md) | Run the [interview](../templates/knowledge-entries/setup-interview.md) once. Create any missing Knowledge page. Adopt the channel skills the owner needs. The frozen setup packet stays the v0.10.0 import; this guide is the current interview. |
| Intake | Save the idea on Content. Leave channel drafting and publication alone. |
| Prepare | Gather the material the channel skill will read. |
| [Produce](../templates/content-produce/SKILL.md) | Load the channel skill for this edition, draft, then run the [quality-gate skill](../templates/channel-quality-gate/SKILL.md). Stop for human approval. The frozen produce packet stays the v0.10.0 import. Distribution still follows its [release contract](../templates/content-produce/references/release-contract.md) and the approval rule on the quality-gate record. |
| Learn | Write one lesson back onto the single owning record. Leave skills unchanged unless the procedure itself changed. |

Produce loads the channel skill beside the frozen packet. The packet is not edited to contain channel facts.

## Long form first

The newsletter is the broad source for the period on the cadence record. It can hold the personal strand and the professional strand the red thread allows. A later post on X, LinkedIn, or another channel is a narrow derivative: one angle, chosen for that channel, linked to the newsletter Edition.

A standalone short post can still follow the [short-post workflow](post-workflow.md) when there is no newsletter parent. A derivative records its angle on the Edition. The quality gate checks that a derivative is a new angle. A translation or a shortened copy fails the gate.

The [newsletter skill](../templates/channel-newsletter/SKILL.md) drafts the broad piece. The [newsletter-to-posts skill](../templates/channel-newsletter-to-posts/SKILL.md) chooses one angle per target channel and hands the draft to that channel's skill. The [X](../templates/channel-x-post/SKILL.md) and [LinkedIn](../templates/channel-linkedin-post/SKILL.md) skills are the examples for those destinations.

## Quality gate, first draft, and approval

Every draft passes the shared quality gate before the human sees it. The checks live only on the [quality-gate record](../templates/knowledge-entries/quality-gate.md), in the First-draft checklist. They read the interview's answers: measured voice, language, theme, skeleton, signature and formatting, private boundaries, rawness and credited inspiration, derivation, and the cadence cap. They also confirm the channel skill still holds pointers rather than a pasted copy.

The [quality-gate skill](../templates/channel-quality-gate/SKILL.md) runs that list. A failed check goes back to the channel skill. The human sees the draft that passes. An optional second model runs only when the quality-gate record says so.

Human approval is a status the owner sets on the Edition. The agent leaves it unset. A passing gate, Ready, or voice approval does not publish. Scheduled and Published require the explicit approval status named on the quality-gate record, then the applicable delivery authority.

## Ask once, at setup

Customers should be able to reach a sound first draft without a correction loop. The [setup interview](../templates/knowledge-entries/setup-interview.md) is the one sitting. It asks for the facts below, writes each answer to its owner, and does not ask again while the answer still stands. Later productions read the records. The quality gate checks them before the human sees a draft.

- Own posts to measure voice from, per channel
- Per-channel language, with purpose, audience, skeleton, length, and visuals
- Red-thread themes, and a link to positioning if that already has an owner
- Signature and formatting rules, including how raw the formatting stays
- Private boundaries, starting from home city and family details, confirmed or replaced
- Inspirations, and the line for what is too raw
- Cadence caps, with an explicit "no cap" when that is the choice
- Who approves publication, which status counts, and whether a second model reviews first

A change later is an edit to the owning record, then the next gate run. It is not a second interview and not a copy inside a skill.

## The journey

These stages build the content side of a business. "Done" is an observable state. A later stage can start while an earlier one is done for the channels already in use. Unused platforms stay absent.

### 1. Setup

Measure voice from the owner's own posts. Write the red thread, private boundaries, channel formats, cadence caps, and approval rules once.

Done when the interview completion is recorded, each selected channel has voice measurements with evidence links, the red thread has confirmed themes, signature rules, and boundaries, each selected channel has a format page including language, the cadence page has a cap or an explicit "no cap", and the quality-gate page has the approval rule. No skill contains those facts.

### 2. First channel skills

Adopt one channel skill from the [channel template](../templates/content-channel/SKILL.md). Point it at the records above. Draft one edition and hold it.

Done when that skill is in the owner's personal Skills, its pointers resolve, and one Edition has been through the quality gate before the human saw it. The Edition is not Scheduled or Published.

### 3. Long form first and derived posts

Write the newsletter as the broad piece. Derive other posts from it, each with its own angle.

Done when a newsletter Edition for the period holds that broad piece. Every other selected channel's Edition for the period links to it, records its own angle, and passes the derivation check. When the newsletter is the only selected channel, that broad Edition completes the stage.

### 4. Quality gate and approvals

Run the first-draft checklist before the human sees any draft. Publish only after an explicit human approval status.

Done when every Edition the human was shown has a passing gate result recorded first, and every Scheduled or Published Edition has the owner's approval status set by the owner.

### 5. Scheduled queue and weekly review

Put approved editions in a queue only under real delivery authority. Review the period and keep one lesson.

Done when every queued Edition has the approval status and, where a schedule exists, the service's job id, and the period's review wrote one lesson onto the owning Knowledge record. The review period is the one on the cadence page. A weekly review is the name of this stage when the owner has chosen a week.

### 6. Mature

Every channel the owner actually uses has one skill. The same shared records feed all of them. The newsletter stays the broad source. The gate and the approval run as part of the work.

Done when stages 3–5 hold for the current period across every channel in the owner configuration, and the cadence page is the only calendar. Leave unselected platforms without a skill or a format page. This is the working shape of a content side that is already running. The module stores no one person's calendar, voice, or private boundaries.

## Add a channel

YouTube, Instagram, TikTok, and any later destination use this path. Newsletter, X, and LinkedIn already have example skills.

1. Add the channel to the selected set in the owner configuration only when the owner chooses it. Role examples stay in [configuration](configuration.md).
2. Create one format page from the [channel format](../templates/knowledge-entries/channel-format.md) form. Ask only the interview fields that are still empty for this channel.
3. Add one cap, and a slot only if the owner names one, on the existing cadence page.
4. Add a section to the existing voice profile, measured from this platform's own posts. Keep one voice profile.
5. Adapt the [channel template](../templates/content-channel/SKILL.md) into personal Skills. Replace role names with the owner's page links. Write the procedure. Leave the record bodies in Knowledge.
6. Draft one edition in a non-publishing state and run the quality gate.

## Lessons from the first real run

The module author was the first real user of OSM Content. The learnings below are generic. Each one now has a single home, and the setup interview asks for it once so a later customer is not walked through the same corrections. The module contains none of that author's calendar, voice, city, or family details.

- Voice measured from the author's own posts is the profile. A description of the voice does not fill it. Home: the voice profile. The interview asks for the posts, then measurement fills the profile.
- Voice and the red thread are data in Knowledge. They are not skills. Skills point at the records.
- The newsletter is broader than the posts that come from it. A post that repeats the newsletter fails the derivation check on the quality gate.
- Raw formatting is the signature default: keep the formatting as raw as the author's own posts. Heavy formatting is a miss unless a confirmed signature rule accepts it. Home: the red thread.
- Signature and formatting rules that a reader should recognize on every platform belong to the red thread. The channel format page owns that channel's skeleton, length, and visuals, and it links to the signature rules.
- Private details stay unpublished. The starter boundaries to confirm are home city and family details. Home: the red thread. The gate checks the confirmed list.
- Each fact lives in one place. A skill that has a pasted copy fails the quality gate.
- Nothing is published without an explicit human approval status on the Edition. The agent does not set that status.
