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
- docs/post-workflow.md and docs/reference-library.md are linked detail in Git.

The existing OSM core publisher owns its seven released native skills. It does
not write these Content guide or template pages. Reuse its distinction between
accepted source, prepared projection, saved readback and anonymous public
verification. This repository adds no second daily writer or automatic Notion
publisher. [Issue #2](https://github.com/onlinesourdough/OSM-Content/issues/2)
tracks that separate integration work.

## Deliver an update

1. Review the source and run python3 scripts/check_release.py. It checks the
   file map, local links and the frozen template bytes.
2. Merge the reviewed change. Bind the exact source commit to the release tag;
   never move a published tag to make a later check pass.
3. Through the authorized public-guide connection, read each named target
   before editing. Keep native children, the catalogue, files, packet hashes
   and useful history. Stop an affected write on conflicting or unknown state;
   read back an uncertain result before retrying.
4. Read back the saved pages and compare with the mapped source. Record the
   exact tag/commit, page ids, what was checked and any unresolved differences.
   A successful API call alone is not a current projection.
5. Verify the changed anonymous pages and linked source/downloads. Keep an
   inaccessible or incomplete public read explicit; do not call it verified.
6. Record the actual result on the release. An unchanged replay should require
   no Notion write. Preserve earlier packets and partial progress.

The release is a method/source distribution, not a qualification of private
adoption, an editor, native installation or automatic sync. A tag can identify
valid source while its Notion/public verification is still pending. The release
record states those results separately. Keep private owner routes, customer
examples, drafts, media and credentials out of both the public source and proof.
