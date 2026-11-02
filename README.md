# Friends of the Road poster archive

Static HTML/CSS, no build step or third-party scripts. One chronological archive across the band’s three names. This first collection is incomplete.

## Preview

Run `python -m http.server 8000` from this directory.

## Check

Run `python scripts/check_archive.py`. It verifies local links, image files and original asset hashes, accessible image text, chronological order, and correspondence between the manifest and gallery.

## Add a poster

Use the original public promotional asset or an authorized band copy. Confirm the event date, the band name on the bill, original source, and known artist credits. Do not infer an event year from an upload date. Keep full-size originals in `posters/` and a smaller WebP for the gallery. Update `archive.json` and the corresponding HTML entry, including alt text, date, source, and credits. Preserve uncertainty; festival dates do not establish the band’s individual performance day. Do not describe this collection as complete.

No general reuse license is claimed for poster artwork. The archive retains source links and known credits. Publication/rights questions should be resolved by the band before broader reuse.

Hosting and DNS are configured separately; this change does not alter them.
