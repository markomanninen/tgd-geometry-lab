# TGD Geometry Software Lab – ohjeet agentille

Projekti tekee symbolista differentiaaligeometriaa Maximalla TGD:lle. Dokumentit ja issuet kirjoitetaan suomeksi ja koodikommentit englanniksi.

## Ennen muutoksia
- Lue `docs/konventiot.md` (etumerkit, normalisoinnit, indeksijärjestys). Kun muutat konventiota, päivitä testit ja dokumentti samassa muutoksessa.
- Tehtävät ovat GitHub-issueita ja milestoneja M1–M8 (`docs/seuranta.md`). Työskentele issuen "Valmis kun" -ehtoa vastaan.

## Paikallinen ympäristö (macOS)
- Asenna Maxima komennolla `brew install maxima` (5.50) ja kloonaa Prodanovin clifford repon viereen hakemistoon `../clifford`.
- Lisää Homebrew polkuun komennolla `export PATH=/opt/homebrew/bin:$PATH`.
- Maxima 5.50 käyttää hakupolkumalleissa merkkejä `###` ja vanhemmat versiot merkkejä `$$$`, joten lataa paketit täydellä polulla (`tgd_load_clifford`).

## Testit
- Aja testit komennolla `./scripts/run_tests.sh ../clifford`, jossa Prodanovin clifford-checkout on valinnainen. Kaikkien testien on mentävä läpi ennen committia.
- Kirjoita uudelle ominaisuudelle ensin testi tunnetulla identiteetillä tai vertailuarvolla (`tests/test-*.mac`, `check(nimi, ehto)`) ja lisää tiedosto `tests/run-all.mac`:n listaan.
- Maxima 5.46:sta puuttuu `getenv`, joten anna polut muuttujina (`tgd_root`, `clifford_path`). Nimi `rules` on varattu, joten käytä muuttujille muita nimiä.
- Yhdistelmäargumentit kuten `f(t-z)` derivoituvat ketjusäännöllä epäluotettavasti, joten käytä `depends`-määrittelyä ja sopivia parametreja (vrt. valokartiokoordinaatit testissä).

## Rakenne
- Moduulit ladataan `tgd-lab.mac`:ssa, ja uusi moduuli lisätään sinne.
- Generoi Colab-kirjat komennolla `python3 scripts/build_notebooks.py` ja aja ne sitten (`jupyter nbconvert --execute --inplace`, `TGD_ROOT`, `CLIFFORD_PATH`, `RUN_LANYON=0`). Tarkista lopuksi, että tulosteissa on vain yleisiä polkuja.

## Sivusto
- Julkinen sivusto on osoitteessa <https://markomanninen.github.io/tgd-geometry-lab/> (MkDocs Material, MathJax). `docs/` on sen sisältö, ja `.github/workflows/pages.yml` julkaisee sen `main`-haarasta.
- Rakenna sivusto paikallisesti komennoilla `pip install -r docs/requirements.txt` ja `./scripts/build_site.sh --strict`. Rakennuksen on mentävä läpi virheittä.
- Kirjoita dokumentit sivustolle. Jokainen määritelmä saa oman lauseensa, ja tärkeä kaava saa oman rivinsä (`$$`). Kirjoita kaavat tekstiin tai omille riveilleen, ja pidä luettelokohdat lyhyinä sanallisina kohtina.
- Kirjoita kokonaisia, sujuvia virkkeitä. Kun ajatus vaatisi puolipisteen, jaa se kahdeksi virkkeeksi tai yhdistä se konjunktiolla. Käytä kaksoispistettä vain listalohkon edellä, ja kirjoita otsikot, taulukon solut ja lihavoidut aloitukset ilman sitä. Suomen taivutuskaksoispiste (`CP2:n`) on eri asia. Sääntö koskee myös explainerien tekstejä, sähköposteja ja issueita. Kirjoita taulukon kaavoissa itseisarvon viivat merkinnöillä `\lvert` ja `\rvert`.
- Merkittävät tulokset kootaan `docs/tulokset.md`:hen.
- Julkaistavat explainerit tulevat hakemistoon `docs/explainerit/`, ja `index.md` on niistä ensimmäinen. Sivusto lisää Explainerit-osion navigaatioon automaattisesti, joten `mkdocs.yml` pysyy ennallaan.
- Videot julkaistaan YouTubessa kanavalla Marko T. Manninen (`@markotmanninen`) soittolistalla *TGD Geometry Lab – explainerit* (`PLXsgqiwlSYA8`). Uusi video ladataan yksityisenä, ja Marko päättää julkisuusasetuksen. Tekstitys ladataan YouTube Studiossa (*Kielet* → *Muokkaa tekstityksiä* → *Lähetä tiedosto*), koska latausskriptin tunnuksella ei ole tekstitysoikeutta. Isot videotiedostot säilytetään repon ulkopuolella. Sivustolle video upotetaan YouTube-linkillä, mikä vaatii vähintään asetuksen *unlisted*.

## Seuranta
- Kirjoita commit-viestiin `Closes #N`. Päivitä tilamerkintä (✅/🟡/⬜) `docs/kehityssuunnitelma.md`:hen ja `docs/seuranta.md`:n tilataulukkoon.

## Yhteistyö
- Projekti tehdään yhdessä Matti Pitkäsen kanssa. Hän on teoreettisen fysiikan tohtori ja on kehittänyt TGD:tä 1980-luvun alusta lähtien. Tutki ensin itse. Etsi vastaus Pitkäsen julkaisuista (arXiv, tgdtheory.fi, ResearchGate, matpitka.blogspot.com) ja vahvista se mahdollisuuksien mukaan testillä, esimerkiksi tunnetulla numeroarvolla. Matilta kysytään vain se, mikä jää tutkimuksen jälkeen avoimeksi, ja TGD:n fysikaalisen tulkinnan ratkaisevat Matti ja Marko.
- Kun `päätös`-issue tarvitsee Matin linjausta, muotoile kysymys issueen niin, että Marko voi välittää sen sähköpostilla. Kun vastaus tulee, kirjaa se issueen ja `docs/konventiot.md`:hen ja lisää vastaava testi.

## Itsenäinen eteneminen ja päätöspisteet
- Etene milestone-järjestyksessä kriittistä polkua pitkin (`docs/seuranta.md`). Puhtaasti matemaattiset issuet, joissa tunnettu identiteetti toimii testinä, saa tehdä itsenäisesti.
- Issue, jolla on tunniste **`päätös`**, vaatii Markon valinnan tai materiaalin. Tee esityö (vaihtoehdot, vertailulaskut), kirjaa se issueen kommenttina ja pysähdy, jotta Marko valitsee konvention tai fysikaalisen tulkinnan.
- Jos symbolinen lasku kestää yli 10 minuuttia tai vaatii arkkitehtuurimuutoksen, kirjaa havainto issueen ja kysy ennen suurta refaktorointia.
