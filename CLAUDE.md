# TGD Geometry Lab – ohjeet agentille

Symbolinen differentiaaligeometria Maximalla TGD:lle. Kieli: dokumentit ja issuet suomeksi, koodikommentit englanniksi.

## Ennen muutoksia
- Lue `docs/konventiot.md` (etumerkit, normalisoinnit, indeksijärjestys). Älä muuta konventioita ilman, että päivität testit ja dokumentin samassa muutoksessa.
- Tehtävät ovat GitHub-issueita ja milestoneja M1–M8 (`docs/seuranta.md`). Työskentele issuen "Valmis kun" -ehtoa vastaan.

## Paikallinen ympäristö (macOS)
- `brew install maxima` (5.50), Prodanovin clifford kloonattuna repon viereen: `../clifford`.
- Homebrew-polku: `export PATH=/opt/homebrew/bin:$PATH`.
- Maxima 5.50 käyttää hakupolkumalleissa `###`, vanhemmat `$$$` – lataa paketit täydellä polulla (`tgd_load_clifford`).

## Testit
- `./scripts/run_tests.sh ../clifford` (Prodanovin clifford-checkout valinnainen). Kaikkien testien on mentävä läpi ennen committia.
- Uusi ominaisuus → ensin testi tunnetulla identiteetillä tai vertailuarvolla (`tests/test-*.mac`, `check(nimi, ehto)`), lisää tiedosto `tests/run-all.mac`:n listaan.
- Maxima 5.46: `getenv` puuttuu – polut annetaan muuttujina (`tgd_root`, `clifford_path`). `rules` on varattu nimi.
- Funktioiden yhdistelmäargumentit (`f(t-z)`) eivät derivoidu ketjusäännöllä luotettavasti → käytä `depends` + sopivia parametreja (vrt. valokartiokoordinaatit testissä).

## Rakenne
- Moduulit ladataan `tgd-lab.mac`:ssa; uusi moduuli lisätään sinne.
- Colab-kirjat generoidaan: `python3 scripts/build_notebooks.py`, sitten aja ne (`jupyter nbconvert --execute --inplace`, `TGD_ROOT`, `CLIFFORD_PATH`, `RUN_LANYON=0`) ja tarkista, ettei tulosteisiin jää paikallisia polkuja.

## Sivusto
- Julkinen sivusto: <https://markomanninen.github.io/tgd-geometry-lab/> (MkDocs Material, MathJax). `docs/` on sen sisältö, ja `.github/workflows/pages.yml` julkaisee sen `main`-haarasta.
- Paikallinen rakennus: `pip install -r docs/requirements.txt`, sitten `./scripts/build_site.sh --strict`. Rakennuksen on mentävä läpi virheittä.
- Kirjoita dokumentit sivustolle: määritelmä omaan lauseeseensa ja tärkeä kaava omalle rivilleen (`$$`). Älä ahda kaavoja luettelokohtiin. Älä käytä taulukon kaavoissa `|`-merkkiä, vaan `\lvert`/`\rvert`.
- Merkittävät tulokset kootaan `docs/tulokset.md`:hen.
- **Explainerit:** julkaistava sisältö tulee hakemistoon `docs/explainerit/` (`index.md` ensin). Sivusto lisää Explainerit-osion navigaatioon automaattisesti, joten `mkdocs.yml`:ää ei tarvitse muuttaa.
- **Videot:** YouTube, kanava Marko T. Manninen (`@markotmanninen`), soittolista *TGD Geometry Lab – explainerit* (`PLXsgqiwlSYA8`). Videot pidetään yksityisinä, kunnes Marko hyväksyy ne. Isoja videotiedostoja ei tallenneta repoon. Sivustolle video upotetaan YouTube-linkillä, mikä vaatii vähintään asetuksen *unlisted*.

## Seuranta
- Commit-viestiin `Closes #N`. Päivitä tilamerkintä (✅/🟡/⬜) `docs/kehityssuunnitelma.md`:hen ja `docs/seuranta.md`:n tilataulukkoon.

## Yhteistyö
- Projekti tehdään yhdessä Matti Pitkäsen kanssa. Hän on teoreettisen fysiikan tohtori ja on kehittänyt TGD:tä 1980-luvun alusta lähtien. **Ensin tutkitaan itse:** etsi vastaus Pitkäsen julkaisuista (arXiv, tgdtheory.fi, ResearchGate, matpitka.blogspot.com) ja vahvista se mahdollisuuksien mukaan testillä (esim. tunnettu numeroarvo). Matille kysytään vain se, mikä jää tutkimuksen jälkeen avoimeksi – Claude ei ratkaise TGD:n fysikaalista tulkintaa itse.
- Kun `päätös`-issue tarvitsee Matin linjausta, muotoile kysymys issueen niin, että Marko voi välittää sen sähköpostilla. Kun vastaus tulee, kirjaa se issueen ja `docs/konventiot.md`:hen ja lisää vastaava testi.

## Itsenäinen eteneminen ja päätöspisteet
- Etene milestone-järjestyksessä kriittistä polkua pitkin (`docs/seuranta.md`). Puhtaasti matemaattiset issuet (tunnettu identiteetti testinä) saa tehdä itsenäisesti.
- Issue, jolla on tunniste **`päätös`**, vaatii Markon valinnan tai materiaalin: tee esityö (vaihtoehdot, vertailulaskut), kirjaa ne issueen kommenttina ja **pysähdy** – älä valitse konventiota tai fysikaalista tulkintaa itse.
- Jos symbolinen lasku ei valmistu kohtuuajassa (> 10 min) tai vaatii arkkitehtuurimuutoksen, kirjaa havainto issueen ja kysy ennen suurta refaktorointia.
