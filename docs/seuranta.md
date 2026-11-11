# Seuranta ja työnkulku

Kehityssuunnitelman ([kehityssuunnitelma.md](kehityssuunnitelma.md)) jokainen vaihe on GitHub-issue, ja välitavoitteet M1–M8 ovat milestoneja. Valmiit vaiheet on suljettu, joten milestone-sivu näyttää edistymisen suoraan.

| Näkymä | Linkki |
|---|---|
| Välitavoitteet ja edistyminen | <https://github.com/markomanninen/tgd-geometry-lab/milestones> |
| Avoimet tehtävät | <https://github.com/markomanninen/tgd-geometry-lab/issues> |
| Testiajot | <https://github.com/markomanninen/tgd-geometry-lab/actions> |
| Julkinen sivusto | <https://markomanninen.github.io/tgd-geometry-lab/> |

## Tila 8.11.2026

| Välitavoite | Valmiina | Seuraavaksi |
|---|---|---|
| M1 Ympäristö | 4/4 ✅ | – |
| M2 CP2-metriikka | 6/6 ✅ | – |
| M3 Muodot | 3/3 ✅ | – |
| M4 Kaarevuus | 3/3 ✅ | – |
| M5 Clifford-geometria | 4/4 ✅ | – |
| M6 Upotus | 4/4 ✅ | – |
| M7 Vaikutus | 6/6 ✅ | – |
| M8 Ratkaisut | 3/3 ✅ | Ratkaisuverkot, alku- ja reunaehdot ja stabiilisuus |
| M9 Partonipinnat | 0/6 | #36 partoniradan metriikkaehdot |

Kaikki 746 testiä menevät läpi.

Vaihe X eli lehtien kokoaminen ja Einsteinin raja on työn alla ([kehityssuunnitelma](kehityssuunnitelma.md#102-vaihe-x-lehtien-kokoaminen-ja-einsteinin-raja)). Sille ei ole vielä välitavoitetta eikä issueita.

Kriittinen polku #18 → #16/#19 → #23 → #27 → #28 on valmis. Ketju upotusavaruudesta kenttäyhtälöihin on laskettu ja testattu symbolisilla kertoimilla $c_K$, $c_V$. Matti Pitkänen vastasi kysymyksiin 31.10.2026, ja vastaukset on kirjattu [konventioihin](konventiot.md) ja issueihin #27, #28 ja #31. Laskenta nosti esiin jatkokysymyksiä, jotka ovat issuessa #35. Matti vastasi niihin 31.10.2026, ja vastaukset ja niiden laskut on kirjattu samaan issueen. Keskustelu jatkui issuessa #35 8.11.2026 asti, ja vielä avoimet kysymykset ovat alla.

## Päätöspisteet (tunniste `päätös`)

Periaatteena on, että vastaukset haetaan ensin itse TGD-kirjallisuudesta (Pitkäsen artikkelit, kirjat, blogi). **Matti Pitkäselle** kysytään vain se, mikä jää tutkimuksen jälkeen avoimeksi.

### Selvitetty kirjallisuudesta 30.10.2026

| Kysymys | Vastaus | Lähde | Tila |
|---|---|---|---|
| CP₂:n normalisointi (#10) | $ds^2=R^2\partial\bar\partial K$, jossa $K=\log(1+r^2)$, sekä $\mathrm{Ric}=6g/R^2$ ja $S_K(CP_2)=\pi/(8\alpha_K)$ | Pitkänen, *The Geometry of CP2…* ja hep-ph/9510361 | ✅ toteutettu ja testattu |
| Kähler-vaikutuksen kerroin (#27) | $L_K=\frac{1}{4g_K^2}J^{\mu\nu}J_{\mu\nu}\sqrt g$, $\alpha_K=g_K^2/4\pi$ | hep-ph/9510361 | ✅ konventioissa |
| M⁴:n Kähler-rakenne | Twistorinosto vaatii sen, mutta vaikutus ~10⁻¹⁷ → ohitetaan toistaiseksi | Pitkäsen blogi 2025 | ✅ päätetty |
| Spinorikytkentä (#19) | Kähler-kytkentä $k=1$ kvarkeille, $k=3$ leptoneille | Pitkäsen blogi 2017 | ✅ toteutusohje |
| ME-ansatsi (#28) | CP₂-koordinaatit funktioita $u=k\cdot m$, $v=\varepsilon\cdot m$ – vastaa omaamme. Lähde rajaa minimipintaväitteen sanoin "in their simplest form at least". Laskettu tulos on `docs/konventiot.md`:ssä | Pitkänen, *Extremals of the Kähler Action* (2024), luvut 6.2–6.3 | 🟡 ks. avoimet |
| Vertailuekstremaalit (#31) | ME, kosminen säie $X^2\times Y^2$, Lagrangen tyhjiöekstremaalit, CP₂-tyyppiset | Pitkäsen blogi 2016 | ✅ lista |

### Matin vastaukset 31.10.–1.11.2026

| Issue | Vastaus | Tila |
|---|---|---|
| #27 | Etumerkki ei näy H-H-pintojen eikä Lagrangen minimipintojen kenttäyhtälöissä. Se vaikuttaa kosmologiseen vakioon ja Kähler-funktion eksponenttiin, ja $1/\alpha_K$ on yhteinen kerroin | ✅ konventioissa |
| #28 | Ansatsi $s^k(u,v)$ on johdettu puhtaalle Kähler-vaikutukselle, ja vaikutukselle $S_K+S_V$ sen korvaa H-H, josta minimipintaominaisuus seuraa | ✅ konventioissa |
| #31 | $f_1=f_2=0$, jossa $f_i$ ovat analyyttisiä koordinaateissa $\xi^1,\xi^2,w,u$. Lagrangen pinnat ovat oma ratkaisutyyppinsä | ✅ toteutettu ja testattu |
| #35 | $J(M^4)$ ja $J(CP_2)$ ovat vaikutuksessa erilliset termit. Lorentz 4-voiman pitäisi hävitä H-H-pinnoilla ilman, että poikittainen virta häviää. Etumerkit seuraavat energian positiivisuudesta | 🟡 merkit laskettu ($c_K,c_V>0$), voima ei häviä litteässä rakenteessa |
| #35 | Lisäehtoja ei tuoda. Sisäosan vaikutus on tilavuustermi, ja Kähler–Chern–Simons-vaikutus on partonipinnoilla. | ✅ kirjattu konventioihin |
| #35 | Pitkänen pohti 2.11.2026 sisäosaan myös kaarevuusskalaaria ja tilavuutta. Hänen mukaansa 3.11.2026 pelkkä tilavuus on elegantein, ja kaarevuusskalaarista voidaan joutua luopumaan, jos minimipinnoista pidetään kiinni. | 🟡 [vertailu](sivututkimus/sisaosan-vaikutus.md) laskettu |
| #35 | Pitkänen ehdotti 3.11.2026 Kähler-vaikutusta ja tilavuutta lisäehdolla, jossa $CP_2$:n Kähler-funktio toteuttaa poikittaisen Laplacen yhtälön. NeuroPajan laskussa ehto sallii holomorfisilla pinnoilla vain riippumattomuuden koordinaatista $w$. Pitkäsen mukaan 4.11.2026 singulariteetit ovat ajatuksen ydin, riippuvuus on vain koordinaatista $u$, ja kosminen säie on rajatapaus. | 🟡 [vertailussa](sivututkimus/sisaosan-vaikutus.md#pitkasen-vastaus-4112026), ei-holomorfinen monopoli laskettu |
| #35 | Pitkänen vastasi 4.11.2026 aiempiin viiteen kysymykseen. Vuoputki on kaksilehtinen ja sen poikkileikkaus suljettu, $G$ selittyy Planckin vakioiden hierarkialla, Kähler-muoto on magneettinen ja poikittainen kaikkialla paitsi singulariteeteissa, ja kerroin $1/16\pi G$ tulee kaarevuusskalaarista, josta hän on valmis luopumaan. | ✅ [kirjattu](sivututkimus/sisaosan-vaikutus.md#pitkasen-vastaukset-aiempiin-kysymyksiin-4112026) |
| #35 | Pitkänen vastasi 5.11.2026. CD:n partonipinnan reuna on timantin reunalla, tekijäavaruudet $H^3/\Gamma$ liittyvät tessellaatioihin, ja kaarevuusskalaari kaatuu Einsteinin tensorin $(2,0)$- ja $(0,2)$-osiin. NeuroPajan laskussa litteän rakenteen pinnat $\xi(u,w)$ ratkaisevat myös vaikutuksen R + tilavuus, ja pallomaisessa rakenteessa myös $(1,1)$-osa antaa puolet supistuksesta. Jos säiemaailmanpinnatkin ovat minimaalipintoja, $H^3$:ssa ei ole jakoa. | ✅ [kirjattu](sivututkimus/sisaosan-vaikutus.md#pitkasen-vastaukset-5112026) |
| #35 | Pitkänen hyväksyi 5.11.2026 iltapäivällä, että säieratojen ei tarvitse olla minimaalipintoja, koska hyperkompleksinen rakenne on pinnan sisäinen ominaisuus. NeuroPaja luokitteli H-J-rakenteet, ja niitä on konformiryhmää vaille kolme. | ✅ [luokittelu](konventiot.md#h-j-rakenteiden-luokittelu) |
| #35 | Pitkänen kysyi 5.11.2026 illalla, onko NeuroPaja vai Gemini väärässä. Tulokset ovat sopusoinnussa, sillä integroituvia jakoja on, mutta säieradat ja partonipinnat eivät ole yhtä aikaa minimaalisia. | ✅ [kirjattu](sivututkimus/sisaosan-vaikutus.md#pitkasen-kysymykset-5112026-illalla) |
| #35 | Pitkäsen mukaan 6.11.2026 minimaalisuus ei ole välttämätöntä. Valokartion reunan viipaloinnissa pallot eivät ole minimaalipintoja, ja molemmat perheet ovat minimaalisia vain litteässä rakenteessa. Hän lähetti myös artikkeliluonnoksen, jonka tarkistus lähti hänelle. | ✅ [kirjattu](sivututkimus/sisaosan-vaikutus.md#valokartion-reunan-viipalointi-ja-minimaalisuus-m4ssa) |
| #35 | Pitkäsen mukaan 6.11.2026 pallo on minimaalipinta valokartion reunan pintana, koska valokartio on metrisesti pallo. NeuroPajan 7.11.2026 lähettämän laskun mukaan jokainen leikkaus on konformisesti pyöreä, mutta sen ala riippuu säteestä, ja pallo on alan minimi kiinteällä keskisäteellä. | ✅ [kirjattu](sivututkimus/sisaosan-vaikutus.md#valokartion-reunan-viipalointi-ja-minimaalisuus-m4ssa) |
| #35 | Pitkäsen mukaan 8.11.2026 pallo on minimaalipinta valinnalla $g^{rr}=0$, ja hänen lisäehtonsa sanoo Kähler-virran olevan valon kaltainen. NeuroPajan samana päivänä lähettämän laskun mukaan valokartion metriikalle ei ole vääntymätöntä metriikkaa säilyttävää konnektiota, ja tulos pätee avaruuskulmamitassa. Valon kaltaisen hypertason leikkauksilla, kuten horosfäärirakenteen partonipinnoilla, ala säilyy sellaisenaan. Valon kaltainen virta sallii pallomaisessa rakenteessa suoran ja kartioleikkauksen. | ✅ [kirjattu](sivututkimus/sisaosan-vaikutus.md#pitkasen-vastaukset-8112026) |
| #35 | Pitkänen lisäsi 9.11.2026 artikkeliin NeuroPajan laskut, joiden mukaan $M^4$:ssä ei ole suljettuja avaruuden kaltaisia minimaalipintoja eikä $H^3$:ssa suljettuja minimaalipintoja. NeuroPajan laskun mukaan $H^3$:n viipalointi totaalisesti geodeettisilla tasoilla toimii, mutta niitä vastaan kohtisuorat kartiot ovat $M^4$:n minimaalipintoja vain akselilla. | ✅ [kirjattu](sivututkimus/sisaosan-vaikutus.md#artikkelin-viimeistely) |
| #35 | Pitkäsen 10.11.2026 tiivistelmän mukaan Laplacen ehto tekee Kähler-virrasta valon kaltaisen, ja Kähler-vaikutuksen kaatuminen on vakavampi ongelma kuin kaarevuusskalaarin, koska twistorinosto antaa vaikutukseksi Kähler-vaikutuksen ja tilavuustermin summan. | ✅ [kirjattu](sivututkimus/sisaosan-vaikutus.md#artikkelin-viimeistely) |

### Avoinna – kysytään Matilta

| Issue | Kysymys |
|---|---|
| – | Mikä määrää monopoliputken paksuuden, kun sisäosassa on pelkkä tilavuustermi? Rakenteella $(t\pm\rho)$ ei luokittelun mukaan ole kompleksikoordinaattia. |
| #35 | Pallomainen rakenne on kausaalisessa timantissa symmetrinen $u$:n ja $v$:n vaihdossa, kun timantti peilataan keskikohtansa yli. Mistä H-H-ansatsin $u$-$v$-epäsymmetria silloin tulee, esimerkiksi timantin aktiivisesta reunasta nollaenergiaontologiassa? |
| #35 | Vastaako valokartioiden kärjen suoran laji, eli aikasuuntainen, valon kaltainen tai avaruussuuntainen, jotain fysikaalista? |
| #35 | Riittääkö Pitkäselle virran valon kaltaisuus, joka pallomaisessa rakenteessa sallii suoran ja kartioleikkauksen mutta litteässä rakenteessa vain Kähler-tyhjiön $\xi=\xi(u)$? |
| #35 | Hitchinin lauseen mukaan kompakteista itseduaaleista neliulotteisista avaruuksista vain $S^4$:llä ja $CP_2$:lla on Kähler-rakenteinen twistoriavaruus. Miten $M^4$ tulee mukaan artikkelin perusteluun TGD:n yksikäsitteisyydestä? |

### Markolle

| Issue | Asia |
|---|---|
| #34 | Esseen (2024, s. 33) kerroin $\frac{1}{2\alpha_K}$ antaa arvon $S_K(CP_2)=\pi^2/\alpha_K$, kun Pitkäsen kerroin $\frac{1}{4g_K^2}=\frac{1}{16\pi\alpha_K}$ antaa arvon $\pi/(8\alpha_K)$. Suhde on $8\pi$. Muut esseen kaavat on testattu ([tulokset](tulokset.md#mannisen-esseen-kaavat-vertailutesteina)), ja esseen korjaamisesta päättää Marko. |
| #42 | 🟡 Schwarzschildin metriikka upottuu kahdella tavalla, ja molemmat ovat testinä. Kerrin metriikka upottuu ensimmäisessä kertaluvussa symmetriaa noudattavalla yritteellä vain likimäärin tarkkuudella $R^2/m^2$, ja toisessa kertaluvussa se ei upotu likimäärinkään ([tulokset](tulokset.md#mustien-aukkojen-metriikat-indusoituna-metriikkana)). Kerrin metriikka saadaan kuitenkin horisontin ulkopuolella paikallisesti likimäärin viiden lehden koottuna metriikkana, ja se on testinä ja Codexin tarkistama. Kerrin ja Schildin muodossa Kerrin metriikka on laakea metriikka ja yksi valon kaltainen neliö, ja 11.11.2026 alkoi lehtien ratkaisuperheen rajaaminen. Seisovien palloaaltojen spektri $1/k^2$ antaa potenssin $1/r$ mutta ei tyhjiötä. Tila ja jatkosuunnat ovat tulossivulla. Tuloksen viemisestä Matille päättää Marko. |

## Sivututkimuspolut

Sivututkimuspolut eivät kuulu milestoneihin. [Regge–Teitelboim ja TGD](sivututkimus/regge-teitelboim.md) kokoaa nykytutkimuksen upotusgravitaatiosta ja sen yhtymäkohdat TGD:hen. Tilanne 1.11.2026 on, että selvitys on tarkistettu ja laskut ovat testeissä. Matille lähetettiin 1.11.2026 viisi kysymystä, jotka on kirjattu [issueen 35](https://github.com/markomanninen/tgd-geometry-lab/issues/35#issuecomment-6552829572). Hän vastasi niihin samana päivänä, ja vastaukset on kirjattu sivulle.

## Tunnisteet

`päätös` · `infra` · `cp2` · `muodot` · `geometria` · `clifford` · `upotus` · `tgd-dynamiikka` · `analyysi` · `testit` · `colab` · `dokumentaatio` · `fysiikka`

## Työnkulku

1. Valitse issue, jolla on milestone. Issuen "Valmis kun" -ehto määrittelee testin.
2. Kirjoita testi ensin `tests/test-*.mac`:iin (tunnettu identiteetti tai vertailuarvo).
3. Toteuta moduuli ja aja `./scripts/run_tests.sh ../clifford`.
4. Commit-viestiin `Closes #N`, jolloin issue sulkeutuu ja milestone päivittyy.
5. Päivitä tilamerkintä (✅/🟡/⬜) kehityssuunnitelmaan ja tarvittaessa Colab-kirja (`python3 scripts/build_notebooks.py`).
6. Lisää merkittävät tulokset sivulle `docs/tulokset.md`. Sivusto päivittyy automaattisesti, kun muutos on `main`-haarassa.

## Projektitaulu (GitHub Projects)

Taulun voi luoda kerran käsin, koska issuet ja milestonet ovat jo valmiina:

1. <https://github.com/markomanninen/tgd-geometry-lab> → **Projects** → **Link a project** → **New project** → pohja **Board** (tai **Roadmap**), nimeksi *TGD Geometry Software Lab*.
2. Lisää issuet valinnoilla **Add item** → `#` → valitse kaikki, tai lisää suodatin `repo:markomanninen/tgd-geometry-lab`.
3. **Workflows** → ota käyttöön *Auto-add to project* (suodatin `is:issue`) sekä *Item closed → Done*.
4. Ryhmittele näkymä kentällä **Milestone**, jolloin M1–M8 näkyvät omina kaistoinaan.

`scripts/seed_tracking.py` luo tunnisteet, milestonet ja issuet uudelleen tyhjään repoon. Se ohittaa jo olemassa olevat.
