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

## Teoria ja yhteistyö

TGD on [Matti Pitkäsen](https://tgdtheory.fi/) kehittämä teoria. Pitkänen on teoreettisen fysiikan tohtori, ja hän on kehittänyt teoriaa 1980-luvun alusta lähtien. Projektia tehdään yhdessä hänen kanssaan. Vastaukset haetaan ensin hänen julkaisuistaan, ja avoimeksi jäävät fysikaaliset kysymykset ratkaisee hän.

## Lanyon AI:n vaikutus

Työtapa on saanut vaikutteita [Lanyon AI](https://lanyon.ai/):sta, joka on Princetonissa toimiva tutkimusyhtiö. Sen perustajat ovat [Jonathan Gorard, Ammar Hakim ja Jimmy Juno](https://lanyon.ai/company/). Gorard on yhtiön toimitusjohtaja ja vastaa sen matemaattisesta suunnittelusta, ja hänet tunnetaan myös Wolfram Physics Projectin perustajajäsenenä.

Lanyonin [ilmoitettu tavoite](https://lanyon.ai/blog/welcome/) on muodollisesti verifioitu perusta, joka yhdistää tekoälyn fyysiseen maailmaan. Kielimalli ehdottaa muodollisen spesifikaation, ja puhtaasti symboliset algoritmit laajentavat siitä samalla koodin ja todistuksen. Jos spesifikaatiota ei voida todistaa oikeaksi, koodia ei synny. Yhtiön ensimmäiset kohdealueet ovat ilmailu- ja avaruustekniikka sekä ydinenergia.

Periaate on sama kuin tässä projektissa, sillä tulosta ei hyväksytä pelkän ehdotuksen perusteella, vaan deterministinen tarkistus ratkaisee. Keino on eri, koska tämä projekti käyttää automaattisia identiteettitestejä eikä muodollisia todistuksia.

Yhteistä on myös rajaus. Lanyonkin [toteaa](https://lanyon.ai/blog/welcome/), että todistus ei vielä kerro, vastaako spesifikaatio käyttäjän tarkoitusta. Samoin meidän testimme tarkistavat matematiikan, eivät TGD:n fysikaalista oikeellisuutta.

TGD ei kuulu Lanyonin ilmoitettuihin kohdealueisiin. Projekti hyödyntää sen julkaisemaa lähestymistapaa ja avointa [LanyonScripts](https://github.com/lanyonai/LanyonScripts)-koodia, joka on yhtiön tutkimusmuistioiden tietokonealgebraa.

## Ohjelmisto

Ohjelmakoodi, testit ja kirjat ovat avoimia [GitHubissa](https://github.com/markomanninen/tgd-geometry-lab). Laskenta tehdään Maximalla, ja Clifford-algebra tulee Dimiter Prodanovin [`clifford`](https://github.com/dprodanov/clifford)-paketista.
