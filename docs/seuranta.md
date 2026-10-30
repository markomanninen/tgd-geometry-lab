# Seuranta ja työnkulku

Kehityssuunnitelman ([kehityssuunnitelma.md](kehityssuunnitelma.md)) jokainen vaihe on GitHub-issue, ja välitavoitteet M1–M8 ovat milestoneja. Valmiit vaiheet on suljettu, joten milestone-sivu näyttää edistymisen suoraan.

| Näkymä | Linkki |
|---|---|
| Välitavoitteet ja edistyminen | <https://github.com/markomanninen/tgd-geometry-lab/milestones> |
| Avoimet tehtävät | <https://github.com/markomanninen/tgd-geometry-lab/issues> |
| Testiajot | <https://github.com/markomanninen/tgd-geometry-lab/actions> |

## Tila 30.10.2026

| Välitavoite | Valmiina | Seuraavaksi |
|---|---|---|
| M1 Ympäristö | 4/4 ✅ | – |
| M2 CP2-metriikka | 4/6 | #8 kartta Z2, #10 R²-normalisointi |
| M3 Muodot | 2/3 | #13 integraalit |
| M4 Kaarevuus | 2/3 | #16 Cartan ja torsio |
| M5 Clifford-geometria | 1/4 | #18 vielbein → #19 spin-yhteys → #20 γ^μ |
| M6 Upotus | 2/4 | #23 toinen perusmuoto → #24 Gauss–Codazzi |
| M7 Toiminta | 2/6 | #27 L_TGD:n variaatio → #28 ekstremaalitarkistus |
| M8 Ratkaisut | 0/2 | #31, #32 |

**Kriittinen polku:** #18 → #16/#19 → #23 → #27 → #28. Kun kosminen säie ja massaton ekstremaali tarkistuvat kenttäyhtälöiden ratkaisuiksi (#28), koko ketju upotusavaruudesta kenttäyhtälöihin on testattu.

## Päätöspisteet (tunniste `päätös`)

TGD:n ydinkysymykset osoitetaan **Matti Pitkäselle** (cc Tuomas Sorakivi). Ensimmäinen kysymyskirje on lähetetty M1–M4:n jälkeen (luonnos 30.10.2026); kysymysten numerot viittaavat siihen.

| Issue | Mitä tarvitaan | Kenelle | Kirjeen kysymys |
|---|---|---|---|
| #10 CP2-säde ja normalisointi | s_kl:n ja J_kl:n normalisointi, R:n kiinnitys | Matti | 1 |
| – Upotusavaruuden etumerkki | h = m − R²s; M4:n Kähler-rakenne mukaan nyt vai myöhemmin | Matti | 2 |
| #27 L_TGD:n variaatio | c_K:n ja c_V:n etumerkki ja normalisointi; yleinen h^k vai QFT-raja | Matti | 3 |
| #19 Spin-yhteys | CP2 ei ole spin → Kähler-kytkentä kvarkeille ja leptoneille | Matti | 4 |
| #31 Uudet ratkaisut | Mitkä ekstremaalit tarkistetaan ensin | Matti | 5 |
| #22 / #28 ME-ansatsi | Vastaako ansatsi MEn määritelmää | Matti | 6 |
| #33 Lanyon-video | Transkriptio | Marko | – |
| #34 Kirjan kaavat | Mitkä väitteet kuuluvat testeiksi | Marko | – |

Muut avoimet issuet ovat puhtaasti matemaattisia, ja ne voi tehdä itsenäisesti.

## Tunnisteet

`päätös` · `infra` · `cp2` · `muodot` · `geometria` · `clifford` · `upotus` · `tgd-dynamiikka` · `analyysi` · `testit` · `colab` · `dokumentaatio` · `fysiikka`

## Työnkulku

1. Valitse issue, jolla on milestone. Issuen "Valmis kun" -ehto määrittelee testin.
2. Kirjoita testi ensin `tests/test-*.mac`:iin (tunnettu identiteetti tai vertailuarvo).
3. Toteuta moduuli ja aja `./scripts/run_tests.sh ../clifford`.
4. Commit-viestiin `Closes #N`, jolloin issue sulkeutuu ja milestone päivittyy.
5. Päivitä tilamerkintä (✅/🟡/⬜) kehityssuunnitelmaan ja tarvittaessa Colab-kirja (`python3 scripts/build_notebooks.py`).

## Projektitaulu (GitHub Projects)

Taulun voi luoda kerran käsin; issuet ja milestonet ovat jo valmiina:

1. <https://github.com/markomanninen/tgd-geometry-lab> → **Projects** → **Link a project** → **New project** → pohja **Board** (tai **Roadmap**), nimeksi *TGD Geometry Lab*.
2. Lisää issuet: **Add item** → `#` → valitse kaikki, tai lisää suodatin `repo:markomanninen/tgd-geometry-lab`.
3. **Workflows** → ota käyttöön *Auto-add to project* (suodatin `is:issue`) sekä *Item closed → Done*.
4. Ryhmittele näkymä kentällä **Milestone**, jolloin M1–M8 näkyvät omina kaistoinaan.

`scripts/seed_tracking.py` luo tunnisteet, milestonet ja issuet uudelleen tyhjään repoon. Se ohittaa jo olemassa olevat.
