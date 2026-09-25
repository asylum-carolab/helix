# HELIX-S24-PACK01 — Installation sur Samsung Galaxy S24

Package autonome : APK ICONS01 existant, deux wallpapers et deux WAV validés. Aucun fichier graphique ou audio n’est converti, recadré ou normalisé. L’APK n’est pas reconstruit. Studio création et Bus Traffic Fever! restent exclus des 38 icônes.

Suivre les étapes dans cet ordre. La copie des fichiers ne configure pas One UI : les sélections décrites ci-dessous sont **manuelles**. Les libellés varient selon la langue et les versions One UI/Theme Park.

## 0. Transférer

Copier ce dossier dans le stockage interne, par exemple `Download/HELIX-S24-PACK01`, et le conserver intact. Les WAV dans `audio/` sont les masters originaux, directement utilisables.

```text
HELIX-S24-PACK01/
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

`SHA256SUMS.txt` contient les empreintes de l’APK, des deux PNG et des deux WAV. Sur ordinateur : `sha256sum -c SHA256SUMS.txt` depuis ce dossier ; sous PowerShell, utiliser `Get-FileHash -Algorithm SHA256 -LiteralPath 'chemin du fichier'` pour une comparaison individuelle.

## 1. Installer l’APK

Dans **Mes fichiers**, ouvrir `HELIX-Icon-Pack-ICONS01-38.apk`, autoriser cette source si Android le demande, puis installer **HELIX Icon Pack**. Si cette même version est déjà installée, la conserver. Identifiant : `fr.carolab.helix.icons`, version `0.2.0-icons01`, code 2.

Ouvrir HELIX pour consulter les diagnostics. Une application absente/désactivée reste non testée. Samsung Messages et Google Messages sont différents. En cas d’erreur de signature, identifier la version déjà installée avant toute désinstallation : une autre clé de signature empêche sa mise à jour directe.

## 2. Appliquer les icônes

Ouvrir **Samsung Good Lock → Theme Park → Icon / Icône → Create new / Créer → Iconpack / Pack d’icônes → Third Party Icon Packs → HELIX Icon Pack**. Installer Theme Park via Good Lock si nécessaire. Selon la version, le bouton Icon précède Iconpack.

Sélectionner HELIX, examiner l’aperçu, enregistrer/installer le thème sous `HELIX PACK01`, puis le sélectionner et choisir **Apply / Appliquer**. Si le thème ICONS01 est déjà appliqué et correct, le conserver. Ne pas remplacer individuellement des icônes pour masquer un échec de correspondance automatique.

Le pack expose 38 dessins et 76 correspondances Android. Il ne remplace pas One UI Home ni les icônes internes des applications. Les contrôles de fichiers ne certifient pas la détection par la version de Theme Park du téléphone.

## 3. Appliquer le wallpaper d’accueil

Dans **Paramètres → Fond d’écran et style → Changer les fonds d’écran → Galerie**, choisir `wallpapers/wallpaper helix.png`, puis **Écran d’accueil uniquement**. Ajuster le cadrage dans l’aperçu et valider. Si nécessaire, copier les PNG vers `Pictures/HELIX` pour les retrouver dans Galerie. [Procédure Samsung](https://www.samsung.com/us/support/answer/ANS10001632/).

Ce PNG 1024 × 1536 représente le bureau HELIX et les écrans affichant **23:42**. Textes et heures sont intégrés à l’image, pas des widgets actifs. Son ratio diffère de celui du S24 : vérifier le cadrage, sans étirement ni modification du master. Ne pas activer d’effet génératif pour conserver le visuel validé.

## 4. Appliquer le wallpaper de verrouillage

Reprendre le même chemin avec `wallpapers/verrouillage helix.png`, puis sélectionner **Écran de verrouillage uniquement**. Ce PNG 853 × 1844 est la vue nocturne avec paysage, bureau au premier plan et logo HELIX. Ajuster l’aperçu et valider ; contrôler la superposition de l’horloge et des notifications One UI. Le cadrage sur le téléphone ne modifie pas le fichier livré.

## 5. Installer et sélectionner la sonnerie

Avec **Mes fichiers**, copier `audio/Ringtones/sonnerie.wav` vers **Stockage interne → Ringtones**, à la racine du stockage ; créer le dossier si absent. Garder le master dans le package. Ouvrir **Paramètres → Sons et vibrations → Sonnerie**, choisir la SIM si demandé, puis `sonnerie`. Utiliser **+** pour sélectionner le WAV s’il n’est pas proposé. Si une sélection automatique d’extrait est disponible, la désactiver pour conserver le début du morceau. Confirmer. [Réglages Samsung](https://www.samsung.com/us/support/answer/ANS10002549/).

Régler progressivement le volume **Sonnerie**. Tester un appel de plus de 32,52 secondes pour entendre la répétition. Aucun découpage, fondu ni changement de niveau n’a été appliqué ; le raccord audible reste à contrôler sur le S24. Les contacts, SIM, modes et Ne pas déranger peuvent avoir leurs propres réglages.

## 6. Installer et sélectionner la notification

Copier `audio/Notifications/Helix notifications.wav` vers **Stockage interne → Notifications**, à la racine. Ouvrir **Paramètres → Sons et vibrations → Son de notification**, choisir `Helix notifications`, puis revenir pour enregistrer. Vérifier le mode **Son** et le volume **Notifications**. Si absent, vérifier le dossier, rouvrir les paramètres et, si nécessaire, redémarrer pour permettre sa réindexation. [Guide Samsung des sons personnalisés](https://www.samsung.com/uk/support/mobile-devices/how-to-set-an-audio-file-as-a-message-notification-or-ringtone/).

Certaines apps imposent leur propre son. Pour une catégorie configurable : **Paramètres → Applications → application → Notifications → Catégories de notification → catégorie sonore → Son**, puis sélectionner HELIX. Selon One UI, activer d’abord l’affichage des catégories dans les paramètres avancés des notifications. Toutes les apps ne proposent pas ce choix. [Guide Samsung par application](https://www.samsung.com/au/support/mobile-devices/customise-ringtone/).

La notification dure 0,95 seconde. Aucun silence, effet ou musique n’est ajouté ; l’attaque originale est intacte.

## 7. Recette physique

- Relever modèle S24, versions Android/One UI/One UI Home/Theme Park, date et commit PACK01.
- Vérifier l’APK, la détection et la sélection dans Theme Park, puis les associations automatiques des 38 applications présentes et leur lancement. Noter les absentes et les composants non associés affichés par HELIX.
- Vérifier séparément les fonds : bon PNG, cadrage acceptable, pas d’étirement, logo et éléments importants visibles. Les 23:42 du fond d’accueil restent fixes.
- Tester un appel réel, les SIM utilisées, le niveau sonore et au moins une jonction de répétition. Consigner toute coupure/clic sans modifier le master.
- Déclencher une vraie notification, écran allumé puis verrouillé : bon son, attaque perçue sans retard gênant, volume et catégories d’apps corrects.
- Redémarrer : choix conservés, aucun plantage de Theme Park ou One UI Home.

Rapporter **réussite / échec / non testé** pour chaque point, avec erreurs et captures utiles. Aucune recette sur le téléphone n’est prétendue réalisée par ce package. Pour revenir en arrière, réappliquer les fonds, sons et thème précédents dans leurs paramètres respectifs.
