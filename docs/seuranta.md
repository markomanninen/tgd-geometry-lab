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

| Issue | Mitä tarvitaan |
|---|---|
| #10 CP2-säde ja normalisointi | Mikä TGD-lähde ja konventio (Pitkäsen s_kl, J_kl) on referenssi |
| #19 Spin-yhteys | CP2 ei ole spin-monisto → spin^c / Kähler-kytkennän valinta TGD:n mukaan |
| #27 L_TGD:n variaatio | Kertoimien c_K, c_V etumerkit ja normalisointi; dynaamiset muuttujat (M4-projektio vai CP2-koordinaatit) |
| #31 Uudet ratkaisut | Mitkä ekstremaaliluokat ovat tutkimuksellisesti kiinnostavimpia |
| #33 Lanyon-video | Transkriptio (en saanut sitä haettua) |
| #34 Kirjan kaavat | Kirjoittajana vahvistat, mitkä väitteet kuuluvat testeiksi |

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
