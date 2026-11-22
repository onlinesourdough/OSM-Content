# Writing-voice acceptance cases

These five fictional cases exercise Content issue #1's acceptance examples.
They contain no private owner writing, customer data or live account action.
They are method checks, not a model comparison, a native client journey, a
retrieval benchmark, or proof of anyone's complete voice profile.

On 22 November 2026 an independent Gemini 4 Neon High worker received the
method and one case per new conversation, with no target answer or reviewer
findings. Native model readback confirmed `gemini-4-neon-high` / High. Evidence
was embedded inline, strict permissions were selected, no MCP was configured,
and all actual streams had zero tool steps. No live record was changed.

## Results and repairs

| Case | First attempt | Affected retry |
| --- | --- | --- |
| Minimal edit | PASS; 148 local characters against 150 | Not rerun |
| Evidence selection | PASS; keeps public writing, dictated instructions and AI candidates distinct | Not rerun |
| Rejected candidate | PASS; rejection and scoped example provenance retained | Not rerun |
| Scoped correction | FAIL; promoted one draft's failure diagnosis into an accepted standing rule | PASS after clarifying candidate failure vs future voice instruction |
| Destination length | PASS; 120 local ASCII characters against 120, fixed first sentence retained | Not rerun |

The final texts were independently counted with Python's `len` (Unicode code
points for the Danish example; ASCII for the configured short-note box). These
local checks establish the supplied fictional limits, not a platform composer.

The candidate review also found a competing minimum field map in the sample
personal configuration. It now points to the Definition/source agreement and
contains only optional editorial fields/views. The affected method and original
scoped-correction case were then given to a fresh worker without the findings.
The repair reviewer accepted those changes and the new result. The four earlier
passes were not rerun against the revised wording; the final review says so.

`voice-cases.json` keeps the original cases. `voice-results-20261122.json` retains
all six worker attempts, outputs, durations and reported usage, including the
failed first attempt. `voice-method-attempt1.md` preserves the exact earlier
method snapshot. The current method is [writing-voice.md](../docs/writing-voice.md).
Both review texts and their model/input-hash receipts are retained beside them.
There is no hidden retry, claimed native storage test or measured performance
advantage over an untreated writer. The main source/transport suite separately
checks the release inventory, frozen packets and public-sync behavior.
