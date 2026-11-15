# Kosmologiset laskut

Tämä sivu kokoaa kaksi Matti Pitkäsen kanssa marraskuussa 2026 käytyä laskua. Ensimmäinen koskee kosmologista minimipintaa ja toinen kosmologisen vakion p-adista portaikkoa. Kummankin laskun tarkistukset ovat labin Maxima-testeinä, ja tällä sivulla laskut on kirjoitettu auki.

## Kosmologinen minimipinta

### Yrite

Pitkänen ehdotti 15.11.2026, että kosmologisia ratkaisuja voisi saada minimipintoina. Upotusavaruutena on $M^4\times S^1$, jossa $S^1$ on $CP_2$:n geodeettinen ympyrä, jonka säde on $R$ ja koordinaatti $\Phi$. Avaruudessa $M^4$ käytetään tulevaisuuden valokartion Robertsonin–Walkerin koordinaatteja, joissa $a$ on valokartion ominaisaika ja $H^3$ on yksikkösäteinen hyperbolinen avaruus. Ympäristön metriikka on

$$
ds^2=da^2-a^2\,d\Omega_{H^3}^2-R^2\,d\Phi^2 .
$$

Pinta on $\Phi=f(a)$, ja sen indusoitu metriikka on

$$
ds^2=\left(1-R^2f'^2\right)da^2-a^2\,d\Omega_{H^3}^2 .
$$

### Minimipintaehto

Pinta on viisiulotteisen avaruuden $M^4\times S^1$ hyperpinta, joten sillä on yksi normaalisuunta. Siksi funktion $f$ Eulerin–Lagrangen yhtälö on koko minimipintaehto. Geodeettinen ympyrä on täysin geodeettinen alimonisto, joten minimipinta avaruudessa $M^4\times S^1$ on minimipinta myös avaruudessa $H=M^4\times CP_2$.

Tilavuus on $H^3$:n tilavuusalkiota vaille

$$
\int a^3\sqrt{1-R^2f'^2}\;da .
$$

Koordinaatti $\Phi$ ei esiinny lausekkeessa, joten ympyrän kiertoa vastaava virta säilyy. Virta on $J^a=\sqrt{|g|}\,g^{aa}\,\partial_a\Phi$ kerrottuna ympyrän metriikalla, ja säilymislaki on

$$
\frac{a^3R^2f'}{\sqrt{1-R^2f'^2}}=C .
$$

Nimittäjässä on neliöjuuri, koska $\sqrt{|g|}=a^3\sqrt{1-R^2f'^2}$ ja $g^{aa}=1/(1-R^2f'^2)$ jättävät nimittäjään yhden neliöjuuren. Pitkäsen viestin muodossa neliöjuuri puuttuu, ja testi näyttää, että se muoto ei anna minimipintaa.

### Ratkaisu

Merkitään

$$
k=\frac{C}{Ra^3}.
$$

Säilymislaki ratkeaa muotoon

$$
Rf'=\frac{k}{\sqrt{1+k^2}},
$$

ja silloin

$$
g_{aa}=\frac{1}{1+k^2}=\frac{R^2a^6}{C^2+R^2a^6}.
$$

Labin testi laskee pinnan toisen perusmuodon ja keskikaarevuuden suoraan upotuksesta ja vahvistaa, että keskikaarevuus häviää jokaiseen suuntaan tällä ratkaisulla.

### Mitä ratkaisusta seuraa

Suurilla $a$:n arvoilla $Rf'\approx C/(Ra^3)$, joten Pitkäsen arvio käyttäytymisestä $1/a^3$ pitää.

Komponentti $g_{aa}$ on positiivinen kaikilla $a>0$. Pinta pysyy siis Lorentzin signatuurissa koko matkan, ja metriikka degeneroituu vasta rajalla $a\to0$, jossa $g_{aa}$ käyttäytyy kuten $a^6$.

Euklidinen haara, jossa $1-R^2f'^2<0$, on oma ratkaisunsa

$$
Rf'=\frac{k}{\sqrt{k^2-1}} .
$$

Se on olemassa vain, kun $k>1$ eli $a<a_0=(C/R)^{1/3}$, ja kohdassa $a_0$ siinä $f'$ kasvaa äärettömäksi. Lorentzin haaralla on samassa kohdassa $Rf'=1/\sqrt2$. Haarat eivät siis liity jatkuvasti, eikä signatuurin vaihto kohdassa $a_0$ seuraa tästä yhdestä pinnasta.

Kosminen aika on $\tau=\int\sqrt{g_{aa}}\,da$. Pienillä $a$:n arvoilla $\sqrt{g_{aa}}\approx Ra^3/C$, joten

$$
\tau\approx\frac{Ra^4}{4C},\qquad a\propto\tau^{1/4} .
$$

Suurilla $a$:n arvoilla $a\approx\tau$, eli ratkaisu lähestyy tyhjää Milnen kosmologiaa, ja poikkeama siitä pienenee kuten $1/a^6$.

### Tilavuustermin energiatiheys

Pitkänen arvioi 15.11.2026, että tilavuustermin energiatiheys käyttäytyy kuten $\cosh\eta/a^3$. Energia on $M^4$:n aikasiirron säilyvä varaus. Valokartion koordinaateissa aikakoordinaatti on $m^0=a\cosh\eta$, jossa $\eta$ on $H^3$:n hyperbolinen kulma, joten $\partial_a m^0=\cosh\eta$. Tilavuustermin Noetherin virran $a$-komponentti on $H^3$:n kulmatekijää vaille

$$
\sqrt{|g|}\,g^{aa}\,\partial_a m^0=\frac{a^3\cosh\eta}{\sqrt{g_{aa}}} .
$$

Kun virta jaetaan $H^3$:n tilavuustekijällä $a^3$, ratkaisulle saadaan energiatiheys

$$
\rho_V=\cosh\eta\,\frac{\sqrt{C^2+R^2a^6}}{Ra^3} .
$$

Pienillä $a$:n arvoilla $\rho_V\approx C\cosh\eta/(Ra^3)$, joten tiheys laimenee kuten aineen dominoimassa kosmologiassa ja divergoi rajalla $a\to0$. Suurilla $a$:n arvoilla $\rho_V\to\cosh\eta$, eli tiheys lähestyy vakiota samalla, kun ratkaisu lähestyy Milnen kosmologiaa. Kähler-termi ei osallistu, koska indusoitu Kähler-muoto on kaksimuoto ja yhden funktion $\Phi=f(a)$ kautta indusoituna se häviää.

Laimeneminen kuten $1/a^3$ on sama kuin pölyllä, mutta laajenemislaki on eri. Einsteinin teoriassa pöly antaa $a\propto\tau^{2/3}$, kun tämä pinta antaa pienillä $a$:n arvoilla $a\propto\tau^{1/4}$. Pinnan laajenemisen määrää minimipintaehto eikä Einsteinin yhtälö.

Tarkistukset ovat tiedostossa [tests/test-cosmo-minimal.mac](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-cosmo-minimal.mac).

## Kosmologisen vakion portaikko

### Lähtökohta

Twistorinostossa tilavuustermin kerroin tulee twistoripallosta. Labin aiemmassa laskussa pallokimpun kaarevuusskalaarin vakio-osa antaa

$$
\Lambda=\frac{1}{R_{cd}^2-r_C^2},
$$

joten suurella $R_{cd}$:llä $\Lambda\approx1/R_{cd}^2$. Pitkäsen mukaan $\Lambda$ on kääntäen verrannollinen p-adisen pituusskaalan neliöön dimensiosyistä. Laskussa käytetään p-adisia pituusskaaloja

$$
L(k)=2^{(k-151)/2}\,L(151),\qquad L(151)=10\ \text{nm},
$$

ja havaittu arvo on Planckin vuoden 2018 mittauksesta $\Lambda=1{,}1056\cdot10^{-52}\ \mathrm{m^{-2}}$.

### Tulokset

| Porras $k$ | $\Lambda=1/L(k)^2$ havaittuun verrattuna |
|---|---|
| 373, alkuluku | 13,4 |
| 376,8 | 1, havaittu arvo |
| 377, oktaavi alkuluvun 379 alapuolella | 0,84 |
| 379, alkuluku | 0,210 |

Pitkäsen mukaan pituusskaalassa on noin 9,5 prosentin epätarkkuus, koska elektronin massan ennuste on välillä $[1,\sqrt{6/5}]$ kertaa minimimassa. $\Lambda$ riippuu pituuden neliöstä, joten sen epätarkkuus on noin 20 prosenttia. Pitkäsen tulkinnassa havaittu skaala on oktaavin pienempi kuin alkulukua 379 vastaava, eli porras $k=377$, mikä vastaa periodin kahdentumista samaan tapaan kuin välibosonien massaskaala hänen [massalaskuissaan](https://tgdtheory.fi/public_html/Martin3.pdf). Porras 377 antaa 0,84 kertaa havaitun arvon, joten havainto osuu epätarkkuuden sisään.

Pitkäsen mittakaava-argumentin mukaan havaittu $\Lambda$ kuuluu havaittavan maailmankaikkeuden kokoskaalaan. Hubblen pituudella $c/H_0$ saadaan

$$
\Lambda\approx\left(\frac{H_0}{c}\right)^2=5{,}3\cdot10^{-53}\ \mathrm{m^{-2}},
$$

mikä on 0,48 kertaa havaittu arvo. Kerroin on $1/(3\Omega_\Lambda)$, joten sisältö on suuruusluokka. Naiivi tyhjöenergia-arvio Planckin rajalla on noin $10^{123}$ kertaa havaittu.

Tarkistukset ovat tiedostossa [tests/test-cosmological-lambda.mac](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-cosmological-lambda.mac).
