# HELIX Icon Pack — pilote HELIX-ICONS02

## Portée et statut

Pilote de compatibilité pour le Samsung Galaxy S24, application `fr.carolab.helix.icons`, version `0.1.0-pilot` (code 1). Seulement cinq applications : Samsung Téléphone, Samsung Messages, Samsung Appareil photo, Google Chrome et Gmail. Elles utilisent volontairement le même dessin temporaire HELIX « H ». Aucun catalogue complet ni nouveau visuel final.

**Validation physique S24 en attente.** La compilation et les contrôles d’APK ne prouvent pas la détection par Theme Park, les cinq associations sur le téléphone ou la stabilité de One UI Home. Ne pas étendre le catalogue avant ce test.

## Construire

Prérequis : JDK 17, Android SDK avec `platforms;android-35` et `build-tools;34.0.0`. `platform-tools` est utile pour ADB. Installer ces composants avec Android Studio ou `sdkmanager`, en acceptant les licences Android SDK. Définir `JAVA_HOME` et `ANDROID_HOME`, ou renseigner `sdk.dir` dans `packages/icon-pack/local.properties` (non versionné).

Versions de compilation fixées : Android Gradle Plugin 8.7.3, Gradle 8.9, API de compilation/cible 35, Build Tools 34.0.0, Java 17. Android minimum : API 26. Aucune dépendance d’exécution tierce, aucune permission Android, aucun réseau dans l’application.

Depuis `packages/icon-pack` :

```sh
./gradlew assembleDebug lintDebug
```

Sous Windows PowerShell :

```powershell
.\gradlew.bat assembleDebug lintDebug
```

Le wrapper est inclus et contrôle le SHA-256 de la distribution Gradle. La première compilation télécharge les outils Gradle et les dépendances de compilation Google/Maven ; elle nécessite Internet.

`verifyPilotResources`, exécuté avant la compilation, vérifie les cinq applications, l’unicité des composants, la cohérence CSV/appfilters/catalogues, les alias du dessin temporaire et l’absence de permissions. Il est aussi exécutable seul : `./gradlew verifyPilotResources`.

Sorties, relatives à la racine du dépôt :

- `packages/icon-pack/app/build/outputs/apk/debug/app-debug.apk` : sortie Gradle conservée localement, non versionnée ;
- `packages/HELIX-Icon-Pack-PILOT.apk` : copie automatique après `assembleDebug` réussi, destinée à l’installation et versionnée ;
- `packages/icon-pack/app/build/reports/lint-results-debug.html` : rapport Lint local.

L’APK debug est signé automatiquement avec la clé de test locale Android. La compilation est reproductible avec les versions ci-dessus ; les APK issus de machines différentes ne sont pas forcément identiques octet pour octet, notamment à cause de cette clé. Ne pas publier de clé privée. Une mise à jour Android doit utiliser la même clé ; si un autre build est déjà installé avec une signature différente, désinstaller l’ancien **HELIX Icon Pack** avant d’installer ce pilote. Ce n’est pas une version de production signée pour distribution en boutique.

## Vérifications de ce build

Compilation exécutée le 24 septembre 2026 sous Windows avec JDK 17.0.20.1 :

```powershell
.\gradlew.bat assembleDebug lintDebug --no-daemon --console=plain
```

Résultat : **BUILD SUCCESSFUL**, 45 tâches exécutées. Lint : 0 erreur, 8 avertissements examinés (ressources découvertes par nom considérées inutilisées, recherche de ressource par nom et règle de sauvegarde Android 12 ; le pilote ne stocke aucune donnée). `apksigner verify --verbose --print-certs` confirme la signature debug v2. `aapt dump badging`, `dump permissions` et `dump resources` confirment l’identifiant, la cible API 35, le minimum API 26, l’activité de lancement, les cinq alias et l’absence de permissions.

APK : 16 338 octets. SHA-256 : `d7299fd7f282bd64155e2b911975c2454e7cfb8e4ff2c646afd5bd457b55c09e`. La copie dans `packages/` est identique à la sortie Gradle. Installation/exécution et tests Theme Park sur le S24 : **non effectués**.

## Structure et correspondances

- `app-map.csv` recense les composants ciblés ; plusieurs lignes peuvent concerner la même application.
- `app/src/main/res/xml/appfilter.xml` et `app/src/main/assets/appfilter.xml` contiennent les mêmes entrées `ComponentInfo{package/classe.complete}`.
- `res/values/drawables.xml` expose cinq alias vers le vecteur existant `res/drawable/helix_pack.xml`.
- `res/values/iconpack.xml` fournit le tableau `icon_pack` ; `res/xml/drawable.xml` et `assets/drawable.xml` fournissent le catalogue standard.
- L’activité exportée possède les filtres de découverte ADW/ActivityStarter/Nova et un filtre de lancement Android. Le nom visible reste **HELIX Icon Pack**.
- L’écran du pilote lit les ressources et affiche les activités de lancement réellement visibles des cinq applications, avec leur présence ou absence dans l’appfilter. Les déclarations `queries` sont limitées à ces cinq paquets ; ce ne sont pas des permissions. Cette vérification locale ne teste pas Theme Park.

| Application | Paquet | Activité candidate |
| --- | --- | --- |
| Samsung Téléphone | `com.samsung.android.dialer` | `com.samsung.android.dialer.DialtactsActivity` |
| Samsung Messages | `com.samsung.android.messaging` | `com.android.mms.ui.ConversationComposer` |
| Samsung Messages | `com.samsung.android.messaging` | `com.samsung.android.messaging.ui.view.main.WithActivity` (candidat initial conservé, non corroboré) |
| Samsung Appareil photo | `com.sec.android.app.camera` | `com.sec.android.app.camera.Camera` |
| Google Chrome | `com.android.chrome` | `com.google.android.apps.chrome.Main` |
| Gmail | `com.google.android.gm` | `com.google.android.gm.ConversationListActivityGmail` |

Les cinq composants principaux, dont l’alias Messages `ConversationComposer`, ont été recoupés dans le [catalogue source Arcticons](https://github.com/Arcticons-Team/Arcticons/blob/main/app/src/main/res/xml/appfilter.xml). Ce recoupement ne remplace pas l’inspection du S24 : versions One UI, activités alias et applications installées peuvent varier. Samsung Messages et Google Messages sont des applications différentes ; Google Messages ne fait pas partie de ce pilote.

Références de structure : [standard de packs ADW documenté par Lawnchair](https://github.com/LawnchairLauncher/docs/blob/main/developers/concepts/icon-packs.md), [exemple officiel Nova](https://github.com/teslacoil/Example_NovaTheme), [compatibilité AGP 8.7](https://developer.android.com/build/releases/agp-8-7-0-release-notes). Aucune spécification publique Samsung examinée ne permet de certifier le comportement de cette version de Theme Park sans essai physique.

## Installer sur le Galaxy S24

1. Transférer `packages/HELIX-Icon-Pack-PILOT.apk` sur le téléphone, ou télécharger le fichier brut depuis GitHub (pas la page HTML).
2. Ouvrir l’APK dans Mes fichiers et autoriser cette source d’installation si Android le demande. Installer **HELIX Icon Pack**.
3. Ouvrir le pack. Vérifier l’absence d’erreur de ressources et lire les cinq résultats locaux. Copier les composants signalés absents du mapping. Une application absente/désactivée doit être signalée comme non testée.

Autre méthode, avec le débogage USB autorisé par le propriétaire du téléphone, depuis la racine du dépôt :

```sh
adb install -r packages/HELIX-Icon-Pack-PILOT.apk
adb shell am start -n fr.carolab.helix.icons/.MainActivity
```

En cas de doute sur un composant, utiliser l’écran du pilote ou, en remplaçant le paquet :

```sh
adb shell cmd package query-activities --brief -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -p com.samsung.android.messaging
```

Reporter le composant exact dans le CSV et les deux appfilters, puis reconstruire. Ne pas déclarer un succès en remplaçant manuellement l’icône dans Theme Park.

## Test physique Theme Park

Les libellés peuvent varier selon la langue et la version ; relever les versions avant le test.

1. Noter le modèle du S24, Android, One UI, Theme Park et One UI Home, ainsi que la version du pack et le commit utilisé.
2. Ouvrir **Samsung Good Lock → Theme Park → Icon / Icône → Create new / Créer**.
3. Ouvrir **Iconpack / Pack d’icônes** (selon la version : bouton Icon puis Iconpack).
4. Dans **Third Party Icon Packs**, vérifier que **HELIX Icon Pack** est présent. Faire une capture de cette liste.
5. Sélectionner **HELIX Icon Pack**. Vérifier dans l’aperçu que Téléphone, Samsung Messages, Appareil photo, Chrome et Gmail reçoivent automatiquement l’icône H. Aucune affectation individuelle.
6. Enregistrer/installer le thème créé avec le bouton de téléchargement/enregistrement de Theme Park et un nom identifiable, par exemple `HELIX PILOT`. Revenir à la liste des thèmes d’icônes, sélectionner ce thème puis **Apply / Appliquer** si l’application n’est pas automatique.
7. Vérifier les cinq icônes sur l’accueil et dans le tiroir d’applications. Ouvrir chacune, revenir à l’accueil et vérifier qu’elle lance toujours la bonne application.
8. Fermer/réouvrir Theme Park et One UI Home, puis redémarrer le téléphone. Vérifier que les icônes persistent et qu’aucun plantage ne survient. Pour revenir à l’état précédent, réappliquer le thème d’icônes précédent/défaut.

## Résultats à transmettre

- Modèle, versions Android/One UI/Theme Park/One UI Home, version du pack et commit.
- Installation : réussite ou message d’erreur exact.
- Pack visible dans Third Party Icon Packs : oui/non ; sélection possible : oui/non.
- Association automatique, séparément : Téléphone, Samsung Messages, Appareil photo, Chrome, Gmail — réussite/échec/non testée ; confirmer qu’aucune icône n’a été assignée à la main.
- Composants affichés par le pilote pour chaque échec et état installé/activé de l’application.
- Application du thème, lancement des cinq apps et persistance après redémarrage : réussite/échec.
- Plantage Theme Park ou One UI Home : oui/non, étape exacte et message éventuel.
- Captures de la liste des packs, de l’aperçu et du résultat sur le téléphone.

La compatibilité n’est validée que lorsque le pack est détecté et sélectionnable, que les cinq applications présentes sont automatiquement associées et que l’application du thème reste stable. Un résultat non testé reste non validé.
