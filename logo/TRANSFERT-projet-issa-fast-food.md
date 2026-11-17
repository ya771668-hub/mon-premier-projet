# KARIBU BRAISE : refonte du logo, récapitulatif de la discussion

*À coller ou importer dans le projet « Issa Fast Food ». Date : 17/11/2026.*

## 1. Brief de départ
- **Restaurant :** KARIBU BRAISE, un fast food (brochettes, grillades, frites). « Karibu » veut dire « bienvenue » en swahili et en comorien.
- **Concept :** la cuisine au feu de bois des Comores, avec une touche africaine.
- **Slogan :** « Le feu de nos îles, le goût de l'Afrique. »
- **Objectif :** un logo moderne et pro, en flat ou semi-flat, lisible de 32 px (icône Glovo, profil Instagram) jusqu'à une enseigne de 3 m.
- **À garder :** l'esprit flamme + brochette, les couleurs noir, or et rouge braise, et une seule touche insulaire (le volcan Karthala OU une vague).
- **À supprimer :** le photoréalisme, les oiseaux, l'accumulation de décors, les dégradés « effet IA ».
- **Contraintes :** des SVG propres avec le texte vectorisé, 4 couleurs maximum, une version une couleur, et un logo reconnaissable en noir et blanc.

## 2. Diagnostic du logo actuel
Les images sont dans `reference/logo-actuel.jpg` et `reference/logo-actuel-slogan.jpg`.
- On compte environ 11 éléments : flamme, 2 brochettes en photo, palmier, oiseaux, volcan, vagues, arc, piques, slogan, et la ligne « Brochettes • Grillades • Frites ».
- Les dégradés dorés sont partout. En 32 px, le logo n'est plus qu'une tache orange.
- Les brochettes en photo ne peuvent être ni vectorisées, ni brodées, ni tamponnées.
- **Les atouts à garder :**
  - la flamme au centre avec les 2 brochettes croisées en X ;
  - KARIBU en capitales serif dorées, avec la vague dans le A ;
  - BRAISE en rouge, entre deux filets.

## 3. Palette proposée (4 couleurs)

| Couleur | HEX | Usage |
|---|---|---|
| Noir charbon | #1C1714 | fond, texte sur fond clair |
| Or chaud | #F2B138 | KARIBU sur fond noir (contraste 9,4:1) |
| Rouge braise | #C7361F | formes, BRAISE sur fond blanc (5,3:1) ; pas de petit texte sur fond noir (3,4:1) |
| Orange flamme | #F47A20 | flamme, BRAISE sur fond noir (6,5:1) |

Pas d'or pour du texte sur fond blanc : le contraste n'est que de 1,9:1.

## 4. Typographies (Google Fonts, libres de droits)
- **KARIBU :**
  - Rammetto One pour la direction A ;
  - Lilita One pour B ;
  - Shrikhand pour C ;
  - Cinzel Black pour D.
- **BRAISE :** Barlow Condensed ExtraBold, avec un grand espacement entre les lettres.
- **Slogan :** Barlow SemiBold. Les accents « îles » et « goût » sont vérifiés.

## 5. Les 4 directions proposées

| Direction | Concept | Touche insulaire | Points forts / limites |
|---|---|---|---|
| **A · Emblème « Karthala »** | Un médaillon rond : la flamme-brochette sort du cratère du volcan | Volcan | Sceau « grillé maison », idéal en tampon et en broderie ; l'icône est la moins nette en 32 px |
| **B · Monogramme « K-brochette »** | Le fût du K est une brochette (viande / légume / viande), la branche haute est une flamme | Vague | **La plus lisible en 32 et 16 px**, comme icône d'appli de grande chaîne |
| **C · Logotype « Torche »** | KARIBU en script gras, dont le I est une brochette coiffée d'une flamme | Vague sous le nom | Le plus appétissant sur une enseigne ; l'icône est plus abstraite |
| **D · Évolution du logo actuel** | La même structure (flamme + 2 brochettes en X + KARIBU serif avec la vague dans le A + BRAISE entre filets), en aplats | Vague dans le A | Continuité totale avec l'enseigne actuelle ; l'icône est un peu plus large |

**Recommandation :**
- D si l'enseigne actuelle est déjà connue des clients ;
- B pour repartir de zéro avec le logo le plus fort en petit format ;
- un mélange est possible, par exemple l'icône de B avec la typo de D.

## 6. Vérifications faites
- Les 4 directions passent en noir pur. Les découpes entre la flamme et les brochettes sont de vraies formes vectorielles, sans masque, donc compatibles avec le tampon, la sérigraphie et la broderie.
- Tests en taille réelle à 32 et à 16 px : B est très net, A, C et D sont corrects.
- Il n'y a aucune image bitmap ni aucun dégradé dans les logos, et chaque version utilise au plus 4 couleurs.

## 7. Prochaine étape (en attente)
**Choisir A, B, C, D ou un mélange.** Le kit complet sera livré ensuite :
- les logos SVG :
  - `logo-principal.svg` (empilé) ;
  - `logo-horizontal.svg` ;
  - `icone.svg` ;
- les versions blanc, noir et or, et une version avec le slogan ;
- les PNG transparents en 512, 1024 et 2048 px ;
- `charte.html` : palette en HEX, RGB et CMJN, typos, zone de protection, taille minimale, et exemples à ne pas faire.

## 8. Fichiers
- `logo/preview.html` : la page de présentation (fond noir et fond blanc, mockups enseigne, gobelet, sac kraft, story et icône d'appli).
- `logo/directions/` : les SVG de chaque direction en couleur, sur fond clair, en noir, et l'icône.
- `logo/src/` : les scripts Python qui génèrent les logos (fontTools + skia-pathops).
- `reference/` : le logo actuel, les 2 photos envoyées.
