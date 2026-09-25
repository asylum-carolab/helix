# HELIX-PACK01 — Rapport de préparation S24

Date : 25 septembre 2026. Base `main` vérifiée et à jour : `cf2cb5623ca999f925a5bb6304f50f41abd7384d`.

## Résultat et périmètre

Package : `packages/HELIX-S24-PACK01/`. Assemblage de fichiers uniquement : **aucun build Android, aucune conversion, aucun recadrage, aucun traitement audio**. Aucun fichier temporaire, cache ou clé privée inclus.

- APK ICONS01 copié depuis sa référence existante, identique au fichier du commit cité. Signature APK v2 vérifiée avec `apksigner verify --verbose --print-certs`, certificat debug inchangé.
- APK ouvert et inspecté : **38 PNG** (comparés pixel pour pixel aux ressources validées), **76 entrées appfilter**, **38 entrées de catalogue**. Studio création et Bus Traffic Fever! restent exclus.
- Quatre fichiers fournis présents et identiques octet pour octet aux originaux. Empreintes des originaux contrôlées avant et après assemblage.
- PNG décodables, format réel et dimensions vérifiés ; WAV ouverts et totalité des trames lues.
- APK pilote et projet ICONS01 inchangés ; les 38 icônes ne sont ni modifiées ni reconstruites.
- **Tests physiques S24 : non effectués.** La validation graphique fournie et les contrôles d’intégrité ne prouvent pas le comportement de One UI.

## Fichiers ajoutés et organisation

```text
packages/HELIX-S24-PACK01/
├── HELIX-Icon-Pack-ICONS01-38.apk
├── wallpapers/
│   ├── wallpaper helix.png
│   └── verrouillage helix.png
├── audio/
│   ├── Ringtones/sonnerie.wav
│   └── Notifications/Helix notifications.wav
├── README.md
├── BUILD-REPORT.md
└── SHA256SUMS.txt
```

Huit fichiers ajoutés. Les deux WAV originaux sont les masters et les fichiers d’installation ; pas de copie supplémentaire « master »/« optimisée ». Les wallpapers originaux sont conservés ici comme références du package. L’unique duplication de l’APK est nécessaire au dossier autonome ; sa référence `packages/HELIX-Icon-Pack-ICONS01-38.apk` reste intacte. Pas de ZIP additionnel ni de réorganisation.

Fichiers existants modifiés uniquement pour ajouter des liens vers ce package : `packages/README.md`, `wallpapers/README.md`, `docs/INSTALL.md`. Aucun changement dans `sources/`, widgets, dossiers, icônes ou configuration Android.

## Intégrité SHA-256

- `HELIX-Icon-Pack-ICONS01-38.apk` — 7,911,536 octets
  SHA-256 : `b5cf6a64a02e8c56a4a786fcf784ddf44d689bf635bbd6c505c50d2ce30e9e98`.
- `wallpapers/wallpaper helix.png` — 1,999,905 octets
  SHA-256 : `3cb2fd6a8f420ac1760776975864f5b8c7039aefc08cbff3f837c8cc082968b2`.
- `wallpapers/verrouillage helix.png` — 2,053,342 octets
  SHA-256 : `aed3ac008e037b4346f673a1abc12e027152925d0ae18564fc5d40458083e792`.
- `audio/Ringtones/sonnerie.wav` — 5,736,492 octets
  SHA-256 : `ceba531255f11b05e8609fe8298f42edf2dd677702ad8a475effc3cfa5523bf2`.
- `audio/Notifications/Helix notifications.wav` — 182,444 octets
  SHA-256 : `2fc9e18a629fcc4df6a44dee69b1727f44da8a8851d098cbbc710d1ecf9da1eb`.

Pilote inchangé : `d7299fd7f282bd64155e2b911975c2454e7cfb8e4ff2c646afd5bd457b55c09e`.

`SHA256SUMS.txt` couvre les cinq assets binaires : APK, deux PNG et deux WAV.

## Images

| Usage | Fichier | Format réel | Dimensions | Couleur |
| --- | --- | --- | --- | --- |
| Accueil | wallpaper helix.png | PNG | 1024 × 1536 | RGB 8 bits/canal |
| Verrouillage | verrouillage helix.png | PNG | 853 × 1844 | RGB 8 bits/canal |

Accueil : bureau HELIX et écrans 23:42, qui restent des éléments statiques du PNG. Verrouillage : paysage nocturne, bureau au premier plan et logo HELIX. Aucune image dérivée. Le ratio accueil 2:3 nécessite un choix de cadrage sur le S24 ; le verrouillage est plus étroit (853:1844). Vérifier l’aperçu One UI, les superpositions et la lisibilité sans étirer ni éditer le master. Ces fichiers ne constituent pas des widgets interactifs.

## WAV masters et compatibilité

| Usage | Encodage | Canaux | Fréquence | Trames | Durée | Débit PCM |
| --- | --- | --- | --- | --- | --- | --- |
| Sonnerie | PCM linéaire signé 16 bits, little-endian, WAVE | 2 (stéréo) | 44 100 Hz | 1 434 112 | 32,519546 s | 1 411,2 kbit/s |
| Notification | PCM linéaire signé 16 bits, little-endian, WAVE | 2 (stéréo) | 48 000 Hz | 45 600 | 0,950000 s | 1 536 kbit/s |

Le décodage PCM/WAVE 16 bits est pris en charge par Android ; aucun besoin de conversion identifié pour ces fréquences usuelles. Les WAV sont livrés directement. [Formats Android officiels](https://developer.android.com/media/platform/supported-formats).

Mesures sur les échantillons originaux, sans traitement :

- Sonnerie : crête −0,727 dBFS, RMS −13,624 dBFS, aucun échantillon à pleine échelle. Le niveau numérique n’impose pas le volume du haut-parleur : régler et écouter sur le S24.
- Notification : crête −4,153 dBFS, RMS −14,285 dBFS, aucun échantillon à pleine échelle. Premier dépassement du seuil −60 dBFS à environ 20,08 ms ; cette attaque d’origine est préservée, sans ajout ni suppression de silence.
- Sonnerie : différence maximale entre le dernier et le premier échantillon, par canal, égale à 0,105713 de la pleine échelle. Cette discontinuité numérique justifie une **écoute du raccord en répétition** ; elle ne suffit pas à prouver un clic audible. Aucune écoute sur haut-parleur S24 n’a été effectuée. Le contenu et la durée de la boucle livrée restent strictement intacts ; aucun fondu ou montage ne serait justifié sans cet essai.

Les deux WAV contiennent les trames audio originales, sans métadonnée de boucle `smpl`. Le comportement de répétition dépend du lecteur de sonnerie One UI. Ne pas déclarer une boucle parfaitement inaudible sur la seule base de l’intégrité du fichier.

## Limites et recette restante

Le README donne l’ordre manuel : APK → Theme Park → accueil → verrouillage → sonnerie → notification → recette. Copier des fichiers ne sélectionne aucun réglage Android. Theme Park doit détecter le pack ; les versions d’apps installées peuvent utiliser d’autres alias. Les menus, catégories de notifications, réglages par SIM ou par contact et modes sonores peuvent différer.

À effectuer sur le S24 : détection/sélection du pack, association automatique des 38 apps présentes, stabilité One UI Home/Theme Park, cadrage des deux PNG, appel réel avec répétition et niveau adapté, notification réelle avec attaque correcte et catégories utiles, conservation après redémarrage. Rapporter réussite/échec/non testé, versions, erreurs et captures. En cas de problème audio, conserver les masters et documenter le défaut avant d’envisager un dérivé distinct.
