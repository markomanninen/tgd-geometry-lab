# TGD Geometry Lab

[![tests](https://github.com/markomanninen/tgd-geometry-lab/actions/workflows/tests.yml/badge.svg)](https://github.com/markomanninen/tgd-geometry-lab/actions/workflows/tests.yml)

Symbolinen differentiaaligeometrian laskentaympäristö **Maximan** päällä Topological Geometrodynamics (TGD) -teorian geometrian tutkimiseen: $CP_2$:n Fubini–Study-geometria, differentiaalimuodot, yhteydet ja kaarevuus, upotusavaruus $H=M^4\times CP_2$, indusoitu geometria ja TGD:n toimintaperiaate.

*Symbolic differential-geometry toolkit for Maxima aimed at Topological Geometrodynamics: CP₂ Fubini–Study geometry, differential forms, curvature, embeddings into M⁴×CP₂ and the Kähler/volume action. Every module is checked by automatic identity tests.*

Rakenne ja ajotapa seuraavat [LanyonScriptsin](https://github.com/lanyonai/LanyonScripts) Colab-esimerkkiä, ja Clifford-algebra tulee Dimiter Prodanovin [`clifford`](https://github.com/dprodanov/clifford)-paketista.

## Colab-kirjat

| Kirja | Sisältö | |
|---|---|---|
| 01 · Ympäristö ja testit | asennus, koko testisarja, Clifford-relaatiot, LanyonScriptsin esimerkit vertailuna | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/markomanninen/tgd-geometry-lab/blob/main/notebooks/01_ymparisto_ja_testit.ipynb) |
| 02 · $CP_2$ ja Fubini–Study | Kähler-potentiaali → metriikka → $\omega$, $J$ → Christoffel → Riemann/Ricci → karttasiirtymät | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/markomanninen/tgd-geometry-lab/blob/main/notebooks/02_cp2_fubini_study.ipynb) |
| 03 · Upotus ja toiminta | $H=M^4\times CP_2$, kanoninen $M^4$, kosminen säie, massaton ekstremaali, Euler–Lagrange | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/markomanninen/tgd-geometry-lab/blob/main/notebooks/03_upotus_ja_toiminta.ipynb) |

## Mitä on varmistettu (53 testiä)

| Alue | Tarkistukset |
|---|---|
| Metriikka | käänteismatriisi, determinantti, signatuuri, tensorimuunnos |
| Muodot | $dx\wedge dy=-dy\wedge dx$, $d^2=0$, Leibniz, Hodge $\star\star=\pm1$ |
| Kaarevuus ($S^2$-vertailu) | $\mathrm{Ric}=g$, $R=2$, $\nabla g=0$ |
| $CP_2$ | $\det g=16/(1+\rho^2)^6$, $J^2=-1$, $d\omega=0$, $\nabla J=0$, $\tfrac12\omega\wedge\omega=\mathrm{vol}$, Riemannin symmetriat, Bianchi I ja II, $\mathrm{Ric}=3g$, $R=12$, holomorfinen leikkauskaarevuus $2$, karttasiirtymä $Z_0\leftrightarrow Z_1$ |
| Upotus | $H$:n signatuuri $(1,7)$; kanoninen $M^4$: $g=m$, $J=0$; kosminen säie: $J_{\alpha\beta}J^{\alpha\beta}=2$; ME: $J\ne0$, $J_{\alpha\beta}J^{\alpha\beta}=0$, $J\wedge J=0$ |
| Toiminta | Euler–Lagrange → aaltoyhtälö; tilavuustoiminta → minimipintayhtälö |
| Clifford | $\{\gamma_a,\gamma_b\}=2\eta_{ab}$ signatuureille $(4,0)$ ja $(1,3)$ |

## Käyttö paikallisesti

```bash
sudo apt-get install maxima
git clone https://github.com/markomanninen/tgd-geometry-lab.git
git clone https://github.com/dprodanov/clifford.git      # valinnainen
cd tgd-geometry-lab
./scripts/run_tests.sh ../clifford
```

```maxima
tgd_root : "/polku/tgd-geometry-lab"$
load(sconcat(tgd_root, "/tgd-lab.mac"))$
G   : cp2_metric()$
Gam : christoffel(G, cp2_X)$
Ric : ricci(riemann(Gam, cp2_X))$
tgd_msimp(Ric - 3*G);          /* => nollamatriisi */
```

## Rakenne

```
core/metric.mac             monistot, metriikat, muunnokset
geometry/curvature.mac      Christoffel, ∇, Riemann, Ricci, Bianchi, leikkauskaarevuus
forms/forms.mac             muodot, ∧, d, sisätulo, Hodge ⋆
spaces/cp2.mac              CP2: Fubini–Study, ω, J, kartat
spaces/embedding-space.mac  M4 ja H = M4 × CP2
embedding/induced.mac       indusoitu metriikka ja Kähler-muoto
tgd/action.mac              L_K, L_V, J∧J, Euler–Lagrange
tests/                      automaattiset testit
notebooks/                  Colab-kirjat + tgdlab.py (Maxima → LaTeX -silta)
docs/                       kehityssuunnitelma ja konventiot
```

## Dokumentaatio

- [Kehityssuunnitelma](docs/kehityssuunnitelma.md): vaiheet I–VIII ja välitavoitteet M1–M8; jokainen vaihe on linkitetty issueensa.
- [Konventiot](docs/konventiot.md): etumerkit, normalisoinnit ja indeksijärjestykset.
- [Seuranta](docs/seuranta.md): tilataulukko, kriittinen polku ja työnkulku.

## Seuranta

| Välitavoite | Edistyminen |
|---|---|
| [M1 Ympäristö](https://github.com/markomanninen/tgd-geometry-lab/milestone/1) | 4/4 ✅ |
| [M2 CP2-metriikka](https://github.com/markomanninen/tgd-geometry-lab/milestone/2) | 4/6 |
| [M3 Muodot](https://github.com/markomanninen/tgd-geometry-lab/milestone/3) | 2/3 |
| [M4 Kaarevuus](https://github.com/markomanninen/tgd-geometry-lab/milestone/4) | 2/3 |
| [M5 Clifford-geometria](https://github.com/markomanninen/tgd-geometry-lab/milestone/5) | 1/4 |
| [M6 Upotus](https://github.com/markomanninen/tgd-geometry-lab/milestone/6) | 2/4 |
| [M7 Toiminta](https://github.com/markomanninen/tgd-geometry-lab/milestone/7) | 2/6 |
| [M8 Ratkaisut](https://github.com/markomanninen/tgd-geometry-lab/milestone/8) | 0/2 |

Ajantasainen tila on [milestone-sivulla](https://github.com/markomanninen/tgd-geometry-lab/milestones). Kriittinen polku on #18 vielbein → #16 Cartan / #19 spin-yhteys → #23 toinen perusmuoto → #27 $L_{TGD}$:n variaatio → #28 tarkistus, että kosminen säie ja ME ovat ekstremaaleja.

Järjestelmä ei todista TGD:tä fysikaalisesti oikeaksi. Sen tarkoitus on tarkistaa johdoksia ja tutkia erikoistapauksia luotettavasti.

## Lisenssi

MIT. Riippuvuudet: Maxima (GPL) ja Prodanovin `clifford` (LGPL-2.1) ladataan erikseen, eikä niitä jaeta tämän repositorion mukana.
