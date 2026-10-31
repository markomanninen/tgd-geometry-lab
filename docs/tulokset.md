# Tulokset

<p class="lead">Tälle sivulle on koottu, mitä on laskettu ja mitä siitä seuraa. Jokaista väitettä vastaa automaattinen testi, ja koko sarjan 283 testiä ajetaan jokaisesta muutoksesta.</p>

Merkinnät ja normalisoinnit ovat [konventioissa](konventiot.md). Lukuarvot on annettu säteellä $R^2=1$.

## Mitä tuli yllätyksenä

Kolme tulosta kannattaa lukea ensin, koska ne tarkentavat aiempaa käsitystä tai lukitsevat normalisoinnin.

**Massaton ekstremaali ei ole yleisessä muodossaan minimipinta.** Pitkäsen ansatsi on $s^k=f^k(u,v)$, ja lähteen mukaan massattomat ekstremaalit ovat minimipintoja "in their simplest form at least". Laskenta tarkentaa tätä. Yleinen $f^k(u,v)$ on Kähler-toiminnan ekstremaali, mutta kenttäyhtälöiden tilavuusosa ei häviä. Pitkäsen vastauksen mukaan ansatsi on johdettu puhtaalle Kähler-toiminnalle, ja toiminnalle $S_K+S_V$ sen korvaa holografia = holomorfia. Tulos on kohdassa [Ekstremaalit](#ekstremaalit).

**Kerroin $k=3$ tulee geometriasta.** Unitaarisessa kehyksessä $CP_2$:n spinoriyhteys on $S^+$-lohkossa täsmälleen $\mathrm{diag}(3iA,-3iA)$, kun $dA=J$. Leptonien kerroin $k=3$ kumoaa siis yhteyden kokonaan, ja yksi spinori on kovariantisti vakio. Tämä on TGD:n oikeakätinen neutriino.

**Holomorfisen pinnan Kähler-osa riippuu siitä, mikä Kähler-muoto toiminnassa on.** Lagrangen vuoputken molemmat kenttäyhtälöiden osat häviävät, ja Pitkäsen vastauksen mukaan se on oma ratkaisutyyppinsä. Holomorfisilla pinnoilla tilavuusosa häviää aina, mutta litteässä Hamilton–Jacobi-rakenteessa pelkkä $CP_2$:n Kähler-muoto ei anna yhtään Kähler-ekstremaalia, jolla on $w$-riippuvuus. Kun mukaan lisätään $M^4$:n poikittainen Kähler-muoto kertoimella $1$, Kähler-osa häviää kaikilla testatuilla pinnoilla. Pallomaisessa rakenteessa se häviää ilman $M^4$:n muotoa täsmälleen suoralle ja kartioleikkaukselle. Tulokset ovat kohdassa [Holografia = holomorfia](#holografia-holomorfia).

## $CP_2$:n geometria

Fubini–Study-metriikka johdetaan Kähler-potentiaalista $K=\log(1+\lvert z\rvert^2)$, ja TGD-normalisointi on lukittu Pitkäsen arvoon.

| Suure | Tulos |
|---|---|
| Einsteinin ehto | $\mathrm{Ric}=6g$ ($=6g/R^2$ yleisesti) |
| Skalaarikaarevuus | $R=24$ |
| Holomorfinen leikkauskaarevuus | $4$ |
| Tilavuus | $\mathrm{Vol}(CP_2)=\pi^2/2$ |
| Kähler-invariantti | $J_{kl}J^{kl}=4$ |
| CP₂-tyyppisen ekstremaalin toiminta | $S_K=\pi/(8\alpha_K)$ |
| Kähler-vuo | $\pi$ yli $CP_1$:n, $2\pi$ yli kartion $z^2=(z^1)^2$ |

Vuo toimii homologisena testinä, koska kartion aste on 2 ja sen vuo on siksi kaksinkertainen. Kaikki kolme karttaa on testattu, ja metriikka ja Kähler-muoto säilyvät jokaisessa karttasiirtymässä.

## Kehykset, yhteydet ja spinorit

Yhteys lasketaan kahdella riippumattomalla reitillä, pelkästä kehyksestä ja Christoffelin symboleista. Reitit antavat saman tuloksen $CP_2$:lla, koko avaruudessa $H$ ja Lorentz-signatuurissa. Torsio häviää, ja Cartanin kaarevuus täsmää koordinaateissa laskettuun Riemannin tensoriin.

Spinoreille on testattu:

- $D_\mu\gamma^\nu=0$ ja $\{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}$ kaarevalla metriikalla,
- Lichnerowicz-termi $\tfrac12\gamma^\mu\gamma^\nu F_{\mu\nu}=-R/4=-6$,
- holonomia unitaarisessa kehyksessä on $U(2)$:ssa,
- $S^+$:n vuo yli $CP_1$:n on $(k\pm3)/2$, joka on kokonaisluku täsmälleen parittomilla $k$.

Viimeinen kohta on syy, miksi $CP_2$ ei ole spin-monisto mutta kertoimet $k=1$ ja $k=3$ kelpaavat.

## Upotetut pinnat

Toinen perusmuoto $B^k{}_{\alpha\beta}$ ja keskikaarevuus $H^k$ on testattu tunnetuilla pinnoilla, myös kaarevassa ympäristössä ja indefiniitissä signatuurissa. Kompleksiset käyrät ovat minimipintoja, vaikka ne eivät olisi totaaligeodeettisia. Kartiolla $z^2=(z^1)^2$ on $B\ne0$ ja silti $H^k=0$.

Gaussin, Codazzin ja Riccin yhtälöt on tarkistettu symbolisesti, kaareva ympäristö $CP_2$ mukaan lukien. Ne tarkistavat, ettei pinnan sisäistä geometriaa ole sekoitettu ympäröivän avaruuden geometriaan.

## Kenttäyhtälöt

Kun $f=c_KJ_{\alpha\beta}J^{\alpha\beta}+c_V$, variaatio upotuskoordinaattien suhteen antaa

$$
\frac{\delta S}{\delta h^k}=-2\sqrt{|g|}\left[h_{kl}D_\alpha\left(T^{\alpha\beta}\partial_\beta h^l\right)+2c_K\,j^\beta J_{kl}\partial_\beta h^l\right],
$$

$$
T^{\alpha\beta}=\tfrac12 f g^{\alpha\beta}-2c_KJ^{\alpha}{}_{\gamma}J^{\beta\gamma},\qquad j^\beta=D_\alpha J^{\alpha\beta}.
$$

Kaava on tarkistettu vertaamalla sitä suoraan määritelmästä laskettuun arvoon $\partial L/\partial h^k-\partial_\alpha\,\partial L/\partial(\partial_\alpha h^k)$ eksplisiittisillä pinnoilla. Kertoimet $c_K$ ja $c_V$ ovat symbolisia, joten mitään etumerkkiä ei ole kiinnitetty.

## Ekstremaalit

Kähler-termi ja tilavuustermi on testattu erikseen. Kanoninen $M^4$ ja kosminen säie toteuttavat molemmat kaikilla kertoimilla. Massattomissa ekstremaaleissa ($u$ valon kaltainen, $x$ poikittainen, $w=x+iy$) tilanne on rikkaampi, kuten taulukosta näkyy.

| Ansatsi | Kähler-termi | Tilavuustermi |
|---|---|---|
| $s^k(u)$ | 0 | 0 |
| $s^k(u,x)$ mielivaltaisena | 0 | $\ne0$ |
| $z^1=\tan(x)\,e^{ia(u)}$ | 0 | 0 |
| holomorfinen $w$:ssä | $\ne0$ | 0 |

Toisella rivillä $T^{\alpha\beta}\propto k^\alpha k^\beta$ ja Kähler-virta on valon kaltainen, kuten Pitkänen kuvaa. Tilavuustermi ei silti häviä. Yksinkertaisin vastaesimerkki on $s^k=F^k(x)$. Silloin pinta on $M^3\times$ käyrä avaruudessa $\mathbb R_x\times CP_2$, ja se on minimaalinen vain, jos käyrä on geodeesi.

Kolmas rivi osoittaa, että $x$-riippuvuus on silti mahdollinen. Se on $CP_2$:n geodeesi, jonka suunta kääntyy $u$:n mukana, ja sillä $J_{ux}\ne0$ ja virta $j^v\ne0$.

Taulukon nolla tarkoittaa, että kyseisen termin Euler–Lagrange-osa häviää. Toiminnan arvon ei tarvitse olla nolla, ja Pitkäsen vastauksen mukaan ekstremaalille riittää juuri tämä. Koska kenttäyhtälöt ovat lineaarisia kertoimissa, minimipinta on toiminnan $S_K+S_V$ ekstremaali täsmälleen silloin, kun myös Kähler-osa häviää.

## Ratkaisugeneraattori

Moduuli `tgd/solutions.mac` ottaa pinnan syötteenä ja kertoo, häviääkö indusoitu Kähler-muoto $J$, häviääkö kenttäyhtälöiden Kähler-osa ja häviääkö niiden tilavuusosa. Yhtälöt ovat lineaarisia kertoimissa $c_K$ ja $c_V$, joten nämä kaksi osaa ratkaisevat pinnan kaikilla kertoimilla. $M^4$:n parametrointi ja $CP_2$:n funktiot ovat syötteitä, joten moduulilla voi tutkia myös H-H-muodon ulkopuolisia pintoja.

| Pinta | $J$ | Kähler-osa | Tilavuusosa |
|---|---|---|---|
| CP₂-tyyppinen, kaareva valon kaltainen käyrä | $\ne0$ | 0 | $\ne0$ |
| CP₂-tyyppinen, valon kaltainen geodeesi ja harmoninen parametri | $\ne0$ | 0 | 0 |
| $\xi^k$ holomorfisia $w$:ssä, litteä rakenne | $\ne0$ | $\ne0$ | 0 |
| sama, $J=J(CP_2)+J(M^4)$ | $\ne0$ | 0 | 0 |
| suora tai kartioleikkaus, pallomainen rakenne | $\ne0$ | 0 | 0 |
| muu holomorfinen pinta, pallomainen rakenne | $\ne0$ | $\ne0$ | 0 |
| Lagrangen pinta, muu kuin konformi kuvaus pallolle | 0 | 0 | $\ne0$ |
| Lagrangen pinta, konformi kuvaus pallolle | 0 | 0 | 0 |
| Pallosymmetrinen katenoidi | 0 | 0 | 0 |

**CP₂-tyyppiset ekstremaalit.** Pinta on $CP_2$, ja $M^4$-koordinaatit seuraavat valon kaltaista käyrää $m^k=f^k(s)$. Kähler-osa häviää kaikilla tällaisilla käyrillä. Tilavuusosa häviää vain, kun käyrä on geodeesi, mikä vastaa Pitkäsen toteamusta artikkelissa [*About Twistor Lift of TGD*](http://tgdtheory.fi/public_html/articles/hgrtwistor.pdf) (luku 4.2.2). Laskenta lisää tähän ehdon, jota lähde ei mainitse. Parametrin $s$ on oltava harmoninen funktio $CP_2$:lla, kuten $\mathrm{Re}\,z^1$ tai $\mathrm{Re}\,(z^1)^2$.

**Lagrangen pinta ja neliulotteinen $M^4$-projektio.** Olkoon $f(w)$ holomorfinen. Pinnan $CP_2$-koordinaatit ovat

$$
x^1=\frac{2\,\mathrm{Re}\,f}{1-\lvert f\rvert^2},\qquad x^2=\frac{2\,\mathrm{Im}\,f}{1-\lvert f\rvert^2},\qquad y^1=y^2=0,
$$

ja $M^4$-koordinaatit ovat pinnan parametrit. Reaalileikkaus $y^1=y^2=0$ on Lagrangen pinta, jonka metriikka on paikallisesti yksikköpallon metriikka, ja kaava kuvaa $f$:n stereografisena koordinaattina tälle pallolle. Siksi $J=0$, ja koska $f$ on konformi kuvaus, pinta on myös minimipinta. Ehto $\lvert f\rvert=1$ on vain kartan raja. Testit kattavat funktiot $f=w$, $f=w/2$ ja $f=w^2$. Keskikaarevuus $H^k=0$ on tarkistettu erikseen, ja konformisuuden rikkova vertailutapaus ei ole minimipinta.

Tämä on eksplisiittinen toteutus Pitkäsen ansatsista, jossa $(w,\bar w)$ riippuu Lagrangen pinnan $Y^2$ kompleksikoordinaateista ja kompleksirakenne tulee indusoidusta metriikasta (luku 4.3, kohta 5). Matemaattisesti tulos on odotettu, sillä holomorfisen kuvauksen kuvaaja on kompleksikäyrä Kähler-tulossa $\mathbb C\times S^2$, ja [tällaiset kuvaajat ovat minimaalisia](https://arxiv.org/abs/1904.00487). Poikkileikkauksen pinta-ala kasvaa määrällä $4\pi R^2$, kun $f=w$.

Pinta ei kuitenkaan voi olla muotoa $f_1=f_2=0$, jossa $f_i$ ovat analyyttisiä $CP_2$:n kompleksikoordinaateissa. Silloin $z^k(w)$ olisi holomorfinen, ja reaalileikkauksessa reaaliarvoinen holomorfinen funktio on vakio. Lagrangen vuoputki jää siis H-H-muodon ulkopuolelle, vaikka sen molemmat osat häviävät.

**Pallosymmetrinen katenoidi.** Kun $M^4$:ssä käytetään pallokoordinaatteja ja $CP_2$:ssa geodeesin kaaripituutta $\chi(r)$, Kähler-osa häviää kaikilla $\chi$, ja tilavuusosa supistuu yhtälöksi

$$
\frac{d}{dr}\left(\frac{r^2\chi'}{\sqrt{1+\chi'^2}}\right)=0,\qquad\text{eli}\qquad \chi'(r)=\frac{C}{\sqrt{r^4-C^2}}.
$$

Pinta on aika-akseli kertaa katenoidi avaruudessa $\mathbb R^3\times$ geodeesi, ja sen kaula on kohdassa $r^2=\lvert C\rvert$.

## Holografia = holomorfia

Pitkäsen muotoilussa pinta on juurijoukko $f_1=f_2=0$, jossa $f_i$ ovat analyyttisiä koordinaateissa $\xi^1,\xi^2,w$ ja valon kaltaisessa $u$:ssa. Generaattorin funktio `hh_sheets` ratkaisee juuret, ja jokainen juuri on yksi lehti. Esimerkiksi ehdot $(\xi^1)^2=w^2/4$ ja $\xi^2=(\xi^1)^2$ antavat kaksi lehteä, ja molemmat ovat minimipintoja. Täsmällinen muotoilu on [konventioissa](konventiot.md#holografia-holomorfia).

**Litteä rakenne.** Pitkäsen mukaan H-H-pinnat ovat minimipintoja ja minkä tahansa indusoituun geometriaan perustuvan toiminnan ekstremaaleja. Minimipintaominaisuus toteutuu kaikilla testatuilla pinnoilla. Kähler-osa ei sen sijaan häviä pelkällä $CP_2$:n Kähler-muodolla yhdelläkään pinnalla, jolla on $w$-riippuvuus. Pinnalla $\xi^1=w/2$ tensorisupistus $A=J^{\alpha}{}_{\gamma}J^{\gamma\beta}H^k_{\alpha\beta}$ on nolla, mutta virta on poikittainen, ja Pitkäsen ehdottama Lorentz-voiman ehto $j\times B=0$ ei päde.

Tämä ei ole yksittäisen esimerkin piirre. Lorentz-voiman häviäminen vaatii, että Fubini–Study-metriikan vetäisy on litteä, ja Calabin jäykkyyslauseen mukaan holomorfinen kuvaus kompleksiviivalta $CP_2$:een ei voi olla sellainen, ellei se ole vakio.

**$M^4$:n Kähler-muoto.** Kun Kähler-muotoon lisätään poikittainen osa $\varepsilon\,dx\wedge dy$, kenttäyhtälöiden Kähler-osa pinnalla $\xi^1=w/2$ kertautuu täsmälleen tekijällä

$$
(1-\varepsilon)^2.
$$

Arvolla $\varepsilon=1$ Kähler-osa häviää kaikilla viidellä testatulla pinnalla, joiden joukossa on $u$-riippuvia. Silloin testatulla pinnalla $\xi^1=w/2$ virta on nolla ja $J_{\alpha\beta}J^{\alpha\beta}=2$ on vakio. Erillisillä toimintatermeillä sama tapahtuu relatiivisella kertoimella $-1$, koska kummankin muodon Kähler-osa on näillä pinnoilla sama. Kertoimen arvo ja $J(M^4)$:n paikka toiminnassa ovat [kysymys Matille](https://github.com/markomanninen/tgd-geometry-lab/issues/35).

**Pallomainen rakenne.** Koordinaateissa $t\pm r$ ja $w$ pallolla $S^2$ tilanne on toinen, koska poikittainen metriikka on nyt kaareva. Pelkällä $CP_2$:n Kähler-muodolla Kähler-osa häviää, kun vetäisy on verrannollinen pallon metriikkaan. Yksinkertaisin esimerkki on suora

$$
\xi^1=w,\qquad\xi^2=0,
$$

jolla $j=0$, $J\ne0$ ja indusoitu metriikka on $\lvert g_{w\bar w}\rvert\propto(r^2+\tfrac14)\rho$. Toinen on kartioleikkaus

$$
\xi^1=\sqrt2\,w,\qquad\xi^2=w^2,
$$

jolla sama kerroin on $r^2+\tfrac12$. Calabin luokittelun mukaan muita ei ole, ja vertailupinnat $\xi^1=w^2$ ja $\xi^1=2w$ ovat vain minimipintoja. Näiden kahden pinnan $M^4$-projektio on neliulotteinen ja ne ovat molempien termien ekstremaaleja kaikilla kertoimilla.

## Säilymislait

Tarkistuksessa on mukana $H$:n kaikki 18 isometriaa eli neljä translaatiota, kuusi Lorentz-generaattoria ja kahdeksan värigeneraattoria. Ne säilyttävät sekä metriikan että Kähler-muodon, ja värigeneraattorit muodostavat $su(3)$-algebran.

Jokaiselle pinnalle pätee identiteetti $D_\alpha j^\alpha=2K^k\mathrm{Eq}_k$, joka on testattu myös pinnalla, joka ei ole ratkaisu. Virran säilyminen ei siis johdu siitä, että kaikki häviää.

Kaikki 18 virtaa säilyvät ratkaisuilla, joita ovat kanoninen $M^4$, kosminen säie ja ME $s^k(u)$. Yleisellä $s^k(u,x)$:llä Kähler-virrat säilyvät mutta tilavuusvirrat eivät, mikä vastaa ekstremaalitaulukon toista riviä. Massattoman ekstremaalin liikemäärävirta kulkee valon kaltaisen suunnan $k$ mukaan.

## Karakteristinen analyysi

Linearisoidut kenttäyhtälöt on kirjoitettu LanyonScriptsin `calcev`-tyyliin muotoon $\partial_tU+A\,\partial_xU=0$, ja $A$:n ominaisarvot ovat häiriön rintaman nopeudet. Vertailutapauksena Nambu–Goto-pinnan nopeudet ovat indusoidun metriikan valokartio.

| Tausta ja toiminta | Suunta | Nopeudet | Tyyppi |
|---|---|---|---|
| $M^4$, tilavuustermi mukana | mikä tahansa | $\pm1$ | hyperbolinen |
| $M^4$, pelkkä Kähler-toiminta | mikä tahansa | pääosa on nolla | degeneroitunut |
| kosminen säie | säikeen suuntaan | $\pm1$ | hyperbolinen, kun $c_V+2c_K\ne0$ |
| kosminen säie | säikeen poikki | $s^2=\dfrac{c_V-2c_K}{c_V+2c_K}$ | riippuu kertoimista |
| ME, pelkkä tilavuustermi | $k$:ta vastaan kohtisuoraan | indusoidun metriikan valokartio | hyperbolinen |
| ME, pelkkä Kähler-toiminta | $k$:n suuntaan | $s=1$ seitsenkertaisena | heikosti hyperbolinen |
| ME, pelkkä Kähler-toiminta | poikittain ($x$) | $s=0$ kuusinkertaisena | |

Kaksi riviä kannattaa nostaa esiin.

Kosmisen säikeen poikki nopeuden neliö voi olla negatiivinen. Pelkällä Kähler-toiminnalla $s^2=-1$, ja yhtälön tyyppi on elliptinen. Kertoimien suhde ja etumerkki ratkaisevat siis yhtälön tyypin tällä taustalla. Pitkäsen mukaan etumerkki ei näy H-H-pintojen kenttäyhtälöissä, mutta kosmisen säikeen $M^4$-projektio on kaksiulotteinen, joten säie ei kuulu H-H-muotoon. Jos magneettinen osa ja tilavuusosa ovat erimerkkisiä myös tässä konventiossa, eli $c_K/c_V<0$, kaava antaa joko $s^2>1$ tai $s^2<0$. Tämä on kysymys [#35](https://github.com/markomanninen/tgd-geometry-lab/issues/35):ssä.

Pelkkä Kähler-toiminta on $M^4$:n ympärillä degeneroitunut ja ME-taustalla heikosti hyperbolinen. Tämä on sopusoinnussa tunnetun Kähler-toiminnan tyhjiödegeneraation kanssa, mutta tulkinta on Pitkäsen.

Tulokset koskevat yhtälön pääosaa yhdessä pisteessä. Ne eivät vielä kerro ratkaisujen stabiiliudesta.

Kuvat ovat kirjassa [Numeriikka ja kuvat](notebooks/04_numeriikka_ja_kuvat.ipynb).

## Avoimet kysymykset

Pitkäsen vastaukset 31.10.2026 ratkaisivat massattoman ekstremaalin aseman, H-H:n muodon ja tilavuustermin merkityksen kenttäyhtälöille. Laskennan perusteella jäljellä on seuraava kysymys ([#35](https://github.com/markomanninen/tgd-geometry-lab/issues/35)):

- Mikä on $J(M^4)$:n paikka ja kerroin toiminnassa, jotta holomorfiset pinnat ovat litteässä Hamilton–Jacobi-rakenteessa myös Kähler-ekstremaaleja?
