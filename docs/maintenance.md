# Source and readable documentation

This repository owns shared Content method development. The Notion guide is
its readable companion. The initial import in provenance.json records the
unchanged v0.10.0 template edition; it is not a second current authoring home.

## One source, explicit targets

The source-to-page mapping is in [release.json](../release.json):

- docs/guide.notion.md owns the Content entry, including its preserved native
  child-page, database and media references.
- docs/setup.md and docs/configuration.md own their named guide pages.
- The five template pages retain their v0.10.0 instructions, downloadable
  packets and history. Their current-source note points to the tagged template
  and the current method guidance. Updating a note does not reversion a packet.
- docs/post-workflow.md, docs/reference-library.md, docs/writing-voice.md,
  docs/sidebar-icons.md and docs/channel-skills.md are linked detail in Git.
  Channel, schedule and gate skeletons and Knowledge entry forms are a later generation
  under templates/. They are not part of the frozen v0.10.0 packets and they
  are not among the eight synced Notion pages.

The existing OSM core publisher owns its seven released native skills. It does
not write these Content guide or template pages. Reuse its distinction between
accepted source, prepared projection, saved readback and anonymous public
verification. The Content workflow reuses the pinned OSM public transport and
anonymous reader, with a public-only Notion credential and exactly eight bound
Content pages. It adds no daily private-context writer or owner-content publisher.

## Automatic synchronization

The [Sync public Content guide](https://github.com/onlinesourdough/OSM-Content/actions/workflows/sync-notion.yml)
workflow follows a successful exact-main Validate method release run, a published
method release, or an explicit main-branch invocation. A superseded source is
skipped before using the Notion connection. Pull requests and forks never receive
that connection. GitHub serializes this publisher through one concurrency group with queue: max, retaining pending runs. Writes wait for a published stable release matching the source version. A release event first uses its validated tag commit, then catches up a validated same-version main revision that was waiting for publication. A manual write waits when main has an unpublished version. If catch-up fails, a rerun uses the same run’s latest valid earlier-attempt tag-pass artifact to verify that the exact-tag whole-set pass already completed, then resumes catch-up without downgrading pages. The tag receipt is uploaded before catch-up can write. Its verified catch-up plan can resume the last accepted published version even if main now has an unpublished version. Missing or incomplete receipts do not bypass the tag pass.

OSM_PUBLIC_DOCS_TOKEN selects the existing public-only documentation connection.
OSM_CONTENT_DOCS_ENABLED enables automatic whole-set writes after live qualification.
The public connection has no private owner-home access. The browser child receives
only the reviewed environment allowlist and a fresh anonymous context.

The writer recognizes the explicit v0.11.0 handoff or exact content rendered from an ancestor of the accepted source. Pinned links only suggest candidates; a marker is never authority by itself. It
preflights the whole set, rechecks each page before writing and holds unknown
edits or a newer source. Mapped prose is authored as one physical line per paragraph. Only transport line endings and outer newline padding are normalized; Markdown content, hard breaks and block spacing remain exact. The original handoff retains its earlier soft breaks. Source provenance accepts the MCP rich-text link serialization and its API labels, with destinations checked separately; the Source property is never rewritten. Native child/catalogue/media/file references and all
non-managed properties are preserved. A failed or lost write is read back before
anything else; the same invocation never retries it. Each Markdown update matches observed prose outside native media; expiring file signatures never enter match strings. A changed selection is not replaced. Exact accepted prose segments and commit-pinned links identify a partially applied update for recovery. Unknown segments hold for review. The native reference sequence, not only its membership, must remain unchanged. Partial progress across pages can resume from its actual state. The report preserves progress on a failure.

Three guide bodies follow their mapped Git source. The five frozen template
instructions and packets keep their original v0.10.0 identity; only their source
note advances. The Source property retains the historical handoff and is read-only to the publisher. API-derived signed downloads are hash-checked; anonymous browser download access is not checked by this workflow. A future template
instruction/version change needs a reviewed new handoff instead of silently
rewriting the frozen packet. No private configuration or personal skill is touched.

Use workflow_dispatch read-only for preflight, one-page for a bounded proof, or
all for authorized whole-set synchronization. The actual report and anonymous
readback are retained as run artifacts. A successful whole-set repeat must record
zero write requests. A bounded proof does not establish whole-set activation.

Run python3 -m unittest discover -s tests -v for the conflict, replay, partial
write, lost-answer and destination-boundary cases. Fixtures are not live proof.
The latest real qualification belongs on the release and in the Actions history.

## Deliver an update

1. Review the source and run python3 scripts/check_release.py. It checks the
   file map, local links and the frozen template bytes. Later template files
   are allowed only when release.json declares their directories, and those
   directories stay outside the frozen v0.10.0 packets.
2. Merge the reviewed change. Bind the exact source commit to the release tag;
   never move a published tag to make a later check pass.
3. Through the authorized public-guide connection, read each named target
   before editing. Keep native children, the catalogue, files, packet hashes
   and useful history. Stop an affected write on conflicting or unknown state;
   read back an uncertain result before retrying.
4. Read back the saved pages and compare with the mapped source. Record the
   exact tag/commit, page ids, what was checked and any unresolved differences.
   A successful API call alone is not a current projection.
   The checker's --notion-snapshots input compares the three supplied guide
   readbacks, retaining structure and code. It does not fetch Notion or verify
   the five template pages or anonymous access. Check template source notes,
   unchanged instructions, native files/history and packet hashes separately.
5. Verify the changed anonymous pages and linked source/downloads. Keep an
   inaccessible or incomplete public read explicit; do not call it verified.
6. Record the actual result on the release. An unchanged replay should require
   no Notion write. Preserve earlier packets and partial progress.

The release is a method/source distribution, not a qualification of private
adoption, an editor, native installation or automatic sync. A tag can identify
valid source while its Notion/public verification is still pending. The release
record states those results separately. Keep private owner routes, customer
examples, drafts, media and credentials out of both the public source and proof.

## Diagram handoff · 20 November 2026

The owner-requested Content diagram revision replaces only the root's old
image section. Editable source and PNGs are pinned to asset commit
`f1e9a02b68744abb7b5e744e48683a11e902ca89`. The authored root readback equals
the previously API-qualified `3f50282` rendering except for that selected
section. Its stable body hash is
`3642954ee9b6987b2607ffb3edfc45f7d7cac98cf3beff50f8e3097735dde905`.

This is a deliberate root-baseline handoff, not relaxed conflict or native-media
checks. The other seven baseline entries and frozen packet bytes remain unchanged.
The next live preflight must independently match the complete API body and
new native media identities before any projection is called qualified.

## PR #15 guide rewrite

The proposed v0.14.0 guide leads with the operating model and the two skill axes. Earlier illustrations remain collapsed as optional reference, preserving the exact native child/catalogue/media sequence required by the publisher. No baseline or live Notion page is changed by this source revision. Later template edition 2026-11-24.1 records its previous generation where applicable; the five v0.10.0 imports and provenance stay frozen.

Second-model review stays an optional owner-policy switch without a named model. Approval uses the existing per-piece review section or an equivalent existing field; no new Select is required. The channel, schedule and gate templates stay in Git and do not expand the eight-page synced catalogue. Live projection and adoption still need their own evidence.
