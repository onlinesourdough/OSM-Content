---
name: channel-quality-gate
description: Run the shared first-draft checklist against a finished draft before the human sees it. Use before review. Does not approve, schedule, or publish.
metadata:
  version: "0.14.0"
---
# Quality gate

Template generation 2026-11-23.1. This skill runs the owner's quality-gate page. Every channel skill calls it after drafting and before the human sees the piece. The checks, the second-model switch, and the approval rule live on that page, created from the [quality-gate form](../knowledge-entries/quality-gate.md).

Read [adoption](../content-channel/references/adaptation.md) when saving a personal skill. The method is [channel skills](../../docs/channel-skills.md). Delivery authority stays in the [release contract](../content-produce/references/release-contract.md).

## Pointers

| Slot | Owning page |
| --- | --- |
| Purpose | The channel format page for the draft being checked |
| Audience | The channel format page for the draft being checked |
| Voice source | Voice profile, section for this channel |
| Format / skeleton | The channel format page |
| Length | The channel format page |
| Visuals | The channel format page |
| Language | The channel format page |
| Signature | Red thread, Signature and formatting |
| Cadence | Cadence page, this channel's block |
| Review / quality gate | Quality-gate page, First-draft checklist |
| Approval | Quality-gate page, Approval rule |

## Notion sources to build from

1. The owner's quality-gate page.
2. The Edition under review, its parent newsletter Edition when it has one, and the channel skill that drafted it.
3. The voice, red-thread, format, and cadence pages named by the checklist.

Run the owner's page. Use the form in this repository only while that page is being created. A blank field on the owner's page fails the check that reads it.

## Procedure

1. Open the owner's quality-gate page and the Edition.
2. Run every row of the First-draft checklist, in order. Write the result and the date on the Edition review section from [setup](../../docs/setup.md).
3. When a check fails, return the failed rows to the channel skill. Do not show the draft to the human.
4. When a second-model switch on the page is on, record that review and its disagreements on the Edition before the result can pass.
5. When every required check passes, the human may see that draft.
6. Leave human approval unset. Do not schedule or publish.

A pass means the draft is ready for the owner to read. It does not set the approval status and it does not move the Edition to Scheduled or Published.
