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

## Mitä on varmistettu (194 testiä)

| Alue | Tarkistukset |
|---|---|
| Metriikka | käänteismatriisi, determinantti, signatuuri, tensorimuunnos |
| Muodot | $dx\wedge dy=-dy\wedge dx$, $d^2=0$, Leibniz, Hodge $\star\star=\pm1$, Stokes, Kähler-vuo $\pi$ yli $CP_1$:n ja $2\pi$ yli kartion |
| Kaarevuus ($S^2$-vertailu) | $\mathrm{Ric}=g$, $R=2$, $\nabla g=0$ |
| $CP_2$ | $\det g=1/(1+\rho^2)^6$, $J^2=-1$, $d\omega=0$, $\nabla J=0$, $\tfrac12\omega\wedge\omega=\mathrm{vol}$, Riemannin symmetriat, Bianchi I ja II, $\mathrm{Ric}=6g$, $R=24$, holomorfinen leikkauskaarevuus $4$, $S_K(CP_2)=\pi/(8\alpha_K)$ (TGD-normalisointi), kaikki karttasiirtymät |
| Upotus | $H$:n signatuuri $(1,7)$; kanoninen $M^4$: $g=m$, $J=0$; kosminen säie: $J_{\alpha\beta}J^{\alpha\beta}=2$; ME: $J\ne0$, $J_{\alpha\beta}J^{\alpha\beta}=0$, $J\wedge J=0$ |
| Kehykset ja Cartan | $g=e^T\eta e$; $T^a=0$; $\Omega$ = Riemann; spin-yhteys kahta reittiä ($CP_2$, $H$, FRW) |
| Spinorit | $D_\mu\gamma^\nu=0$; $\tfrac12\gamma\gamma F=-R/4$; $k=3$ antaa vakion $\nu_R$; vuo kokonaisluku parittomilla $k$ |
| Ekstrinsinen geometria | $B^k{}_{\alpha\beta}$, $H^k$; Gauss, Codazzi ja Ricci kaarevassa ympäristössä |
| Toiminta | Euler–Lagrange → aaltoyhtälö; tilavuustoiminta → minimipintayhtälö; kovariantti kenttäyhtälö = määritelmästä laskettu $E_k$ |
| Ekstremaalit | kosminen säie ja ME $s^k(u)$ kaikilla $c_K$, $c_V$; yleinen $s^k(u,x)$ on Kähler-ekstremaali, mutta tilavuustermi ei häviä ([taulukko](docs/konventiot.md)) |
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
tgd_msimp(Ric - 6*G);          /* => nollamatriisi */
```

## Rakenne

```
core/metric.mac             monistot, metriikat, muunnokset
geometry/curvature.mac      Christoffel, ∇, Riemann, Ricci, Bianchi, leikkauskaarevuus
forms/forms.mac             muodot, ∧, d, sisätulo, Hodge ⋆
algebra/vielbein.mac        kehykset
algebra/spinor.mac          spinoriyhteys, Kähler-kytkentä, gammat, Dirac
geometry/cartan.mac         yhteysmuodot, torsio, kaarevuusmuodot, spin-yhteys
spaces/cp2.mac              CP2: Fubini–Study, ω, J, kartat
spaces/embedding-space.mac  M4 ja H = M4 × CP2
embedding/induced.mac       indusoitu metriikka ja Kähler-muoto
embedding/second-form.mac   toinen perusmuoto, Gauss, Codazzi, Ricci
tgd/action.mac              L_K, L_V, J∧J, Euler–Lagrange
tgd/field-equations.mac     kovariantit kenttäyhtälöt
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
| [M2 CP2-metriikka](https://github.com/markomanninen/tgd-geometry-lab/milestone/2) | 6/6 ✅ |
| [M3 Muodot](https://github.com/markomanninen/tgd-geometry-lab/milestone/3) | 3/3 ✅ |
| [M4 Kaarevuus](https://github.com/markomanninen/tgd-geometry-lab/milestone/4) | 3/3 ✅ |
| [M5 Clifford-geometria](https://github.com/markomanninen/tgd-geometry-lab/milestone/5) | 4/4 ✅ |
| [M6 Upotus](https://github.com/markomanninen/tgd-geometry-lab/milestone/6) | 4/4 ✅ |
| [M7 Toiminta](https://github.com/markomanninen/tgd-geometry-lab/milestone/7) | 2/6 |
| [M8 Ratkaisut](https://github.com/markomanninen/tgd-geometry-lab/milestone/8) | 0/2 |

Ajantasainen tila on [milestone-sivulla](https://github.com/markomanninen/tgd-geometry-lab/milestones). Kriittinen polku #18 → #16/#19 → #23 → #27 → #28 on laskettu ja testattu. #27 ja #28 odottavat Matti Pitkäsen linjausta toiminnan $S_K+S_V$ kertoimista ja ME:n määritelmästä.

Järjestelmä ei todista TGD:tä fysikaalisesti oikeaksi. Sen tarkoitus on tarkistaa johdoksia ja tutkia erikoistapauksia luotettavasti.

## Lisenssi

MIT. Riippuvuudet: Maxima (GPL) ja Prodanovin `clifford` (LGPL-2.1) ladataan erikseen, eikä niitä jaeta tämän repositorion mukana.
