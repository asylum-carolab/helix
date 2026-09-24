# HELIX icon-pack workflow

HELIX uses an installable Android icon pack rather than assigning every icon manually in Theme Park.

## Workflow

1. Design and validate a HELIX master icon.
2. Export one PNG per supported application.
3. Associate each icon with the Android application/component in `packages/icon-pack/app-map.csv`.
4. Build and sign the HELIX Icon Pack APK.
5. Install the APK on the Galaxy S24.
6. In Theme Park, create an icon theme and choose HELIX from **Third Party Icon Packs**.
7. Apply the theme.

## Compatibility gate

Do not produce the complete application catalog before the pilot APK is recognized by Theme Park and the five pilot icons map correctly on the target Galaxy S24.

After validation, extend the same visual master and mapping mechanism to the full application list.
