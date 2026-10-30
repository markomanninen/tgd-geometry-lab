# Seuranta ja työnkulku

Kehityssuunnitelman ([kehityssuunnitelma.md](kehityssuunnitelma.md)) jokainen vaihe on GitHub-issue, ja välitavoitteet M1–M8 ovat milestoneja. Valmiit vaiheet on suljettu, joten milestone-sivu näyttää edistymisen suoraan.

| Näkymä | Linkki |
|---|---|
| Välitavoitteet ja edistyminen | <https://github.com/markomanninen/tgd-geometry-lab/milestones> |
| Avoimet tehtävät | <https://github.com/markomanninen/tgd-geometry-lab/issues> |
| Testiajot | <https://github.com/markomanninen/tgd-geometry-lab/actions> |
| Julkinen sivusto | <https://markomanninen.github.io/tgd-geometry-lab/> |

## Tila 30.10.2026

| Välitavoite | Valmiina | Seuraavaksi |
|---|---|---|
| M1 Ympäristö | 4/4 ✅ | – |
| M2 CP2-metriikka | 6/6 ✅ | – |
| M3 Muodot | 3/3 ✅ | – |
| M4 Kaarevuus | 3/3 ✅ | – |
| M5 Clifford-geometria | 4/4 ✅ | – |
| M6 Upotus | 4/4 ✅ | – |
| M7 Toiminta | 4/6 | #27 ja #28 odottavat Matin linjausta |
| M8 Ratkaisut | 1/2 | #31 odottaa Matin linjausta |

Kaikki 234 testiä menevät läpi.

Kriittinen polku on #18 → #16/#19 → #23 → #27 → #28. Ketju upotusavaruudesta kenttäyhtälöihin on nyt laskettu ja testattu symbolisilla kertoimilla $c_K$, $c_V$, ja kosminen säie ja ME $s^k(u)$ ovat ekstremaaleja. #27 ja #28 ovat auki, koska yleisen ME-ansatsin asema toiminnalle $S_K+S_V$ vaatii Matin linjauksen. Issueiden #27, #28 ja #31 kysymykset lähetettiin Matille sähköpostilla 31.10.2026, ja vastausta odotetaan.

## Päätöspisteet (tunniste `päätös`)

Periaatteena on, että vastaukset haetaan ensin itse TGD-kirjallisuudesta (Pitkäsen artikkelit, kirjat, blogi). **Matti Pitkäselle** kysytään vain se, mikä jää tutkimuksen jälkeen avoimeksi.

### Selvitetty kirjallisuudesta 30.10.2026

| Kysymys | Vastaus | Lähde | Tila |
|---|---|---|---|
| CP₂:n normalisointi (#10) | $ds^2=R^2\partial\bar\partial K$, jossa $K=\log(1+r^2)$, sekä $\mathrm{Ric}=6g/R^2$ ja $S_K(CP_2)=\pi/(8\alpha_K)$ | Pitkänen, *The Geometry of CP2…* ja hep-ph/9510361 | ✅ toteutettu ja testattu |
| Kähler-toiminnan kerroin (#27) | $L_K=\frac{1}{4g_K^2}J^{\mu\nu}J_{\mu\nu}\sqrt g$, $\alpha_K=g_K^2/4\pi$ | hep-ph/9510361 | ✅ konventioissa |
| M⁴:n Kähler-rakenne | Twistorinosto vaatii sen, mutta vaikutus ~10⁻¹⁷ → ohitetaan toistaiseksi | Pitkäsen blogi 2025 | ✅ päätetty |
| Spinorikytkentä (#19) | Kähler-kytkentä $k=1$ kvarkeille, $k=3$ leptoneille | Pitkäsen blogi 2017 | ✅ toteutusohje |
| ME-ansatsi (#28) | CP₂-koordinaatit funktioita $u=k\cdot m$, $v=\varepsilon\cdot m$ – vastaa omaamme. Lähde rajaa minimipintaväitteen sanoin "in their simplest form at least". Laskettu tulos on `docs/konventiot.md`:ssä | Pitkänen, *Extremals of the Kähler Action* (2024), luvut 6.2–6.3 | 🟡 ks. avoimet |
| Vertailuekstremaalit (#31) | ME, kosminen säie $X^2\times Y^2$, Lagrangen tyhjiöekstremaalit, CP₂-tyyppiset | Pitkäsen blogi 2016 | ✅ lista |

### Avoinna – kysytään Matilta

| Issue | Kysymys |
|---|---|
| #27 | Mikä on twistorinoston $S_K+S_V$ tilavuustermin kertoimen etumerkki ja normalisointi suhteessa Kähler-termiin Minkowski-alueilla, ja mikä on kompleksisen $\alpha_K$:n rooli nykyisessä muotoilussa? |
| #28 | Mikä on ME:n täsmällinen määritelmä toiminnalle $S_K+S_V$? Yleinen $s^k(u,v)$ on Kähler-ekstremaali, mutta se ei ole minimipinta. Ks. kysymys issuessa #28 |
| #31 | Holografia = holomorfia -periaatteen (H-H) nykyinen täsmällinen muoto, jonka voisi toteuttaa ratkaisugeneraattorina (koordinaatit $u$, $w$ ja ehdot $f_1=f_2=0$) |

### Markolle

| Issue | Asia |
|---|---|
| #34 | Oman kirjan (2024, s. 34) kerroin $L_K=\frac{1}{2\alpha_K}\ldots$ poikkeaa Pitkäsen määritelmästä $\frac{1}{4g_K^2}=\frac{1}{16\pi\alpha_K}$ – tarkista |

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

1. <https://github.com/markomanninen/tgd-geometry-lab> → **Projects** → **Link a project** → **New project** → pohja **Board** (tai **Roadmap**), nimeksi *TGD Geometry Lab*.
2. Lisää issuet valinnoilla **Add item** → `#` → valitse kaikki, tai lisää suodatin `repo:markomanninen/tgd-geometry-lab`.
3. **Workflows** → ota käyttöön *Auto-add to project* (suodatin `is:issue`) sekä *Item closed → Done*.
4. Ryhmittele näkymä kentällä **Milestone**, jolloin M1–M8 näkyvät omina kaistoinaan.

`scripts/seed_tracking.py` luo tunnisteet, milestonet ja issuet uudelleen tyhjään repoon. Se ohittaa jo olemassa olevat.
