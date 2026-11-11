# Tulokset

<p class="lead">Tälle sivulle on koottu, mitä on laskettu ja mitä siitä seuraa. Jokaista väitettä vastaa automaattinen testi, ja koko sarjan 419 testiä ajetaan jokaisesta muutoksesta.</p>

Merkinnät ja normalisoinnit ovat [konventioissa](konventiot.md). Lukuarvot on annettu säteellä $R^2=1$.

## Mitä tuli yllätyksenä

Kolme tulosta kannattaa lukea ensin, koska ne tarkentavat aiempaa käsitystä tai lukitsevat normalisoinnin.

**Massaton ekstremaali ei ole yleisessä muodossaan minimipinta.** Pitkäsen ansatsi on $s^k=f^k(u,v)$, ja lähteen mukaan massattomat ekstremaalit ovat minimipintoja "in their simplest form at least". Laskenta tarkentaa tätä. Yleinen $f^k(u,v)$ on Kähler-vaikutuksen ekstremaali, mutta kenttäyhtälöiden tilavuusosa ei häviä. Pitkäsen vastauksen mukaan ansatsi on johdettu puhtaalle Kähler-vaikutukselle, ja vaikutukselle $S_K+S_V$ sen korvaa holografia = holomorfia. Tulos on kohdassa [Ekstremaalit](#ekstremaalit).

**Kerroin $k=3$ tulee geometriasta.** Unitaarisessa kehyksessä $CP_2$:n spinoriyhteys on $S^+$-lohkossa täsmälleen $\mathrm{diag}(3iA,-3iA)$, kun $dA=J$. Leptonien kerroin $k=3$ kumoaa siis yhteyden kokonaan, ja yksi spinori on kovariantisti vakio. Tämä on TGD:n oikeakätinen neutriino.

**Holomorfisen pinnan Kähler-osa riippuu siitä, mikä Kähler-muoto vaikutuksessa on.** Lagrangen vuoputken molemmat kenttäyhtälöiden osat häviävät, ja Pitkäsen vastauksen mukaan se on oma ratkaisutyyppinsä. Holomorfisilla pinnoilla tilavuusosa häviää aina, mutta litteässä Hamilton–Jacobi-rakenteessa Lorentz 4-voima ei häviä yhdelläkään pinnalla, jolla on $w$-riippuvuus. Yhdellä summamuodolla $J(CP_2)+J(M^4)$ Kähler-osa häviäisi, mutta Pitkäsen linjauksen mukaan muodot ovat erilliset termit. Pallomaisessa rakenteessa Kähler-osa häviää ilman $M^4$:n muotoa täsmälleen suoralle ja kartioleikkaukselle. Tulokset ovat kohdassa [Holografia = holomorfia](#holografia-holomorfia).

## $CP_2$:n geometria

Fubini–Study-metriikka johdetaan Kähler-potentiaalista $K=\log(1+\lvert z\rvert^2)$, ja TGD-normalisointi on lukittu Pitkäsen arvoon.

| Suure | Tulos |
|---|---|
| Einsteinin ehto | $\mathrm{Ric}=6g$ ($=6g/R^2$ yleisesti) |
| Skalaarikaarevuus | $R=24$ |
| Holomorfinen leikkauskaarevuus | $4$ |
| Tilavuus | $\mathrm{Vol}(CP_2)=\pi^2/2$ |
| Kähler-invariantti | $J_{kl}J^{kl}=4$ |
| CP₂-tyyppisen ekstremaalin vaikutus | $S_K=\pi/(8\alpha_K)$ |
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

Taulukon nolla tarkoittaa, että kyseisen termin Euler–Lagrange-osa häviää. Vaikutuksen arvon ei tarvitse olla nolla, ja Pitkäsen vastauksen mukaan ekstremaalille riittää juuri tämä. Koska kenttäyhtälöt ovat lineaarisia kertoimissa, minimipinta on vaikutuksen $S_K+S_V$ ekstremaali täsmälleen silloin, kun myös Kähler-osa häviää.

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

**Litteä rakenne.** Pitkäsen mukaan H-H-pinnat ovat minimipintoja ja minkä tahansa indusoituun geometriaan perustuvan vaikutuksen ekstremaaleja. Minimipintaominaisuus toteutuu kaikilla testatuilla pinnoilla. Kähler-osa ei sen sijaan häviä pelkällä $CP_2$:n Kähler-muodolla yhdelläkään pinnalla, jolla on $w$-riippuvuus. Pinnalla $\xi^1=w/2$ tensorisupistus $A=J^{\alpha}{}_{\gamma}J^{\gamma\beta}H^k_{\alpha\beta}$ on nolla, mutta virta on poikittainen, eikä Lorentz 4-voima häviä.

Pitkäsen mukaan poikittaisen virran ei tarvitse hävitä, koska riittää, että Lorentz 4-voima häviää, ja H-H takaa tämän. Se laskettiin suoraan koko pintaluokalle $\xi^k=f^k(u,w)$. Virralla ei ole $u$-komponenttia, ja voimalle pätee $f_v=0$, $f_x=-j^yJ_{xy}$ ja $f_y=j^xJ_{xy}$. Voima häviää siis täsmälleen, kun poikittainen virta häviää. Sama ehto seuraa topologisoidusta virrasta ja virran valon kaltaisuudesta, koska instantonivirralla on tällä pintaluokalla vain $v$-komponentti ja $j^\alpha j_\alpha\propto(j^x)^2+(j^y)^2$.

Poikittaisen virran häviäminen vaatii, että Fubini–Study-metriikan vetäisy on litteä. Holomorfinen kuvaus kompleksiviivalta $CP_2$:een ei voi olla sellainen, ellei se ole vakio, ja [konventioissa](konventiot.md#kahler-osa-h-h-pinnoilla) on tälle suora rangilasku. Tulos tunnetaan Calabin jäykkyyslauseena, joka on eri lause kuin Calabi–Yau-lause, ja se koskee kuvan käyrää $CP_2$:ssa eikä nelipintaa. NeuroPaja toisti virran laskun hilalla ilman Maxima-kirjastoa, ja [arvot](sivututkimus/regge-teitelboim.md#matin-toinen-viesti-1112026) ovat samat kuin symbolisessa laskussa. Pitkänen vahvisti 1.11.2026 virran toisen termin ja johti kenttäyhtälön Kähler-osalle muodon $j^\alpha X^k_{\ \alpha}$. Lasku vahvistaa rakenteen testatuilla holomorfisilla minimipinnoilla, ja [ehto](sivututkimus/regge-teitelboim.md#matin-vastaus-viiteen-kysymykseen) ei täyty niillä automaattisesti. Hänen [linjauksensa](sivututkimus/regge-teitelboim.md#matin-linjaus-sisaosan-vaikutuksesta) 1.11.2026 oli, että lisäehtoja ei tuoda, sisäosan vaikutus on tilavuustermi ja Kähler–Chern–Simons-vaikutus on vain partonipinnoilla. Hän ehdotti 3.11.2026 lisäehtoa, jossa $CP_2$:n Kähler-funktio toteuttaa poikittaisen Laplacen yhtälön. NeuroPajan laskussa tämä ehto on sama kuin litteän vetäisyn ehto, joten se sallii holomorfisilla pinnoilla vain riippumattomuuden koordinaatista $w$. Vaihtoehtoja verrataan sivulla [Sisäosan vaikutus](sivututkimus/sisaosan-vaikutus.md).

**$M^4$:n Kähler-muoto.** Kun Kähler-muotoon lisätään poikittainen osa $\varepsilon\,dx\wedge dy$, kenttäyhtälöiden Kähler-osa pinnalla $\xi^1=w/2$ kertautuu täsmälleen tekijällä

$$
(1-\varepsilon)^2.
$$

Arvolla $\varepsilon=1$ Kähler-osa häviää kaikilla viidellä testatulla pinnalla, joiden joukossa on $u$-riippuvia. Silloin testatulla pinnalla $\xi^1=w/2$ virta on nolla ja $J_{\alpha\beta}J^{\alpha\beta}=2$ on vakio. Pitkäsen linjaus on kuitenkin, että $J(M^4)$ ja $J(CP_2)$ ovat vaikutuksessa erilliset termit. Julkaistuna ratkaisu on artikkelissa Martin2 partoniratojen Kähler–Chern–Simons-vaikutukselle. Koska kummankin muodon Kähler-osa on testatuilla pinnoilla sama, kokonaisosa on kertoimien summa kerrottuna tällä osalla. Molemmat kertoimet ovat etumerkkisääntöjen mukaan positiivisia, joten osa ei häviä näillä pinnoilla. Tämä kuuluu [jatkokysymykseen Matille](https://github.com/markomanninen/tgd-geometry-lab/issues/35).

**Pallomainen rakenne.** Koordinaateissa $t\pm r$ ja $w$ pallolla $S^2$ tilanne on toinen, koska poikittainen metriikka on nyt kaareva. Pelkällä $CP_2$:n Kähler-muodolla Kähler-osa häviää, kun vetäisy on verrannollinen pallon metriikkaan. Yksinkertaisin esimerkki on suora

$$
\xi^1=w,\qquad\xi^2=0,
$$

jolla $j=0$, $J\ne0$ ja indusoitu metriikka on $\lvert g_{w\bar w}\rvert\propto(r^2+\tfrac14)\rho$. Toinen on kartioleikkaus

$$
\xi^1=\sqrt2\,w,\qquad\xi^2=w^2,
$$

jolla sama kerroin on $r^2+\tfrac12$. Calabin luokittelun mukaan muita ei ole, ja vertailupinnat $\xi^1=w^2$ ja $\xi^1=2w$ ovat vain minimipintoja. Näiden kahden pinnan $M^4$-projektio on neliulotteinen ja ne ovat molempien termien ekstremaaleja kaikilla kertoimilla. Ne kantavat Kähler-vuon $\pi$ ja $2\pi$ jokaisen pallon läpi, ja niillä $M^4$:n ja $CP_2$:n Kähler-osat häviävät erikseen, kun $J(M^4)$ on pallon pintamuoto. Suoran metriikka on sileä kohdassa $r=0$, jossa pallon säde on $1/2$. Pinnat kuuluvat Pitkäsen Martin3-artikkelin luokitteluun genuksen $0$ käyrinä tulossa $CP_1\times CP_2$, joiden aste pinnassa $CP_2$ on $1$ ja $2$.

**Valon suuntainen riippuvuus pallomaisessa rakenteessa.** Litteässä rakenteessa $u$-riippuvuus säilyttää minimipintaominaisuuden, mutta pallomaisessa rakenteessa ei. Pinnat $\xi^1=u$, $\xi^1=u+w$ ja kierretty suora $\xi^1=e^{ia(u)}w$ eivät ole siellä minimipintoja. Syy on tuttu aaltoyhtälöstä. Pallomainen aalto ei ole $f(t-r)$ vaan $f(t-r)/r$, koska valonsäteiden kimppu laajenee ja

$$
\Box f(t-r)=\frac{2f'(t-r)}{r}.
$$

Pitkänen pitää todennäköisenä, ettei $u=t-r$ riko minimipintaominaisuutta, ja pyysi tarkistamaan asian. Hänen artikkelissaan H-J-rakenteen ehto on $\{k\,w\bar w\}=0$, ja pallomaisessa rakenteessa juuri tämä ei päde, koska poikittainen metriikka riippuu $v$:stä.

**Laplacen ehto pallomaisessa rakenteessa.** Kun $\xi(u,w)$ on holomorfinen $w$:n suhteen, pinnan perimän Kähler-funktion Laplacen summa on

$$
(\partial_x^2+\partial_y^2)K(\xi)=4K_{i\bar j}\,\partial_w\xi^i\,\overline{\partial_w\xi^j},
$$

eli se on verrannollinen poikittaisen koordinaattineliön Kähler-lukuun alayksikköä kohti. Fubini–Study-metriikka on positiivisesti definiitti, joten Laplacen ehto koko säännöllisellä alueella jättää pallomaisessakin rakenteessa vain pinnat $\xi(u)$. Niiden $CP_2$-kuva on käyrä, joten Kähler-kenttä ja kenttäyhtälöiden Kähler-osa häviävät, ja kenttäyhtälöt vaativat minimipintaa. Keskikaarevuuden komponentti $H^\xi=2r\rho\,\xi_u/\Phi$ ei häviä siellä, missä $\xi_u\ne0$. Laplacen ehdon muodossa pallomaiseen rakenteeseen jäävät siis ratkaisuyritteen pinnoista vain vakiokuvaukset. Valon kaltaisen virran muodossa sinne jäävät lisäksi suora ja kartioleikkaus, joilla virta on nolla mutta Kähler-kenttä ei. Testit ovat tiedostossa [test-solutions.mac](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-solutions.mac).

Tulos on yleinen. Jos $u$:n ja $w$:n gradientit ovat keskenään valon kaltaisia, kaikki funktiot $F(u,w)$ ovat harmonisia täsmälleen, kun $\Box u=\Box w=0$. Bochnerin kaavan mukaan tasopinnat $u=$ vakio ovat silloin valon kaltaisia hypertasoja, ja ehto $\Box w=0$ pakottaa ne yhdensuuntaisiksi. Tällaisista rakenteista ainoa on siis litteä rakenne muunnoksia vaille.

**Kuinka paljon H-J-rakenteita on.** Funktioille $F(w)$ rakenteita on paljon enemmän. Keskenään valon kaltaisilla gradienteilla ne saadaan valokartioista, joiden kärki kulkee radalla $z(\tau)$, ja $w$ on säteen suunta. Tilavuusosa häviää symbolisesti mielivaltaisella radalla. Kähler-osa on tiukempi, sillä se häviää suoralle ja kartioleikkaukselle levossa olevalla kärjellä ja niiden Lorentz-muunnoksille mutta ei testatulla kiihtyvällä kärjellä. Valon kaltaisen gradientin säteet ovat suoria, joten Pitkäsen pohtimat käyräviivaiset säteet jäävät tämän luokan ulkopuolelle. Yksityiskohdat ovat [konventioissa](konventiot.md#mitka-hamiltonjacobi-rakenteet-kantavat-kaikki-holomorfiset-funktiot).

## Kaarevuusskalaari ja indusoidun geometrian vaikutukset

NeuroPaja laski 1.11.2026 tilavuuden, kaarevuusskalaarin ja vaikutuksen $\int R^2\sqrt{\lvert g\rvert}$ kenttäyhtälöt Hamilton–Jacobi-rakenteiden pinnoilla. Kaarevuusskalaarin kenttäyhtälö $G^{\alpha\beta}B^k_{\alpha\beta}=0$ on Pitkäsen johtama muoto, jolla on sama rakenne kuin Regge–Teitelboimin tyhjiöyhtälöllä.

Pallomaisessa rakenteessa kaikkien kolmen kenttäyhtälöt toteutuvat suoralla, kartioleikkauksella ja kuvauksella $S^2\to RP^2$. NeuroPajan päättelyn mukaan syy on symmetria, joten sama pätee jokaiselle indusoidusta geometriasta rakennetulle vaikutukselle. Litteässä rakenteessa kaarevuusskalaarin kenttäyhtälö toteutuu pinnoilla, jotka eivät riipu koordinaatista $v$, ja testatuilla holomorfisilla pinnoilla vaikutuksen $R^2$ kenttäyhtälö ei toteudu. Laskut, testit ja tulkintaa koskevat kysymykset ovat [sivututkimussivulla](sivututkimus/regge-teitelboim.md#osa-3-laskut).

NeuroPaja vertasi 2.11.2026 ehdokkaita R + tilavuus ja pelkkä tilavuus. Tuotepinnalla $M^2\times Y^2$ jännitys on $8GT=d\,\Lambda R_C^2-2\chi$, joten yksikkövuon säikeellä $T\to-1/(2G)$, kun $\Lambda$ on pieni ja vaikutuksessa on kaarevuusskalaari. Tulos koskee suljettuja tuotteita, sillä avoimella poikkileikkauksella jännitys tasoon verrattuna on $\Lambda R_C^2/8G$. Arvolla $\Lambda>K=4/R_C^2$ säikeen $M^2\times CP_1$ jännitys on positiivinen ja säie on lineaarisesti vakaa, koska kenttäyhtälön molemmat lohkokertoimet ovat silloin samanmerkkiset. Ehdokkaat eroavat pallomaisen rakenteen holomorfisilla pinnoilla. Pitkäsen 5.11.2026 esittämä syy tähän eroon on Einsteinin tensorin riippuvuus koordinaatista $v$, ja NeuroPajan laskussa pallomaisen rakenteen minimaalipinnalla $\xi=2w$ supistus $G^{ab}B^k{}_{ab}$ ei ole nolla, kun taas litteän rakenteen pinnalla $\xi=uw/3$ se on identtisesti nolla. Vaikutuksesta riippumaton tulos koskee jakoja. Jos partonipinnat ovat minimaalipintoja hyperboloideilla $a=$ vakio ja myös säiemaailmanpinnat ovat minimaalipintoja $M^4$:ssä, säiemaailmanpinnat ovat kartioita $H^3$:n geodeesien yli, partonipinnat ovat yhdensuuntaisia pintoja, ja Riccatin yhtälö $k'=1-k^2$ yhdessä Gaussin ja Codazzin yhtälöiden kanssa osoittaa, että tällaista jakoa ei ole. Avaruudessa $E^3$ vastaava jako koostuu vain yhdensuuntaisista tasoista. OpenAI:n Codex vahvisti päättelyn riippumattomasti. Vertailu, rajat ja avoimet kohdat ovat sivulla [Sisäosan vaikutus](sivututkimus/sisaosan-vaikutus.md#pitkasen-vastaukset-5112026).

NeuroPaja luokitteli 5.11.2026 $M^4$:n H-J-rakenteet paikallisesti. H-J-rakenne on sama asia kuin kaksi toisiaan vastaan kohtisuoraa lehditystä, joiden säieradat ja partonipinnat ovat kokonaan napaisia pintoja. Konformiryhmää vaille rakenteita on kolme, $E^{1,1}\times E^2$, $AdS_2\times S^2$ ja $dS_2\times H^2$. Poincarén muunnosta vaille rakenteet, joiden säieradat ovat tasoja, ovat litteä, pallomainen, horosfääri- ja tasoetäisyysrakenne. Kolmessa jälkimmäisessä valokartioiden kärki kulkee aikasuuntaista, valon kaltaista tai avaruussuuntaista suoraa pitkin. Kenttäyhtälöiden Kähler-osa häviää $w$:stä riippuvilla pinnoilla vain aikasuuntaisella suoralla, ja pallomainen rakenne on ainoa rakenne, jonka jokainen partonipinta on kausaalisen timantin kummankin kärjen hyperboloidilla. Napainen minimaalipinta on taso, joten säieradat ja partonipinnat ovat yhtä aikaa $M^4$:n minimaalipintoja vain litteässä rakenteessa, ja hyperboloidilla oleva partonipinta ei ole koskaan $M^4$:n minimaalipinta. Perustelut ovat konventioiden osiossa [H-J-rakenteiden luokittelu](konventiot.md#h-j-rakenteiden-luokittelu).

Pitkäsen ehdottamassa valokartion sisäosan viipaloinnissa partonipinnat ovat jokaisen hyperboloidin $H^3(\tau)$ totaalisesti geodeettisia tasoja $m^3=m^0\tanh s$. NeuroPajan 9.11.2026 laskun mukaan niitä vastaan kohtisuorat säiepinnat ovat kartioita sellaisten $H^3$:n käyrien yli, jotka pysyvät vakioetäisyydellä $d$ akselista. Kartion keskikaarevuuden pituus on $\tanh d/\tau$, joten säiepinta on $M^4$:n minimaalipinta vain akselilla. Laskut ovat [sivututkimussivulla](sivututkimus/sisaosan-vaikutus.md#artikkelin-viimeistely).

## Säilymislait

Tarkistuksessa on mukana $H$:n kaikki 18 isometriaa eli neljä translaatiota, kuusi Lorentz-generaattoria ja kahdeksan värigeneraattoria. Ne säilyttävät sekä metriikan että Kähler-muodon, ja värigeneraattorit muodostavat $su(3)$-algebran.

Jokaiselle pinnalle pätee identiteetti $D_\alpha j^\alpha=2K^k\mathrm{Eq}_k$, joka on testattu myös pinnalla, joka ei ole ratkaisu. Virran säilyminen ei siis johdu siitä, että kaikki häviää.

Kaikki 18 virtaa säilyvät ratkaisuilla, joita ovat kanoninen $M^4$, kosminen säie ja ME $s^k(u)$. Yleisellä $s^k(u,x)$:llä Kähler-virrat säilyvät mutta tilavuusvirrat eivät, mikä vastaa ekstremaalitaulukon toista riviä. Massattoman ekstremaalin liikemäärävirta kulkee valon kaltaisen suunnan $k$ mukaan.

## Karakteristinen analyysi

Linearisoidut kenttäyhtälöt on kirjoitettu LanyonScriptsin `calcev`-tyyliin muotoon $\partial_tU+A\,\partial_xU=0$, ja $A$:n ominaisarvot ovat häiriön rintaman nopeudet. Vertailutapauksena Nambu–Goto-pinnan nopeudet ovat indusoidun metriikan valokartio.

| Tausta ja vaikutus | Suunta | Nopeudet | Tyyppi |
|---|---|---|---|
| $M^4$, tilavuustermi mukana | mikä tahansa | $\pm1$ | hyperbolinen |
| $M^4$, pelkkä Kähler-vaikutus | mikä tahansa | pääosa on nolla | degeneroitunut |
| kosminen säie | säikeen suuntaan | $\pm1$ | hyperbolinen, kun $c_V+2c_K\ne0$ |
| kosminen säie | säikeen poikki | $s^2=\dfrac{c_V-2c_K}{c_V+2c_K}$ | riippuu kertoimista |
| ME, pelkkä tilavuustermi | $k$:ta vastaan kohtisuoraan | indusoidun metriikan valokartio | hyperbolinen |
| ME, pelkkä Kähler-vaikutus | $k$:n suuntaan | $s=1$ seitsenkertaisena | heikosti hyperbolinen |
| ME, pelkkä Kähler-vaikutus | poikittain ($x$) | $s=0$ kuusinkertaisena | |

Kaksi riviä kannattaa nostaa esiin.

Kosmisen säikeen poikki nopeuden neliö voi olla negatiivinen. Pelkällä Kähler-vaikutuksella $s^2=-1$, ja yhtälön tyyppi on elliptinen. Kertoimien suhde ja etumerkki ratkaisevat siis yhtälön tyypin tällä taustalla. Pitkäsen etumerkkisäännöistä seuraa $c_K>0$ ja $c_V>0$ ([konventiot](konventiot.md#kertoimien-etumerkki)), joten nopeus jää valon nopeuden alle ja $0<s^2<1$, kun $c_V>2c_K$. Jos magneettinen osa on suurempi, eli $c_V<2c_K$, kaava antaa $s^2<0$, jolloin häiriö kasvaa säikeen poikki. Pitkäsen mukaan magneettinen osa on kosmisilla säikeillä suuri ja säikeet ovat epästabiileja $M^4$-projektion paksuuntumiselle. Tulos näyttää sopivan tähän, mutta se koskee vain yhtälön pääosaa.

Pelkkä Kähler-vaikutus on $M^4$:n ympärillä degeneroitunut ja ME-taustalla heikosti hyperbolinen. Tämä on sopusoinnussa tunnetun Kähler-vaikutuksen tyhjiödegeneraation kanssa, mutta tulkinta on Pitkäsen.

Tulokset koskevat yhtälön pääosaa yhdessä pisteessä. Ne eivät vielä kerro ratkaisujen stabiiliudesta.

Kuvat ovat kirjassa [Numeriikka ja kuvat](notebooks/04_numeriikka_ja_kuvat.ipynb).

## Mannisen esseen kaavat vertailutesteinä

Marko Mannisen essee *Through the Wormhole on Spacetime Surface* (2024) esittää TGD:n vaikutuksen, indusoidun geometrian ja minimipintojen kenttäyhtälön kaavoina. NeuroPaja kävi kaavat läpi issuessa [#34](https://github.com/markomanninen/tgd-geometry-lab/issues/34) ja muotoili kustakin väitteen, jonka Maxima voi tarkistaa. Taulukon sivunumero viittaa esseeseen. Kaavat on luettu esseen tekstiversiosta, josta indeksien korkeudet ovat kadonneet, joten yläindeksit on päätelty asiayhteydestä.

| Sivu | Testattu väite | Testit |
|---|---|---|
| 18 | Einstein–Hilbert-vaikutuksen $\int R\sqrt{-g}\,d^4x$ variaatio antaa Einsteinin tensorin signatuurissa $(-,+,+,+)$. | [curvature](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-curvature.mac) |
| 21–23 | Riemannin tensorin kaava on sama kuin konventioissa, ja $G^{\mu\nu}$:n divergenssi häviää. | [curvature](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-curvature.mac), [cp2](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-cp2.mac), [curvature-action](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-curvature-action.mac) |
| 23 | Riemannin tensorilla on neljässä ulottuvuudessa 20 riippumatonta komponenttia, ja niistä 10 kuuluu Riccin tensorille. | [curvature](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-curvature.mac) |
| 32 | Tason $M^2$ imaginaariyksikön neliö on $+1$ ja tason $E^2$ imaginaariyksikön neliö on $-1$. | [embedding](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-embedding.mac) |
| 33 | Kokonaisvaikutus on Kähler-vaikutuksen ja tilavuusvaikutuksen summa $S=S_K+S_V$, joten kenttäyhtälöt ovat lineaarisia kertoimissa $c_K$ ja $c_V$. | [field-equations](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-field-equations.mac) |
| 33 | Summan arvo tunnetulla ratkaisulla on kosmisella säikeellä $\pi(2c_K+c_V)$ tason $M^2$ pinta-alayksikköä kohti. | [embedding](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-embedding.mac) |
| 33 | Kähler-vaikutuksen kerroin $1/(2\alpha_K)$ antaa $CP_2$:n yli arvon $\pi^2/\alpha_K$, ja Pitkäsen arvo $\pi/(8\alpha_K)$ vaatii kertoimen $1/(16\pi\alpha_K)$. | [cp2](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-cp2.mac) |
| 33 | $J_{\mu\nu}J^{\mu\nu}$ on skalaari, ja $\sqrt{\lvert g\rvert}\,d^4x$ säilyy parametrien vaihdossa. | [embedding](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-embedding.mac) |
| 34 | $g_{\alpha\beta}=h_{kl}\partial_\alpha h^k\partial_\beta h^l$ ja $J_{\alpha\beta}=J_{kl}\partial_\alpha h^k\partial_\beta h^l$ muuntuvat tensoreina, ja vertailuarvot ovat kanoninen $M^4$ ja kosminen säie. | [embedding](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-embedding.mac) |
| 34 | Muoto $J_{\alpha\beta}$ on antisymmetrinen ja suljettu. | [embedding](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-embedding.mac) |
| 34 | Tilavuustiheyden $\sqrt{\lvert g\rvert}$ kenttäyhtälö on $\tfrac12h_{kl}H^l=0$, joka on minimipintayhtälö. | [field-equations](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-field-equations.mac), [action](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-action.mac) |
| 35 | Instantonitermin tiheys $J\wedge J$ on kokonaisdivergenssi $d(A\wedge J)$. Sen variaatio antaa kenttäyhtälöihin nollan, ja integraali supistuu reunan Chern–Simons-termiksi. | [forms](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-forms.mac), [field-equations](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-field-equations.mac) |
| 35 | Valon kaltaisella 3-pinnalla $\det g=0$, joten käänteismetriikkaa ei ole. | [embedding](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-embedding.mac) |
| 35, 38 | Twistorinoston yksinkertaisimmassa tulomallissa 6-ulotteinen Kähler-vaikutus antaa neliulotteiset kenttäyhtälöt, joissa on tilavuustermi. | [field-equations](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-field-equations.mac) |
| 36 | Holomorfisella pinnalla jokainen tulo $g^{ab}B^k_{ab}$ häviää kompleksikannassa erikseen, ei vain summa. | [second-form](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-second-form.mac) |
| 36 | Säikeen maailmanpinta $s^k(u)$ on minimipinta, ja suora käyrä avaruudessa $H$ on geodeesi myös valon kaltaisena. | [second-form](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-second-form.mac) |
| 36 | Yhtälöistä $E_k$ vain neljä on riippumattomia, koska $E_k\partial_\alpha h^k=0$ pätee jokaisella pinnalla. | [field-equations](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-field-equations.mac) |
| 36 | Yang–Mills-analogian virta säilyy, eli $D_\beta j^\beta=0$ myös pinnalla, joka ei ole ratkaisu. | [field-equations](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-field-equations.mac) |
| 36 | Alaviitteen 33 divergenssi on $D_\alpha(G^{\alpha\beta}\partial_\beta h^k)=G^{\alpha\beta}B^k_{\alpha\beta}$. | [curvature-action](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-curvature-action.mac) |
| 38 | Lainauksen väite minimipinnoista ja indusoidun geometrian vaikutuksista on tarkistettu Hamilton–Jacobi-rakenteiden pinnoilla, ja tulos on osiossa Kaarevuusskalaari ja indusoidun geometrian vaikutukset. | [curvature-action](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-curvature-action.mac), [solutions](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-solutions.mac) |
| 40 | $CP_2=SU(3)/U(2)$, sillä $SU(3)$ toimii transitiivisesti ja isotropiaryhmän ulottuvuus on 4. Holonomian ulottuvuus on samoin 4. | [noether](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-noether.mac), [cp2](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-cp2.mac) |
| 40 | $CP_2$:lla ei ole tavallista spin-rakennetta, ja Kähler-kytkentä tekee vuosta kokonaisluvun. | [spinor](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-spinor.mac) |

Twistorinoston tulomalli on yksinkertaistus. Siinä pinta $X^6$ on neliulotteinen pinta kertaa pallo, ja yksi pallon piste kuvautuu samaan pisteeseen avaruuksien $T(M^4)$ ja $T(CP_2)$ pallotekijöissä. Mallissa kuusiulotteisen invariantin $J_{\alpha\beta}J^{\alpha\beta}$ pallo-osa on vakio. Kun vakio kerrotaan mittatekijällä $\sqrt{\lvert g\rvert}$, tulos on neliulotteisen pinnan tilavuustermi. Kertoimien suhteeksi tulee

$$
\frac{c_V}{c_K}=\frac{2(k_1+k_2)^2}{(r_1^2+r_2^2)^2},
$$

jossa $r_i$ ovat pallotekijöiden säteet ja $k_i$ niiden Kähler-muotojen kertoimet. Suhde $c_V/c_K$ on positiivinen, ja sama merkki seuraa [etumerkkisäännöistä](konventiot.md#kertoimien-etumerkki). Tulomalli ei kiinnitä suhteen lukuarvoa, koska säteet ja kertoimet ovat siinä vapaita. Todellisessa nostossa $X^6$ on pallokimppu eikä tulo.

## Lehtien kokoaminen ja Einsteinin raja

Pitkäsen resepti kokoaa lehdet yhteisissä $M^4$-koordinaateissa. Koottu metriikka on Minkowskin metriikka lisättynä lehtien poikkeamien summalla.

$$
g^{\mathrm{eff}}_{ab}=\eta_{ab}+\sum_i\bigl(g^{(i)}_{ab}-\eta_{ab}\bigr)
$$

Hänen tekstissään ([*Btgdclass1*](https://tgdtheory.fi/bookpdf/Btgdclass1.pdf), luku 7) testihiukkanen on madonreikäkontakti, joka koskettaa kaikkia lehtiä, joiden $M^4$-projektio osuu kohdalle. Einsteinin yhtälöstä hän kirjoittaa "could hold true for the effective metric", ja geodeesiliike on postulaatti "one can also postulate". Hän ei anna reseptiä kootun metriikan energia-liikemäärätensorille. Siksi NeuroPaja laski väitteen niiltä osin, jotka voi laskea ilman sitä. Testit ovat tiedostossa [test-effective-metric](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-effective-metric.mac).

**Yhden lehden ehto ei ole yleinen.** Vanhemmassa tekstissä Pitkänen ehdottaa jokaiselle ekstremaalille ehtoa $T=\kappa G+\Lambda g$. Lehti $CP_2$ toteuttaa sen, koska Kählerin Maxwell-tensori häviää ja $G^{ab}=-6\sigma g^{ab}$, jolloin $\Lambda=6\sigma\kappa$ ja $R=4\Lambda/\kappa=24\sigma$. Holomorfisella viivalla $G^{ab}$ ei ole verrannollinen metriikkaan, ja yhtälön ainoa ratkaisu on triviaali $\kappa=0$, $c_K=0$. Yhtälö kuuluu siis koottuun metriikkaan eikä yksittäiseen lehteen, mikä sopii Pitkäsen myöhempään muotoiluun.

**Kaksi tasaista lehteä tuottaa kaarevuuden.** Olkoot lehdet $s(u)$ ja $s(v)$, joissa $u=t-z$ ja $v=t-x$. Molempien poikkeama on muotoa $-A(u)\,k_ak_b$ ja $-B(v)\,l_al_b$, niiden Riemannin tensori on nolla ja niiden Kähler-muoto on nolla. Kootun metriikan Ricci-tensori häviää ensimmäisessä kertaluvussa, ja toisessa kertaluvussa se on

$$
R_{ab}=\tfrac14A'(u)B'(v)\,(k_al_b+l_ak_b).
$$

Einsteinin tensori on sama rakenne kuin massattoman skalaarikentän ristitermi.

$$
G_{ab}=\tfrac14A'(u)B'(v)\,\bigl(k_al_b+l_ak_b-\eta_{ab}\,k\cdot l\bigr)
$$

Lehtien omat Kähler-tensorit ovat nolla, joten kootun metriikan tensori ei ole lehtien tensorien summa. Tämä on täsmällinen muoto Pitkäsen lauseelle, että koottu metriikka sisältää lehtien väliset vuorovaikutustermit. Jos $A$ on jaksollinen, sen derivaatan keskiarvo jakson yli on nolla, joten ristitermi häviää keskiarvossa, kun $u$ ja $v$ ovat riippumattomia. Tässä esimerkissä summa pätee siis pitkän mittakaavan keskiarvona.

**Kosmologinen termi vaatii poikkeamien summan.** Jos $N$ lehteä täyttää ehdon erikseen, tensorien suora summa laskee Minkowskin osan $N$ kertaa. Ristiriita poistuu ensimmäisessä kertaluvussa, kun myös tensori kootaan poikkeamista, eli $T^{\mathrm{eff}}=\Lambda\eta+\sum_i(T^{(i)}-\Lambda\eta)$. Tämä sääntö on NeuroPajan päättelyä, eikä sitä ole lähteessä.

**Newtonin kenttä saadaan kahdesta lehdestä.** Heikko kenttä on isotrooppisissa koordinaateissa $h_{ab}=-2\phi\,\delta_{ab}$, ja se on Schwarzschildin metriikan ensimmäinen kertaluku. Kaksi lehteä, joilla on yhteensä neljä ympyrää $(a/k)(\cos kq,\sin kq)$ koordinaateissa $q=t,x,y,z$, antavat $CP_2$:n origon lähellä täsmälleen

$$
\sum_i h^{(i)}_{ab}=\sigma\Bigl(a^2\,\delta_{ab}+\frac{4}{k^2}\,\partial_aa\,\partial_ba\Bigr).
$$

Kun $a^2=2\phi$, tulos on Newtonin kenttä, ja suhteellinen virhe on luokkaa $1/(kr)^2$. Ympyrän säteen $a/k$ on oltava pieni $CP_2$:n säteeseen verrattuna. Kuvaajan poikkeamalla on sama etumerkki kuin puoleensavetävällä kentällä. Rakenne on kinemaattinen, koska nämä lehdet eivät ole minimipintoja. Valon kaltaiset lehdet eivät riitä staattiseen kenttään, koska niiden Minkowski-jälki on nolla ja Newtonin kentän jälki ei ole. Kysymys siitä, antavatko kenttäyhtälöiden ratkaisut tämän summan, jää auki.

**Geodeesi antaa sanalle likimain suuruusluvun.** Staattisessa kentässä $h_{ab}=-2\Phi\,\delta_{ab}$, jossa $\Phi$ on lehtien potentiaalien summa, pätee $\Gamma^x{}_{tt}=-\Phi'/(1+2\Phi)$. Ensimmäisessä kertaluvussa kiihtyvyydet summautuvat, ja suhteellinen korjaus on $2\Phi$, Maan pinnalla noin $1{,}4\cdot10^{-9}$. Tämä pätee, jos hiukkanen kulkee kootun metriikan geodeesia, eli luku ei testaa postulaattia.

**Yksi massa ja jaettu massa eroavat.** Massa $m$ kootussa metriikassa saa kiihtyvyyksien summan. Jos massa jaetaan lehdille osuuksina $m_i$, tulos on painotettu keskiarvo painoilla $m_i/m$. Pitkäsen postulaatti vastaa ensimmäistä mallia. Toisessa mallissa putoamiskiihtyvyys riippuisi massan jakautumisesta, mikä on ristiriidassa ekvivalenssiperiaatteen kanssa, joten NeuroPaja pitää ensimmäistä mallia johdonmukaisena.

**Kootun metriikan energia ei säily.** Jokaisen lehden Noether-virta säilyy. Kun energia määritellään kootulle metriikalle yhtälöllä $T^{\mathrm{eff}}=G/\kappa$, kahden aallon energiatase häviää täsmälleen. Kolmen aallon $A(t-z)$, $B(t-x)$, $C(t-y)$ tapauksessa kolmannessa kertaluvussa saadaan

$$
\partial_a\bigl(\sqrt{\lvert g\rvert}\,G^a{}_t\bigr)=-\tfrac34A'B'C'.
$$

Tämä on esimerkki Pitkäsen lauseesta, että globaalit säilymislait eivät päde tarkasti kootulle aika-avaruudelle, vaikka lehtien varaukset säilyvät. Energian siirtymisen mekanismi lehdeltä toiselle vaatii kosketuksen mallin.

## Mustien aukkojen metriikat indusoituna metriikkana

Jakson kysymys on, mitä Einsteinin teorian ratkaisuja TGD rajaa pois ja kuvaavatko pois rajautuvat ratkaisut tunnettua fysiikkaa. TGD:n pinnan metriikka peritään kahdeksalta upotusfunktiolta, joten vain osa Einsteinin teorian metriikoista on yhden pinnan indusoituja metriikoita.

| Einsteinin teorian ratkaisu | Tunnettua fysiikkaa | TGD:n yhdellä pinnalla |
|---|---|---|
| Aikakoneratkaisut, kuten Gödelin universumi | Ei | Rajautuvat pois |
| Schwarzschildin metriikka eli pyörimätön massa | Kyllä, planeettojen radat ja valon taipuminen | Upottuu |
| Avaruuden kiertyminen pyörivän massan mukana, kertaluku $a^1$ | Kyllä, Gravity Probe B ja LAGEOS-satelliitit | Upottuu likimäärin, poikkeama noin $R^2/m^2$ |
| Kerrin metriikan $a^2$-termit eli nopeasti pyörivä musta aukko | Kyllä, gravitaatioaallot ja röntgenhavainnot | Ei upotu tarkasti testatulla yritteellä. Saadaan paikallisesti likimäärin viiden lehden koottuna metriikkana |
| Ikuisesti kriittinen tai ylikriittinen kosmologia | Osittain, havaittu maailmankaikkeus on lähes laakea | Pitkäsen mukaan upottuu vain äärellisen ajan |

Aikakoneratkaisut rajautuvat pois, koska pinnalla ajankaltaisen käyrän $M^4$-projektio on ajankaltainen ja $M^4$:n aika kasvaa sillä koko ajan. Kosmologian rivi on Pitkäsen teksteistä (*Btgdclass1*, PDF s. 333 ja 415), eikä sitä ole laskettu tässä.

Pyörivän mustan aukon rivin vakavuus riippuu kolmesta asiasta:

- Metriikan pienintä mahdollista poikkeamaa ei ole laskettu. Välttämättömän ehdon suhteellinen jäännös on pieni, noin $4\cdot10^{-5}$ arvolla $a/m=0{,}9$.
- Pitkäsen monilehtisessä kuvassa havaittava metriikka on usean lehden poikkeamien summa, jota kahdeksan ulottuvuuden raja ei sido. Silloin tarkkaa upotusta yhdelle pinnalle ei tarvita.
- Este koskee vain symmetriaa noudattavaa yritettä, eikä yleistä todistusta ole.

Tämä jakso koskee vain indusoitua metriikkaa. Kenttäyhtälöitä näillä pinnoilla ei ole testattu ([#42](https://github.com/markomanninen/tgd-geometry-lab/issues/42)).

**Schwarzschildin metriikka upottuu.** Pitkäsen pallosymmetrisessä yritteessä (*Btgdclass1*, luku 7.3.3) $M^4$:n aika on $m^0=\lambda t+h(r)$, $M^4$:n paikka annetaan pallokoordinaateissa $(r,\theta,\varphi)$ ja $CP_2$-koordinaatit ovat

$$
\xi^1=s(r)\,e^{i(\omega t+f(r))},\qquad \xi^2=0 .
$$

Indusoidun metriikan kulmaosa on laakean avaruuden kulmaosa. Muut nollasta poikkeavat komponentit ovat

$$
g_{tt}=\lambda^2-\omega^2R^2H(s),\qquad g_{tr}=\lambda h'-\omega R^2H(s)\,f',\qquad g_{rr}=h'^2-1-R^2\,\frac{s'^2+s^2f'^2}{(1+s^2)^2},
$$

jossa $H(s)=s^2/(1+s^2)^2$. Kolme ehtoa antaa Schwarzschildin metriikan. Ehto $g_{tt}=1-2m/r$ määrää funktion $s(r)$. Ehto $g_{tr}=0$ määrää derivaatan $f'$. Ehto $g_{rr}=-1/(1-2m/r)$ määrää derivaatan $h'$. Testi `tests/test-schwarzschild.mac` vahvistaa tämän symbolisesti arvolla $R=1$.

Funktion $H$ suurin arvo on $1/4$, joten upotus on olemassa vain, kun

$$
\tfrac14\,\omega^2R^2\ \ge\ \lambda^2-1+\frac{2m}{r}.
$$

Arvolla $\lambda=1$ ehto on $r\ge 8m/(\omega R)^2$. Tämä vastaa Pitkäsen toteamusta, että upotus katkeaa kriittisellä säteellä. Testin pallo $\xi^2=0$ on homologisesti epätriviaali, kun taas Pitkäsen tyhjiöekstremaali käyttää homologisesti triviaalia geodeettista palloa.

**Kerrin metriikka ei upotu ensimmäisessä kertaluvussa testatulla yritteellä.** Pitkäsen mukaan Kerrin metriikka luultavasti ei upotu (*Btgdclass1*, PDF s. 415), eikä hänen teksteissään ole tästä laskua. NeuroPaja testasi yritteen, joka noudattaa metriikan kahta symmetriaa. Ajan $t$ siirto on $M^4$:n ajan siirto ja $CP_2$:n kierto. Kulman $\varphi$ siirto on $M^4$:n kierto akselin ympäri ja $CP_2$:n kierto, jonka kierrosluku on kokonaisluku $n$. Kahdeksan upotusfunktiota riippuu koordinaateista $r$ ja $\theta$. Kerrin metriikka kehitettiin pyörimisparametrin $a$ ensimmäiseen kertalukuun, jolloin Schwarzschildin metriikkaan tulee yksi uusi termi

$$
g_{t\varphi}=\frac{2ma}{r}\,\sin^2\theta .
$$

Lasku antaa neljä tulosta:

- Metriikan kymmenen komponenttia antavat kymmenen yhtälöä kahdeksalle funktiolle. Kolme funktiota ratkeaa algebrallisesti, ja jäljelle jää seitsemän yhtälöä viidelle funktiolle, joten yhtälöitä on kaksi liikaa.
- Akselilla $g_{\varphi\varphi}=0$, joten kulmaan $\varphi$ liitetty $CP_2$:n kierto pitää Schwarzschildin upotuksen pallon $\xi^2=0$ paikallaan ja kiertää vain koordinaattia $\xi^2$. Silloin $\xi^2=\sqrt a\,q(r)\sin\theta\,e^{i(n\varphi+\omega_2t+f_2(r))}$.
- Komponentit $g_{\theta\theta}$ ja $g_{r\theta}$ vaativat, että $n^2=1$. Muilla arvoilla komponenttiin $g_{r\theta}$ jää termi, joka on verrannollinen lausekkeeseen $(n^2-1)\cot\theta$.
- Arvolla $n=1$ kaikki yhtälöt ratkeavat yhtä lukuun ottamatta. Komponenttiin $g_{rr}$ jää poikkeama $a\sin^2\theta\,\varrho(r)$, joka poikkeaa nollasta kaikilla testatuilla vakioilla.

Poikkeama on verrannollinen $CP_2$:n säteeseen $R$, kun tulo $\omega R$ pidetään vakiona. Esimerkiksi arvoilla $m=1$, $\lambda=1$, $\omega_1R=1{,}5$ ja $\omega_2/\omega_1=0{,}02$ säteellä $r=7{,}48$ saadaan $\varrho=-0{,}0107\,R$.

Poikkeama pienenee myös, kun vakio $\lambda$ kasvaa. Arvoilla $m=1$, $\omega_1R=3\lambda$ ja $\omega_2/\omega_1=0{,}02$ säteellä $r=6$ saadaan suurilla $\lambda$:n arvoilla

$$
\varrho\approx-0{,}065\,\frac{R}{\lambda}.
$$

Vakioiden numeerinen haku ei löytänyt äärellisiä arvoja, joilla poikkeama häviäisi kaikilla säteillä. Poikkeama oli samanmerkkinen koko hakualueella, ja se lähestyi nollaa vain, kun vakiot kasvoivat rajatta. Ensimmäisen kertaluvun upotus on siis tällä yritteellä mielivaltaisen tarkka mutta ei tarkka. Haku on numeerinen eikä todistus.

Kierrosluku rajoittaa myös pyörimisen suuruutta. Cauchyn–Schwarzin epäyhtälöstä seuraa täsmällinen raja

$$
g_{t\varphi}^2\ \le\ \tfrac14\,(\lambda^2-g_{tt})\,R^2n^2 .
$$

Arvolla $\lambda=1$ raja on $a\sin^2\theta\le nR\sqrt{r/8m}$, joten $n=1$ sallii silloin vain pyörimisen, jonka $a$ on $CP_2$:n säteen suuruusluokkaa. Auringon massaisen mustan aukon $a$ on kilometrin luokkaa. Se vaatisi joko kierrosluvun $n\sim10^{34}$, jonka ehto $n^2=1$ kieltää, tai vakion $\lambda\sim10^{34}$. Jälkimmäisessä tapauksessa komponentin $g_{rr}$ poikkeama on suuruusluokkaa $R^2/m^2$ eli noin $10^{-70}$, ja $M^4$:n aika $m^0=\lambda t$ kulkee pinnan aikaan nähden tekijän $\lambda$ verran nopeammin. Tämän tulkinta kuuluu Pitkäselle.

**Toisessa kertaluvussa upotus kaatuu myös likimääräisenä.** Ensimmäisen kertaluvun poikkeama häviää rajalla, jossa $R$ lähestyy nollaa ja tulo $\lambda R$ pysyy äärellisenä. Tällä rajalla upotusyhtälöt supistuvat yhdeksi yhtälöksi

$$
\frac{\Sigma}{\Delta}\,dr^2+\Sigma\,d\theta^2=d\rho^2+dz^2+\frac{N^2}{k^2}\,d\Gamma^2+c(g_{t\varphi})\,dg_{t\varphi}^2,\qquad N^2=\frac{\Delta\Sigma}{A}.
$$

Vasen puoli on Kerrin metriikan $(r,\theta)$-osa, ja $\rho^2=-g_{\varphi\varphi}$. Vapaita ovat funktio $z(r,\theta)$ ja kaksi yhden muuttujan funktiota. Funktio $\Gamma$ riippuu vain kulmanopeudesta $\omega_K=-g_{t\varphi}/g_{\varphi\varphi}$, ja funktio $c\ge0$ riippuu vain komponentista $g_{t\varphi}$. Kertaluvuissa $a^0$ ja $a^1$ yhtälö ratkeaa. Kertaluvussa $a^2$ se vaatii, että

$$
c_2=\frac{5r^2p_0+r\tilde G(r)}{3\,(3rp_0-4m)^2},\qquad p_0=\frac{2m\sin^2\theta}{r},
$$

on pelkän $p_0$:n funktio jollakin vapaalla funktiolla $\tilde G(r)$. Tämä on mahdotonta jokaisella avoimella alueella, koska ehto antaa $r\tilde G=C$ ja $-40m-6C/r=0$ kaikilla $r$. Toisen kertaluvun poikkeama ei siis pienene $R$:n mukana, vaan on suuruusluokkaa $a^2/m^2$.

Supistetun yhtälön johto on tehty käsin, ja se on aineiston tiedostossa `johto-toinen-kertaluku.md`. Riippumaton tarkistus Codexilla vahvisti tarkat yhtälöt, kertoimen $N^2/k^2$, lausekkeen $c_2$ ja esteen tämän kehitelmän sisällä. Tarkistuksen mukaan supistus pätee vain säännöllisellä haaralla, jolla $CP_2$-kuvauksen derivaatat pysyvät rajoitettuina. Tulos olettaa kierrosluvun $n=1$, potenssisarjan parametrin $a$ suhteen ja lähtökohdaksi pallosymmetrisen Schwarzschildin upotuksen.

Supistettu yhtälö testattiin myös äärellisellä $a$:lla ilman kehitelmää. Yhtälön vasemman ja oikean puolen erotuksen determinantin on hävittävä, ja tästä seuraa ehto $\gamma'=\alpha+\beta\gamma+\delta\gamma^2$, jossa $\gamma=\Gamma'^2/k^2$ ja kertoimet lasketaan Kerrin metriikasta. Lukujen $\gamma$ ja $\gamma'$ on oltava samat kaikissa pisteissä, joissa $\omega_K$ on sama. Ehto jäi toteutumatta kaikilla testatuilla arvoilla $a/m=0{,}05\dots0{,}9$. Suhteellinen jäännös on noin $4\cdot10^{-5}$ arvolla $a/m=0{,}9$ ja pienenee otosalueella kuten $a^4$. Testi ei oleta potenssisarjaa, Schwarzschildin lähtökohtaa eikä $CP_2$-käyrän haaraa. Codex vahvisti ehdon johdon ja toisti jäännökset. Metriikan pienintä mahdollista poikkeamaa ei ole vielä laskettu, joten jäännöksen pienuudesta ei voi vielä päätellä, kuinka tarkka likimääräinen upotus on.

**Puskutyyppinen upotus kattaa horisontin mutta ei pyöri.** Toisessa yritteessä ajan siirto on $M^4$:n Lorentz-pusku tasossa $(m^0,z)$. Fronsdalin upotus vuodelta 1959 on tätä tyyppiä, ja se siirtyy $H$:hon $CP_2$:n laakean Cliffordin toruksen $\lvert\xi^1\rvert=\lvert\xi^2\rvert=1$ kautta. Upotus on

$$
m^0=\sigma\sinh\frac{t}{4m},\qquad z=\sigma\cosh\frac{t}{4m},\qquad \sigma=4m\sqrt{1-\frac{2m}{r}},
$$

ja koordinaatit $x$ ja $y$ ovat $r\sin\theta\cos\varphi$ ja $r\sin\theta\sin\varphi$. Toruksen kaksi laakeaa koordinaattia ovat $r\cos\theta$ ja funktio $Z(r)$, jolle

$$
Z'^2=\frac{2m}{r}\Bigl(1+\frac{2m}{r}+\frac{4m^2}{r^2}\Bigr).
$$

Indusoitu metriikka on Schwarzschildin metriikka, ja $Z'$ on äärellinen horisontilla. Testi vahvistaa tämän. Toruksen kulmat kiertyvät monta kertaa, joten kuvaus on immersio eikä yksi yhteen.

Tätä upotusta ei saa pyörimään symmetriaa noudattavalla yritteellä. Molemmissa yritteissä pätee

$$
g_{t\varphi}=-\Omega\rho^2-R^2\,s(K_\omega,K_n),
$$

jossa $\rho$ on etäisyys $M^4$:n akselista, $\Omega$ on jäykän kierron kulmanopeus ja $K_\omega$ ja $K_n$ ovat ajan ja kulman siirtoihin liitetyt $CP_2$:n kierrot. Akselilla $g_{\varphi\varphi}=0$, joten $K_n$ häviää akselin $CP_2$-kuvalla. $CP_2$:n kierron nollakohdat ovat joko yksi kompleksinen suora ja yksi piste tai kolme pistettä. Kompleksinen suora leikkaa Cliffordin toruksen pisteissä tai ympyrässä, joka on toruksen laakeissa koordinaateissa suora. Akselin kuva on toruksella käyrä $(Z(r),\pm r)$, joka ei ole suora. Siksi $K_n=0$, ja jäljelle jää jäykkä kierto $g_{t\varphi}=-\Omega\rho^2$, joka ei ole Kerrin termi. Tämä päättely on tehty käsin, eikä se ole testinä.

Tulos koskee vain näitä yritteitä, ja sillä on kolme rajaa:

- Puskutyyppisistä upotuksista on tutkittu vain Cliffordin toruksen kautta kulkeva. Muut puskutyyppiset Schwarzschildin upotukset ovat luokittelematta.
- Upotus, joka ei noudata metriikan symmetrioita, on testaamatta.
- Laskut ovat kehitelmiä parametrin $a$ suhteen Schwarzschildin upotuksen ympärillä, joten ne eivät sulje pois upotusta, joka ei lähesty Schwarzschildin upotusta, kun $a$ lähestyy nollaa.

Kerrin ensimmäisen kertaluvun lasku on tehty SymPy-skripteillä, jotka ovat aineiston kansiossa `laskut-2026-11-10-kerr`. Labin testinä ovat Schwarzschildin kaksi upotusta.

**Kerrin metriikka saadaan paikallisesti likimäärin viiden lehden koottuna metriikkana.** Pitkäsen mukaan Einsteinin teorian rajan ei tarvitse upota yhdelle pinnalle, vaan havaittava metriikka on lehtien poikkeamien summa (*Btgdclass1*, PDF s. 334 ja 337, ja yleiskatsaus *TGD2024I*, luku 2). Lehden poikkeama on $CP_2$:n metriikan vetäisy miinusmerkillä, joten erotuksen $P=\eta-g$ on oltava positiivisesti semidefiniittien vetäisyjen summa. Kun Boyerin–Lindquistin koordinaatit $(t,r,\theta,\varphi)$ samastetaan $M^4$:n pallokoordinaatteihin, Kerrin metriikalle pätee täsmälleen

$$
\eta-g=p_t\,dt^2+p_5\,(dt-a\,d\varphi)^2+p_r\,dr^2+p_\theta\,d\theta^2+p_\varphi\,d\varphi^2,
$$

$$
p_t=\frac{2mr\cos^2\theta}{\Sigma},\quad p_5=\frac{2mr\sin^2\theta}{\Sigma},\quad p_r=\frac{2mr-a^2\sin^2\theta}{\Delta},\quad p_\theta=a^2\cos^2\theta,\quad p_\varphi=\frac{a^2\sin^2\theta\,(r^2\sin^2\theta+\Delta\cos^2\theta)}{\Sigma}.
$$

Kaikki viisi kerrointa ovat ei-negatiivisia horisontin ulkopuolella, kun $a\le m$. Jokaista termiä $p\,dq^2$ vastaa lehti, jonka $CP_2$-koordinaatti kiertää ympyrää,

$$
\xi=\frac{A}{k}\,e^{ikq},
$$

jossa $A^2=p$ ja amplitudi $A$ saa vaihtaa merkkiä. Lehden vetäisy on täsmälleen

$$
F\,\Bigl(p\,dq^2+\frac{dA^2}{k^2}\Bigr),\qquad F=\frac{1}{(1+p/k^2)^2}.
$$

Viiden lehden kootun metriikan ja Kerrin metriikan täsmällinen erotus on siksi

$$
g_{\mathrm{eff}}-g=\sum_j\Bigl[(1-F_j)\,p_j\,dq_j^2-\frac{F_j}{k^2}\,dA_j^2\Bigr]
=\frac{1}{k^2}\sum_j\bigl(2p_j^2\,dq_j^2-dA_j^2\bigr)+O(k^{-4}).
$$

Erotus häviää kiinteässä pisteessä, kun aaltoluku $k$ kasvaa. Erotuksen kaksi osaa ovat samaa kertalukua. Ensimmäinen osa tulee $CP_2$:n kaarevuudesta ja toinen amplitudin muutoksesta. Sama rakenne antoi aiemmin Newtonin kentän kahdesta lehdestä. Testit ovat tiedostossa `tests/test-kerr-sheets.mac`. Ne tarkistavat hajotelman, yhden lehden täsmällisen vetäisyn ja viiden lehden summan $CP_2$:n origon laakeassa approksimaatiossa, jossa $F=1$.

Rakenteella on kuusi rajaa:

- Tulos on paikallinen. Erotus on suuruusluokkaa $1/k^2$ jokaisessa kompaktissa alueessa, joka on irti horisontista ja akselista, ja vakio riippuu alueesta.
- Kerroin $p_r$ kasvaa horisontilla rajatta, koska Boyerin–Lindquistin koordinaatit ovat siellä singulaariset. Millään äärellisellä $k$:n arvolla $p_r/k^2$ ei ole pieni horisontin lähellä, joten rakenne ei kata horisonttia eikä sen lähiympäristöä.
- Kulma $\varphi$ on jaksollinen, joten lehdet ovat yksikäsitteisiä vain, kun termin $d\varphi^2$ aaltoluku $k$ ja termin $(dt-a\,d\varphi)^2$ tulo $ka$ ovat kokonaislukuja. Kahdella eri aaltoluvulla ehdot eivät sido toisiaan.
- Kolme lehteä on akselilla jatkuvia mutta ei derivoituvia. Termien $d\varphi^2$ ja $(dt-a\,d\varphi)^2$ lehdet käyttäytyvät akselin lähellä kuten $\rho\,e^{in\varphi}$, joka on sileä vain arvolla $n=\pm1$. Termin $d\theta^2$ lehti $a\cos\theta\,e^{ik\theta}/k$ ei ole kulman $\theta$ parillinen funktio.
- Lehdiltä ei ole vaadittu kenttäyhtälöitä, eikä näiden viiden lehden kenttäyhtälöitä ole testattu.
- Summasääntö on Pitkäsen postulaatti, jota ei ole johdettu kenttäyhtälöistä. Boyerin–Lindquistin koordinaattien samastus $M^4$:n pallokoordinaatteihin on valinta, ja toinen samastus antaisi toisen hajotelman.

Riippumaton tarkistus Codexilla vahvisti hajotelman, kertoimien merkit, vetäisyn ja laakean approksimaation tuloksen. Sama tarkistus toi täsmällisen erotuksen sekä rajat, jotka koskevat paikallisuutta, horisonttia ja akselia.

Yhden pinnan upotus ja lehtien summa ovat siis eri kysymyksiä. Yhden pinnan upotuksena Kerrin metriikka kaatuu testatulla yritteellä toisessa kertaluvussa. Summasääntö ei aseta vastaavaa estettä, koska Kerrin metriikan poikkeama laakeasta metriikasta on horisontin ulkopuolella viiden ei-negatiivisen termin summa.

**Tutkimuksen tila 10.11.2026.** Työ on toistaiseksi pysäytetty tähän ([#42](https://github.com/markomanninen/tgd-geometry-lab/issues/42)). Tähän asti on tutkittu seuraavat asiat:

| Kysymys | Tulos | Varmuus |
|---|---|---|
| Schwarzschild Pitkäsen yritteellä | Upottuu kriittisen säteen ulkopuolella | Labin testi |
| Schwarzschild puskutyyppisellä yritteellä | Upottuu Cliffordin toruksen kautta myös horisontilla | Labin testi |
| Kerr, kertaluku $a^1$, symmetriaa noudattava yrite | Upottuu likimäärin, poikkeama on verrannollinen suureeseen $R/\lambda$ | SymPy-lasku, numeerinen |
| Kerr, kertaluku $a^2$, raja $R\to0$ | Ei upotu | Käsin tehty johto, Codexin tarkistama |
| Kerr, äärellinen $a$, raja $R\to0$ | Välttämätön ehto ei toteudu testatuissa pisteissä | Numeerinen, Codexin toistama |
| Puskutyyppinen upotus pyörivänä | Cliffordin toruksen upotus ei pyöri | Käsin tehty päättely |
| Kerr lehtien koottuna metriikkana | Saadaan viidestä lehdestä paikallisesti virheellä, joka on verrannollinen lukuun $1/k^2$. Lehdet eivät ole sileitä akselilla, eikä rakenne kata horisonttia | Labin testi, Codexin tarkistama |
| Yleinen todistus kirjallisuudessa | Ei löytynyt avaruudelle $H$ eikä kahdeksalle laakealle ulottuvuudelle | Kaksi hakua, ei kattava |

Mahdolliset jatkosuunnat ovat nämä:

- Metriikan pienin mahdollinen poikkeama supistetussa yhtälössä äärellisellä $a$:lla. Se kertoisi, kuinka tarkka likimääräinen upotus on nopeasti pyörivälle mustalle aukolle.
- Toinen $R$:n skaalaus, jossa $CP_2$-koordinaatit vaihtelevat $CP_2$:n pituusskaalassa. Silloin termi $R^2G_{AB}$ ei häviä rajalla, ja yhtälössä on enemmän vapautta.
- Muut puskutyyppiset Schwarzschildin upotukset ja niiden pyörivät versiot.
- Symmetriaa noudattamattomat upotukset Gaussin, Codazzin ja Riccin yhtälöiden kautta. Tämä on sama kuin yleinen todistus.
- Kerrin ensimmäisen ja toisen kertaluvun laskujen vienti labin Maxima-testeiksi.
- Kirjallisuuden varmistus. Luettavana ovat Stephanin ja muiden kirjan luku 37 ja Van den Bergh (1996), ja Sheykiniltä ja Pastonilta voi kysyä, onko Kerrin upotus seitsemään tai kahdeksaan laakeaan ulottuvuuteen ratkaistu.
- Pitkäsen monilehtinen kuva. Kerrin metriikka saadaan paikallisesti viidestä ympyrälehdestä, joilta ei ole vaadittu kenttäyhtälöitä. Auki on, saadaanko se lehdistä, jotka ovat kenttäyhtälöiden ratkaisuja, ja miten horisontti kuvataan.

Pitkäselle kuuluvat kysymykset ovat, vaatiiko TGD tarkan upotuksen, mitä vakio $\lambda\sim10^{34}$ tarkoittaisi ja miten pyörivä musta aukko kuvataan, jos Kerrin metriikka ei upotu yhdelle pinnalle.

## Avoimet kysymykset

Pitkäsen vastaukset 31.10.–8.11.2026 ratkaisivat massattoman ekstremaalin aseman, H-H:n muodon, tilavuustermin merkityksen kenttäyhtälöille, $J(M^4)$:n paikan erillisenä terminä, kertoimien etumerkit ja kaarevuusskalaarin aseman. Pitkänen hyväksyy, että H-H ei toteuta Kähler-vaikutuksen kenttäyhtälöitä ilman lisäoletusta, ja jättää kaarevuusskalaarin pois vaikutuksesta. Säieradoilta ja partonipinnoilta hän ei vaadi minimaalisuutta. Laskennan perusteella auki on kolme kysymystä ([#35](https://github.com/markomanninen/tgd-geometry-lab/issues/35)):

- Pitkäsen korjausehdotus oli Laplacen ehto, ja 8.11.2026 hän muotoili sen Kähler-virran valon kaltaisuudeksi. H-J-ansatsin pinnoilla virran normi on nolla täsmälleen, kun virran poikittainen osa häviää, ja silloin Lorentzin 4-voima häviää. Ehto on väljempi kuin Laplacen ehto, sillä pallomaisessa rakenteessa sen täyttävät myös suora ja kartioleikkaus. Litteässä rakenteessa se sallii vain Kähler-tyhjiön $\xi(u)$. Pitkäsen 10.11.2026 tiivistelmässä korjauksena on Laplacen ehto, joka tekee virrasta valon kaltaisen. Riittääkö Pitkäselle myös väljempi ehto? Laskut ovat [sivututkimussivulla](sivututkimus/sisaosan-vaikutus.md#pitkasen-vastaukset-8112026).
- Pinnat $f(u,w)$ ovat minimaalipintoja litteässä rakenteessa ja horosfäärirakenteessa mutta eivät pallomaisessa rakenteessa, joka on kausaalisessa timantissa symmetrinen $u$:n ja $v$:n vaihdossa. Mistä $u$:n ja $v$:n epäsymmetria tulee?
- Vastaako valokartioiden kärjen suoran laji, eli aikasuuntainen, valon kaltainen tai avaruussuuntainen, jotain fysikaalista?
