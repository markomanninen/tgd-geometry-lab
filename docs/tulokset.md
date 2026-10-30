# Tulokset

<p class="lead">Tälle sivulle on koottu, mitä on laskettu ja mitä siitä seuraa. Jokaista väitettä vastaa automaattinen testi, ja koko sarjan 234 testiä ajetaan jokaisesta muutoksesta.</p>

Merkinnät ja normalisoinnit ovat [konventioissa](konventiot.md). Lukuarvot on annettu säteellä $R^2=1$.

## Mitä tuli yllätyksenä

Kaksi tulosta kannattaa lukea ensin, koska ne tarkentavat aiempaa käsitystä tai lukitsevat normalisoinnin.

**Massaton ekstremaali ei ole yleisessä muodossaan minimipinta.** Pitkäsen ansatsi on $s^k=f^k(u,v)$, ja lähteen mukaan massattomat ekstremaalit ovat minimipintoja "in their simplest form at least". Laskenta tarkentaa tämän: yleinen $f^k(u,v)$ on Kähler-toiminnan ekstremaali, mutta tilavuustermi ei häviä. Tulos ja avoin kysymys ovat kohdassa [Ekstremaalit](#ekstremaalit).

**Kerroin $k=3$ tulee geometriasta.** Unitaarisessa kehyksessä $CP_2$:n spinoriyhteys on $S^+$-lohkossa täsmälleen $\mathrm{diag}(3iA,-3iA)$, kun $dA=J$. Leptonien kerroin $k=3$ kumoaa siis yhteyden kokonaan, ja yksi spinori on kovariantisti vakio. Tämä on TGD:n oikeakätinen neutriino.

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

Vuo on homologinen testi: kartion aste on 2, joten sen vuo on kaksinkertainen. Kaikki kolme karttaa on testattu, ja metriikka ja Kähler-muoto säilyvät jokaisessa karttasiirtymässä.

## Kehykset, yhteydet ja spinorit

Yhteys lasketaan kahdella riippumattomalla reitillä: pelkästä kehyksestä ja Christoffelin symboleista. Reitit antavat saman tuloksen $CP_2$:lla, koko avaruudessa $H$ ja Lorentz-signatuurissa. Torsio häviää, ja Cartanin kaarevuus täsmää koordinaateissa laskettuun Riemannin tensoriin.

Spinoreille on testattu:

- $D_\mu\gamma^\nu=0$ ja $\{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}$ kaarevalla metriikalla,
- Lichnerowicz-termi $\tfrac12\gamma^\mu\gamma^\nu F_{\mu\nu}=-R/4=-6$,
- holonomia unitaarisessa kehyksessä on $U(2)$:ssa,
- $S^+$:n vuo yli $CP_1$:n on $(k\pm3)/2$, joka on kokonaisluku täsmälleen parittomilla $k$.

Viimeinen kohta on syy, miksi $CP_2$ ei ole spin-monisto mutta kertoimet $k=1$ ja $k=3$ kelpaavat.

## Upotetut pinnat

Toinen perusmuoto $B^k{}_{\alpha\beta}$ ja keskikaarevuus $H^k$ on testattu tunnetuilla pinnoilla, myös kaarevassa ympäristössä ja indefiniitissä signatuurissa. Kompleksiset käyrät ovat minimipintoja, vaikka ne eivät olisi totaaligeodeettisia: kartiolla $z^2=(z^1)^2$ on $B\ne0$ ja silti $H^k=0$.

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

Kähler-termi ja tilavuustermi on testattu erikseen. Kanoninen $M^4$ ja kosminen säie toteuttavat molemmat kaikilla kertoimilla. Massattomissa ekstremaaleissa ($u$ valon kaltainen, $x$ poikittainen, $w=x+iy$) kuva on rikkaampi:

| Ansatsi | Kähler-termi | Tilavuustermi |
|---|---|---|
| $s^k(u)$ | 0 | 0 |
| $s^k(u,x)$ mielivaltaisena | 0 | $\ne0$ |
| $z^1=\tan(x)\,e^{ia(u)}$ | 0 | 0 |
| holomorfinen $w$:ssä | $\ne0$ | 0 |

Toisella rivillä $T^{\alpha\beta}\propto k^\alpha k^\beta$ ja Kähler-virta on valon kaltainen, kuten Pitkänen kuvaa. Tilavuustermi ei silti häviä. Yksinkertaisin vastaesimerkki on $s^k=F^k(x)$: pinta on $M^3\times$ käyrä avaruudessa $\mathbb R_x\times CP_2$, ja se on minimaalinen vain, jos käyrä on geodeesi.

Kolmas rivi osoittaa, että $x$-riippuvuus on silti mahdollinen. Se on $CP_2$:n geodeesi, jonka suunta kääntyy $u$:n mukana, ja sillä $J_{ux}\ne0$ ja virta $j^v\ne0$.

## Säilymislait

$H$:n 18 isometriaa on tarkistettu: neljä translaatiota, kuusi Lorentz-generaattoria ja kahdeksan värigeneraattoria. Ne säilyttävät sekä metriikan että Kähler-muodon, ja värigeneraattorit muodostavat $su(3)$-algebran.

Jokaiselle pinnalle pätee identiteetti $D_\alpha j^\alpha=2K^k\mathrm{Eq}_k$, joka on testattu myös pinnalla, joka ei ole ratkaisu. Virran säilyminen ei siis johdu siitä, että kaikki häviää.

Ratkaisuilla kaikki 18 virtaa säilyvät: kanoninen $M^4$, kosminen säie ja ME $s^k(u)$. Yleisellä $s^k(u,x)$:llä Kähler-virrat säilyvät mutta tilavuusvirrat eivät, mikä vastaa ekstremaalitaulukon toista riviä. Massattoman ekstremaalin liikemäärävirta kulkee valon kaltaisen suunnan $k$ mukaan.

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

Kaksi riviä on merkityksellisiä avoimien kysymysten kannalta.

Kosmisen säikeen poikki nopeuden neliö voi olla negatiivinen. Pelkällä Kähler-toiminnalla $s^2=-1$, ja yhtälön tyyppi on elliptinen. Kertoimien suhde ja etumerkki ratkaisevat siis yhtälön tyypin, ja se tekee [#27](https://github.com/markomanninen/tgd-geometry-lab/issues/27):n kysymyksestä laskennallisesti merkityksellisen.

Pelkkä Kähler-toiminta on $M^4$:n ympärillä degeneroitunut ja ME-taustalla heikosti hyperbolinen. Tämä on sopusoinnussa tunnetun Kähler-toiminnan tyhjiödegeneraation kanssa, mutta tulkinta on Pitkäsen.

Tulokset koskevat yhtälön pääosaa yhdessä pisteessä. Ne eivät vielä kerro ratkaisujen stabiiliudesta.

## Avoimet kysymykset

Nämä odottavat Matti Pitkäsen linjausta:

- **[#28](https://github.com/markomanninen/tgd-geometry-lab/issues/28):** mikä on massattoman ekstremaalin täsmällinen määritelmä toiminnalle $S_K+S_V$, ja vaaditaanko ekstremaalisuutta kummallekin termille erikseen vai vain niiden summalle?
- **[#27](https://github.com/markomanninen/tgd-geometry-lab/issues/27):** tilavuustermin kertoimen etumerkki ja normalisointi Kähler-termiin nähden Minkowski-alueilla sekä kompleksisen $\alpha_K$:n rooli.
- **[#31](https://github.com/markomanninen/tgd-geometry-lab/issues/31):** holografia = holomorfia -periaatteen täsmällinen muoto ratkaisugeneraattorina.
