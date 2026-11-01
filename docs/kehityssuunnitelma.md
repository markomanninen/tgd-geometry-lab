# TGD Geometry Lab – kehitys- ja toteutussuunnitelma Maximan päälle

Versio 1.1, 30.10.2026.
Tavoitteena on rakentaa avoimeen Maxima-ympäristöön perustuva symbolisen geometrian laskentajärjestelmä, jolla voidaan tutkia Topological Geometrodynamics (TGD) -teorian geometrisia rakenteita vaiheittain aina $CP_2$-avaruuden kaarevuuteen, differentiaalimuotoihin, yhteyksiin ja aika-avaruuspinnan kenttäyhtälöihin asti.

> Toteutuksen tila on merkitty jokaiseen vaiheeseen. ✅ tarkoittaa toteutettua ja testattua, 🟡 osittain tehtyä ja ⬜ tekemätöntä.
> Testit ajetaan komennolla `./scripts/run_tests.sh`, ja nykyisin kaikki 376 testiä menevät läpi.
> GitHubissa jokainen vaihe on issue, ja välitavoitteet M1–M8 ovat [milestoneja](https://github.com/markomanninen/tgd-geometry-lab/milestones). Tilanne on koottu [seurantaan](seuranta.md).

---

## 0. Lähtökohdat

Suunnitelmassa erotetaan kolme tasoa, jotka näkyvät taulukossa.

| Taso | Sisältö |
|---|---|
| **Laskentainfrastruktuuri** | Maxima, Clifford-algebra ja tarvittavat uudet laskentamoduulit |
| **Matemaattinen malli** | TGD:n upotusgeometria ja sen geometriset rakenteet |
| **Fysikaalinen teoria** | TGD:n omista lähtöoletuksista johdetut yhtälöt ja niiden tutkiminen |

Suunnitteluperiaate on, että emme yritä toteuttaa koko TGD:tä kerralla. Jokaisen vaiheen pitää tuottaa itsenäisesti testattava matemaattinen tulos, jonka oikeellisuus tarkistetaan tunnetuilla identiteeteillä tai vertailulaskuilla.

Periaate on samassa hengessä kuin [Lanyon AI](https://lanyon.ai/):n lähestymistapa. Lanyon on Jonathan Gorardin, Ammar Hakimin ja Jimmy Junon perustama tutkimusyhtiö, ja Gorard on sen toimitusjohtaja. Sen tavoitteena on muodollisesti verifioitu tieteellinen laskenta. Kielimalli ehdottaa spesifikaation omalla formaalilla kielellä, ja symboliset algoritmit laajentavat siitä samalla koodin ja todistuksen. Jos spesifikaatiota ei voida todistaa oikeaksi, koodia ei synny ([Announcing Lanyon AI](https://lanyon.ai/blog/welcome/), 2026). Meillä vastaavaa roolia hoitavat automaattiset identiteettitestit, jotka eivät ole muodollisia todistuksia. Symbolinen tulos hyväksytään vasta, kun se läpäisee riippumattomat tarkistukset.

Lanyonin [esittelyvideo](https://youtu.be/gSH50n-9ZLk) jakaa fysiikan verifioinnin kolmeen kysymykseen. Matemaattinen kysymys on, onko malli sisäisesti ristiriidaton. Teoreettinen kysymys on, sopiiko malli yhteen muun tiedetyn kanssa, sillä malli voi esimerkiksi säilyttää energian vain joillakin alueilla. Kokeellinen kysymys on, vastaako malli havaintoja.

Sama jako näyttää tämän projektin rajat. Testit tarkistavat ensimmäistä kysymystä johdosten tasolla ja osaa toisesta, kun tuloksia verrataan Pitkäsen julkaisemiin arvoihin ja Noether-virtojen säilymiseen. Kolmatta kysymystä projekti ei käsittele, koska se ei vertaa laskuja mittaustuloksiin.

### Tekninen toteutustapa

$CP_2$ toteutetaan ensin itsenäisenä neljän reaalisen ulottuvuuden Kähler-monistona. Sen jälkeen se liitetään $M^4$:ään tuloksi $H=M^4\times CP_2$. Näin geometriaa voidaan testata ilman, että TGD:n koko dynamiikka on mukana.

$CP_2$:n paikallinen koordinaattiesitys aloitetaan yhdestä kompleksisesta koordinaattikartasta $(z^1,z^2)$. Fubini–Study-metriikka saadaan Kähler-potentiaalista

$$
K=\log\left(1+|z^1|^2+|z^2|^2\right),\qquad g_{i\bar j}=\partial_i\partial_{\bar j}K .
$$

Metriikka, käänteismetriikka, Kähler-muoto, Christoffelin symbolit ja kaarevuus voidaan johtaa toisistaan ja tarkistaa tunnettuja identiteettejä vasten. Sen jälkeen lisätään differentiaalimuodot, yhteydet ja kaarevuuden Cartan-muotoilu. Vasta tämän jälkeen tuodaan mukaan aika-avaruuspinnan upotus ja Kähler-vaikutuksen variaatio.

---

## 1. Projektin tavoite ja rajaus

Laskentaympäristön avulla voidaan:

1. mallintaa TGD:n upotusavaruutta $H=M^4\times CP_2$,
2. laskea $CP_2$:n kaarevan geometrian ominaisuuksia,
3. käsitellä differentiaalimuotoja ja niiden välisiä operaatioita,
4. laskea yhteydet, kaarevuustensorit ja niihin liittyvät geometriset suureet,
5. rakentaa Clifford-algebran laskenta kaarevalle monistolle,
6. kuvata aika-avaruuspintojen upotuksia ja niistä indusoituvaa geometriaa,
7. muodostaa TGD:n vaikutusintegraalista johdettavia kenttäyhtälöitä,
8. tutkia yhtälöiden ratkaisuja, symmetrioita ja karakteristisia ominaisuuksia.

Lähtökohdat:

- Maxima symbolisen laskennan moottorina,
- Dimiter Prodanovin [`clifford`](https://github.com/dprodanov/clifford)- ja `cliffordan`-paketit Clifford-algebran laskentaan,
- [LanyonScriptsin](https://github.com/lanyonai/LanyonScripts) yhtälömallien käsittelytapa (kvasilineaarinen muoto, karakteristinen matriisi, ominaisarvot),
- uudet, erityisesti TGD-geometriaan rakennetut laskentamoduulit.

Tärkeä rajaus on, että Lanyonin nykyinen koodi ei muodosta TGD-laskentajärjestelmää. Sen laskentatapaa hyödynnetään ja laajennetaan tarvittavilla geometrisilla rakenteilla.

---

## 2. Kokonaisarkkitehtuuri

| Kerros | Sisältö | Moduulit |
|---|---|---|
| 1. Algebra | Maxima, symbolit, matriisit, Clifford-algebra | `core/`, Prodanov `clifford` |
| 2. Monistogeometria | Koordinaatit, metriikat, koordinaattimuunnokset | `core/metric.mac` |
| 3. Differentiaaligeometria | Muodot, yhteydet, kaarevuus | `forms/`, `geometry/` |
| 4. Upotusgeometria | $M^4\times CP_2$, indusoitu metriikka | `spaces/`, `embedding/` |
| 5. TGD-dynamiikka | Kähler-vaikutus, kenttäyhtälöt | `tgd/` |
| 6. Analyysi | Ratkaisut, ominaisarvot, numeriikka | `notebooks/`, Python |

Moduulit ovat erillisiä Maxima-tiedostoja, ja niiden tulee olla uudelleenkäytettäviä myös muiden geometria- ja fysiikkamallien yhteydessä.

---

## 3. Vaihe I – Perusinfrastruktuuri ja upotusgeometria

### Step 1.1 – Maxima-ympäristön vakiointi ✅

Issuet [#1](https://github.com/markomanninen/tgd-geometry-lab/issues/1), [#2](https://github.com/markomanninen/tgd-geometry-lab/issues/2) ja [#3](https://github.com/markomanninen/tgd-geometry-lab/issues/3).
- Maxima ja Clifford-paketit asennetaan ja ladataan (`tgd-lab.mac`, `tgd_load_clifford`).
- Yhteiset konventiot kirjataan [konventioihin](konventiot.md).
- Testiympäristö on Google Colabissa kirjassa `notebooks/01_ymparisto_ja_testit.ipynb`, ja GitHub Actions ajaa testit jokaisesta muutoksesta.

### Step 1.2 – Koordinaattien ja metriikan perusrakenne ✅

Issue [#4](https://github.com/markomanninen/tgd-geometry-lab/issues/4).
```maxima
define_manifold(name, dimension, coordinates)$
define_metric(name, metric_matrix)$
metric_inverse(name)$
metric_determinant(name)$
```

Lisäksi käytössä ovat `metric_signature_at`, `metric_direct_sum`, `jacobian_matrix` ja `transform_02`, joka muuntaa tensorin.

### Step 1.3 – Upotusavaruuden määrittely ✅

Issue [#21](https://github.com/markomanninen/tgd-geometry-lab/issues/21).
$$
H=M^4\times CP_2,\qquad h_{kl}=m_{kl}\oplus\left(-s_{kl}\right),
$$

jossa $m=\mathrm{diag}(1,-1,-1,-1)$ ja $s_{kl}$ on positiividefiniitti Fubini–Study-metriikka. $H$:n signatuuri on siis $(1,7)$. Etumerkki on parametri `cp2_sign`.

### Step 1.4 – Indusoitu metriikka ✅

Issue [#21](https://github.com/markomanninen/tgd-geometry-lab/issues/21).
Aika-avaruuspinnan upotus $h^k=h^k(\xi^0,\xi^1,\xi^2,\xi^3)$ ja indusoitu metriikka

$$
g_{\alpha\beta}=h_{kl}(h(\xi))\,\partial_\alpha h^k\,\partial_\beta h^l .
$$

Toteutettuna ovat determinantti, käänteismatriisi, signatuuri, koordinaattimuunnokset ja testit.

Vaiheen I tuloksena on toimiva laskentapohja, jolla upotuksesta syntyvä metriikka voidaan muodostaa.

---

## 4. Vaihe II – Kaarevan $CP_2$-avaruuden geometria

$CP_2$ on kompleksisesti kaksiulotteinen eli reaalisesti neliulotteinen kompakti monisto, jonka standardimetriikka on Fubini–Study.

### Step 2.1 – Kompleksiset koordinaattikartat ✅

Issue [#5](https://github.com/markomanninen/tgd-geometry-lab/issues/5).
Homogeeniset koordinaatit ovat $[Z_0:Z_1:Z_2]$, ja paikallisessa kartassa $Z_0\neq0$ pätee

$$
z^1=\frac{Z_1}{Z_0},\qquad z^2=\frac{Z_2}{Z_0},\qquad z^k=x_k+i\,y_k .
$$

### Step 2.2 – Fubini–Study-Kähler-potentiaali ✅

$$
K(z,\bar z)=R^2\log\left(1+|z^1|^2+|z^2|^2\right).
$$

### Step 2.3 – Fubini–Study-metriikka ✅

Issuet [#5](https://github.com/markomanninen/tgd-geometry-lab/issues/5) ja [#10](https://github.com/markomanninen/tgd-geometry-lab/issues/10).
$$
g_{i\bar j}=\frac{\partial^2 K}{\partial z^i\,\partial\bar z^j},\qquad ds^2=g_{i\bar j}\,dz^i\,d\bar z^j\quad\text{(TGD-normalisointi)} .
$$

Lasketaan metriikkamatriisi, käänteismetriikka, determinantti $\det g=1/(1+\rho^2)^6$, tilavuusmuoto ja positiividefiniittisyys. Kaikki tulokset tarkistetaan symbolisesti.

### Step 2.4 – Koordinaattikarttojen väliset muunnokset ✅

Issuet [#7](https://github.com/markomanninen/tgd-geometry-lab/issues/7) ja [#8](https://github.com/markomanninen/tgd-geometry-lab/issues/8).
$CP_2$ ei ole yksi globaali kompleksinen koordinaattialue. Kartat ovat $Z_0\neq0$, $Z_1\neq0$ ja $Z_2\neq0$.
Kaikki siirtymät tulevat homogeenisista koordinaateista (`cp2_chart_map`). Testien mukaan metriikka ja Kähler-muoto säilyvät kaikissa kuudessa suunnatussa karttaparissa, kokosykliehto pätee kolmen kartan leikkauksessa, ja $\mathrm{Ric}=6g$, $R=24$ saadaan myös muunnetusta metriikasta.

### Step 2.5 – Kähler-rakenne ✅

Issue [#6](https://github.com/markomanninen/tgd-geometry-lab/issues/6).
$$
J=\tfrac{i}{2}\,g_{i\bar j}\,dz^i\wedge d\bar z^j,\qquad dJ=0,\qquad J_{kl}J^{kl}=4 .
$$

Lisäksi tarkistetaan $J^2=-1$, $J^TgJ=g$, $\nabla J=0$ ja $\tfrac12\,\omega\wedge\omega=\mathrm{vol}_g$.

Vaiheen II tuloksena on itsenäisesti testattu $CP_2$-geometriamoduuli `spaces/cp2.mac`.

---

## 5. Vaihe III – Differentiaalimuodot

### Step 3.1 – Muotojen tietorakenne ✅

Issue [#11](https://github.com/markomanninen/tgd-geometry-lab/issues/11).
$$
\alpha=\frac{1}{p!}\,\alpha_{\mu_1\ldots\mu_p}\,dx^{\mu_1}\wedge\cdots\wedge dx^{\mu_p}
$$

Muoto esitetään harvana listana `[[kerroin, [i1<i2<...<ip]], ...]`. Asteet 0–4 (ja yleisesti $p\le n$) ovat tuettuja.

### Step 3.2 – Ulkotulo ✅

$\alpha\wedge\beta$ lasketaan automaattisin merkkisäännöin, ja testeinä ovat $dx^\mu\wedge dx^\nu=-dx^\nu\wedge dx^\mu$ ja $dx^\mu\wedge dx^\mu=0$.

### Step 3.3 – Ulkoderivaatta ✅

$$
d:\Omega^p(M)\to\Omega^{p+1}(M),\qquad d^2=0 .
$$

Lisäksi testataan asteittainen Leibnizin sääntö.

### Step 3.4 – Sisätulo ja Hodge-tähti ✅

Issue [#12](https://github.com/markomanninen/tgd-geometry-lab/issues/12).
$$
\star:\Omega^p(M)\to\Omega^{n-p}(M).
$$

Hodge-operaattori on yleinen metriikkapohjainen operaatio, joka toimii sekä positiividefiniitissä ($\star\star=+1$ 2-muodoille $\mathbb R^4$:ssä) että Lorentz-signatuurissa ($\star\star=-1$).

### Step 3.5 – Differentiaalimuotojen integraalit ✅

Issue [#13](https://github.com/markomanninen/tgd-geometry-lab/issues/13).
`form_pullback` ja `form_integral` muodostavat ja laskevat integraalin parametrisoidulla pinnalla. Testeissä tarkistetaan Stokesin lause neliöllä, paraboloidilla ja $CP_1$:n kiekolla sekä Kähler-vuo $\pi$ yli $CP_1$:n ja $2\pi$ yli kartion $z^2=(z^1)^2$ (aste 2).

Vaiheen III tuloksena on yleinen differentiaalimuotojen laskentakirjasto `forms/forms.mac`.

---

## 6. Vaihe IV – Yhteydet ja kovariantti derivaatta

### Step 4.1 – Christoffelin symbolit ✅

Issue [#14](https://github.com/markomanninen/tgd-geometry-lab/issues/14).
$$
\Gamma^\rho{}_{\mu\nu}=\tfrac12\,g^{\rho\sigma}\left(\partial_\mu g_{\sigma\nu}+\partial_\nu g_{\sigma\mu}-\partial_\sigma g_{\mu\nu}\right),
\qquad \Gamma^\rho{}_{\mu\nu}=\Gamma^\rho{}_{\nu\mu}.
$$

### Step 4.2 – Kovariantti derivaatta ✅

$$
\nabla_\mu V^\nu=\partial_\mu V^\nu+\Gamma^\nu{}_{\mu\rho}V^\rho,\qquad \nabla_\rho g_{\mu\nu}=0 .
$$

Toteutettu vektoreille, $(0,2)$- ja $(1,1)$-tensoreille.

### Step 4.3 – Ortonormaalit kehykset ✅

Issue [#18](https://github.com/markomanninen/tgd-geometry-lab/issues/18).
$$
g_{\mu\nu}=e^a{}_\mu\,e^b{}_\nu\,\eta_{ab}.
$$

### Step 4.4 – Spin-yhteys ✅

Issue [#19](https://github.com/markomanninen/tgd-geometry-lab/issues/19).
Spin-yhteys lasketaan kahdella reitillä, jotka tarkistavat toisensa, eli kehyksestä ja Christoffeleista (`spin_connection`) sekä pelkästä anholonomiasta (`connection_forms`). $CP_2$:n unitaarisessa kehyksessä holonomia on $U(2)$:ssa. Kähler-kytkennällä $dA=J$ kerroin $k=3$ antaa kovariantisti vakion spinorin $\nu_R$, ja $S^+$:n vuo yli $CP_1$:n on kokonaisluku täsmälleen parittomilla $k$.

### Step 4.5 – Clifford-algebran liittäminen ✅

Issuet [#17](https://github.com/markomanninen/tgd-geometry-lab/issues/17) ja [#20](https://github.com/markomanninen/tgd-geometry-lab/issues/20).
$$
\gamma^a\gamma^b+\gamma^b\gamma^a=2\eta^{ab},\qquad \gamma^\mu=e_a{}^\mu\,\gamma^a .
$$

Clifford-relaatiot on testattu Prodanovin paketilla signatuureille $(4,0)$ ja $(1,3)$ sekä kaarevalla $CP_2$:lla. Eksplisiittisillä matriiseilla on testattu lisäksi $D_\mu\gamma^\nu=0$, Lichnerowicz-termi $\tfrac12\gamma^\mu\gamma^\nu F_{\mu\nu}=-R/4$ ja Diracin operaattori ($S^2$:n ominaisarvo $i$).
Periaatteena on, että kaarevalla monistolla Clifford-algebra määritellään paikallisissa ortonormaaleissa kehyksissä. Yhtä globaalia vakiomuotoista Clifford-kehystä ei oleteta.

---

## 7. Vaihe V – Kaarevuustensorit ja Cartanin formalismi

### Step 5.1 – Riemannin kaarevuustensori ✅

Issue [#15](https://github.com/markomanninen/tgd-geometry-lab/issues/15).
$$
R^\rho{}_{\sigma\mu\nu}=\partial_\mu\Gamma^\rho{}_{\nu\sigma}-\partial_\nu\Gamma^\rho{}_{\mu\sigma}
+\Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma}-\Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma}.
$$

### Step 5.2 – Riccin tensori ja skalaarikaarevuus ✅

$$
R_{\mu\nu}=R^\rho{}_{\mu\rho\nu},\qquad R=g^{\mu\nu}R_{\mu\nu}.
$$

### Step 5.3 – Cartanin rakenneyhtälöt ✅

Issue [#16](https://github.com/markomanninen/tgd-geometry-lab/issues/16).
$$
\Omega^a{}_b=d\omega^a{}_b+\omega^a{}_c\wedge\omega^c{}_b,\qquad
T^a=de^a+\omega^a{}_b\wedge e^b,\qquad T^a=0\ \text{(Levi-Civita)}.
$$

### Step 5.4 – Bianchin identiteetit ✅

Testataan Riemannin tensorin algebralliset symmetriat, ensimmäinen Bianchin identiteetti ja kontrahoitu toinen Bianchin identiteetti $\nabla^\mu\!\left(R_{\mu\nu}-\tfrac12 g_{\mu\nu}R\right)=0$.

### Step 5.5 – $CP_2$:n geometriset testit ✅

Issue [#9](https://github.com/markomanninen/tgd-geometry-lab/issues/9).
| Ominaisuus | Tulos ($R^2=1$) |
|---|---|
| Kähler–Einstein | $\mathrm{Ric}=6g$ ($=6g/R^2$ yleisesti) |
| Skalaarikaarevuus | $R=24$ |
| Holomorfinen leikkauskaarevuus | vakio $4$ (yleisessä pisteessä) |
| Totaalisesti reaalinen taso | $K=1$ (minimi) |
| Tilavuus | $\pi^2/2$ |
| CP₂-tyyppisen ekstremaalin vaikutus | $S_K=\pi/(8\alpha_K)$ (Pitkäsen arvo) |
| Karttasiirtymä | metriikka säilyy |

Vaiheen V tuloksena $CP_2$:n metriikka, yhteydet ja kaarevuus johdetaan kokonaan symbolisesti.

---

## 8. Vaihe VI – $M^4\times CP_2$-upotusgeometria

### Step 6.1 – Tulomoniston metriikka ✅
### Step 6.2 – Upotuskoordinaatit ✅

$h^k=(m^0,\ldots,m^3,s^1,\ldots,s^4)$ ja $h^k=h^k(\xi^0,\ldots,\xi^3)$.

### Step 6.3 – Indusoitu metriikka ja Kähler-muoto ✅

Issuet [#21](https://github.com/markomanninen/tgd-geometry-lab/issues/21) ja [#22](https://github.com/markomanninen/tgd-geometry-lab/issues/22).
$$
g_{\alpha\beta}=h_{kl}\,\partial_\alpha h^k\,\partial_\beta h^l,\qquad
J_{\alpha\beta}=J_{kl}\,\partial_\alpha h^k\,\partial_\beta h^l .
$$

Taulukossa ovat testatut esimerkit.

| Upotus | Tulos |
|---|---|
| Kanoninen $M^4$ (vakio $CP_2$-piste) | $g=m$, $J=0$ (tyhjiöekstremaali) |
| Kosminen säie $X^2\times CP_1$ | $J_{\alpha\beta}J^{\alpha\beta}=2$ (vakio magneettinen kenttä) |
| Massaton ekstremaali, $s^k(u,x)$, $u=t-z$ | $J\neq0$, $g^{uu}=0$, $J_{\alpha\beta}J^{\alpha\beta}=0$, $J\wedge J=0$ |

### Step 6.4 – Normaalivektorit ja toinen perusmuoto ✅

Issue [#23](https://github.com/markomanninen/tgd-geometry-lab/issues/23).
Toteutettuna ovat `second_fundamental_form`, `mean_curvature`, `normal_projector` ja `normal_frame`. Testeissä ovat mukana pallo ja sylinteri $R^3$:ssa, sylinteri käyräviivaisessa ympäristössä, hyperboloidi $R^{1,2}$:ssa, helikoidi, $CP_1$ ja kartio $z^2=(z^1)^2$ $CP_2$:ssa sekä upotukset $H$:ssa.

### Step 6.5 – Gaussin, Codazzin ja Riccin yhtälöt ✅

Issue [#24](https://github.com/markomanninen/tgd-geometry-lab/issues/24).
Nämä ovat tärkeä tarkistus, koska aika-avaruuspinnan sisäinen geometria ei ole sama asia kuin ympäröivän $H$:n geometria.

---

## 9. Vaihe VII – TGD:n vaikutusintegraali ja kenttäyhtälöt

TGD:n vaikutus (twistorinosto) on Kähler-vaikutuksen ja tilavuustermin summa

$$
S_{TGD}=S_K+S_V=\int\left(c_K\,J_{\alpha\beta}J^{\alpha\beta}+c_V\right)\sqrt{|g|}\;d^4\xi ,
$$

jossa Pitkäsen määritelmän mukaan $c_K=1/(4g_K^2)$, $\alpha_K=g_K^2/4\pi$ (testattu arvolla $S_K(CP_2)=\pi/(8\alpha_K)$), ja $c_V$ on kosmologisen vakion analogi. $c_V$:n etumerkki ja normalisointi suhteessa Kähler-termiin on avoin kysymys Matille (#27). Lisäksi on topologinen instantonitermi $J\wedge J$, joka on kokonaisdivergenssi.

### Step 7.1 – Kähler-vaikutuksen muodostaminen ✅

Issue [#25](https://github.com/markomanninen/tgd-geometry-lab/issues/25).
`kahler_invariant`, `kahler_density`, `volume_density`, `tgd_density`, `instanton_density`.

### Step 7.2 – Variaatiolaskenta ✅

Issuet [#27](https://github.com/markomanninen/tgd-geometry-lab/issues/27) ja [#28](https://github.com/markomanninen/tgd-geometry-lab/issues/28).
Dynaamisia muuttujia ovat **upotuskoordinaatit** $h^k$. Variaatio $\delta S=0$ johdetaan niiden suhteen. Metriikkaa ja Kähler-muotoa ei oleteta toisistaan riippumattomiksi variaatiomuuttujiksi.

Yhtälöt on muodostettu symbolisilla kertoimilla $c_K$, $c_V$ ja tarkistettu kovarianttia muotoa vasten (ks. [konventiot](konventiot.md)). Kosminen säie ja ME $s^k(u)$ ovat ekstremaaleja kaikilla kertoimilla. Yleinen $s^k(u,x)$ on Kähler-ekstremaali, mutta tilavuustermi ei häviä. Matin linjaukset 31.10.2026 on kirjattu [konventioihin](konventiot.md), ja niiden mukaan vaikutukselle $S_K+S_V$ ansatsin korvaa holografia = holomorfia.

### Step 7.3 – Euler–Lagrange-yhtälöt ✅

Issue [#26](https://github.com/markomanninen/tgd-geometry-lab/issues/26).
Yleinen symbolinen variaatiomoottori `euler_lagrange(L, kentät, muuttujat)` on toteutettu ensimmäisen kertaluvun derivaattoja sisältäville tiheyksille. Testeissä se antaa aaltoyhtälön ja tilavuusvaikutuksesta minimipintayhtälön. Kovariantti muoto on `tgd_field_equations`, ja sitä verrataan suoraan määritelmästä laskettuun arvoon.

### Step 7.4 – Säilymislait ja Noether-rakenteet ✅

Issue [#29](https://github.com/markomanninen/tgd-geometry-lab/issues/29).
`noether_current` muodostaa virran $H$:n 18 isometriasta (Poincaré ja väri-$SU(3)$). Identiteetti $D_\alpha j^\alpha=2K^k\mathrm{Eq}_k$ on testattu myös pinnalla, joka ei ole ratkaisu, ja kaikki virrat säilyvät vertailuratkaisuilla.

### Step 7.5 – PDE-järjestelmien muodostaminen ✅

Issue [#30](https://github.com/markomanninen/tgd-geometry-lab/issues/30).
Tässä hyödynnetään Lanyonin lähestymistapaa, jossa muodostetaan yhtälöjärjestelmä, karakteristinen matriisi, ominaisarvot, ominaisvektorit ja karakteristiset rakenteet (vrt. LanyonScriptsin `calcev`). TGD:n kenttäyhtälöt ovat geometrisesti monimutkaisempia kuin Lanyonin virtausfysiikan esimerkit, esimerkiksi minimipintaehto $g^{\alpha\beta}D_\beta\partial_\alpha h^k=0$ yhdessä Kähler-termin kanssa.

Moduuli `tgd/characteristics.mac` laskee pääosan suoraan $L$:n toisista derivaatoista ja muodostaa matriisin $A$ yhtälölle $\partial_tU+A\,\partial_xU=0$. Analysoidut taustat ovat $M^4$, kosminen säie ja massaton ekstremaali. Yhtälön tyyppi riippuu taustasta ja kertoimista (ks. [tulokset](tulokset.md)). Pelkkä Kähler-vaikutus on $M^4$:n ympärillä degeneroitunut, joten hyperbolinen analyysi ei sovellu siihen.

---

## 10. Vaihe VIII – Ratkaisujen analyysi ja numeerinen jatkokehitys 🟡

Issuet [#31](https://github.com/markomanninen/tgd-geometry-lab/issues/31), [#32](https://github.com/markomanninen/tgd-geometry-lab/issues/32) ja [#35](https://github.com/markomanninen/tgd-geometry-lab/issues/35).
- **8.1 Symmetriset erikoistapaukset** – moduuli `tgd/solutions.mac` luokittelee syötteenä annetun pinnan. CP₂-tyyppiset ekstremaalit, Lagrangen pinnat ja pallosymmetrinen ansatsi on tehty ([tulokset](tulokset.md#ratkaisugeneraattori)).
- **8.2 Analyyttiset ratkaisut** – tarkat ratkaisut ovat Pitkäsen Lagrangen vuoputkiansatsin eksplisiittinen muoto ja pallosymmetrinen katenoidi. H-H-generaattori on toteutettu Matin vastauksen mukaan, ja lisäksi tarkkoja ratkaisuja ovat suora ja kartioleikkaus pallomaisessa rakenteessa ([tulokset](tulokset.md#holografia-holomorfia)). Lorentz 4-voiman rooli H-H-pinnoilla on avoinna (#35).
- **8.3 Karakteristinen analyysi** – tehty vaiheessa 7.5.
- **8.4 Numeeriset menetelmät** – Maxima-lausekkeet muunnetaan NumPy-funktioiksi (`lab.numeric`). Ratkaisuverkot, alku- ja reunaehdot ja stabiilisuus ovat vielä tekemättä.
- **8.5 Visualisointi** – kirja `04_numeriikka_ja_kuvat.ipynb` (Maxima vastaa symbolisesta laskennasta, Python numeriikasta ja kuvista). Kirja tarkistaa numeeriset arvot analyyttisiä arvoja vasten.

---

## 11. Ohjelmiston rakenne (toteutettu)

```
tgd-geometry-lab/
├── tgd-lab.mac               lataaja
├── core/metric.mac           monistot, metriikat, muunnokset
├── algebra/vielbein.mac      kehykset
├── algebra/spinor.mac        spinoriyhteys, Kähler-kytkentä, gammat, Dirac
├── geometry/curvature.mac    Christoffel, kovariantti derivaatta, Riemann, Ricci, Bianchi
├── geometry/cartan.mac       yhteys- ja kaarevuusmuodot, torsio, spin-yhteys
├── forms/forms.mac           muodot, wedge, d, sisätulo, Hodge
├── spaces/cp2.mac            CP2 Fubini–Study, Kähler-rakenne, kartat
├── spaces/embedding-space.mac  M4, H = M4 x CP2
├── embedding/induced.mac     indusoitu metriikka ja Kähler-muoto
├── embedding/second-form.mac toinen perusmuoto, Gauss, Codazzi, Ricci
├── tgd/action.mac            vaikutustiheydet, Euler–Lagrange
├── tgd/field-equations.mac   kovariantit kenttäyhtälöt
├── tgd/noether.mac           isometriat ja Noether-virrat
├── tgd/characteristics.mac   karakteristinen analyysi
├── tgd/solutions.mac         ratkaisugeneraattori
├── tests/                    376 automaattista testiä
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
| Torsio | Levi-Civitalle $T=0$ | ✅ |
| Kaarevuus | Bianchin identiteetit | ✅ |
| Clifford-algebra | Clifford-relaatiot | ✅ |
| Upotusgeometria | Gauss–Codazzi | ✅ |
| TGD-vaikutus | variaatioyhtälöiden tarkistus | 🟡 |

Testit ajetaan myös yksinkertaisilla tunnetuilla geometrioilla (yksikköpallo $S^2$, $\mathbb R^4$, Minkowski), jotta mahdolliset virheet voidaan erottaa TGD:n omista matemaattisista oletuksista.

---

## 13. Toteutusjärjestys ja välitavoitteet

| | Sisältö | Valmis kun | Tila |
|---|---|---|---|
| [M1](https://github.com/markomanninen/tgd-geometry-lab/milestone/1) | Maxima- ja Clifford-ympäristö | peruslaskenta toimii | ✅ |
| [M2](https://github.com/markomanninen/tgd-geometry-lab/milestone/2) | $CP_2$-metriikka | Fubini–Study-tulokset täsmäävät | ✅ |
| [M3](https://github.com/markomanninen/tgd-geometry-lab/milestone/3) | Differentiaalimuodot | muoto-operaatiot ja $d^2=0$ toimivat | ✅ |
| [M4](https://github.com/markomanninen/tgd-geometry-lab/milestone/4) | Yhteydet ja kaarevuus | kaarevuus- ja Bianchi-testit läpäisty | ✅ |
| [M5](https://github.com/markomanninen/tgd-geometry-lab/milestone/5) | Clifford-geometria | paikalliset kehykset ja spin-yhteys | ✅ |
| [M6](https://github.com/markomanninen/tgd-geometry-lab/milestone/6) | Upotusgeometria | indusoitu geometria ja Gauss–Codazzi | ✅ |
| [M7](https://github.com/markomanninen/tgd-geometry-lab/milestone/7) | TGD:n vaikutusintegraali | variaatioyhtälöt muodostuvat | 🟡 |
| [M8](https://github.com/markomanninen/tgd-geometry-lab/milestone/8) | Ratkaisuanalyysi | ensimmäiset testattavat ratkaisut | ✅ |

Toteutusjärjestys on ensin M1–M4, sitten M5–M6 ja vasta sen jälkeen M7–M8. Näin TGD-fysiikan oletukset eivät sekoitu laskentakirjaston virheisiin.

---

## 14. Ensimmäinen kehitystehtävä `cp2.mac` ✅

1. ✅ $CP_2$:n paikallinen kompleksinen koordinaattikartta
2. ✅ Fubini–Study-Kähler-potentiaali
3. ✅ metriikka ja käänteismetriikka
4. ✅ Kähler-muoto
5. ✅ $d\omega=0$
6. ✅ Christoffelin symbolit
7. ✅ Riemannin ja Riccin tensorit
8. ✅ Kähler–Einstein-ominaisuus ($\mathrm{Ric}=6g$, kun $R^2=1$, TGD-normalisointi)

Koska tehtävä on valmis, seuraavat askeleet ovat:

1. **Ratkaisuverkot, alku- ja reunaehdot ja stabiilisuus.** Nämä ovat vaiheen 8.4 laskematta olevat osat.
2. **Rakenteen $(t\pm\rho)$ kompleksikoordinaatti.** Pitkänen tarkoitti tätä sylinterirakennetta, ja koordinaatti $z+i\phi$ ei ole siinä kompleksinen.
3. **Partonipinnat.** Pitkäsen linjauksen mukaan Kähler–Chern–Simons-vaikutus ja Diracin vaikutus ovat partonipinnoilla, joten laskennan painopiste siirtyy niihin.
---

## 15. Lopullinen tavoite

Tavoitteena ei ole pelkästään TGD:n yhtälöiden syöttäminen Maximalle, vaan järjestelmä, jossa voidaan tehdä seuraava laskentaketju

$$
\text{Upotusavaruus}\to\text{Geometria}\to\text{Differentiaalimuodot}\to\text{Yhteydet}\to\text{Kaarevuus}\to\text{Vaikutus}\to\text{Kenttäyhtälöt}\to\text{Ratkaisut}
$$

Ympäristö tarjoaa systemaattisen tavan tutkia TGD:n matemaattista rakennetta ja testata sen geometrisia seurauksia symbolisesti. Se ei itsessään todista TGD:n fysikaalista oikeellisuutta, mutta se voi auttaa löytämään matemaattisia seurauksia, tarkistamaan johdoksia ja tutkimaan erikoistapauksia, joiden käsin laskeminen olisi työlästä.

---

## Lähteet ja taustamateriaali

- M. T. Manninen, *Through the Wormhole on Spacetime Surface – Early History of Topological Geometrodynamics Theory* (2024). Erityisesti luvut TGD:n vaikutusintegraalista ($S_K+S_V$, indusoitu $g_{\alpha\beta}$ ja $J_{\alpha\beta}$, variaatio upotuskoordinaattien $h^k$ suhteen), kenttäyhtälöistä (minimipinnat) ja twistorinostosta.
- M. Pitkänen, *Topological Geometrodynamics* ja tgdtheory.fi.
- M. Pitkänen, *The Geometry of CP2 and its Relationship to Standard Model* (CP₂-normalisointi).
- M. Pitkänen, *About the construction of p-adic QFT limit of TGD*, hep-ph/9510361 ($L_K$, $S_K(CP_2)=\pi/8\alpha_K$).
- M. Pitkänen, [*About Twistor Lift of TGD*](http://tgdtheory.fi/public_html/articles/hgrtwistor.pdf), luvut 4.2.2 ja 4.3 tyhjiöekstremaaleista ja holomorfisuudesta.
- M. Pitkänen, matpitka.blogspot.com, kirjoitukset massattomista ekstremaaleista (8/2016), minimipintaekstremaaleista (12/2016), Kähler-kytkennästä k=1/k=3 (1/2017) ja H-H-periaatteesta (8/2025).
- Lanyon AI, <https://lanyon.ai/>, *Announcing Lanyon AI* (J. Gorard, 2026), [yhtiön esittely](https://lanyon.ai/company/) ja [esittelyvideo](https://youtu.be/gSH50n-9ZLk).
- LanyonScripts, <https://github.com/lanyonai/LanyonScripts> (MIT) ja Lanyonin Colab-esimerkki *Run LanyonScripts in Colab*.
- D. Prodanov, Clifford-algebrapaketti Maximalle, <https://github.com/dprodanov/clifford> (LGPL-2.1).
- Fubini–Study-metriikan eksplisiittiset paikalliset lausekkeet ja kaarevuus löytyvät tavanomaisista differentiaaligeometrian oppikirjoista, esimerkiksi teoksesta Kobayashi–Nomizu II, luku IX.
