# HELIX-PACK02 — Écran de verrouillage, Galaxy S24 / One UI 8.5

Cette livraison documentaire complète [PACK01](../HELIX-S24-PACK01/README.md). Elle décrit la configuration manuelle après réinitialisation du S24. Aucun réglage n'a encore été appliqué au téléphone, aucun profil importable n'est livré. La version cible One UI 8.5 est confirmée par le propriétaire ; les versions des modules seront relevées après leur installation.

Le bloc de la maquette `dyptique helix.png` est la référence de composition, pas un fond à installer. Utiliser exclusivement le fichier validé [verrouillage helix.png](../HELIX-S24-PACK01/wallpapers/verrouillage%20helix.png), strictement inchangé. Son paysage diffère de celui du diptyque : on reproduit le bloc typographique, pas toute la scène. Le logo déjà présent en bas du wallpaper reste visible.

## 1. Préparer le téléphone après le reset

1. Terminer l'assistant initial, connecter le réseau et le compte Samsung. Vérifier **Paramètres → À propos du téléphone → Informations sur le logiciel : One UI 8.5**. Installer les mises à jour proposées pour cette version et celles du Galaxy Store.
2. Dans **Gestion globale → Date et heure**, activer l'heure et le fuseau automatiques, puis le format **24 heures**. Choisir le français comme langue système pour la date. Ne pas fixer l'heure sur 14:46 ou la date sur le 27 août : ce sont seulement les exemples de la maquette.
3. Installer **Good Lock** depuis le Galaxy Store, puis ouvrir Good Lock et installer **ClockFace** et **LockStar** depuis leurs fiches officielles. Installer aussi **Theme Park** pour les icônes PACK01. Home Up et QuickStar ne sont pas nécessaires à ce bloc.
4. Ouvrir chacun des deux modules, suivre les demandes nécessaires à leur fonctionnement et relever leurs versions. Prendre les dernières versions compatibles proposées au S24, sans imposer un ancien numéro. Si un module n'est pas proposé dans la région ou déclaré incompatible, utiliser le repli de la section 6 et consigner ce blocage.
5. Exécuter les étapes 1 à 4 de PACK01 : APK existant, Theme Park, fond d'accueil, fond de verrouillage. Puis configurer le bloc ci-dessous, avant de reprendre les sons et la recette PACK01.

Ne pas appliquer de filtre, effet génératif, fond animé, rotation de fonds ou retouche au wallpaper. Conserver son cadrage validé ; si un ajustement d'affichage est indispensable, le noter, sans enregistrer une nouvelle image. Les textes du bloc sont des éléments d'interface indépendants du PNG.

## 2. Cible visuelle

Les mesures suivantes sont des repères de composition estimés sur le panneau gauche du diptyque, et non des valeurs garanties dans les menus Samsung. Utiliser l'aperçu pour les approcher. Priorité : lisibilité et fonctionnement dynamique, puis fidélité visuelle.

| Élément | Cible HELIX | Nature |
| --- | --- | --- |
| Heure | Numérique sur une ligne, HH:mm, sans secondes, sans AM/PM ; police sans empattement la plus fine disponible | Horloge système dynamique |
| Date | Jour abrégé, numéro, mois ; exemple de forme : `mer. 27 août`, sans année si proposé | Date dynamique liée au système |
| Séparateur | Trait court et fin cyan, centré sous la date | Décor d'interface |
| Signature | `H E L I X` en capitales, lettres espacées | Texte statique dans ClockFace |
| Sous-titre | `// MOBILE NODE`, petit, lettres aérées si réglage disponible | Texte statique dans ClockFace |

Repères : axe central du bloc vers **39 % de la largeur** ; haut de l'heure vers **14 % de la hauteur** ; bas du sous-titre vers **31 %**. Largeur de l'heure environ **30 % de l'écran**, signature 16 %, sous-titre 18 %, trait 5 %. Conserver environ une hauteur de date entre les niveaux. Déplacer légèrement l'ensemble si les contraintes de l'interface ou le paysage réel réduisent la lisibilité.

Palette de départ proposée, sans prétendre à une mesure exacte de la maquette : heure blanc glacé `#DDF8FF`, date bleu clair `#B9EFFF`, trait et signature cyan `#21DDF5`. Choisir la teinte disponible la plus proche si le module ne propose pas de saisie hexadécimale. La maquette montre une nuance cyan dans l'heure : une couleur unie est le repli prévu si le dégradé ou la couleur distincte du deux-points ne sont pas réglables.

## 3. Composer dans ClockFace

Samsung confirme l'ajout de textes et d'images dans ClockFace, et de date dans ses fonctions d'horloge. Les libellés et les contrôles précis dépendent de la version installée ; les étapes ci-dessous décrivent les choix à effectuer, sans garantir une commande absente de l'éditeur. [Fiche officielle ClockFace](https://galaxystore.samsung.com/detail/com.samsung.android.app.clockface?cntyCd=USA) ; [présentation Samsung des modules](https://www.samsung.com/lb/support/mobile-devices/good-lock-elevate-your-samsung-experience/).

1. Ouvrir **Good Lock → ClockFace**, choisir l'écran de verrouillage si ce choix apparaît. Créer une composition ou éditer une copie d'un cadran numérique minimal. La nommer `HELIX PACK02` si le nom est éditable.
2. Garder un véritable élément d'horloge numérique et une véritable date. Choisir la disposition HH:mm et la police fine disponible la plus proche. Régler l'heure comme élément dominant ; mettre la date plus petite juste dessous. Retirer seulement les ornements inutiles de cette nouvelle composition, jamais l'heure dynamique.
3. Ajouter un texte `H E L I X`, puis un deuxième texte `// MOBILE NODE`. Les centrer sur l'horloge, en cyan, avec le sous-titre nettement plus petit. Utiliser l'espacement des lettres si proposé ; sinon conserver les espaces explicites du titre et le sous-titre exact. Ne pas importer de police en supposant qu'elle sera prise en charge.
4. Pour le séparateur, utiliser une ligne ou forme fine **si disponible**. À défaut, essayer un élément texte `────` en cyan, à petite taille. C'est une approximation typographique : vérifier que le trait est continu. Si l'éditeur ne permet pas un résultat propre, omettre le trait et noter l'écart. Ne pas le dessiner sur le wallpaper.
5. Régler les couleurs, tailles et espacements selon la section 2, dans les limites offertes. Préserver assez de place pour une date longue et pour des chiffres larges. Enregistrer puis appliquer le cadran à l'écran de verrouillage avec l'action proposée par le module. Contrôler le résultat réel après verrouillage.

Si le format compact de date n'est pas proposé, conserver la date système disponible. Ne jamais saisir une fausse date en texte. Ne jamais importer une capture contenant heure et date. Aucun fond opaque ne doit masquer le paysage derrière le bloc.

## 4. Placer avec LockStar

Ouvrir **Good Lock → LockStar**, activer la personnalisation du verrouillage si demandé, puis ouvrir son éditeur. Sélectionner le cadran ClockFace enregistré si nécessaire et déplacer/redimensionner le groupe vers les repères ci-dessus. Enregistrer et vérifier sur l'écran verrouillé, pas seulement dans l'aperçu. Samsung décrit LockStar comme le module de placement des composants, avec choix de taille et disposition. [Présentation de l'équipe Samsung Members](https://r2.community.samsung.com/t5/Tips-How-to/Good-Lock-Clock/ba-p/21776115).

Conserver une seule horloge visible. Si une deuxième heure/date apparaît, vérifier le cadran sélectionné et les éléments de la composition ; ne pas masquer l'heure fonctionnelle avec une image. Si LockStar ne propose pas le cadran, revenir à l'éditeur natif par appui long sur le verrouillage, puis toucher l'horloge et rechercher le style ClockFace. Si aucune intégration n'est disponible dans les versions installées, passer à la section 6.

Choisir une taille et une disposition fixes lorsque ces options existent. Ne pas sélectionner la police adaptative/étirable pour cette composition : elle peut changer la silhouette recherchée. Samsung documente aussi des interactions entre l'horloge adaptative et les versions de LockStar ; maintenir le module à jour. [Aide Samsung sur l'horloge adaptative](https://www.samsung.com/us/support/troubleshoot/TSG10007610/).

Laisser une zone libre sous le bloc pour les notifications, le lecteur multimédia et la Now Bar lorsqu'elle apparaît. Préférer les notifications compactes si nécessaire, sans en masquer le contenu utile uniquement pour réussir une capture. Ne pas empiéter sur le lecteur d'empreinte, les raccourcis ou les indications de sécurité.

## 5. Limites à consigner sous One UI 8.5

| Point | Décision si la reproduction exacte est impossible |
| --- | --- |
| Police fine exacte de la maquette | Police installée la plus proche ; aucun nom de police exact n'est établi par l'image |
| Dégradé de l'heure / deux-points cyan | Heure unie blanc glacé ou cyan clair |
| Position au pixel près / taille maximale | Position permise la plus proche, sans chevauchement |
| Date française compacte | Format dynamique disponible ; casse et ponctuation peuvent différer |
| Trait cyan | Ligne disponible, puis texte `────`, sinon omission documentée |
| Espacement et nombre de textes | Espaces explicites dans HELIX ; si manque de place, réduire les textes avant l'heure |
| AOD | Recette distincte : taille, position, couleurs et synchronisation peuvent différer du verrouillage éveillé |

Les sources Samsung confirment les capacités générales, mais ne certifient pas tous ces réglages sur chaque combinaison S24 / One UI 8.5 / région / versions de modules. La fiche ClockFace indique la compatibilité de la famille 3.4.x avec One UI 8 et versions ultérieures, avec des exceptions selon les modèles. La fidélité exacte reste à valider sur le téléphone après reset.

## 6. Repli avec l'éditeur One UI

Faire un appui long sur l'écran verrouillé, s'authentifier si demandé, toucher l'horloge et choisir un style numérique fin avec sa date dynamique. Régler taille et couleur dans les contrôles disponibles. Pour la signature, utiliser **Paramètres → Écran de verrouillage et AOD → Informations de contact** avec `H E L I X // MOBILE NODE`, si ce champ n'est pas déjà réservé à des coordonnées utiles. [Guide Samsung de l'éditeur et des informations de contact](https://www.samsung.com/us/support/answer/ANS10013248/).

Ce repli conserve heure/date dynamiques et fond original, mais ne garantit ni deux lignes de texte, ni leur placement sous la date, ni le séparateur cyan. Le noter comme **reproduction partielle**, pas comme une validation visuelle complète. Si seul LockStar manque, conserver d'abord le cadran ClockFace et le placement natif ; réserver le repli complet à l'absence de cadran utilisable.

## 7. Recette sur le S24 physique

Tout est **non testé sur appareil** à la livraison de cette documentation. Relever la date du test, le modèle, la version complète One UI 8.5 et les versions Good Lock, ClockFace, LockStar, Theme Park.

- Vérifier le wallpaper d'origine, son cadrage et l'absence de filtre ; ne pas utiliser le diptyque comme fond.
- Observer au moins deux changements de minute sur le verrouillage : l'heure évolue sans intervention. Vérifier aussi après veille/réveil et redémarrage.
- Vérifier le changement de date au prochain minuit, le français et le format 24 heures ; ne pas valider sur une simple capture statique. Renseigner « non testé » tant que le passage de date n'a pas été observé.
- Contrôler heure/date uniques, lisibilité, signature et sous-titre exacts, séparateur et écart visuel par rapport à la maquette. Photographier le résultat et consigner les écarts acceptés.
- Tester plusieurs notifications, lecteur musical, Now Bar si disponible, appel entrant et déverrouillage par empreinte : aucun élément indispensable ne doit être masqué.
- Contrôler séparément l'AOD si utilisé, puis le retour au verrouillage éveillé. Vérifier la persistance du cadran après redémarrage.
- Terminer les essais PACK01 des icônes, fonds et sons. Reporter chaque contrôle comme réussite / échec / non testé.

Pour revenir à l'horloge standard : désactiver la personnalisation LockStar, sélectionner un cadran natif dans l'éditeur One UI, retirer la signature des informations de contact si ajoutée. Garder le wallpaper original. Ce retour ne nécessite pas de réinstaller l'APK.
