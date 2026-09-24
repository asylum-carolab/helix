# HELIX Icon Pack

Android icon-pack source for the HELIX interface.

## Goal

Build one installable APK that can be selected from Samsung Theme Park as a third-party icon pack.

## Visual master

- graphite / near-black rounded tile
- subtle relief and angular technical paneling
- cyan-blue luminous rim
- cyan highlight near the top-left
- restrained amber accent near the bottom-right
- original app identity remains immediately recognizable

## Pilot

The first compatibility build targets a small core set before expanding to the complete HELIX catalog:

- Phone
- Messages
- Camera
- Chrome
- Gmail

Mappings live in `app-map.csv`.

The final PNG assets will be stored under `icons/` and copied into the Android drawable resources during the build.
