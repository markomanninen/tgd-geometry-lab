# TGD Geometry Lab

<p class="lead">Symbolinen laskentaympäristö, jolla Topological Geometrodynamics -teorian geometria lasketaan ja tarkistetaan vaihe vaiheelta upotusavaruudesta kenttäyhtälöihin.</p>

Topological Geometrodynamics (TGD) kuvaa aika-avaruuden neliulotteisena pintana kahdeksanulotteisessa avaruudessa $H=M^4\times CP_2$. Teorian yhtälöt ovat pitkiä, ja käsin laskettaessa etumerkit ja normalisoinnit menevät helposti vikaan. Tämä projekti laskee ne Maximalla ja hyväksyy tuloksen vasta, kun se läpäisee automaattisen tarkistuksen tunnettua identiteettiä tai vertailuarvoa vasten.

Laskenta ei todista TGD:tä fysikaalisesti oikeaksi. Se tarkistaa johdoksia ja tuo näkyviin seurauksia, joita olisi työlästä löytää käsin.

## Mistä aloittaa

| Sivu | Sisältö |
|---|---|
| [Tulokset](tulokset.md) | Mitä on laskettu ja varmistettu, sekä avoimet kysymykset |
| [Konventiot](konventiot.md) | Etumerkit, normalisoinnit ja indeksijärjestykset, joihin kaikki laskut nojaavat |
| [Kehityssuunnitelma](kehityssuunnitelma.md) | Vaiheet I–VIII ja välitavoitteet M1–M8 |
| [Seuranta](seuranta.md) | Nykyinen tila, päätöspisteet ja työnkulku |
| [Laskentakirjat](notebooks/01_ymparisto_ja_testit.ipynb) | Valmiiksi ajetut Colab-kirjat tulosteineen |

## Laskentaketju

$$
\text{upotusavaruus}\to\text{geometria}\to\text{muodot}\to\text{yhteydet}\to\text{kaarevuus}\to\text{toiminta}\to\text{kenttäyhtälöt}\to\text{ratkaisut}
$$

Ketju on laskettu ja testattu kenttäyhtälöihin asti, ja ensimmäiset tunnetut ratkaisut on tarkistettu. Ratkaisuanalyysi on seuraava vaihe.

## Tekijät ja lähteet

Projektia tehdään yhdessä Matti Pitkäsen (TGD:n kehittäjä) ja Tuomas Sorakiven kanssa. Ohjelmakoodi, testit ja kirjat ovat avoimia [GitHubissa](https://github.com/markomanninen/tgd-geometry-lab). Clifford-algebra tulee Dimiter Prodanovin [`clifford`](https://github.com/dprodanov/clifford)-paketista, ja rakenne seuraa [LanyonScriptsin](https://github.com/lanyonai/LanyonScripts) mallia.
