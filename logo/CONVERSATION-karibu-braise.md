# Conversation : refonte du logo KARIBU BRAISE (pour le projet Issa Fast Food)

> Contexte à donner à Claude : voici l'historique de notre travail sur le logo du fast food KARIBU BRAISE. Le travail (SVG, page preview.html, scripts) est sur GitHub : dépôt `ya771668-hub/mon-premier-projet`, branche `claude/focused-faraday-ekur9v`, dossiers `logo/` et `reference/`. Les 2 photos du logo actuel sont jointes.

---

## Message 1 : moi (le brief)

Tu es un directeur artistique spécialisé en identité de marque pour la restauration rapide, avec 10 ans d'expérience en création de logos (fast food, street food, food trucks). Tu travailles en SVG propre et vectoriel.

**Contexte :** je refais le logo de mon fast food « KARIBU BRAISE » (brochettes, grillades, frites). « Karibu » veut dire « bienvenue » en swahili et en comorien. Le concept : la cuisine au feu de bois des îles Comores, avec une touche africaine.
Slogan : « Le feu de nos îles, le goût de l'Afrique. »

**Diagnostic du logo actuel :**
- Trop d'éléments : flamme, 2 brochettes photoréalistes, palmier, oiseaux, volcan, vagues, arc, piques. Résultat : illisible en petit.
- Les brochettes en photo ne passent pas en vectoriel, en impression ou en broderie.
- Les dégradés dorés « effet IA » font amateur.
- Il ne fonctionne pas en petit format (icône Glovo, photo de profil Instagram, tampon sur emballage).
- Il n'existe aucune version une couleur.

**Ce que je veux :** un logo moderne et professionnel, qui donne faim et qui attire l'œil. Style flat ou semi-flat, formes simples, lisible de 32 px jusqu'à l'enseigne de 3 m.
- **À garder :** l'esprit flamme + brochette, les couleurs noir, or et rouge braise, une touche insulaire discrète (le volcan Karthala ou une vague, PAS les deux).
- **À supprimer :** le photoréalisme, les oiseaux, l'accumulation de décors.

**Étapes :**
1. Proposer 3 directions créatives en SVG (A = emblème/badge, B = monogramme « K » + flamme, C = logotype typographique fort), avec 3 lignes d'explication chacune.
2. Les montrer dans une page preview.html : fond noir, fond blanc, et mockups simples (enseigne, gobelet, sac kraft, icône d'appli ronde, story Instagram).
3. Attendre mon choix avant de finaliser.
4. Sur la direction choisie, livrer le kit complet :
   - `logo-principal.svg` (empilé) ;
   - `logo-horizontal.svg` ;
   - `icone.svg` (lisible en 32 px) ;
   - versions monochromes blanc, noir et or ;
   - version avec slogan ;
   - PNG en 512, 1024 et 2048 px (fond transparent) ;
   - `charte.html` : palette en HEX, RGB et CMJN, typos Google Fonts, zone de protection, taille minimale, exemples à ne pas faire.

**Contraintes :**
- SVG propres avec le texte vectorisé, aucune image bitmap, 4 couleurs maximum.
- Palette : noir charbon, or chaud, rouge braise, orange flamme, avec un contraste vérifié.
- Typo : un titre fort et chaleureux pour KARIBU, une sans-serif lisible pour BRAISE et le slogan.
- Accents du slogan vérifiés (« îles », « goût »).
- Le logo doit rester reconnaissable en noir et blanc pur.
- Avant de livrer : vérifier que l'icône est lisible en 32 px, que le logo marche en une couleur et qu'il donne envie de manger.

## Réponse 1 : Claude (3 directions + preview.html)

Le fichier `reference/logo-actuel.jpg` était absent, j'ai donc travaillé à partir du diagnostic écrit. La page `logo/preview.html` montre chaque direction sur fond noir, sur fond blanc et en noir seul, avec les mockups (enseigne, gobelet, sac kraft, story Instagram, icône d'appli à 120, 64, 48 et 32 px) et un test réel à 32 et 16 px.

- **A · Emblème « Karthala »** (volcan)
  - Concept : un médaillon rond, avec la flamme-brochette qui sort du cratère du Karthala. KARIBU est en Rammetto One, BRAISE est espacé.
  - Atout : le badge se lit comme un sceau « grillé maison », idéal pour le tampon kraft et la broderie.
  - Limite : c'est la direction la plus détaillée, donc l'icône est la moins nette en 32 px.
- **B · Monogramme « K-brochette »** (vague)
  - Concept : la barre du K est une brochette (viande / légume / viande), la branche haute est une flamme. Typo Lilita One.
  - Atout : le K se lit même à 16 px, en couleur, en noir et en blanc. C'est la direction la plus forte en petit format.
- **C · Logotype « Torche »** (vague)
  - Concept : KARIBU en Shrikhand, une police grasse et généreuse, dont le I devient une brochette surmontée d'une flamme.
  - Atout : le style street food rétro est le plus appétissant sur une enseigne.
  - Limite : l'icône est plus abstraite.

**Palette (4 couleurs) :**

| Couleur | HEX |
|---|---|
| Noir charbon | #1C1714 |
| Or chaud | #F2B138 |
| Rouge braise | #C7361F |
| Orange flamme | #F47A20 |

**Contrastes :**
- Sur fond noir, l'or ressort très bien (9,4:1) et l'orange aussi (6,5:1).
- Le rouge sur noir est faible (3,4:1) : je ne l'utilise que pour des formes, jamais pour un petit texte.
- Le rouge sur blanc passe (5,3:1).
- L'or sur blanc ne fonctionne pas (1,9:1) : sur fond clair, le texte passe donc en noir.

**Typos :**
- KARIBU : Rammetto One, Lilita One ou Shrikhand, selon la direction ;
- BRAISE : Barlow Condensed ExtraBold ;
- slogan : Barlow SemiBold.

Le texte est vectorisé. Il n'y a ni image bitmap, ni dégradé, ni masque : les découpes sont de vraies formes vectorielles.

Ma recommandation : B comme base, éventuellement avec la typo de C pour plus de chaleur.

---

## Message 2 : moi

« Vois les photos d'exemple » (j'ai envoyé 2 photos de mon logo actuel : la version simple, et la version avec « BROCHETTES • GRILLADES • FRITES » et le slogan en script).

## Réponse 2 : Claude (analyse + direction D)

Les images ont été ajoutées dans `reference/logo-actuel.jpg` et `reference/logo-actuel-slogan.jpg`.

**Analyse du logo actuel :**
- Il compte environ 11 éléments, avec des dégradés partout. En 32 px, ce n'est plus qu'une tache orange.
- Ses atouts à garder : la flamme au centre avec 2 brochettes croisées en X, KARIBU en capitales serif dorées avec une vague dans le A, et BRAISE en rouge entre deux filets.

**Nouvelle direction D · « Évolution du logo actuel »**
- **On garde :** la flamme centrale, les brochettes en X, KARIBU en serif or (Cinzel Black), la vague dans le A, BRAISE entre ses filets.
- **On retire :** le palmier, les oiseaux, le volcan, l'arc, les piques et les dégradés. Les brochettes en photo deviennent des formes pleines.
- **Résultat :** il marche en noir seul ; en 32 px, il est correct mais moins net que B.

**Avis :**
- D si l'enseigne actuelle est déjà connue des clients (continuité, sans perdre la clientèle) ;
- B pour repartir de zéro avec le logo le plus fort en petit format.

---

## Messages 3 et 4 : moi

« Transfère toute notre discussion et les images sur notre projet Issa Fast Food », puis « regarde dans mes projets sur Claude Code ».

## Réponse : Claude

Aucun projet « Issa Fast Food » n'a été trouvé (ni GitHub, ni sessions Claude Code, ni Drive, ni Notion). J'ai préparé un dossier de transfert :
- `logo/TRANSFERT-projet-issa-fast-food.md` ;
- `logo/karibu-braise-transfert.zip` ;
- les 2 images.

---

## OÙ ON EN EST / PROCHAINE ÉTAPE

**Décision en attente :** choisir la direction A, B, C, D ou un mélange (par exemple l'icône de B avec la typo de D).

Ensuite, livrer le kit complet :
- `logo-principal.svg`, `logo-horizontal.svg`, `icone.svg` ;
- les versions blanc, noir et or, et la version avec slogan ;
- les PNG en 512, 1024 et 2048 px ;
- `charte.html`.

**Fichiers sur GitHub** (`ya771668-hub/mon-premier-projet`, branche `claude/focused-faraday-ekur9v`) :
- `logo/preview.html` : page de présentation des 4 directions ;
- `logo/directions/` : les SVG de A, B, C et D ;
- `logo/src/` : les scripts Python de génération (fontTools + skia-pathops, polices Google Fonts via npm @fontsource) ;
- `reference/` : les photos du logo actuel.
