# Sisäosan vaikutus ja kaarevuusskalaari

Tämä sivu vertaa ehdokkaita TGD:n aika-avaruuspinnan sisäosan vaikutukseksi. Sisäosan vaikutus on avoin tutkimuskohde, ja sivu kokoaa, mihin kukin vaihtoehto johtaa. Ehdokkaita on kolme. Pelkkä tilavuus on Matti Pitkäsen linjaus 1.11.2026. Kaarevuusskalaaria ja tilavuutta Pitkänen pohti 2.11.2026 kysymyksenä. Kähler-vaikutusta ja tilavuutta lisäehdolla, jossa $CP_2$:n Kähler-funktio toteuttaa Laplacen yhtälön, hän ehdotti 3.11.2026. Laskut, lähteiden lukemisen ja päättelyn teki Claude 2.–3.11.2026. Tulokset koskevat mainittuja pintaluokkia, ja fysikaalisen tulkinnan tekee Pitkänen.

Merkinnät ovat projektin konventioiden mukaiset, ja signatuuri on $(+,-,-,-)$. Kirjain $R$ tarkoittaa pinnan kaarevuusskalaaria, ja $R_C$ on $CP_2$:n säde. Vaikutus on

$$
S=\int\sqrt{\lvert g\rvert}\,\bigl(c_V+c_R R\bigr),\qquad c_V=\frac{\Lambda}{8\pi G},\quad c_R=\frac{1}{16\pi G},
$$

ja sen Noether-virta on

$$
P^{ab}=\frac{\Lambda g^{ab}-G^{ab}}{8\pi G}.
$$

Kertoimet on otettu Einsteinin rajasta. Ne ovat oletus, jota Pitkänen ei ole vahvistanut.

## Vertailu

Taulukko näyttää, mitä kukin testi antaa. Jokainen rivi koskee vain mainittua pintaluokkaa, joten taulukko ei ole yleinen konsistenssitodistus kummallekaan ehdokkaalle. Säikeet eivät erota ehdokkaita, jos avoin poikkileikkaus kelpaa säikeeksi. Ehdokkaat eroavat pallomaisen rakenteen holomorfisilla pinnoilla. Laskut eivät ratkaise, ovatko nämä pinnat sallittuja H-J-pintoja, joten tästä ei seuraa ristiriitaa Pitkäsen kanssa.

| Testi | R + tilavuus | Pelkkä tilavuus | Kähler + tilavuus, Laplacen ehto |
|---|---|---|---|
| Litteän H-J-rakenteen holomorfiset pinnat | Ratkaisuja | Ratkaisuja | Vain pinnat, joilla $\partial_w\xi=0$, ja testatuista vain $\xi(u)$ |
| Pallomainen rakenne, pinnat $\xi(w)$ | Vain suora ja kartioleikkaus | Kaikki holomorfiset pinnat | Ei laskettu |
| Genuksen $g$ lehti $y^2=F(w)$ | Ei ratkaisu | Ratkaisu | Ei laskettu |
| Yksikkövuon suljettu tuotesäie, $\Lambda R_C^2\ll 4$ | $T\approx-1/(2G)$ | $T>0$ | Säie rikkoo ehdon |
| Yksikkövuon avoin poikkileikkaus, jännitys tasoon verrattuna | $\Lambda R_C^2/8G$ | $\Lambda R_C^2/8G$ | Ei laskettu |
| Translaatiovirta radalla | Riippuu mallista | Ei hajaannu | Ei laskettu |
| $G$:n arvo | Yhteinen kerroin, ei johtoa | Ei vaikutuksessa, ei johtoa | Ei laskettu |

## Säiejännitys

Tarkastellaan tuotepintaa $M^2\times Y^2$, jossa $Y^2$ on suljettu pinta avaruudessa $CP_2$. Tuotteella Einsteinin tensorin $Y^2$-lohko on nolla, joten kenttäyhtälöt supistuvat ehtoon, että $Y^2$ on minimipinta. Lisäksi $G^{tt}$ on pinnan $Y^2$ Gaussin kaarevuus $K$. Gaussin–Bonnetin lause antaa siksi jännitykseksi

$$
T=\frac{\Lambda A-2\pi\chi}{8\pi G}.
$$

Asteen $d$ sileällä kompleksikäyrällä ala on $A=d\pi R_C^2$ ja Eulerin luku on $\chi=3d-d^2$, joten

$$
8GT=d\,\Lambda R_C^2-2\chi=d\,\bigl(\Lambda R_C^2+2d-6\bigr).
$$

Ainoa aste, jolla $\chi=0$, on $d=3$. Pienellä $\Lambda$:lla muiden asteiden jännitys on luokkaa $1/G$, kun havaittu arvo on noin $0{,}22\cdot10^{-6}/G$. Yhtälö $v^2=2GT$ antaa havaitusta arvosta nopeudeksi noin 199 km/s, joka on galaksien tyypillinen pyörimisnopeus.

Kuutiokäyrä täyttää Pitkäsen rakenteelliset ehdot, sillä Pitkäsen kirjan *Physics in Many-Sheeted Space-Time: Part II* mukaan $Y^2$ on $CP_2$:n kompleksinen alimonisto. Se ei silti riitä ratkaisuksi. Sen homologiavaraus on kolme, joten yksikkövuon holomorfinen säie on yhä $CP_1$, jolla $T\to-1/(2G)$. Kalibraation mukaan $A(Y)\ge\pi R_C^2$, joten ei-holomorfinen edustaja ei auta tuotteiden joukossa. Kirja myös sijoittaa galaktiset säikeet genukseen $g=0$.

### Etumerkki

Jännityksen negatiivinen osa ei riipu Noether-virran sopimuksesta. Vaikutus $S=-\tfrac{1}{16\pi G}\int\sqrt{\lvert g\rvert}\,(R+2\Lambda)$ supistuu tuotteella Nambu–Goto-muotoon $-T\int\sqrt{\lvert\gamma\rvert}$, ja kerroin $T$ on sama kuin edellä. Tässä käytetään tulosta $R=-2K$. Positiivinen tilavuusenergia kiinnittää vaikutuksen kokonaismerkin, ja de Sitter -ratkaisu kiinnittää suhteellisen merkin. Pitkäsen kaava $\Lambda=3/\alpha^2$ ja tiheys $3/(8\pi G\alpha^2)$ ovat näiden kanssa samaa mieltä.

### Paksuuntuminen ja avoin poikkileikkaus

Pitkäsen kirjan *Physics in Many-Sheeted Space-Time: Part II* luvun 13 mukaan kosmiset säikeet ovat epävakaita paksuuntumista vastaan. Lasku tukee tätä, sillä tuotteella

$$
\omega^2-k^2=-\frac{l(l+1)\,\Lambda K}{K-\Lambda},
$$

joten arvolla $0<\Lambda<K$ jokaisella $l\ge1$ on takionimoodi.

Arvolla $\Lambda>K$ tuote on vakaa. Tuotteella $M^2\times CP_1$ toinen perusmuoto on nolla kaikissa suunnissa, koska $CP_1$ on $CP_2$:n totaaligeodeettinen pinta, joten kenttäyhtälön linearisointi on $P^{ab}\,\delta B^k_{ab}=0$, jossa $P^{ab}$ on taustan arvo. Sen $M^2$-lohko on verrannollinen kertoimeen $\Lambda-K$ ja $CP_1$-lohko kertoimeen $\Lambda$. Jacobin operaattori on minimipinnan alan toisen variaation operaattori. Jokaiselle normaalimoodille, jolla on Jacobin operaattorin ominaisarvo $\mu$, saadaan

$$
\omega^2-k^2=\frac{\mu\,\Lambda}{\Lambda-K}.
$$

$M^4$-suunnissa $\mu=l(l+1)K$, ja Maxima tarkistaa kaavan moodilla $\cos(\omega t-kz)\cos\theta$ suoraan kirjaston Einsteinin tensorista. $CP_2$-suunnissa $\mu\ge0$, koska kompleksikäyrä on kalibroitu ja siksi vakaa minimipinta. Näiden suuntien nollamoodit siirtävät suoraa $CP_2$:ssa. Kun $\Lambda>K$, kaikilla moodeilla $\omega^2-k^2\ge0$, joten mikään moodi ei kasva ajassa, ja jännitys $(\Lambda-K)\pi R_C^2/8\pi G$ on positiivinen. Säikeellä $CP_1$ on $K=4/R_C^2$, joten raja on $\Lambda R_C^2=4$. Arvolla $\Lambda=K$ jännitys on nolla, ja yhtälöstä katoaa $M^2$-osa.

Pyöreällä pallolla $K$ on vakio, joten tiheys $(\Lambda-K)/8\pi G$ häviää jokaisessa pisteessä, kun $\Lambda=K$. Silloin myös jokaisen geodeesin rajaaman palan jännitys on nolla, ja esimerkiksi puolipallolla ehto on sama $\Lambda=1/r^2$, kun $r$ on pallon säde. Jos pinnalla on $g$ kädensijaa ja $n$ reikää, joiden reunat ovat geodeeseja, Eulerin luku on $\chi=2-2g-n$. Arvolla $\Lambda=0$ jännitys on silloin $T=(g-1+n/2)/2G$.

Suljetusta poikkileikkauksesta ei silti tule paksua. Jos $X^2$ on suljettu minimipinta avaruudessa $E^2\times CP_2$, sen $E^2$-projektio on harmoninen funktio suljetulla pinnalla, joten se on vakio. Lasketut suljetut kierrehaarat vievät energiaa negatiivisemmaksi.

Avoin poikkileikkaus on eri asia. Holomorfinen käyrä $\xi=w/\lambda$ avaruudessa $E^2\times CP_1$ kantaa yksikkövuon, sillä sen kompaktisointi on astetta yksi. Sen ala ylittää tason alan määrällä $\pi R_C^2$, ja $\int K\,dA=0$, joten tasoon verrattuna

$$
T=\frac{\Lambda R_C^2}{8G}
$$

kaikilla koilla $\lambda$. Pallon kaarevuus $4\pi$ kumoutuu kaulassa. Tämä on sama arvo kuin pelkällä tilavuudella, joten negatiivinen jännitys poistuu, jos poikkileikkaus saa päättyä $M^4$-levyyn. Tulos koskee suhteellista jännitystä, eikä tason vähentämistä ole perusteltu dynaamisesti. Kysymys on, kelpaako tällainen pinta säikeeksi.

Kuutiokäyrä ei ole ratkaisu ongelmaan. Sen paikallinen jännitystiheys $(\Lambda-K)/8\pi G$ on negatiivinen lähes puolella alasta, joten ei-tuotehäiriöillä on takionimoodeja. Kokonaisarvo $\int K\,dA=0$ vahvistui Fermat-kuutiolla numeerisesti.

Saman kirjan kohdassa 3.1.7 kosmisen säikeen gravitaatiomassa on $M_{gr}=(1-g)/4G$. Einsteinin tensorin integraali antaa arvon

$$
\frac{1}{8\pi G}\int_{Y^2}\sqrt h\,G^{tt}=\frac{1-g}{2G},
$$

joten kaavoissa on tekijän kaksi ero. Pitkäsen käyttämä kerroin $T^{\mu\nu}=G^{\mu\nu}/16\pi G$ toistaa arvon $(1-g)/4G$, mutta tavallinen Noether-normalisointi antaa arvon $(1-g)/2G$.

### Gravitaatiovakio

Kummassakaan ehdokkaassa $G$:n arvo ei tule vaikutuksesta. Vaikutuksessa R + tilavuus $G$ on yhteinen kerroin, ja pelkkä tilavuus antaa vain tulon $G\rho$. Kirjan *TGD as a Generalized Number Theory: Part I* luvun 6 eksponenttikaava $\hbar G=pR_C^2\exp(-2aS_K(CP_2))$ antaa suhteen $R_C^2/G\sim10^7$, mutta sen $a\simeq0{,}976$ on sovite, ja kaava riippuu euklidisen alueen Kähler-vaikutuksesta. Muut reitit tuovat luvun normalisoinnista tai lukuteoreettisesta oletuksesta.

## Massa

Euklidisella $CP_2$-alueella Einsteinin tensori on $G^{ab}=k\,g^{ab}$, kun $k=6/R_C^2$, joten

$$
P^{ab}=\frac{(\Lambda-k)\,g^{ab}}{8\pi G}.
$$

Radan suuntainen energia on positiivinen, kun $\Lambda<k$. Kenttäyhtälö $(\Lambda-k)\,\Box m^k=0$ pakottaa kuitenkin valonkaltaisen käyrän suoraksi, kun $\Lambda\ne k$, joten sileän kappaleen neliliikemäärä on valonkaltainen. Tämä ei ole ristiriidassa TGD:n kanssa. Pitkäsen kirjan *Towards M-Matrix: Part II* mukaan hiukkaset ovat massattomia kahdeksanulotteisessa mielessä, massa syntyy $p$-adisesta termodynamiikasta, ja kvanttinen neliliikemäärä tulee superkonformiesityksistä.

Lasku tukee tätä muotoa. Mallissa $\xi=t+x^2/2b$ radan ydinvektorin kuva on valonkaltainen avaruudessa $H$, ja siksi $M^2=P_\xi^2$. Neljäulotteinen massa on tässä $CP_2$-liikemäärän osuus, joka on olemassa jo geometriassa, eikä se synny virrasta radan yli. Lasku antaa massan muodon mutta ei sen arvoa.

## Partonirata

Partonirata on pinta, jolla signatuuri vaihtuu Minkowskin signatuurista euklidiseksi. Silloin metriikan yksi ominaisarvo vaihtaa merkkiä, joten sen nollakohdan kertaluku on pariton. Mallissa $g_{tt}=x$ pätee $R=-1/(2x^2)$ radan molemmilla puolilla, ja Pitkäsen linjauksen $\sqrt{\lvert g\rvert}$ kanssa hajaantuvat osat ovat samanmerkkisiä, joten ne eivät kumoa toisiaan. Malli on tarkka, sillä sillä on upotus avaruuteen $M^4\times S^2$, helikoidi kertaa $\mathbb R^2$, joka on sekä minimipinta että vaikutuksen R + tilavuus ekstremaali.

Hajaantuminen riippuu mallista, ja kaksi laskua koskee eri suureita. Gibbons–Hawking–York-reunatermi kumoaa mallissa $g_{tt}=x$ vaikutuksen hajaantuvan osan. Upotusmuuttujilla reunatermin hajaantuva kerroin on radan poikkileikkauksen keskikaarevuus, ja paikallisessa mallissa kenttäyhtälö pakottaa sen nollaksi, kun kertaluku ei ole kaksi. Tulos on johdettu vain tälle mallille. Kertaluku $a=3$ on aito, sillä siitä on tarkka polynomiupotus, mutta häiriö hajottaa kolmoisnollakohdan.

Toinen suure on translaatiovirta. Eräässä sileässä mallissa sen kaarevuusosa hajaantuu kuten $1/\sqrt\delta$, eikä kokeiltu reunatermi poista sitä. Toisessa mallissa normaalivirta on täsmälleen nolla. Tilavuusosan virta häviää radalla kuten $\sqrt\delta$ kaikissa malleissa.

Pitkäsen kaava $4\pi(2-n)$ ei tule radalta, koska geodeettisen kaarevuuden osuus saa siellä painon, joka menee nollaan. Kaava vaatii aikamaisen reunan ja reunatermin.

## Pallomainen rakenne

Pinnoilla $\xi(w)$ ehto $G^{ab}B^k{}_{ab}=0$ vaatii, että $\omega/\rho$ on vakio. Tämä antaa metriikan

$$
ds^2=dt^2-dr^2-(r^2+c)\,d\Omega^2,
$$

joka on $SO(3)$-symmetrinen, joten rajoitus tarkoittaa pallosymmetriaa.

Pinnat $\xi(u,w)$ eivät yleensä ole minimipintoja pallomaisessa rakenteessa, sillä

$$
H^\xi=\frac{2r\rho\,\xi_u}{\Phi}.
$$

Vaikutuksella R + tilavuus ei löytynyt $u$-riippuvia ratkaisuja, mutta tapausjako on päättelyä ilman testiä.

Pallomaisessa rakenteessa on silti tarkkoja minimipintoja, jotka voivat riippua ajasta. Jos $Y$ on holomorfisen yhtälön $G(Y,a,b)=0$ juuri, niin $\xi^k=f^k(Y)$ on minimipinta siellä, missä haara on säännöllinen. Yhtälö on Kerrin tyyppinen, ja kaustiikat $G_Y=0$ jäävät ulkopuolelle. Vaikutukselle R + tilavuus tämä perhe ei kelpaa.

Genuksen $g$ lehti $y^2=F(w)$ saadaan, kun $w$ on $M^4$:n pallolla ja $y$ avaruudessa $CP_1$. Se on sileä ja minimipinta myös haarapisteissä, mutta se ei ole vaikutuksen R + tilavuus ekstremaali millään $n\ge1$.

## Twistoripallo

Tulomallissa avaruudenkaltaisen pallon kaarevuus on $-2/r^2$ ja aikamaisen $+2/r^2$. Pitkäsen kirjan *Towards M-Matrix: Part II* luvun 7 mukaan $M^4$-puolen pallo on aikamainen, joten malli antaa oikean merkin. Todellisella pallokimpulla kaarevuusskalaari on

$$
R(Z)=s+\frac{2}{r^2}-\frac{r^2s^2}{72},
$$

missä $s$ on kannan kaarevuusskalaari ja $r$ kuidun säde. Kaava täsmää tunnettuihin arvoihin. Vakio-osa säilyy muodossa

$$
\Lambda=\frac{1}{R_{cd}^2-r_C^2},
$$

ja vertailu kaavaan $\Lambda=3/\alpha^2$ antaa $\alpha^2=3(R_{cd}^2-r_C^2)$.

Tilavuustermi tulee siis pallon kaarevuudesta ilman Kähler-rakennetta. Einsteinin tensorin $(1,1)$-tyyppisyys ei riipu Kähler-rakenteesta. Holomorfia tarvitsee kohdeavaruuden Kähler-rakenteen, koska se määrää toisen perusmuodon tyypin, mutta se ei tarvitse Kähler-vaikutusta.

Kaavan viimeinen osa on sähköheikon yhteyden vasenkätisen osan Yang–Millsin neliö. Kompleksikäyrillä sillä on sama ensimmäinen variaatio kuin Kähler-termillä, joten kiinteän $X^4$:n yläpuolisessa kimpussa se palauttaa saman esteen, jonka takia sisäosan Kähler-termistä luovuttiin.

Holomorfinen $X^6$ ei ole yhden aika-avaruuspinnan esikuvakimppu. Esimerkissä $s=\varepsilon w$, $\tau=0$ viipaleet ovat pintoja $M^2\times L_\zeta$, joissa kompleksisuora $L_\zeta$ riippuu pisteestä $\zeta$. Yhdessä testatussa variaatiossa neliötermin osuus kumoutuu, mutta yksi suunta ei riitä yleiseen johtopäätökseen. Tulossa $T(M^4)\times T(CP_2)$ termin kerroin näyttää olevan $r_C^4\kappa^2/6\rho^2$, joka pienenee suurella $R_{cd}$:llä, mutta tämä on yhden ansatsin numeerinen tulos.

## H-J-rakenne ja torukset

Pitkäsen artikkelin *Holography= holomorphy vision: analogues of elliptic curves and partonic orbits* mukaan metriikka on hermiittinen ja tyyppiä $(1,1)$, ja konjugaatio vaihtaa koordinaatit $u$ ja $v$. Artikkelin mukaan partoniratoja ei ole ilman tätä konjugaatiota. Ristitermit $g_{u\bar w}$ ja $g_{vw}$ koskevat pinnan indusoitua metriikkaa, ja ne tulevat $CP_2$-osasta. Ehto $(\nabla u)^2=(\nabla v)^2=0$ koskee $M^4$:n metriikkaa, ja se poistaa ristitermit $M^4$:n viivaelementistä (2.4.19) kirjassa *Physics in Many-Sheeted Space-Time: Part I*. Määritelmät eivät siis ole ristiriidassa.

Pelkkä gradienttiehto sallii minkä tahansa genuksen. Esimerkki on

$$
u,v=t\mp\sqrt{(\rho-R_0)^2+z^2},
$$

jonka lehdet ovat sisäkkäisiä toruksia alueella, joka rajautuu ydinympyrään ja akseliin. Suljetut lehdet pakottaa palloiksi vasta se, että kaikilla lehdillä on yhteinen koordinaatti $w$. Dipolin pinnat eivät kelpaa, koska harmonisen funktion tasa-arvopinnat ovat yhdensuuntaisia vain tasolle, pallolle ja sylinterille.

Multipoliajatus toimii pallolla. Pinta $y^2=F(w)$, jossa $F$ on $n$ vastapistedipolin tulo, on genusta $n-1$.

## Pelkkä tilavuus ja K-C-S

Pelkän tilavuuden normaalivuo radalla on muotoa $\rho\,n_k$, jossa $n$ on valonkaltainen ydinvektori, ja sileällä signatuurin vaihdolla $\rho=0$. Kun $J(M^4)$ on poikittainen, kuten Pitkäsen artikkelissa *About the relationship of electroweak and strong interactions in the TGD Universe: part I*, K-C-S ei voi ottaa vastaan hyppyä $\rho\,n_k$. Silloin sisäosa ja rata säilyttävät $M^4$-liikemäärän ja värin erikseen.

Ehdokkaalla on kolme hintaa. Euklidisen alueen energia on negatiivinen tai imaginäärinen, kytkentävakiot katoavat klassisista yhtälöistä, ja pintojen välinen $U(1)$-voima puuttuu sisäosasta. Saman artikkelin väite, että pelkällä tilavuudella radat ovat mahdottomia, ei päde kirjaimellisesti, sillä pyörivä sauva kertaa $CP_1$ on paikallinen ekstremaali, jolla $E^2=2\pi TL$. Se ei kuitenkaan kuulu luokkaan $(f_1,f_2)=0$.

## Kähler ja tilavuus Laplacen ehdolla

Pitkänen ehdotti 3.11.2026, että Kähler-vaikutus pidetään sisäosassa, kun avaruusaikapinnoille lisätään yksi ehto. Ehdon mukaan $CP_2$:n Kähler-funktio $K$ pinnalle vedettynä toteuttaa poikittaisissa koordinaateissa Laplacen yhtälön

$$
\partial_w\partial_{\bar w}K=0.
$$

Hänen mukaansa induusoidun Kähler-kentän poikittainen magneettikenttä häviää silloin, varaukset ja virrat ovat vain alempiulotteisissa singulariteeteissa, ja H-H toimii myös Kähler-vaikutukselle. Twistorinosto säilyy, ja induusoitu Kähler-kenttä määrää H-J-rakenteen.

Clauden laskussa koordinaatit $\xi^1=f(w)$ ja $\xi^2=g(w)$ ovat holomorfisia muuttujan $w$ suhteen, ja $K=\log(1+\lvert\xi^1\rvert^2+\lvert\xi^2\rvert^2)$. Vedetyn Kähler-funktion Laplacen operaattori on silloin derivaatan $\partial_w\xi$ normin neliö Fubini–Studyn metriikassa.

$$
\partial_w\partial_{\bar w}K=\frac{\lvert f'\rvert^2+\lvert g'\rvert^2+\lvert fg'-gf'\rvert^2}{(1+\lvert f\rvert^2+\lvert g\rvert^2)^2}.
$$

Lauseke on nolla vain, kun $f'=g'=0$. Clauden laskussa ehto ei siis salli riippuvuutta poikittaisesta koordinaatista $w$ niissä kohdissa, joissa pinta on säännöllinen, ja $CP_2$-koordinaatit riippuvat silloin vain pitkittäisistä koordinaateista. Sama tulos on [tulossivulla](../tulokset.md) poikittaisen virran ehtona, jossa Fubini–Study-metriikan vetäisyn pitää olla litteä. Laplacen ehto on saman ehdon toinen muoto.

Claude laski 3.11.2026 ehdon seuraukset viidestä suunnasta.

**Kosminen säie.** Säikeellä $M^2\times CP_1$ poikittainen koordinaatti on $CP_1$:n koordinaatti, eli $\xi=w$. Silloin $\partial_w\partial_{\bar w}K=1/(1+\lvert w\rvert^2)^2$, joka ei ole missään nolla. Tämä Laplacen operaattori on säikeen monopolivuon tiheys. Ehto sulkee siis pois monopolivuoputket, ellei niitä lueta singulariteeteiksi.

**Singulariteetit.** Navalla $\xi=1/w$ Laplacen operaattori on navan ulkopuolella sama $1/(1+\lvert w\rvert^2)^2$. Poikittaisen tason pisteet vastaavat aika-avaruudessa fermionisäikeitä ja säiemaailmanpintoja. Pisteet eivät jaa tasoa osiin, joten säännöllinen alue on yhtenäinen, ja ehto tekee $\xi$:stä vakion koko alueessa. Poikittainen riippuvuus ei siis voi olla pelkästään pistemäisissä singulariteeteissa. Se voisi olla vain tason jakavissa viivoissa, jotka ovat aika-avaruudessa kolmiulotteisia seinämiä, ja niiden yli $\xi$ hyppäisi, jolloin pinta ei ole jatkuva.

**Hyperkompleksinen luenta.** Jos $\xi$ riippuu koordinaateista $u$ ja $v$, poikittainen Kähler-kenttä häviää ja pitkittäinen komponentti $J_{uv}$ jää. Pinnalla $\xi=(u+iv)/2$ eivät häviä kenttäyhtälöiden Kähler-osa eikä tilavuusosa. Samoin käy pinnoilla $\xi=uv/3+iu/2$, $\xi=(t+iz)/3$ ja $\xi=v\,e^{iu}/4$. Pinnalla $\xi=e^{i(u-v)/2}/2$ Kähler-osa häviää, mutta tilavuusosa ei. Ainoa testattu ratkaisu on $\xi=u/2$, joka on massattoman ekstremaalin tyyppiä, ja sillä induusoitu Kähler-muoto on nolla. Laskut eivät osoita, ettei muita ratkaisuja ole.

**Ei-holomorfinen luenta.** Jos $\xi$ saa riippua muuttujista $w$ ja $\bar w$, ehdolla on muitakin ratkaisuja. Esimerkiksi $\xi=\sqrt{e^{ax}-1}$ antaa lineaarisen funktion $K=ax$. Kähler-muoto on silloin nolla, koska $\xi$ riippuu vain yhdestä koordinaatista, mutta pinta ei ole minimipinta. Tällainen pinta ei myöskään kuulu H-J-rakenteen holomorfisiin pintoihin.

**H-J-koordinaatit Kähler-funktiosta.** Pitkäsen ehdotuksessa H-J-koordinaatit rakennetaan induusoidusta Kähler-potentiaalista. Valon kaltaisen koordinaatin gradientti on valon kaltainen. Funktion $K$ gradientin neliö on $4K_uK_v$, joten se on valon kaltainen vain, jos $K$ riippuu yhdestä valon kaltaisesta koordinaatista. Pinnalla $\xi=(u+iv)/2$ näin ei ole, joten rakenne palauttaa valon kaltaisen koordinaatin vain massattoman ekstremaalin tyyppisillä pinnoilla.

**Twistorinosto.** Aiempi tulos oli, että Yang–Millsin neliötermillä on kompleksikäyrillä sama ensimmäinen variaatio kuin Kähler-termillä. Laplacen ehdolla este häviää siis täsmälleen silloin, kun kenttäyhtälöiden Kähler-osa häviää. Testatuista pinnoista näin käy pinnalla $\xi=u/2$, jolla Kähler-muoto on nolla. Kysymys palautuu siksi hyperkompleksisen luennan ratkaisuihin.

Kysymykset Pitkäselle ovat nämä. Koskeeko ehto vain osaa pinnoista, vai ovatko monopolivuoputket hänen tarkoittamiaan singulariteetteja? Tarkoittaako hän riippuvuutta pelkästä koordinaatista $u$ vai hyperkompleksisesta koordinaatista $t+ez$?

Testit ovat tiedostossa [test-interior-string.mac](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-interior-string.mac).

## Tarkistus ja rajat

Maxima-testit ovat tiedostoissa [test-interior-curvature.mac](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-interior-curvature.mac), [test-interior-energy.mac](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-interior-energy.mac) ja [test-interior-string.mac](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-interior-string.mac). Erilliset Python-skriptit ovat kansiossa [scripts/sisaosa](https://github.com/markomanninen/tgd-geometry-lab/tree/main/scripts/sisaosa). OpenAI:n Codex tarkisti tulokset riippumattomasti kahdessa kierroksessa. Jännityksen kaava, avoin poikkileikkaus, tuotteen epävakaus, minimipintaperhe, genuksen $g$ lehti ja polynomiupotus vahvistuivat. Yleiset väitteet rajattiin tällä sivulla olevaan muotoon. Holomorfista $X^6$:ta koskevaa johtopäätöstä tarkistus ei vahvistanut, ja se on siksi kirjattu yhden esimerkin tulokseksi.

Auki ovat nämä kohdat:

- Ovatko pallomaiset pinnat ja genuksen $g$ lehti sallittuja H-J-pintoja.
- Kelpaako avoin poikkileikkaus säikeeksi, ja onko tasoon verrattu jännitys oikea suure.
- Mistä $T$ ja $G$ saavat arvonsa ilman sisäosan Kähler-termiä.
- Onko $J(M^4)$ poikittainen myös radalla.
- Reunatermin johto yleisille upotuksille.
- Holomorfisen $X^6$:n yleinen tapaus.
- Mitkä pinnat Laplacen ehto sallii, kun $CP_2$-koordinaatit riippuvat hyperkompleksisesta koordinaatista, ja mihin Kähler- ja tilavuusvaikutus silloin johtaa säikeille ja radoille.
