# TGD Geometry Lab

[![tests](https://github.com/markomanninen/tgd-geometry-lab/actions/workflows/tests.yml/badge.svg)](https://github.com/markomanninen/tgd-geometry-lab/actions/workflows/tests.yml)

Symbolinen differentiaaligeometrian laskentaympäristö **Maximan** päällä Topological Geometrodynamics (TGD) -teorian geometrian tutkimiseen. Mukana ovat $CP_2$:n Fubini–Study-geometria, differentiaalimuodot, yhteydet ja kaarevuus, upotusavaruus $H=M^4\times CP_2$, indusoitu geometria ja TGD:n toimintaperiaate.

**Tulokset voi lukea [sivustolta](https://markomanninen.github.io/tgd-geometry-lab/).**

*Symbolic differential-geometry toolkit for Maxima aimed at Topological Geometrodynamics, covering CP₂ Fubini–Study geometry, differential forms, curvature, embeddings into M⁴×CP₂ and the Kähler/volume action. Every module is checked by automatic identity tests.*

TGD on Matti Pitkäsen kehittämä teoria. Pitkänen on teoreettisen fysiikan tohtori, ja hän on kehittänyt sitä 1980-luvun alusta lähtien.

Rakenne ja ajotapa seuraavat [LanyonScriptsin](https://github.com/lanyonai/LanyonScripts) Colab-esimerkkiä, ja työtapa on saanut vaikutteita Jonathan Gorardin johtaman [Lanyon AI](https://lanyon.ai/):n verifioidusta laskennasta. Clifford-algebra tulee Dimiter Prodanovin [`clifford`](https://github.com/dprodanov/clifford)-paketista.

## Colab-kirjat

| Kirja | Sisältö | |
|---|---|---|
| 01 · Ympäristö ja testit | asennus, koko testisarja, Clifford-relaatiot, LanyonScriptsin esimerkit vertailuna | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/markomanninen/tgd-geometry-lab/blob/main/notebooks/01_ymparisto_ja_testit.ipynb) |
| 02 · $CP_2$ ja Fubini–Study | Kähler-potentiaali → metriikka → $\omega$, $J$ → Christoffel → Riemann/Ricci → karttasiirtymät | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/markomanninen/tgd-geometry-lab/blob/main/notebooks/02_cp2_fubini_study.ipynb) |
| 03 · Upotus ja toiminta | $H=M^4\times CP_2$, kanoninen $M^4$, kosminen säie, massaton ekstremaali, Euler–Lagrange | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/markomanninen/tgd-geometry-lab/blob/main/notebooks/03_upotus_ja_toiminta.ipynb) |
| 04 · Numeriikka ja kuvat | yhtälön tyyppi kertoimien funktiona, Kähler-vuo ja kentät ratkaisulla, ja numeriikka tarkistetaan analyyttisiä arvoja vasten | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/markomanninen/tgd-geometry-lab/blob/main/notebooks/04_numeriikka_ja_kuvat.ipynb) |

## Mitä on varmistettu (329 testiä)

| Alue | Tarkistukset |
|---|---|
| Metriikka | käänteismatriisi, determinantti, signatuuri, tensorimuunnos |
| Muodot | $dx\wedge dy=-dy\wedge dx$, $d^2=0$, Leibniz, Hodge $\star\star=\pm1$, Stokes, Kähler-vuo $\pi$ yli $CP_1$:n ja $2\pi$ yli kartion |
| Kaarevuus ($S^2$-vertailu) | $\mathrm{Ric}=g$, $R=2$, $\nabla g=0$ |
| $CP_2$ | $\det g=1/(1+\rho^2)^6$, $J^2=-1$, $d\omega=0$, $\nabla J=0$, $\tfrac12\omega\wedge\omega=\mathrm{vol}$, Riemannin symmetriat, Bianchi I ja II, $\mathrm{Ric}=6g$, $R=24$, holomorfinen leikkauskaarevuus $4$, $S_K(CP_2)=\pi/(8\alpha_K)$ (TGD-normalisointi), kaikki karttasiirtymät |
| Upotus | $H$:n signatuuri on $(1,7)$. Kanonisella $M^4$:llä $g=m$ ja $J=0$. Kosmisella säikeellä $J_{\alpha\beta}J^{\alpha\beta}=2$. ME:llä $J\ne0$, $J_{\alpha\beta}J^{\alpha\beta}=0$ ja $J\wedge J=0$. |
| Kehykset ja Cartan | $g=e^T\eta e$, $T^a=0$ ja $\Omega$ = Riemann sekä spin-yhteys kahta reittiä ($CP_2$, $H$, FRW) |
| Spinorit | $D_\mu\gamma^\nu=0$ ja $\tfrac12\gamma\gamma F=-R/4$. Kerroin $k=3$ antaa vakion $\nu_R$, ja vuo on kokonaisluku parittomilla $k$. |
| Ekstrinsinen geometria | $B^k{}_{\alpha\beta}$ ja $H^k$ sekä Gauss, Codazzi ja Ricci kaarevassa ympäristössä |
| Toiminta | Euler–Lagrange → aaltoyhtälö, tilavuustoiminta → minimipintayhtälö ja kovariantti kenttäyhtälö = määritelmästä laskettu $E_k$ |
| Säilymislait | $H$:n 18 isometriaa, $su(3)$ ja $D_\alpha j^\alpha=2K^k\mathrm{Eq}_k$ myös ei-ratkaisuilla. Virrat säilyvät vertailuratkaisuilla. |
| Holografia = holomorfia | Juuret $f_1=f_2=0$ lehdittäin, minimipintaominaisuus sekä Kähler-osa litteässä ja pallomaisessa rakenteessa, $M^4$:n Kähler-muodon vaikutus $(1-\varepsilon)^2$, Lorentz 4-voima, kertoimien etumerkit ja Hamilton–Jacobi-rakenteiden ehto |
| Karakteristiikat | $\partial_tU+A\,\partial_xU=0$ sekä nopeudet $M^4$:n, kosmisen säikeen ja ME:n ympärillä. Yhtälön tyyppi riippuu kertoimista. |
| Ekstremaalit | kosminen säie ja ME $s^k(u)$ kaikilla $c_K$, $c_V$. Yleinen $s^k(u,x)$ on Kähler-ekstremaali, mutta tilavuustermi ei häviä ([taulukko](docs/konventiot.md)) |
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
tgd/noether.mac             isometriat ja Noether-virrat
tgd/characteristics.mac     karakteristinen analyysi
tests/                      automaattiset testit
notebooks/                  Colab-kirjat + tgdlab.py (Maxima → LaTeX -silta)
docs/                       sivuston sisältö: tulokset, konventiot, suunnitelma, seuranta
```

## Dokumentaatio

Dokumentit on tarkoitettu luettaviksi [sivustolla](https://markomanninen.github.io/tgd-geometry-lab/), jossa kaavat piirtyvät oikein. GitHubin esikatselu näyttää osan kaavoista väärin.

- [Tulokset](docs/tulokset.md) kertoo, mitä on laskettu ja mitkä kysymykset ovat auki.
- [Kehityssuunnitelma](docs/kehityssuunnitelma.md) esittää vaiheet I–VIII ja välitavoitteet M1–M8, ja jokainen vaihe on linkitetty issueensa.
- [Konventiot](docs/konventiot.md) kokoaa etumerkit, normalisoinnit ja indeksijärjestykset.
- [Seuranta](docs/seuranta.md) sisältää tilataulukon, kriittisen polun ja työnkulun.

## Seuranta

| Välitavoite | Edistyminen |
|---|---|
| [M1 Ympäristö](https://github.com/markomanninen/tgd-geometry-lab/milestone/1) | 4/4 ✅ |
| [M2 CP2-metriikka](https://github.com/markomanninen/tgd-geometry-lab/milestone/2) | 6/6 ✅ |
| [M3 Muodot](https://github.com/markomanninen/tgd-geometry-lab/milestone/3) | 3/3 ✅ |
| [M4 Kaarevuus](https://github.com/markomanninen/tgd-geometry-lab/milestone/4) | 3/3 ✅ |
| [M5 Clifford-geometria](https://github.com/markomanninen/tgd-geometry-lab/milestone/5) | 4/4 ✅ |
| [M6 Upotus](https://github.com/markomanninen/tgd-geometry-lab/milestone/6) | 4/4 ✅ |
| [M7 Toiminta](https://github.com/markomanninen/tgd-geometry-lab/milestone/7) | 6/6 |
| [M8 Ratkaisut](https://github.com/markomanninen/tgd-geometry-lab/milestone/8) | 2/3 |

Ajantasainen tila on [milestone-sivulla](https://github.com/markomanninen/tgd-geometry-lab/milestones). Kriittinen polku #18 → #16/#19 → #23 → #27 → #28 on valmis, ja Matti Pitkäsen linjaukset on kirjattu konventioihin. Avoimet jatkokysymykset Kähler-osasta ja $u$:n roolista ovat issuessa #35.

Järjestelmä ei todista TGD:tä fysikaalisesti oikeaksi. Sen tarkoitus on tarkistaa johdoksia ja tutkia erikoistapauksia luotettavasti.

## Lisenssi

Lisenssi on MIT. Maxima (GPL) ja Prodanovin `clifford` (LGPL-2.1) ladataan erikseen, eikä niitä jaeta tämän repositorion mukana.
