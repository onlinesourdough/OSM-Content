---
name: channel-newsletter-to-posts
description: Choose one narrow angle per target channel from a newsletter edition and hand drafting to that channel skill. Use after a newsletter draft exists. Does not translate, rehash, or publish.
metadata:
  version: "0.14.0"
---
# Newsletter to posts

Template generation 2026-11-23.1. This skill sits between the newsletter and the other channel skills. It chooses angles. The target channel skill drafts the post and runs the quality gate.

Read [adoption](../content-channel/references/adaptation.md) when saving a personal skill. The method is [channel skills](../../docs/channel-skills.md).

## Pointers

| Slot | Owning page |
| --- | --- |
| Purpose | Each target channel's format page |
| Audience | Each target channel's format page |
| Voice source | Left for the target channel skill. This skill does not read voice into its own draft |
| Format / skeleton | Each target channel's format page, read only to see what kind of piece the angle must fit |
| Length | Each target channel's format page |
| Visuals | Each target channel's format page |
| Language | Each target channel's format page |
| Signature | Red thread, Signature and formatting |
| Cadence | Cadence page, each target channel's cap |
| Review / quality gate | Run by the target channel skill against the quality-gate page |
| Approval | Quality-gate page, Approval rule. This skill does not set it |

## Notion sources to build from

1. The newsletter Edition for this period, including its link to the Content productions it used.
2. Red thread themes, so each angle sits on a theme.
3. Each target channel's format page: purpose, audience, language, and length, so the angle fits that piece.
4. Cadence caps for those channels.
5. The new Edition created for each angle, linked to the newsletter with Derived from.

Voice measurements, signature rules, skeletons, and checklist items stay on their own pages. The target skill reads them when it drafts.

## Procedure

1. Read the newsletter Edition and the sources above.
2. For each selected target that is still under its cap, choose one angle narrower than the newsletter and on a theme. Record the angle on a new Edition. Set Type to Edition, link Derived from to the newsletter, and leave Status at Producing.
3. Hand that Edition to the target channel skill. That skill drafts and runs the quality gate.
4. Do not write a translation, a paragraph-for-paragraph shortening, or the target channel's skeleton into this skill.
5. The human sees a derivative only after that channel's quality gate has passed. Leave approval unset. Do not schedule or publish.

A target with no format page goes back to the setup interview for that channel. Do not invent the angle's language, length, or purpose.
