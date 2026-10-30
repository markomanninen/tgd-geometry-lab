# TGD Geometry Lab – kehitys- ja toteutussuunnitelma Maximan päälle

**Versio:** 1.1 (30.10.2026)
**Tavoite:** rakentaa avoimeen Maxima-ympäristöön perustuva symbolisen geometrian laskentajärjestelmä, jolla voidaan tutkia Topological Geometrodynamics (TGD) -teorian geometrisia rakenteita vaiheittain aina $CP_2$-avaruuden kaarevuuteen, differentiaalimuotoihin, yhteyksiin ja aika-avaruuspinnan kenttäyhtälöihin asti.

> Toteutuksen tila on merkitty jokaiseen vaiheeseen: ✅ toteutettu ja testattu · 🟡 osittain · ⬜ ei vielä.
> Testit: `./scripts/run_tests.sh` – nykyisin **53/53 läpi**.
> **Seuranta GitHubissa:** jokainen vaihe on issue, ja välitavoitteet M1–M8 ovat [milestoneja](https://github.com/markomanninen/tgd-geometry-lab/milestones). Ks. [docs/seuranta.md](seuranta.md).

---

## 0. Lähtökohdat

Suunnitelmassa erotetaan kolme asiaa:

| Taso | Sisältö |
|---|---|
| **Laskentainfrastruktuuri** | Maxima, Clifford-algebra ja tarvittavat uudet laskentamoduulit |
| **Matemaattinen malli** | TGD:n upotusgeometria ja sen geometriset rakenteet |
| **Fysikaalinen teoria** | TGD:n omista lähtöoletuksista johdetut yhtälöt ja niiden tutkiminen |

**Suunnitteluperiaate:** emme yritä toteuttaa koko TGD:tä kerralla. Jokaisen vaiheen pitää tuottaa itsenäisesti testattava matemaattinen tulos, jonka oikeellisuus tarkistetaan tunnetuilla identiteeteillä tai vertailulaskuilla.

Tämä periaate on samassa hengessä kuin Lanyon AI:n lähestymistapa. Lanyonin tavoitteena on <em>verifioitu</em> tieteellinen laskenta: kielimalli ehdottaa spesifikaation, ja deterministinen järjestelmä tuottaa siitä sekä ajettavan koodin että todistuksen (Lean). Meillä vastaava rooli on automaattisilla identiteettitesteillä: symbolinen tulos hyväksytään vasta, kun se läpäisee riippumattomat tarkistukset.

### Tekninen toteutustapa

$CP_2$ toteutetaan ensin itsenäisenä neljän reaalisen ulottuvuuden Kähler-monistona. Sen jälkeen se liitetään $M^4$:ään tuloksi $H=M^4\times CP_2$. Näin geometriaa voidaan testata ilman, että TGD:n koko dynamiikka on mukana.

$CP_2$:n paikallinen koordinaattiesitys aloitetaan yhdestä kompleksisesta koordinaattikartasta $(z^1,z^2)$. Fubini–Study-metriikka saadaan Kähler-potentiaalista

$$
K=\log\left(1+|z^1|^2+|z^2|^2\right),\qquad g_{i\bar j}=\partial_i\partial_{\bar j}K .
$$

Metriikka, käänteismetriikka, Kähler-muoto, Christoffelin symbolit ja kaarevuus voidaan johtaa toisistaan ja tarkistaa tunnettuja identiteettejä vasten. Sen jälkeen lisätään differentiaalimuodot, yhteydet ja kaarevuuden Cartan-muotoilu. Vasta tämän jälkeen tuodaan mukaan aika-avaruuspinnan upotus ja Kähler-toiminnan variaatio.

---

## 1. Projektin tavoite ja rajaus

Laskentaympäristön avulla voidaan:

1. mallintaa TGD:n upotusavaruutta $H=M^4\times CP_2$,
2. laskea $CP_2$:n kaarevan geometrian ominaisuuksia,
3. käsitellä differentiaalimuotoja ja niiden välisiä operaatioita,
4. laskea yhteydet, kaarevuustensorit ja niihin liittyvät geometriset suureet,
5. rakentaa Clifford-algebran laskenta kaarevalle monistolle,
6. kuvata aika-avaruuspintojen upotuksia ja niistä indusoituvaa geometriaa,
7. muodostaa TGD:n toimintaperiaatteista johdettavia kenttäyhtälöitä,
8. tutkia yhtälöiden ratkaisuja, symmetrioita ja karakteristisia ominaisuuksia.

Lähtökohdat:

- Maxima symbolisen laskennan moottorina,
- Dimiter Prodanovin [`clifford`](https://github.com/dprodanov/clifford)- ja `cliffordan`-paketit Clifford-algebran laskentaan,
- [LanyonScriptsin](https://github.com/lanyonai/LanyonScripts) yhtälömallien käsittelytapa (kvasilineaarinen muoto, karakteristinen matriisi, ominaisarvot),
- uudet, erityisesti TGD-geometriaan rakennetut laskentamoduulit.

**Tärkeä rajaus:** Lanyonin nykyinen koodi ei muodosta TGD-laskentajärjestelmää. Sen laskentatapaa hyödynnetään ja laajennetaan tarvittavilla geometrisilla rakenteilla.

---

## 2. Kokonaisarkkitehtuuri

| Kerros | Sisältö | Moduulit |
|---|---|---|
| 1. Algebra | Maxima, symbolit, matriisit, Clifford-algebra | `core/`, Prodanov `clifford` |
| 2. Monistogeometria | Koordinaatit, metriikat, koordinaattimuunnokset | `core/metric.mac` |
| 3. Differentiaaligeometria | Muodot, yhteydet, kaarevuus | `forms/`, `geometry/` |
| 4. Upotusgeometria | $M^4\times CP_2$, indusoitu metriikka | `spaces/`, `embedding/` |
| 5. TGD-dynamiikka | Kähler-toiminta, kenttäyhtälöt | `tgd/` |
| 6. Analyysi | Ratkaisut, ominaisarvot, numeriikka | `notebooks/`, Python |

Moduulit ovat erillisiä Maxima-tiedostoja, ja niiden tulee olla uudelleenkäytettäviä myös muiden geometria- ja fysiikkamallien yhteydessä.

---

## 3. Vaihe I – Perusinfrastruktuuri ja upotusgeometria

### Step 1.1 – Maxima-ympäristön vakiointi ✅

Seuranta: [#1](https://github.com/markomanninen/tgd-geometry-lab/issues/1), [#2](https://github.com/markomanninen/tgd-geometry-lab/issues/2), [#3](https://github.com/markomanninen/tgd-geometry-lab/issues/3)
- Maxima ja Clifford-paketit asennetaan ja ladataan (`tgd-lab.mac`, `tgd_load_clifford`).
- Yhteiset konventiot kirjataan: [`docs/konventiot.md`](konventiot.md).
- Testiympäristö Google Colabissa: `notebooks/01_ymparisto_ja_testit.ipynb`, ja GitHub Actions ajaa testit jokaisesta muutoksesta.

### Step 1.2 – Koordinaattien ja metriikan perusrakenne ✅

Seuranta: [#4](https://github.com/markomanninen/tgd-geometry-lab/issues/4)

```maxima
define_manifold(name, dimension, coordinates)$
define_metric(name, metric_matrix)$
metric_inverse(name)$
metric_determinant(name)$
```

Lisäksi: `metric_signature_at`, `metric_direct_sum`, `jacobian_matrix` ja `transform_02` (tensorin muunnos).

### Step 1.3 – Upotusavaruuden määrittely ✅

Seuranta: [#21](https://github.com/markomanninen/tgd-geometry-lab/issues/21)

$$
H=M^4\times CP_2,\qquad h_{kl}=m_{kl}\oplus\left(-s_{kl}\right),
$$

jossa $m=\mathrm{diag}(1,-1,-1,-1)$ ja $s_{kl}$ on positiividefiniitti Fubini–Study-metriikka. $H$:n signatuuri on siis $(1,7)$. Etumerkki on parametri `cp2_sign`.

### Step 1.4 – Indusoitu metriikka ✅

Seuranta: [#21](https://github.com/markomanninen/tgd-geometry-lab/issues/21)

Aika-avaruuspinnan upotus $h^k=h^k(\xi^0,\xi^1,\xi^2,\xi^3)$ ja indusoitu metriikka

$$
g_{\alpha\beta}=h_{kl}(h(\xi))\,\partial_\alpha h^k\,\partial_\beta h^l .
$$

Toteutettu: determinantti, käänteismatriisi, signatuuri, koordinaattimuunnokset ja testit.

**Vaiheen I tulos:** toimiva laskentapohja, jolla upotuksesta syntyvä metriikka voidaan muodostaa.

---

## 4. Vaihe II – Kaarevan $CP_2$-avaruuden geometria

$CP_2$ on kompleksisesti kaksiulotteinen eli reaalisesti neliulotteinen kompakti monisto, jonka standardimetriikka on Fubini–Study.

### Step 2.1 – Kompleksiset koordinaattikartat ✅

Seuranta: [#5](https://github.com/markomanninen/tgd-geometry-lab/issues/5)

Homogeeniset koordinaatit $[Z_0:Z_1:Z_2]$ ja paikallinen kartta $Z_0\neq0$:

$$
z^1=\frac{Z_1}{Z_0},\qquad z^2=\frac{Z_2}{Z_0},\qquad z^k=x_k+i\,y_k .
$$

### Step 2.2 – Fubini–Study-Kähler-potentiaali ✅

$$
K(z,\bar z)=R^2\log\left(1+|z^1|^2+|z^2|^2\right).
$$

### Step 2.3 – Fubini–Study-metriikka ✅

Seuranta: [#5](https://github.com/markomanninen/tgd-geometry-lab/issues/5), [#10](https://github.com/markomanninen/tgd-geometry-lab/issues/10)

$$
g_{i\bar j}=\frac{\partial^2 K}{\partial z^i\,\partial\bar z^j},\qquad ds^2=2\,g_{i\bar j}\,dz^i\,d\bar z^j .
$$

Lasketaan metriikkamatriisi, käänteismetriikka, determinantti $\det g=16/(1+\rho^2)^6$, tilavuusmuoto ja positiividefiniittisyys. Kaikki tulokset tarkistetaan symbolisesti.

### Step 2.4 – Koordinaattikarttojen väliset muunnokset 🟡

Seuranta: [#7](https://github.com/markomanninen/tgd-geometry-lab/issues/7), [#8](https://github.com/markomanninen/tgd-geometry-lab/issues/8)

$CP_2$ ei ole yksi globaali kompleksinen koordinaattialue. Kartat ovat $Z_0\neq0$, $Z_1\neq0$ ja $Z_2\neq0$.
Toteutettu ja testattu on siirtymä $Z_0\leftrightarrow Z_1$ ($z^1=1/w^1$, $z^2=w^2/w^1$) Jacobin matriiseineen: metriikka muuntuu oikein. Kartta $Z_2$ tehdään samalla mallilla.

### Step 2.5 – Kähler-rakenne ✅

Seuranta: [#6](https://github.com/markomanninen/tgd-geometry-lab/issues/6)

$$
\omega=i\,g_{i\bar j}\,dz^i\wedge d\bar z^j,\qquad d\omega=0 .
$$

Lisäksi tarkistetaan $J^2=-1$, $J^TgJ=g$, $\nabla J=0$ ja $\tfrac12\,\omega\wedge\omega=\mathrm{vol}_g$.

**Vaiheen II tulos:** itsenäisesti testattu $CP_2$-geometriamoduuli `spaces/cp2.mac`.

---

## 5. Vaihe III – Differentiaalimuodot

### Step 3.1 – Muotojen tietorakenne ✅

Seuranta: [#11](https://github.com/markomanninen/tgd-geometry-lab/issues/11)

$$
\alpha=\frac{1}{p!}\,\alpha_{\mu_1\ldots\mu_p}\,dx^{\mu_1}\wedge\cdots\wedge dx^{\mu_p}
$$

Muoto esitetään harvana listana `[[kerroin, [i1<i2<...<ip]], ...]`. Asteet 0–4 (ja yleisesti $p\le n$) ovat tuettuja.

### Step 3.2 – Ulkotulo ✅

$\alpha\wedge\beta$ lasketaan automaattisin merkkisäännöin; testinä $dx^\mu\wedge dx^\nu=-dx^\nu\wedge dx^\mu$ ja $dx^\mu\wedge dx^\mu=0$.

### Step 3.3 – Ulkoderivaatta ✅

$$
d:\Omega^p(M)\to\Omega^{p+1}(M),\qquad d^2=0 .
$$

Lisäksi testataan asteittainen Leibnizin sääntö.

### Step 3.4 – Sisätulo ja Hodge-tähti ✅

Seuranta: [#12](https://github.com/markomanninen/tgd-geometry-lab/issues/12)

$$
\star:\Omega^p(M)\to\Omega^{n-p}(M).
$$

Hodge-operaattori on yleinen metriikkapohjainen operaatio, joka toimii sekä positiividefiniitissä ($\star\star=+1$ 2-muodoille $\mathbb R^4$:ssä) että Lorentz-signatuurissa ($\star\star=-1$).

### Step 3.5 – Differentiaalimuotojen integraalit ⬜

Seuranta: [#13](https://github.com/markomanninen/tgd-geometry-lab/issues/13)

Integraalilausekkeiden symbolinen muodostaminen (ei vielä yleistä numeerista integrointia monistoilla).

**Vaiheen III tulos:** yleinen differentiaalimuotojen laskentakirjasto `forms/forms.mac`.

---

## 6. Vaihe IV – Yhteydet ja kovariantti derivaatta

### Step 4.1 – Christoffelin symbolit ✅

Seuranta: [#14](https://github.com/markomanninen/tgd-geometry-lab/issues/14)

$$
\Gamma^\rho{}_{\mu\nu}=\tfrac12\,g^{\rho\sigma}\left(\partial_\mu g_{\sigma\nu}+\partial_\nu g_{\sigma\mu}-\partial_\sigma g_{\mu\nu}\right),
\qquad \Gamma^\rho{}_{\mu\nu}=\Gamma^\rho{}_{\nu\mu}.
$$

### Step 4.2 – Kovariantti derivaatta ✅

$$
\nabla_\mu V^\nu=\partial_\mu V^\nu+\Gamma^\nu{}_{\mu\rho}V^\rho,\qquad \nabla_\rho g_{\mu\nu}=0 .
$$

Toteutettu vektoreille, $(0,2)$- ja $(1,1)$-tensoreille.

### Step 4.3 – Ortonormaalit kehykset ⬜

Seuranta: [#18](https://github.com/markomanninen/tgd-geometry-lab/issues/18)

$$
g_{\mu\nu}=e^a{}_\mu\,e^b{}_\nu\,\eta_{ab}.
$$

### Step 4.4 – Spin-yhteys ⬜

Seuranta: [#19](https://github.com/markomanninen/tgd-geometry-lab/issues/19)

Spin-yhteys johdetaan ortonormaalista kehyksestä (paikallisen Lorentz- tai ortogonaalikehyksen yhteysmuodot).

### Step 4.5 – Clifford-algebran liittäminen 🟡

Seuranta: [#17](https://github.com/markomanninen/tgd-geometry-lab/issues/17), [#20](https://github.com/markomanninen/tgd-geometry-lab/issues/20)

$$
\gamma^a\gamma^b+\gamma^b\gamma^a=2\eta^{ab},\qquad \gamma^\mu=e_a{}^\mu\,\gamma^a .
$$

Clifford-relaatiot on testattu Prodanovin paketilla signatuureille $(4,0)$ ja $(1,3)$. Vielbein-liitos odottaa vaiheita 4.3–4.4.
**Periaate:** kaarevalla monistolla Clifford-algebra määritellään paikallisissa ortonormaaleissa kehyksissä. Yhtä globaalia vakiomuotoista Clifford-kehystä ei oleteta.

---

## 7. Vaihe V – Kaarevuustensorit ja Cartanin formalismi

### Step 5.1 – Riemannin kaarevuustensori ✅

Seuranta: [#15](https://github.com/markomanninen/tgd-geometry-lab/issues/15)

$$
R^\rho{}_{\sigma\mu\nu}=\partial_\mu\Gamma^\rho{}_{\nu\sigma}-\partial_\nu\Gamma^\rho{}_{\mu\sigma}
+\Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma}-\Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma}.
$$

### Step 5.2 – Riccin tensori ja skalaarikaarevuus ✅

$$
R_{\mu\nu}=R^\rho{}_{\mu\rho\nu},\qquad R=g^{\mu\nu}R_{\mu\nu}.
$$

### Step 5.3 – Cartanin rakenneyhtälöt ⬜

Seuranta: [#16](https://github.com/markomanninen/tgd-geometry-lab/issues/16)

$$
\Omega^a{}_b=d\omega^a{}_b+\omega^a{}_c\wedge\omega^c{}_b,\qquad
T^a=de^a+\omega^a{}_b\wedge e^b,\qquad T^a=0\ \text{(Levi-Civita)}.
$$

### Step 5.4 – Bianchin identiteetit ✅

Testataan Riemannin tensorin algebralliset symmetriat, ensimmäinen Bianchin identiteetti ja kontrahoitu toinen Bianchin identiteetti $\nabla^\mu\!\left(R_{\mu\nu}-\tfrac12 g_{\mu\nu}R\right)=0$.

### Step 5.5 – $CP_2$:n geometriset testit ✅

Seuranta: [#9](https://github.com/markomanninen/tgd-geometry-lab/issues/9)

| Ominaisuus | Tulos ($R^2=1$) |
|---|---|
| Kähler–Einstein | $\mathrm{Ric}=3g$ |
| Skalaarikaarevuus | $R=12$ |
| Holomorfinen leikkauskaarevuus | vakio $2$ (yleisessä pisteessä) |
| Totaalisesti reaalinen taso | $K=1/2$ (minimi) |
| Karttasiirtymä | metriikka säilyy |

**Vaiheen V tulos:** $CP_2$:n metriikka, yhteydet ja kaarevuus johdetaan kokonaan symbolisesti.

---

## 8. Vaihe VI – $M^4\times CP_2$-upotusgeometria

### Step 6.1 – Tulomoniston metriikka ✅
### Step 6.2 – Upotuskoordinaatit ✅

$h^k=(m^0,\ldots,m^3,s^1,\ldots,s^4)$ ja $h^k=h^k(\xi^0,\ldots,\xi^3)$.

### Step 6.3 – Indusoitu metriikka ja Kähler-muoto ✅

Seuranta: [#21](https://github.com/markomanninen/tgd-geometry-lab/issues/21), [#22](https://github.com/markomanninen/tgd-geometry-lab/issues/22)

$$
g_{\alpha\beta}=h_{kl}\,\partial_\alpha h^k\,\partial_\beta h^l,\qquad
J_{\alpha\beta}=J_{kl}\,\partial_\alpha h^k\,\partial_\beta h^l .
$$

Testatut esimerkit:

| Upotus | Tulos |
|---|---|
| Kanoninen $M^4$ (vakio $CP_2$-piste) | $g=m$, $J=0$ (tyhjiöekstremaali) |
| Kosminen säie $X^2\times CP_1$ | $J_{\alpha\beta}J^{\alpha\beta}=2$ (vakio magneettinen kenttä) |
| Massaton ekstremaali, $s^k(u,x)$, $u=t-z$ | $J\neq0$, $g^{uu}=0$, $J_{\alpha\beta}J^{\alpha\beta}=0$, $J\wedge J=0$ |

### Step 6.4 – Normaalivektorit ja toinen perusmuoto ⬜

Seuranta: [#23](https://github.com/markomanninen/tgd-geometry-lab/issues/23)

Tangentti- ja normaalikehykset sekä $B^i{}_{\alpha\beta}$ ja ekstrinsiset kaarevuussuureet (tangenttivektorit ovat jo saatavilla: `tangent_vectors`).

### Step 6.5 – Gaussin, Codazzin ja Riccin yhtälöt ⬜

Seuranta: [#24](https://github.com/markomanninen/tgd-geometry-lab/issues/24)

Nämä ovat tärkeä tarkistus: aika-avaruuspinnan sisäinen geometria ei ole sama asia kuin ympäröivän $H$:n geometria.

---

## 9. Vaihe VII – TGD:n toimintaperiaatteet ja kenttäyhtälöt

TGD:n toiminta (twistorinosto) on Kähler-toiminnan ja tilavuustermin summa:

$$
S_{TGD}=S_K+S_V=\int\left(c_K\,J_{\alpha\beta}J^{\alpha\beta}+c_V\right)\sqrt{|g|}\;d^4\xi ,
$$

jossa $c_K\propto 1/\alpha_K$ ja $c_V$ on kosmologisen vakion analogi. Kertoimet pidetään symbolisina, koska kirjallisuudessa normalisointi ja etumerkki vaihtelevat. Lisäksi on topologinen instantonitermi $J\wedge J$, joka on kokonaisdivergenssi.

### Step 7.1 – Kähler-toiminnan muodostaminen ✅

Seuranta: [#25](https://github.com/markomanninen/tgd-geometry-lab/issues/25)
`kahler_invariant`, `kahler_density`, `volume_density`, `tgd_density`, `instanton_density`.

### Step 7.2 – Variaatiolaskenta 🟡

Seuranta: [#27](https://github.com/markomanninen/tgd-geometry-lab/issues/27), [#28](https://github.com/markomanninen/tgd-geometry-lab/issues/28)

Dynaamisia muuttujia ovat **upotuskoordinaatit** $h^k$. Variaatio $\delta S=0$ johdetaan niiden suhteen; metriikkaa ja Kähler-muotoa ei oleteta toisistaan riippumattomiksi variaatiomuuttujiksi.

### Step 7.3 – Euler–Lagrange-yhtälöt 🟡

Seuranta: [#26](https://github.com/markomanninen/tgd-geometry-lab/issues/26)

Yleinen symbolinen variaatiomoottori `euler_lagrange(L, kentät, muuttujat)` on toteutettu ensimmäisen kertaluvun derivaattoja sisältäville tiheyksille. Testit: aaltoyhtälö sekä minimipintayhtälö tilavuustoiminnasta. Seuraavaksi sovelletaan sitä suoraan $L_{TGD}(h,\partial h)$:hen.

### Step 7.4 – Säilymislait ja Noether-rakenteet ⬜

Seuranta: [#29](https://github.com/markomanninen/tgd-geometry-lab/issues/29)
Virran muodostaminen, divergenssi, säilymislain tarkistus ja symmetrioiden vaikutus toimintaan.

### Step 7.5 – PDE-järjestelmien muodostaminen ⬜

Seuranta: [#30](https://github.com/markomanninen/tgd-geometry-lab/issues/30)

Tässä hyödynnetään Lanyonin lähestymistapaa: yhtälöjärjestelmä, karakteristinen matriisi, ominaisarvot, ominaisvektorit ja karakteristiset rakenteet (vrt. LanyonScriptsin `calcev`). TGD:n kenttäyhtälöt ovat geometrisesti monimutkaisempia kuin Lanyonin virtausfysiikan esimerkit, esimerkiksi minimipintaehto $g^{\alpha\beta}D_\beta\partial_\alpha h^k=0$ yhdessä Kähler-termin kanssa.

---

## 10. Vaihe VIII – Ratkaisujen analyysi ja numeerinen jatkokehitys ⬜

Seuranta: [#31](https://github.com/markomanninen/tgd-geometry-lab/issues/31), [#32](https://github.com/markomanninen/tgd-geometry-lab/issues/32)

- **8.1 Symmetriset erikoistapaukset** – yksinkertaiset upotukset, joilla on selkeät symmetriat (pohja on jo olemassa: kosminen säie ja ME).
- **8.2 Analyyttiset ratkaisut** – tarkat symboliset ratkaisut erikoistapauksissa.
- **8.3 Karakteristinen analyysi** – ominaisarvot ja ominaisvektorit; milloin hyperbolinen PDE-analyysi on sovellettavissa.
- **8.4 Numeeriset menetelmät** – ratkaisuverkot, parametriskannaus, alku- ja reunaehdot, stabiilisuus.
- **8.5 Visualisointi** – Python (Maxima vastaa symbolisesta laskennasta, Python numeriikasta ja visualisoinnista).

---

## 11. Ohjelmiston rakenne (toteutettu)

```
tgd-geometry-lab/
├── tgd-lab.mac               lataaja
├── core/metric.mac           monistot, metriikat, muunnokset
├── geometry/curvature.mac    Christoffel, kovariantti derivaatta, Riemann, Ricci, Bianchi
├── forms/forms.mac           muodot, wedge, d, sisätulo, Hodge
├── spaces/cp2.mac            CP2 Fubini–Study, Kähler-rakenne, kartat
├── spaces/embedding-space.mac  M4, H = M4 x CP2
├── embedding/induced.mac     indusoitu metriikka ja Kähler-muoto
├── tgd/action.mac            toimintatiheydet, Euler–Lagrange
├── tests/                    53 automaattista testiä
├── notebooks/                Colab-kirjat + tgdlab.py-silta
└── docs/                     tämä suunnitelma ja konventiot
```

Alkuperäisen suunnitelman hienojakoisempi jako (`wedge.mac`, `hodge.mac`, `riemann.mac` …) on tässä vaiheessa yhdistetty muutamaksi moduuliksi. Jako tarkennetaan, kun moduulit kasvavat.

---

## 12. Testaus- ja validointiperiaatteet

| Kohde | Pakollinen testi | Tila |
|---|---|---|
| Metriikka | käänteismatriisin oikeellisuus | ✅ |
| Koordinaatistot | metriikan muunnossäännöt | ✅ |
| Kähler-geometria | $d\omega=0$, $\nabla J=0$ | ✅ |
| Differentiaalimuodot | $d^2=0$ | ✅ |
| Yhteys | metriikan yhteensopivuus | ✅ |
| Torsio | Levi-Civita: $T=0$ | ⬜ (Cartan) |
| Kaarevuus | Bianchin identiteetit | ✅ |
| Clifford-algebra | Clifford-relaatiot | ✅ |
| Upotusgeometria | Gauss–Codazzi | ⬜ |
| TGD-toiminta | variaatioyhtälöiden tarkistus | 🟡 |

Testit ajetaan myös yksinkertaisilla tunnetuilla geometrioilla (yksikköpallo $S^2$, $\mathbb R^4$, Minkowski), jotta mahdolliset virheet voidaan erottaa TGD:n omista matemaattisista oletuksista.

---

## 13. Toteutusjärjestys ja välitavoitteet

| | Sisältö | Valmis kun | Tila |
|---|---|---|---|
| [M1](https://github.com/markomanninen/tgd-geometry-lab/milestone/1) | Maxima- ja Clifford-ympäristö | peruslaskenta toimii | ✅ |
| [M2](https://github.com/markomanninen/tgd-geometry-lab/milestone/2) | $CP_2$-metriikka | Fubini–Study-tulokset täsmäävät | ✅ |
| [M3](https://github.com/markomanninen/tgd-geometry-lab/milestone/3) | Differentiaalimuodot | muoto-operaatiot ja $d^2=0$ toimivat | ✅ |
| [M4](https://github.com/markomanninen/tgd-geometry-lab/milestone/4) | Yhteydet ja kaarevuus | kaarevuus- ja Bianchi-testit läpäisty | ✅ (Cartan ⬜) |
| [M5](https://github.com/markomanninen/tgd-geometry-lab/milestone/5) | Clifford-geometria | paikalliset kehykset ja spin-yhteys | 🟡 |
| [M6](https://github.com/markomanninen/tgd-geometry-lab/milestone/6) | Upotusgeometria | indusoitu geometria ja Gauss–Codazzi | 🟡 |
| [M7](https://github.com/markomanninen/tgd-geometry-lab/milestone/7) | TGD:n toimintaperiaate | variaatioyhtälöt muodostuvat | 🟡 |
| [M8](https://github.com/markomanninen/tgd-geometry-lab/milestone/8) | Ratkaisuanalyysi | ensimmäiset testattavat ratkaisut | ⬜ |

**Toteutusjärjestys:** ensin M1–M4, sitten M5–M6 ja vasta sen jälkeen M7–M8. Näin TGD-fysiikan oletukset eivät sekoitu laskentakirjaston virheisiin.

---

## 14. Ensimmäinen konkreettinen kehitystehtävä: `cp2.mac` ✅

1. ✅ $CP_2$:n paikallinen kompleksinen koordinaattikartta
2. ✅ Fubini–Study-Kähler-potentiaali
3. ✅ metriikka ja käänteismetriikka
4. ✅ Kähler-muoto
5. ✅ $d\omega=0$
6. ✅ Christoffelin symbolit
7. ✅ Riemannin ja Riccin tensorit
8. ✅ Kähler–Einstein-ominaisuus ($\mathrm{Ric}=3g$, kun $R^2=1$)

Koska tehtävä on valmis, seuraavat askeleet ovat:

1. **Cartan-moduuli** (vielbein → spin-yhteys → kaarevuus-2-muodot, $T^a=0$), joka avaa M5:n.
2. **Toinen perusmuoto ja Gauss–Codazzi** M6:een.
3. **$L_{TGD}$:n variointi upotuskoordinaattien suhteen** ja tulosten vertailu tunnettuihin ekstremaaleihin (kosminen säie, ME, $CP_2$-tyyppiset tyhjiöekstremaalit) M7:ään.

---

## 15. Lopullinen tavoite

Tavoitteena ei ole pelkästään TGD:n yhtälöiden syöttäminen Maximalle, vaan järjestelmä, jossa voidaan tehdä seuraava laskentaketju:

$$
\text{Upotusavaruus}\to\text{Geometria}\to\text{Differentiaalimuodot}\to\text{Yhteydet}\to\text{Kaarevuus}\to\text{Toiminta}\to\text{Kenttäyhtälöt}\to\text{Ratkaisut}
$$

Ympäristö tarjoaa systemaattisen tavan tutkia TGD:n matemaattista rakennetta ja testata sen geometrisia seurauksia symbolisesti. Se ei itsessään todista TGD:n fysikaalista oikeellisuutta, mutta se voi auttaa löytämään matemaattisia seurauksia, tarkistamaan johdoksia ja tutkimaan erikoistapauksia, joiden käsin laskeminen olisi työlästä.

---

## Lähteet ja taustamateriaali

- M. T. Manninen, *Through the Wormhole on Spacetime Surface – Early History of Topological Geometrodynamics Theory* (2024). Erityisesti luvut TGD:n toiminnasta ($S_K+S_V$, indusoitu $g_{\alpha\beta}$ ja $J_{\alpha\beta}$, variaatio upotuskoordinaattien $h^k$ suhteen), kenttäyhtälöistä (minimipinnat) ja twistorinostosta.
- M. Pitkänen, *Topological Geometrodynamics* ja tgdtheory.fi.
- LanyonScripts: <https://github.com/lanyonai/LanyonScripts> (MIT) ja Lanyonin Colab-esimerkki *Run LanyonScripts in Colab*.
- D. Prodanov, Clifford-algebrapaketti Maximalle: <https://github.com/dprodanov/clifford> (LGPL-2.1).
- Fubini–Study-metriikan eksplisiittiset paikalliset lausekkeet ja kaarevuus: tavanomaiset differentiaaligeometrian oppikirjat (esim. Kobayashi–Nomizu II, luku IX).
