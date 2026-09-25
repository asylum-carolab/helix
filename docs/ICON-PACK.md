# HELIX Icon Pack — ICONS01, 38 icônes

Application existante : `fr.carolab.helix.icons`, version **0.2.0-icons01**, code **2**. Le projet Gradle/Android du pilote est réutilisé. **Studio création et Bus Traffic Fever! sont exclus de cette version à la demande de l’utilisatrice** : aucune ressource Android et aucun mapping pour ces deux applications.

La grille approuvée sert de source de pixels, pas de prétexte à redessiner les logos. Les 38 pictogrammes ont été extraits, dimensionnés et centrés individuellement, puis composés dans un cadre HELIX commun noir/anthracite, néon cyan/bleu, accent orange inférieur. Aucun générateur d’images ni nouveau dessin n’a été utilisé.

## Fichiers graphiques et contrôle visuel

- `app/src/main/res/drawable-nodpi/helix_*.png` : 38 PNG RGBA 512 × 512, sans légende, intégrés à l’APK.
- `../../icons/helix-icons01/reference-grid.png` (depuis le projet Android) : copie intacte de la maquette source ; elle contient encore les deux cases exclues, uniquement comme référence historique.
- `icons/helix-icons01/frame-master.png` depuis la racine du dépôt : cadre commun, extrait du cadre Téléphone. La plaque sombre intérieure est nettoyée à partir de pixels sombres des cases alignées pour retirer le pictogramme initial.
- `icons/helix-icons01/artwork-layout.json` : rectangle source, échelle proportionnelle, décalage et rectangle de sortie de chaque pictogramme.
- `icons/helix-icons01/contact-sheet.png` et `review-preview.png` : planches des **38** résultats, examinées côte à côte.
- `icons/helix-icons01/artwork-checks.json` : empreintes des PNG, vérification du cadre identique, des coins transparents, des marges et de l’unicité des 38 images.

La seconde passe corrige le bord supérieur de Photos et rééquilibre Maps, YouTube et Google TV. Les formes fines comme Horloge, ChatGPT et Gemini occupent davantage d’espace que les blocs compacts ; aucun logo n’est étiré. Le cadre extérieur est identique pixel pour pixel pour les 38 ressources. La source étant une grille 1536 × 1024, les PNG 512 × 512 sont des agrandissements interpolés des pixels extraits, pas des originaux HD réinventés.

Reproduire la préparation, depuis `packages/icon-pack`, avec Python, Pillow et NumPy :

```sh
python tools/prepare_artwork.py ../../icons/helix-icons01/reference-grid.png
python tools/verify_artwork.py
python tools/sync_resources.py
```

Ces étapes ne sont pas requises pour compiler : les PNG et XML sont versionnés. Les paramètres optiques individuels se trouvent dans `tools/prepare_artwork.py` et leur résultat dans `artwork-layout.json`.

## Catalogue et mappings

`catalog.json` recense les 38 ressources dans l’ordre de la maquette, en sautant les deux exclusions. `app-map.csv` contient **76 composants pour 38 applications**. Les mappings historiques corrects de Téléphone, Appareil photo, Chrome et Gmail sont conservés, ainsi que l’alias Samsung Messages `com.android.mms.ui.ConversationComposer`. Deux autres alias Messages corroborés sont inclus.

Chaque composant actif a été recoupé dans le [catalogue source public Arcticons](https://github.com/Arcticons-Team/Arcticons/blob/main/app/src/main/res/xml/appfilter.xml), consulté le 25 septembre 2026. La source, son empreinte SHA-256 et la liste exacte des composants corroborés sont conservées dans `mapping-evidence.json`. Les variantes retenues restent limitées aux applications demandées ; les composants de mods, de TV, d’archivage Android ou de réglages annexes ont été écartés.

**À confirmer sur le S24 :** le composant réellement utilisé pour chaque version installée, notamment les alias Samsung, le lanceur LinkedIn, Google TV et leboncoin. Aucune correspondance n’est annoncée testée physiquement. L’ancien candidat Messages `com.samsung.android.messaging.ui.view.main.WithActivity`, non corroboré, est documenté dans `mapping-evidence.json` et retiré de l’appfilter actif ; ne le rétablir qu’après lecture sur le téléphone. Aucun nom de paquet ou composant non vérifié n’est ajouté silencieusement.

Samsung Messages désigne `com.samsung.android.messaging`, pas Google Messages. Meet cible `com.google.android.apps.tachyon`, pas une autre application portant un nom voisin. Calendrier conserve le **31 statique** du dessin approuvé : aucun calendrier dynamique n’est ajouté.

Les deux appfilters (`assets/` et `res/xml/`), les deux catalogues `drawable.xml`, le tableau `icon_pack` et les déclarations de visibilité du manifeste sont synchronisés. Les cinq anciens alias vers l’icône H sont remplacés par de vrais PNG. Le label **HELIX Icon Pack**, l’activité de lancement et les filtres de découverte ADW/Nova sont conservés. Aucune permission Android et aucune dépendance d’exécution tierce ne sont ajoutées. Le pack ne fait aucun appel réseau.

L’écran du pack affiche les composants de lancement visibles des 38 applications et signale les correspondances absentes. Une application absente/désactivée reste non testée. Cette vérification locale ne démontre pas la compatibilité Theme Park.

| Application | Ressource PNG | Composants |
| --- | --- | --- |
| Téléphone | helix_phone | 1 |
| Messages | helix_messages | 3 |
| Contacts | helix_contacts | 2 |
| Calendrier | helix_calendar | 2 |
| Appareil photo | helix_camera | 1 |
| Galerie | helix_gallery | 2 |
| Mes fichiers | helix_files | 3 |
| Paramètres | helix_settings | 1 |
| Chrome | helix_chrome | 2 |
| Google | helix_google | 2 |
| Play Store | helix_play_store | 2 |
| YouTube | helix_youtube | 2 |
| Spotify | helix_spotify | 2 |
| TikTok | helix_tiktok | 4 |
| ChatGPT | helix_chatgpt | 1 |
| Gemini | helix_gemini | 1 |
| Outlook | helix_outlook | 2 |
| Gmail | helix_gmail | 1 |
| Drive | helix_drive | 3 |
| Photos | helix_photos | 1 |
| Maps | helix_maps | 1 |
| Google TV | helix_google_tv | 3 |
| Shazam | helix_shazam | 2 |
| YouTube Music | helix_youtube_music | 1 |
| Samsung Notes | helix_samsung_notes | 1 |
| Horloge | helix_clock | 2 |
| Calculatrice | helix_calculator | 1 |
| Bixby | helix_bixby | 2 |
| Samsung Health | helix_samsung_health | 2 |
| Galaxy Store | helix_galaxy_store | 3 |
| Good Lock | helix_good_lock | 3 |
| Samsung Members | helix_samsung_members | 3 |
| Meet | helix_meet | 2 |
| VLC | helix_vlc | 2 |
| LinkedIn | helix_linkedin | 3 |
| Amazon Alexa | helix_alexa | 2 |
| leboncoin | helix_leboncoin | 4 |
| Icon Pack Studio | helix_icon_pack_studio | 1 |

## Construire et récupérer l’APK

Prérequis : JDK 17, Android SDK API 35 et Build Tools 34.0.0. Définir `JAVA_HOME` et `ANDROID_HOME`, ou fournir `sdk.dir` dans `local.properties` (non versionné). Le wrapper inclus fixe Gradle 8.9 et vérifie sa distribution par SHA-256 ; Android Gradle Plugin reste à 8.7.3. Cible Android 35, minimum 26.

Depuis `packages/icon-pack` :

```sh
./gradlew assembleDebug lintDebug --no-daemon --console=plain
```

Sous Windows :

```powershell
.\gradlew.bat assembleDebug lintDebug --no-daemon --console=plain
```

La première compilation nécessite Internet pour les outils de compilation ; `--offline` fonctionne ensuite avec le cache déjà rempli. `verifyIconResources` s’exécute automatiquement avant le build : 38 PNG RGBA 512 × 512, catalogue complet, unicité des composants, justificatif de chaque mapping, cohérence des XML, visibilité des 38 paquets et absence de permissions.

Chemins relatifs à la racine du dépôt :

- **Nouvel APK : `packages/HELIX-Icon-Pack-ICONS01-38.apk`** ; export automatique uniquement après assemblage réussi.
- Sortie Gradle conservée : `packages/icon-pack/app/build/outputs/apk/debug/app-debug.apk`.
- Rapport Lint local : `packages/icon-pack/app/build/reports/lint-results-debug.html`.
- **Pilote préservé : `packages/HELIX-Icon-Pack-PILOT.apk`**, inchangé. SHA-256 : `d7299fd7f282bd64155e2b911975c2454e7cfb8e4ff2c646afd5bd457b55c09e`.

L’APK ICONS01 reste un APK de test signé avec la même clé debug locale que le pilote. Il peut remplacer ce pilote sur le téléphone avec `adb install -r` ; le fichier pilote dans Git reste intact. Ce n’est pas une signature de production pour boutique. Sur une autre machine, une clé debug différente produit une signature différente ; une installation existante ne peut être mise à jour qu’avec sa clé de signature. Aucune clé privée n’est versionnée.

## Installation et test Galaxy S24

**La compilation ne valide pas Theme Park. L’installation et l’application sur le S24 physique restent à effectuer.**

1. Transférer `HELIX-Icon-Pack-ICONS01-38.apk` sur le téléphone et l’ouvrir avec Mes fichiers ; autoriser cette source si Android le demande. Ou exécuter `adb install -r packages/HELIX-Icon-Pack-ICONS01-38.apk` depuis la racine du dépôt, avec le débogage USB autorisé.
2. Ouvrir **HELIX Icon Pack** et noter les composants signalés sans correspondance. Vérifier que les applications attendues sont présentes et activées.
3. Ouvrir **Good Lock → Theme Park → Icon / Icône → Create new / Créer → Iconpack / Pack d’icônes → Third Party Icon Packs → HELIX Icon Pack**. Les libellés peuvent varier selon la version.
4. Sélectionner le pack, vérifier les associations automatiques dans l’aperçu, enregistrer/installer un nouveau thème nommé par exemple `HELIX ICONS01`, puis choisir **Apply / Appliquer**.
5. Vérifier les icônes sur l’accueil et dans le tiroir, puis ouvrir les applications. Ne pas affecter les icônes individuellement pour masquer une absence de mapping.
6. Fermer/réouvrir Theme Park et One UI Home, puis redémarrer le téléphone ; vérifier la persistance du thème et l’absence de plantage. Le retour arrière consiste à réappliquer le thème d’icônes précédent/défaut.

En cas d’échec de mapping, copier le composant affiché dans HELIX, ou interroger un paquet précis :

```sh
adb shell cmd package query-activities --brief -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -p com.samsung.android.messaging
```

Reporter le composant effectivement observé dans `app-map.csv`, documenter son origine dans `mapping-evidence.json`, régénérer les XML avec `tools/sync_resources.py`, puis reconstruire.

À transmettre : modèle S24 et versions Android/One UI/Theme Park/One UI Home, version du pack/commit, installation réussie ou erreur exacte, visibilité et sélection du pack, résultat automatique par application (réussite/échec/non testée), composants problématiques, captures de l’aperçu et du résultat, persistance après redémarrage, étape de tout plantage.

## Vérification de livraison

Voir `icons/helix-icons01/BUILD-REPORT.md` pour le résultat effectif de compilation, les contrôles d’APK, les empreintes et le contrôle visuel. L’ancien état du pilote et sa procédure restent consultables au [commit pilote 2311e10](https://github.com/asylum-carolab/helix/commit/2311e100c9a1460da743c32d0fc6e4184cb78a60).
