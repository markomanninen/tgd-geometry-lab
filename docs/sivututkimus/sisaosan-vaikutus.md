# Sisäosan vaikutus ja kaarevuusskalaari

Tämä sivu vertaa ehdokkaita TGD:n aika-avaruuspinnan sisäosan vaikutukseksi. Sisäosan vaikutus on avoin tutkimuskohde, ja sivu kokoaa, mihin kukin vaihtoehto johtaa. Ehdokkaita on kolme. Pelkkä tilavuus on Matti Pitkäsen linjaus 1.11.2026. Kaarevuusskalaaria ja tilavuutta Pitkänen pohti 2.11.2026 kysymyksenä. Kähler-vaikutusta ja tilavuutta lisäehdolla, jossa $CP_2$:n Kähler-funktio toteuttaa Laplacen yhtälön, hän ehdotti 3.11.2026. Pitkäsen mukaan 4.11.2026 kuva pysyy alkuperäisenä twistorinosto mukaan lukien, ja kaarevuusskalaari on tarpeeton. Hän perusteli 5.11.2026, miksi kaarevuusskalaari ei tuota minimaalipintoja. Laskut, lähteiden lukemisen ja päättelyn teki NeuroPaja 2.–5.11.2026. Tulokset koskevat mainittuja pintaluokkia, ja fysikaalisen tulkinnan tekee Pitkänen.

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
| Yksikkövuon suljettu tuotesäie, $\Lambda R_C^2\ll 4$ | $T\approx-1/(2G)$ | $T>0$ | Rajatapaus, joka ei kuulu ehdon pintoihin |
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

NeuroPajan laskussa koordinaatit $\xi^1=f(w)$ ja $\xi^2=g(w)$ ovat holomorfisia muuttujan $w$ suhteen, ja $K=\log(1+\lvert\xi^1\rvert^2+\lvert\xi^2\rvert^2)$. Vedetyn Kähler-funktion Laplacen operaattori on silloin derivaatan $\partial_w\xi$ normin neliö Fubini–Studyn metriikassa.

$$
\partial_w\partial_{\bar w}K=\frac{\lvert f'\rvert^2+\lvert g'\rvert^2+\lvert fg'-gf'\rvert^2}{(1+\lvert f\rvert^2+\lvert g\rvert^2)^2}.
$$

Lauseke on nolla vain, kun $f'=g'=0$. NeuroPajan laskussa ehto ei siis salli riippuvuutta poikittaisesta koordinaatista $w$ niissä kohdissa, joissa pinta on säännöllinen, ja $CP_2$-koordinaatit riippuvat silloin vain pitkittäisistä koordinaateista. Sama tulos on [tulossivulla](../tulokset.md) poikittaisen virran ehtona, jossa Fubini–Study-metriikan vetäisyn pitää olla litteä. Laplacen ehto on saman ehdon toinen muoto.

NeuroPaja laski 3.11.2026 ehdon seuraukset viidestä suunnasta.

**Kosminen säie.** Säikeellä $M^2\times CP_1$ poikittainen koordinaatti on $CP_1$:n koordinaatti, eli $\xi=w$. Silloin $\partial_w\partial_{\bar w}K=1/(1+\lvert w\rvert^2)^2$, joka ei ole missään nolla. Tämä Laplacen operaattori on säikeen monopolivuon tiheys. Ehto sulkee siis pois monopolivuoputket, ellei niitä lueta singulariteeteiksi.

**Singulariteetit.** Navalla $\xi=1/w$ Laplacen operaattori on navan ulkopuolella sama $1/(1+\lvert w\rvert^2)^2$. Poikittaisen tason pisteet vastaavat aika-avaruudessa fermionisäikeitä ja säiemaailmanpintoja. Pisteet eivät jaa tasoa osiin, joten säännöllinen alue on yhtenäinen, ja ehto tekee $\xi$:stä vakion koko alueessa. Poikittainen riippuvuus ei siis voi olla pelkästään pistemäisissä singulariteeteissa. Se voisi olla vain tason jakavissa viivoissa, jotka ovat aika-avaruudessa kolmiulotteisia seinämiä, ja niiden yli $\xi$ hyppäisi, jolloin pinta ei ole jatkuva.

**Hyperkompleksinen luenta.** Jos $\xi$ riippuu koordinaateista $u$ ja $v$, poikittainen Kähler-kenttä häviää ja pitkittäinen komponentti $J_{uv}$ jää. Pinnalla $\xi=(u+iv)/2$ eivät häviä kenttäyhtälöiden Kähler-osa eikä tilavuusosa. Samoin käy pinnoilla $\xi=uv/3+iu/2$, $\xi=(t+iz)/3$ ja $\xi=v\,e^{iu}/4$. Pinnalla $\xi=e^{i(u-v)/2}/2$ Kähler-osa häviää, mutta tilavuusosa ei. Ainoa testattu ratkaisu on $\xi=u/2$, joka on massattoman ekstremaalin tyyppiä, ja sillä induusoitu Kähler-muoto on nolla. Laskut eivät osoita, ettei muita ratkaisuja ole.

**Ei-holomorfinen luenta.** Jos $\xi$ saa riippua muuttujista $w$ ja $\bar w$, ehdolla on muitakin ratkaisuja. Esimerkiksi $\xi=\sqrt{e^{ax}-1}$ antaa lineaarisen funktion $K=ax$. Kähler-muoto on silloin nolla, koska $\xi$ riippuu vain yhdestä koordinaatista, mutta pinta ei ole minimipinta. Tällainen pinta ei myöskään kuulu H-J-rakenteen holomorfisiin pintoihin.

**H-J-koordinaatit Kähler-funktiosta.** Pitkäsen ehdotuksessa H-J-koordinaatit rakennetaan induusoidusta Kähler-potentiaalista. Valon kaltaisen koordinaatin gradientti on valon kaltainen. Funktion $K$ gradientin neliö on $4K_uK_v$, joten se on valon kaltainen vain, jos $K$ riippuu yhdestä valon kaltaisesta koordinaatista. Pinnalla $\xi=(u+iv)/2$ näin ei ole, joten rakenne palauttaa valon kaltaisen koordinaatin vain massattoman ekstremaalin tyyppisillä pinnoilla.

**Twistorinosto.** Aiempi tulos oli, että Yang–Millsin neliötermillä on kompleksikäyrillä sama ensimmäinen variaatio kuin Kähler-termillä. Laplacen ehdolla este häviää siis täsmälleen silloin, kun kenttäyhtälöiden Kähler-osa häviää. Testatuista pinnoista näin käy pinnalla $\xi=u/2$, jolla Kähler-muoto on nolla. Kysymys palautuu siksi hyperkompleksisen luennan ratkaisuihin.

NeuroPaja kysyi Pitkäseltä, koskeeko ehto vain osaa pinnoista ja tarkoittaako hän riippuvuutta pelkästä koordinaatista $u$ vai hyperkompleksisesta koordinaatista $t+ez$.

### Pitkäsen vastaus 4.11.2026

Pitkäsen mukaan perus-H-J-rakenne syntyy, kun $M^4$ jaetaan säiemaailmanpinnoiksi $X^2$ ja niitä vastaan kohtisuoriksi partonipinnoiksi $Y^2$. Molemmat pinnat ovat minimaalipintoja. Kohtisuoruusehdon toteuttaminen on hänen mukaansa avoin matemaattinen ongelma. Litteä jako on erikoistapaus, ja jokainen jako määrää oman H-J-rakenteensa. Indusoitu Kähler-rakenne on tämän rakenteen deformaatio konformikuvauksen vastineella, ja deformaatioon liittyy singulariteetteja.

Pitkäsen mukaan NeuroPajan päättely ei salli paikallisia singulariteetteja, vaikka ne ovat ajatuksen ydin. Hän vertaa tilannetta kaksiulotteiseen sähköstatiikkaan, jossa Laplacen yhtälön ratkaisuilla on varauksia, viivavarauksia ja dipoleja. Ne merkitsevät holomorfian rikkoutumista. Singulariteetin ympärillä on alue, jossa upotus rikkoutuu, ja sen tilalle tulee partonipinta, jonka sisällä on euklidinen alue.

Kosminen säie on Pitkäsen mukaan rajatapaus, koska sen projektio $M^4$:ään on kaksiulotteinen. Säie kuuluu samaan luokkaan kuin $CP_2$-tyyppiset ekstremaalit. H-J-deformaatioiden projektio on neliulotteinen, ja niillä Kähler-virta häviää. Monopolivuoputken magneettikenttä ei tarvitse virtoja, mikä Pitkäsen mukaan ratkaisee pitkän kantaman magneettikenttien vakauden ongelman.

Ratkaisuyritteen $\xi^k=f_k(u,w)$ perusoletus on Pitkäsen mukaan, että funktiot riippuvat pitkittäisistä koordinaateista vain koordinaatin $u$ kautta. Silloin $J_{uv}=0$. Testi vahvistaa tämän pinnalla $\xi=uw/3$.

### Singulariteetit ei-holomorfisella $\xi$:llä

Kun $\xi$ on holomorfinen muuttujan $w$ suhteen, poikittainen Kähler-kenttä on sama lauseke kuin vedetyn Kähler-funktion Laplacen operaattori, eli $J_{w\bar w}=i\,\partial_w\partial_{\bar w}K$. Lauseke on positiivinen kaikkialla, missä $\partial_w\xi\neq 0$. Navan $\xi=1/w$ kenttä ei siksi keskity napaan vaan levittäytyy koko tasoon.

Kaksiulotteisen sähköstatiikan monopolia vastaa funktio $K=\log\lvert w\rvert^2$, joka on harmoninen kaikkialla paitsi origossa. NeuroPajan laskussa tällainen $K$ syntyy ehdosta $1+\lvert\xi\rvert^2=\lvert w\rvert^2$, joka on mahdollinen vain ei-holomorfisella $\xi$:llä. Ehto toteutuu vain, kun $\lvert w\rvert\ge 1$, joten pinnassa on singulariteetin ympärillä reikä, jossa upotusta ei ole. Tämä vastaa Pitkäsen kuvaa alueesta, jossa upotus rikkoutuu.

Pinta riippuu siitä, miten $\xi$:n vaihekulma valitaan, ja NeuroPaja laski kaksi valintaa:

- Kun $\xi=w\sqrt{1-1/\lvert w\rvert^2}$, funktio $K$ on harmoninen, mutta poikittainen Kähler-kenttä on $J_{xy}=1/\lvert w\rvert^4$. Kenttäyhtälöiden Kähler-osa ei häviä.
- Kun $\xi=\sqrt{\lvert w\rvert^2-1}$ on reaalinen, Kähler-muoto on nolla, mutta tilavuusosa ei häviä, joten pinta ei ole minimipinta.

Ei-holomorfisella $\xi$:llä poikittainen kenttä ei ole $i\,\partial_w\partial_{\bar w}K$, joten harmoninen $K$ ei hävitä kenttää. Laskussa $M^4$-koordinaatit ovat litteän H-J-rakenteen koordinaatit. Pitkäsen kuvaama konformikuvauksen vastine muuttaa myös $M^4$:n puolta, eikä sitä ole vielä laskettu.

Holografia = holomorfia -periaatteessa pinta on analyyttisten funktioiden yhtälöiden $f_1=f_2=0$ ratkaisu, joten $CP_2$-koordinaatit ovat holomorfisia muuttujan $w$ suhteen. Konformikuvauksen vastine ei muuta tätä, koska kaksiulotteinen Laplacen operaattori on konformisti invariantti. Kun $w=\phi(z)$ on holomorfinen, pätee

$$
\partial_z\partial_{\bar z}K=\lvert\phi'\rvert^2\,\partial_w\partial_{\bar w}K,
$$

joten Laplacen lauseke on positiivinen missä tahansa holomorfisessa koordinaatissa, jossa $\xi$ riippuu poikittaisesta koordinaatista. Holomorfisilla pinnoilla Laplacen ehto tekee siis $\xi$:stä riippumattoman poikittaisesta koordinaatista jokaisessa koordinaatistossa, joka saadaan holomorfisella koordinaatinvaihdolla. Jos Pitkäsen deformaatio on yleisempi kuin holomorfinen koordinaatinvaihto, tulos pitää laskea erikseen.

Navan kohdalla affiinissa kartassa laskettu $K$ käyttäytyy kuten $-\log\lvert w\rvert^2$, ja sen Laplacen operaattori antaa distribuutiona pistemäisen termin $-\pi\delta$. Termi syntyy kartan valinnasta, koska $K$ on vain paikallinen potentiaali. Meromorfinen $\xi$ on sileä kuvaus avaruuteen $CP_2$, joten vedetty Kähler-muoto on navassa sileä eikä sisällä pistevarausta. Pitkäsen mukaan singulariteetit merkitsevät holomorfian rikkoutumista, joten riippuvuus poikittaisesta koordinaatista voi olla vain alueissa, joissa holomorfia rikkoutuu. Holomorfisessa alueessa ehto jättää jäljelle pinnat $\xi=\xi(u)$. Niillä koko poikittainen taso kuvautuu yhteen $CP_2$:n pisteeseen, joten Kähler-muoto on kokonaan nolla, myös komponentit $J_{uw}$. Testissä pinta $\xi^1=e^{iu}/2+u^2/3$, $\xi^2=\sin(u)/4$ ratkaisee sekä Kähler-osan että tilavuusosan. Singulariteettialueiden ulkopuolella pinta on siis Kähler-tyhjiö.

Tästä seuraa, että singulariteetin ympärillä ei ole Kähler-kenttää, joten siellä ei ole Coulombin kenttää. Silmukka, joka kiertää singulariteetin poikittaisessa tasossa, kuvautuu yhteen $CP_2$:n pisteeseen, joten vedetyn Kähler-yhteyden holonomia silmukan yli on triviaali. Triviaali holonomia ei kuitenkaan estä vuota silmukan sisällä, koska holonomia määrää vuon vain vuokvantin monikertoja vaille. Reiän sisällä voi siis olla kvantittunut magneettivuo, kuten monopolivuoputkessa, vaikka kenttä reiän ulkopuolella on nolla. Kaikki Kähler-kenttä on alueissa, joissa holomorfia rikkoutuu. Monopoliesimerkissä tällainen alue on reikä, jonka reunalla $\xi=0$. Onko reuna partonipinta, on Pitkäsen fysikaalinen tulkinta. OpenAI:n Codex tarkisti päättelyn riippumattomasti 4.11.2026 ja lisäsi holonomiaa ja deformaatiota koskevat varaukset.

### Pallomainen jako

Pitkäsen mukaan myös pallomainen jako tuottaa H-J-rakenteen. Siinä $u$ ja $v$ ovat $t\mp r$, säiemaailmanpinnat ovat $(t,r)$-tasoja ja partonipinnat ovat palloja, joilla $t$ ja $r$ ovat vakioita. NeuroPajan laskussa $(t,r)$-taso on $M^4$:ssä minimaalipinta. Pallon keskikaarevuus on sen sijaan $(2/r_0)\,\hat r$, joten pallo ei ole minimaalipinta $M^4$:ssä. Pallomaisen jaon pallot eivät voi olla minimaalipintoja myöskään $CP_2$-deformaation jälkeen. Avaruudessa $H=M^4\times CP_2$ keskikaarevuuden $M^4$-komponentit ovat pinnan Laplacen operaattori sovellettuna $M^4$-koordinaatteihin, koska $M^4$ on litteä ja tulometriikalla ei ole sekatermejä. Avaruuden kaltaisen pinnan metriikka on definiitti, joten minimaalipinnalla jokainen $M^4$-koordinaatti on harmoninen funktio. Suljetulla pinnalla harmoninen funktio on vakio, joten suljetun minimaalipinnan $M^4$-projektio on piste. Testissä pallo $r=r_0$, joka yhdistetään $CP_1$:een kuvauksella $\xi=\tan(\theta/2)\,e^{i\phi}$, ei ole minimaalipinta. Päättely koskee pintoja, joilla ei ole reunaa ja joiden metriikka ei rappeudu, ja se koskee vain pinta-alafunktionaalin kriittisiä pintoja. Artikkelin *Holography and Hamilton-Jacobi Structure as a 4-D generalization of 2-D complex structure* (2024) kohdassa 2.3 Pitkänen toteaa saman. Hänen mukaansa pallomaisissa koordinaateissa pallot eivät ole minimaalipintoja, mutta $M^2(x)$ integroituu tasoksi, joka on minimaalipinta. Viestissä 4.11.2026 molemmat pinnat ovat minimaalipintoja. Suljetuilla partonipinnoilla vaatimus voi siis toteutua vain, jos partonipinnan $M^4$-projektio on piste, tai jos minimaalisuus tarkoittaa jonkin muun funktionaalin kuin pinta-alan kriittisyyttä. Pistemäinen $M^4$-projektio on $CP_2$-tyyppisen ekstremaalin partonipinnalla, jonka $M^4$-projektio on valon kaltainen käyrä ja jonka jokainen aikaviipale on $M^4$:ssä piste. Tiukassa mielessä vaatimus toteutuu siis litteässä jaossa ja $CP_2$-tyyppisillä partonipinnoilla mutta ei pallomaisen jaon palloilla, mikä on sama kuin artikkelin kohdassa 2.3.

### Minimaalisuus kolmiulotteisessa avaruudessa

Pitkänen selvitti 4.11.2026, mitä tiedetään jaoista, joissa säieradat ja kaksiulotteiset pinnat ovat toisiaan vastaan kohtisuoria minimaalipintoja. Hänen mukaansa $M^4$:ssä tällaisia jakoja on vähän ja ne tunnetaan. Niiden partonipinnat ovat ei-kompakteja minimaalipintoja avaruudessa $E^3$, säikeet ovat ei-dynaamisia, ja partonipinnat voivat pyöriä. Kausaalisessa timantissa (CD) luonteva kolmiulotteinen avaruus on hyperbolinen avaruus $H^3$, ja jakoja on paljon. Partonipinnat voivat silloin olla kompakteja, ja Pitkänen näkee yhteyden tessellaatioihin.

Pitkäsen tarkoittama minimaalisuus koskee siis pintaa kolmiulotteisessa avaruudessa $E^3$ tai $H^3$ eikä avaruudessa $M^4$ tai $H$. Edellä johdettu tulos, että suljetun minimaalipinnan $M^4$-projektio on piste, koskee minimaalisuutta avaruudessa $M^4$ tai $H$, joten se ei ole ristiriidassa Pitkäsen kuvan kanssa. NeuroPajan laskussa pinta, joka on minimaalinen hyperboloidilla $t^2-r^2=a^2$, ei ole minimaalinen $M^4$:ssä. Esimerkiksi hyperboloidin kokonaan geodeettisen tason $H^2$ keskikaarevuus $M^4$:ssä on $-(2/a^2)(t,x,y,0)$, eli se osoittaa hyperboloidin normaalin suuntaan.

Kompakti minimaalipinta vaatii $H^3$:ssa lisärakenteen. Yksinkertaisesti yhtenäisessä avaruudessa, jonka kaarevuus on kaikkialla ei-positiivinen, ei ole suljettuja minimaalipintoja, koska etäisyyden neliö on siellä aidosti konveksi funktio ja maksimiperiaate pätee. Testissä $H^3$:n geodeettisen pallon keskikaarevuus on $2\coth\rho_0$. Suljettuja minimaalipintoja on sen sijaan äärellisen tilavuuden hyperbolisissa avaruuksissa $H^3/\Gamma$, jotka syntyvät, kun $H^3$ jaetaan diskreetin ryhmän $\Gamma$ mukaisiin kopioihin. Tällainen jako on tessellaatio, joten Pitkäsen mainitsema äärellinen tilavuus ja yhteys tessellaatioihin ovat kompaktien partonipintojen edellytys. Toinen mahdollisuus on, että pinnalla on reuna CD:n reunalla.

### Pitkäsen vastaukset aiempiin kysymyksiin 4.11.2026

Pitkänen vastasi 4.11.2026 toisessa viestissään viiteen kysymykseen, jotka NeuroPaja oli esittänyt 2.11.2026.

Väite, että holografia = holomorfia pätee kaikille indusoidusta geometriasta määräytyville vaikutuksille, oli Pitkäsen mukaan spekulaatio. Kaarevuusskalaaria ei tarvita, jos twistorinosto toimii. Olennaista on, että H-J-rakenne on konsistentti ratkaisutyypin kanssa ja että Kähler-varaukset keskittyvät singulariteetteihin. H-J-rakenteen määrittelevät säierata ja kaksiulotteinen partonipinta minimaalipintoina, ja niiden täytyy hänen mukaansa olla kohtisuorassa, jotta metriikassa ei ole ristitermejä $g_{uw}$. Silloin metriikka on tyyppiä $(1,1)$, ja Pitkänen arvelee, että myös Einsteinin tensori on.

Pitkänen kysyi, unohtuiko kaarevuusskalaarin laskuissa oletus, että $\xi$ riippuu pitkittäisistä koordinaateista vain $u$:n kautta. Johtopäätökset tehtiin pinnoilla $\xi(w)$ ja $\xi(u,w)$. Ainoa pinta, joka riippui sekä $u$:sta että $v$:stä, oli $\xi=uvw$, ja se oli testissä merkitty ratkaisuyritteen ulkopuoliseksi vertailuksi.

Vuoputki ei Pitkäsen mukaan pääty tasaiseen $M^4$-lehteen. Sen poikkileikkaus on suljettu pinta, jota ei voi toteuttaa yhtenä lehtenä $M^4$:ssä. Kosmisen säikeen deformaationa vuoputken $M^4$-projektio on $E^3$:n äärellinen alue ilman reunaa, joten vuoputki on vähintään kaksilehtinen, kuten pallo, jonka yläpinta kääntyy alapinnaksi. Avoin poikkileikkaus $\xi=w/\lambda$ ei siis vastaa hänen kuvaansa. Jos suljetun poikkileikkauksen pitäisi olla minimaalipinta avaruudessa $H$, edellä johdettu tulos estäisi sen, koska poikkileikkauksen $M^4$-projektio on kiekko eikä piste.

Kaava $\hbar G=pR_C^2\exp(-2aS_K)$ on Pitkäsen mukaan aiempi arvaus. Uskottavimpana hän pitää selitystä Planckin vakioiden hierarkiasta. Siinä $l_P^2(\hbar_0)=R^2$, ja kun $\hbar=7!^2\hbar_0$, Planckin pituuden neliö pienenee tekijällä $\hbar_0/\hbar$. Hänen mukaansa argumentti on hatara, koska TGD:ssä ei ole polkuintegraalia eikä sen häiriöteoriaa. Toisenlainen tulkinta on artikkelissa *About the relationship of electroweak and strong interactions in the TGD Universe: part III*.

Partoniradalla Kähler-muodolla voisi periaatteessa olla sähköinen osa, mutta reunaehdot viittaavat Pitkäsen mukaan vahvasti siihen, että se häviää samoin kuin metriikan vastaava komponentti. Oletus on, että Kähler-muoto on puhtaasti magneettinen ja siksi poikittainen kaikkialla paitsi singulariteeteissa. Kvanttilukujen vaihto ympäristön kanssa tapahtuu singulariteeteissa, eli särmissä ja fermioniviivojen pisteissä, joissa fermionin liikemäärä voi muuttua.

Partoniradan kysymykseen vastaa Pitkäsen artikkeli *About the relationship of electroweak and strong interactions in the TGD Universe: part I*. Sen kohdan 2.1.3 mukaan radan valon kaltaisuus tekee metriikasta ja Kähler-muodosta poikittaisia, ja kohdan 4.2 mukaan $J(M^4)$:llä on vain poikittainen osa $J_{w\bar w}$. Kohdan 2.1.1 reunaehdossa isometriavirran normaalikomponentin hyppy radalla on yhtä suuri kuin radalla kulkeva K-C-S-virta. Kohta 4.2 toteaa, että poikittaisella $B(M^4)$:llä K-C-S-tiheyden $M^4$-osa häviää, ja suosii vaihtoehtoa, jossa $B_t(M^4)$ on vakio. Värin vaihtoa sisäosan ja radan välillä artikkeli ei mainitse.

Kosmisen säikeen gravitaatiomassan pitäisi Pitkäsen viimeisen arvion mukaan olla vastakkaismerkkinen, jolloin vain pallomainen poikkileikkaus antaisi negatiivisen energian. Kerroin $1/16\pi G$ tulee kaarevuusskalaarin kertoimesta, ja Pitkänen on valmis unohtamaan kaarevuusskalaarin.

Vaikutuksen R + tilavuus Noether-tensori, partoniradan Gibbonsin–Hawkingin–Yorkin reunatermi ja kaarevuusosan virran hajaantuminen koskivat kaarevuusskalaaria, joten ne eivät enää koske Pitkäsen linjaamaa vaikutusta. Twistoripallon tilavuustermi tulee Pitkäsen mukaan twistoriavaruuden Kähler-vaikutuksesta eikä kaarevuusskalaarista. Yang–Millsin neliötermin este palautuu samaan kysymykseen kuin kenttäyhtälöiden Kähler-osa.

H-J-määritelmän ehto $g^{uu}=g^{vv}=0$ antaa viivaelementin kertoimille $B=D=0$. Tämä on sama ehto kuin Pitkäsen 4.11. mainitsema kohtisuoruusehto, jonka mukaan säiemaailmanpinnat ja partonipinnat ovat toisiaan vastaan kohtisuorassa.

### Pitkäsen vastaukset 5.11.2026

Pitkänen vastasi 5.11.2026 neljällä kohdalla. Ne koskevat jakoja avaruuksissa $E^3$ ja $H^3$, tekijäavaruuksia $H^3/\Gamma$, kenttäviivojen synnyttämiä pintoja ja syytä siihen, että kaarevuusskalaari ei tuota minimaalipintoja. NeuroPaja arvioi kohdat laskulla ja lähteillä, ja OpenAI:n Codex tarkisti jakoja koskevan päättelyn riippumattomasti 5.11.2026.

#### Einsteinin tensorin tyyppi

Pitkäsen selityksen mukaan kaarevuustensori sisältää metriikan toisia derivaattoja, ja indusoitu metriikka riippuu sekä koordinaateista $u$ ja $w$ että niiden konjugaateista $v$ ja $\bar w$. Siksi Einsteinin tensorilla on tyypin $(1,1)$ komponenttien lisäksi tyyppien $(2,0)$ ja $(0,2)$ komponentteja, eikä sen supistus toisen perusmuodon kanssa häviä. Pitkänen päättelee, että twistorinoston Kähler-vaikutus ja tilavuus on ainoa vaihtoehto, jos halutaan kosmologinen vakio ja minimaalipinnat. Viestissä 4.11.2026 hän oli arvellut, että Einsteinin tensori on tyyppiä $(1,1)$.

NeuroPaja laski Einsteinin tensorin $G^{ab}$ ja supistuksen $G^{ab}B^k{}_{ab}$ kompleksikoordinaateissa $(u,v,w,\bar w)$. Tyypin $(1,1)$ komponenteissa toinen indeksi on joukosta $\{u,w\}$ ja toinen joukosta $\{v,\bar w\}$. Tulokset riippuvat H-J-rakenteesta.

Litteässä rakenteessa, jossa $u=t-z$, pinnalla $\xi=uw/3$ supistus on symbolisesti nolla kaikissa kahdeksassa komponentissa, joten pinta ratkaisee myös vaikutuksen R + tilavuus. NeuroPajan laskussa myös pinnalla $\xi^1=uw/3$, $\xi^2=w^2/5+\sin(u)/7$ supistus on nolla yhdessä kokeillussa pisteessä. Pitkäsen havainto pitää silti paikkansa, sillä komponentti $G^{vv}$ ei ole nolla. Se kohtaa kuitenkin vain toisen perusmuodon komponentteja, joissa on indeksi $v$, ja ne ovat nollia, koska pinta ei riipu koordinaatista $v$. Tämä vastaa vertailutaulukon riviä, jonka mukaan litteän rakenteen holomorfiset pinnat ratkaisevat vaikutuksen R + tilavuus.

Pallomaisessa rakenteessa $u$ ja $v$ ovat $t\mp r$, ja metriikan pallo-osa $r^2d\Omega^2$ riippuu säteestä $r=(v-u)/2$, siis myös koordinaatista $v$. Pinta $\xi=2w$ on tässä rakenteessa minimaalipinta, mutta supistus ei ole nolla, joten pinta ei ratkaise vaikutusta R + tilavuus. Toisella perusmuodolla on tässä tapauksessa myös tyypin $(1,1)$ komponentteja $B_{vw}$ ja $B_{u\bar w}$, Pinta ei riipu ajasta, joten $B_{tw}=B_{uw}+B_{vw}=0$, ja komponentti $B_{rw}=B_{vw}-B_{uw}$ jakautuu yhtä suuriin osiin $B_{vw}$ ja $-B_{uw}$. Siksi Einsteinin tensorin $(1,1)$-osa antaa testipisteessä tarkalleen puolet supistuksesta ja $(2,0)$- ja $(0,2)$-osat toisen puolen. Pitkäsen mekanismi, eli riippuvuus koordinaatista $v$, toteutuu siis pallomaisessa rakenteessa, mutta laskussa supistusta ei aiheuta pelkästään Einsteinin tensorin $(2,0)$- ja $(0,2)$-osa.

Laskun perusteella Pitkäsen johtopäätös pätee pallomaisessa rakenteessa, jonka hän katsoo kausaalisessa timantissa olennaiseksi. Litteässä rakenteessa myös vaikutus R + tilavuus sallii holomorfiset minimaalipinnat.

Pitkäsen mukaan $CP_2$:n Kähler-funktion Laplacen yhtälö yleistyy triviaalisti d'Alembertin yhtälöksi $M^4$:ssä, koska $K$ riippuu vain koordinaatista $u$. Valokartiokoordinaateissa d'Alembertin operaattori on

$$
\Box=4\,\partial_u\partial_v-4\,\partial_w\partial_{\bar w}.
$$

Ratkaisuyritteessä $\xi(u,w)$ pätee $\partial_vK=0$, joten $\Box K=-4\,\partial_w\partial_{\bar w}K$. D'Alembertin yhtälö ja poikittainen Laplacen yhtälö ovat siis sama ehto, ja ehdon jälkeen $K$ riippuu vain koordinaatista $u$.

#### Jaot avaruuksissa $E^3$ ja $H^3$

Pitkäsen mukaan jakoja, joissa partonipinnat ovat minimaalipintoja ja kohtisuorassa säieratoja vastaan, on vähän, jos partonipinta on avaruudessa $E^3$, mutta todella paljon, jos se on avaruudessa $H^3$. Hyperbolinen jako rajoittuu valokartion sisälle, ja Pitkäsen mukaan se on syy laajenevaan kosmologiaan, kausaaliseen timanttiin ja nollaenergiaontologiaan.

Valokartion sisällä Milnen koordinaatit $t=a\cosh\rho$, $r=a\sinh\rho$ antavat testissä metriikan

$$
ds^2=da^2-a^2\bigl(d\rho^2+\sinh^2\rho\,d\Omega^2\bigr).
$$

Tämä on Robertsonin–Walkerin metriikka, jonka avaruusosa on $H^3$ ja skaalatekijä $a$. Hyperboloidit $a=$ vakio täyttävät siis valokartion sisäosan laajenevina kopioina avaruudesta $H^3$, mikä on geometrinen pohja Pitkäsen kosmologiselle tulkinnalle.

Arvio riippuu siitä, vaaditaanko myös säieradoilta minimaalisuutta. Viestissä 4.11.2026 molemmat pinnat olivat minimaalipintoja, ja viestissä 5.11.2026 minimaalisuus mainitaan partonipinnoista. NeuroPajan päättely etenee neljässä vaiheessa:

1. Jos jokainen partonipinta on jollakin hyperboloidilla $a=$ vakio, säiemaailmanpinnan tangenttitaso sisältää säteittäisen suunnan $\partial_a$, koska $\partial_a$ on kohtisuorassa koko hyperboloidia vastaan. Säiemaailmanpinta on silloin kartio, jonka muodostavat origon kautta kulkevat suorat käyrän $\gamma\subset H^3$ yli. Testissä kartio on $M^4$:ssä minimaalipinta, kun $\gamma$ on $H^3$:n geodeesi, joka ei kulje akselin kautta, mutta ei, kun $\gamma$ on ympyrä. Kartion keskikaarevuus on käyrän $\gamma$ geodeettinen kaarevuus jaettuna luvulla $a$.
2. Jos säiemaailmanpinnat ovat minimaalipintoja, partonipintojen normaalikäyrät $H^3$:ssa ovat geodeesejä. Partonipinnat ovat silloin toistensa yhdensuuntaisia pintoja, eli niiden etäisyys toisistaan on vakio normaaligeodeesiä pitkin.
3. Yhdensuuntaisilla pinnoilla avaruudessa, jonka kaarevuus on $-1$, kumpikin pääkaarevuus noudattaa normaaligeodeesiä pitkin yhtälöä $k'=1-k^2$. Testi tarkistaa yhtälön geodeettisille palloille, ekvidistanttipinnoille ja horosfääreille. Jos jokainen partonipinta on minimaalipinta, pääkaarevuudet ovat $k$ ja $-k$, ja yhtälö pakottaa arvon $k^2=1$.
4. Pinnalla, jonka pääkaarevuudet ovat vakiot $+1$ ja $-1$, Codazzin yhtälöt tekevät sisäisestä kaarevuudesta nollan. Gaussin yhtälö antaa kuitenkin $K=-1+k_1k_2=-2$, joten tällaista pintaa ei ole.

Jos siis myös säiemaailmanpinnat ovat minimaalipintoja $M^4$:ssä, $H^3$:ssa ei ole yhtään tällaista jakoa edes paikallisesti. Avaruudessa $E^3$ sama päättely, jossa säiemaailmanpinnat ovat ajan ja käyrän tuloja, antaa yhtälön $k'=-k^2$, ja ainoa jako koostuu yhdensuuntaisista tasoista ja niitä vastaan kohtisuorista suorista. Codex vahvisti molemmat johtopäätökset.

Jos minimaalisuutta vaaditaan vain partonipinnoilta, Pitkäsen väitteelle on tunnettu perusta. Minimaalipintojen lehdityksen lehdet ovat stabiileja, ja täydelliset stabiilit minimaalipinnat avaruudessa $\mathbb R^3$ ovat tasoja (do Carmo–Peng 1979, Fischer-Colbrie–Schoen 1980, Pogorelov 1981). Täydellisten lehtien jako avaruudessa $E^3$ koostuu siksi yhdensuuntaisista tasoista. Avaruudessa $H^3$ jokainen äärettömyyspallon Jordanin käyrä rajaa täydellisen pinta-alaltaan minimaalisen kiekon (Anderson 1982), joten stabiileja minimaalipintoja on paljon. Codexin varauksen mukaan tämä osoittaa yksittäisten pintojen runsauden mutta ei sitä, että pinnat muodostavat jaon.

#### Tekijäavaruudet ja CD:n reuna

Pitkänen vahvisti, että avaruudessa $H^3$ ei ole reunattomia minimaalipintoja. Kausaalisen timantin sisällä partonipinnan reuna tulee siitä, että timantin puolikas on äärellinen. Tämä vastaa NeuroPajan 4.11.2026 esittämään kysymykseen, ja vastaus on, että partonipinnalla on reuna timantin reunalla. Testissä timantin, jonka kärjet ovat origo ja $Q=(T,0)$, viipale $a=$ vakio on $H^3$:n geodeettinen kuula, jonka säde yksikkökaarevuuden metriikassa on

$$
\rho_{\max}=\log\frac{T}{a},\qquad \sinh\rho_{\max}=\frac{T^2-a^2}{2Ta}.
$$

Kuulan reunapallo on timantin menneisyyskartiolla, joten kuulan minimaalipinnan reuna on timantin reunalla.

Pitkäsen mukaan $H^3$:sta saadaan tessellaatioiden avulla ääretön määrä kompakteja tekijäavaruuksia $H^3/\Gamma$, ja aika-avaruuspinta toteuttaa jaksollisuutta vastaavat reunaehdot. Hän vertaa tätä kuution samaistamiseen kolmitorukseksi. Kompakteja hyperbolisia 3-monistoja on todella äärettömän monta. Monisto syntyy kuitenkin vain, jos ryhmä $\Gamma$ toimii ilman kiintopisteitä. Tessellaation koko symmetriaryhmä sisältää peilauksia ja kiertoja, joilla on kiintopisteitä, ja sen tekijäavaruus on orbifoldi. Kolmitoruksen vertauksessa ryhmä koostuu pelkistä siirroista. Selbergin lemman (1960) mukaan jokaisella äärellisesti generoidulla matriisiryhmällä on äärellisen indeksin aliryhmä, jossa ei ole äärellisen kertaluvun alkioita. Diskreetissä ryhmässä kiintopiste on vain äärellisen kertaluvun alkioilla, joten tällainen aliryhmä toimii $H^3$:ssa ilman kiintopisteitä, ja jokaisesta kompaktista tessellaatiosta saadaan kompakti monisto, joka koostuu äärellisen monesta solusta. Myös kolmitoruksessa on suljettuja minimaalipintoja, esimerkiksi Schwarzin P-pinta, jonka genus on 3. Suljettujen minimaalipintojen olemassaolo ei siis erota avaruuksia $E^3$ ja $H^3$, kun jaksollisuus on mukana. Ikosatetraedrinen tessellaatio kvanttibiologiassa sekä tähtien ja galaksien tessellaatiot ovat Pitkäsen fysikaalisia tulkintoja, joita NeuroPaja ei arvioinut.

#### Kenttäviivojen synnyttämät pinnat

Pitkäsen spekulatiivisen ehdotuksen mukaan indusoitu metriikka ja Kähler-muoto synnyttävät kompakteja pintoja multipolikenttien kenttäviivoista. Tällaiset pinnat tuottaisivat monimutkaisemman jaon, jossa on singulariteetteja ja reikiä. Reikiin voi liittyä madonreikäkontakteja pienempiin tai suurempiin aika-avaruuslehtiin. Pinnoilla on genus, ja ne voitaisiin luokitella kompleksirakenteensa avulla.

Ehdotuksella on täsmällinen topologinen seuraus. Jos suljettu pinta koostuu kenttäviivoista, kenttä on pinnan tangentti, ja Poincarén–Hopfin lauseen mukaan tangenttikentän nollakohtien indeksien summa on pinnan Eulerin karakteristika $2-2g$. Kenttä, jolla ei ole nollakohtia, synnyttää siksi vain toruksia. Pallo ja genuksen $g\ge2$ pinnat vaativat kentän nollakohtia tai singulariteetteja, joiden indeksien summa on $2-2g$, mikä sopii Pitkäsen arvioon, että singulariteetteja syntyy. Esimerkiksi dipolin kenttäviivat $r=L\sin^2\theta$ muodostavat pyörähdyspinnan, joka kulkee dipolin kautta. Genuksen $g$ pinnan kompleksirakenteiden avaruuden kompleksinen dimensio on $3g-3$, kun $g\ge2$, toruksella 1 ja pallolla 0. Ehdotusta ei laskettu tämän pidemmälle.

Testit ovat tiedostossa [test-interior-string.mac](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-interior-string.mac).

#### Pitkäsen vastaukset 5.11.2026 iltapäivällä

Pitkänen vahvisti, että Einsteinin tensorin tyypit tarkoittavat jakoa, jossa $u$ ja $w$ ovat holomorfisia ja $v$ ja $\bar w$ niiden konjugaatteja. Hänen mukaansa Einsteinin yhtälöt eivät yleensä päde minimaalipinnoille, ja vain erikoistapauksissa, kuten vakiokaarevuusavaruudessa, $G^{w\bar w}$ on verrannollinen metriikkaan. Silloin supistus toisen perusmuodon kanssa on minimaalipinnalla nolla, koska toisen perusmuodon jälki on nolla.

Säieratojen minimaalisuus oli Pitkäsen mukaan puolitietoinen oletus. Hänen mukaansa hyperkompleksinen rakenne on kaksiulotteisen pinnan sisäinen ominaisuus, joka seuraa Minkowskin signatuurista, joten säieradan ei tarvitse olla minimaalipinta, eikä ehkä partonipinnankaan. Myöhemmissä viesteissään hän kertoi, että Googlen mukaan tessellaatioihin liittyvät säieradat ovat $H^3$:n tapauksessa $M^4$:n minimaalipintoja eli Nambu–Goto-säikeitä.

Jokaisella kaksiulotteisella pinnalla, jonka metriikalla on Minkowskin signatuuri, on paikallisesti valokoordinaatit, joissa pinnan metriikka on muotoa $e^f\,du\,dv$. H-J-rakenteessa $u$ ja $v$ ovat kuitenkin koko avaruusajan koordinaatteja, jotka ovat vakioita partonipinnoilla. Jokaisen säieradan omista valokoordinaateista saadaan tällaiset koordinaatit vain, jos säieradan metriikka on konformitekijää vaille sama kaikissa partonipinnan pisteissä. Kun partonipinnat ovat hyperboloideilla, säieradan metriikka on

$$
da^2-a^2\lambda^2ds^2,
$$

missä $\lambda$ on vierekkäisten partonipintojen etäisyys $H^3$:ssa jaettuna parametrin $s$ muutoksella. Yhteinen koordinaatti $u(a,s)$ on olemassa vain, jos $\lambda$ ei riipu paikasta partonipinnalla. Silloin normaalikäyrät ovat $H^3$:n geodeesejä, ja säierata on origon kautta kulkevan tason osa. Kun partonipinnat ovat hyperboloideilla, H-J-ehto tekee siis säieradoista Nambu–Goto-pintoja ilman erillistä oletusta, mikä sopii Googlen vastaukseen. Ilman hyperboloidioletusta säieradat voivat olla myös de Sitter -pintoja, jotka eivät ole minimaalipintoja. Esimerkiksi geodeesiä vastaan kohtisuorat tasot ovat kokonaan geodeettisia, mutta niiden säieradan metriikka on $da^2-a^2\cosh^2\!d\,ds^2$, joten yhteistä koordinaattia ei ole, ja säieradan keskikaarevuus on verrannollinen lukuun $\tanh d/a$.

Partonipintojen ehto koskee kompleksikoordinaattia $w$. Yhdensuuntaisen pinnan metriikka säilyy konformitekijää vaille samana vain, jos pinnan pääkaarevuudet ovat yhtä suuret. Hyperboloideilla jäljelle jäävät siksi geodeettiset pallot, horosfäärit ja tasosta vakioetäisyydellä olevat pinnat. Missään näistä perheistä kaikki partonipinnat eivät ole minimaalipintoja $H^3$:ssa, joten aiempi tulos pätee ilman oletusta säieratojen minimaalisuudesta. Yleinen luokittelu on konventioiden osiossa [H-J-rakenteiden luokittelu](../konventiot.md#h-j-rakenteiden-luokittelu).

Pitkänen tulkitsi Andersonin tuloksen niin, että laajenevan säikeen muoto on mielivaltainen. Andersonin tuloksessa Jordanin käyrä on $H^3$:n äärettömyyspallolla, joka Milnen kuvassa vastaa valokartion valonsäteiden suuntia, ja käyrä on minimaalikiekon reuna. Mielivaltainen muoto koskee siis partonipinnan reunaa valokartiolla.

Pitkäsen mukaan $H^3$:ssa ryhmä $\Gamma$ on ääretön ja korvaa siirtojen ryhmän. Selbergin lemma koskee kuitenkin alkioiden kertalukua eikä niiden määrää, sillä myös kolmitoruksen ryhmä $\mathbb Z^3$ on ääretön. Lemma takaa äärellisen indeksin aliryhmän, jonka epätriviaalit alkiot ovat kiintopisteettömiä. Pitkänen täydensi Poincarén–Hopfin kohtaa toteamalla, että kenttään syntyy sekä nollakohtia että napojen vastineita.

Testit ovat tiedostoissa [test-interior-string.mac](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-interior-string.mac) ja [test-hj-classification.mac](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-hj-classification.mac).

#### Pitkäsen kysymykset 5.11.2026 illalla

Pitkänen kysyi, onko NeuroPaja vai Googlen Gemini väärässä, kun Gemini sanoo integroituvan 2+2-jaon olevan olemassa. Tulokset ovat sopusoinnussa keskenään. Integroituvia jakoja on, ja mahdotonta on vain se, että säieradat ovat Nambu–Goto-pintoja ja partonipinnat samalla minimaalipintoja hyperboloideilla $H^3$. Pallojaossa säieradat ovat Nambu–Goto-pintoja mutta pallot eivät ole minimaalipintoja. Kun partonipinnat ovat geodeesiä vastaan kohtisuoria tasoja, ne ovat minimaalipintoja $H^3$:ssa, mutta säieradat eivät ole Nambu–Goto-pintoja.

Pitkänen arveli myös, että integroituvuus rikkoutuu koordinaatille $v$, koska sisäänpäin kulkevat valonsäteet suppenevat timantin kärkiä yhdistävälle aikajanalle, ja että tämä olisi syy siihen, että vain $u$-riippuvuus on mahdollinen. Milnen koordinaateissa $t=a\cosh\rho$, $r=a\sinh\rho$ valon kaltaiset käyrät antavat

$$
a\,e^{-\rho}=t-r,\qquad a\,e^{\rho}=t+r,
$$

joten molemmat koordinaatit integroituvat koko alueessa $r>0$. Pallomainen rakenne on singulaarinen aikajanalla $r=0$, jossa partonipallot kutistuvat pisteiksi. Kyse on koordinaatiston rajasta eikä integroituvuuden rikkoutumisesta. Pelkkä $u$-riippuvuus säilyttää minimaalisuuden horosfäärirakenteessa, jossa $\Box u=0$ ja $\Box v=4/(t-z)$, mutta ei pallomaisessa rakenteessa, jossa $\Box(t\mp r)=\pm2/r$.

#### Valokartion reunan viipalointi ja minimaalisuus $M^4$:ssä

Pitkäsen mukaan 6.11.2026 minimaalisuus ei ole välttämätöntä, ja H-J-rakenteeseen riittävät integroituva jako, kompleksinen ja hyperkompleksinen rakenne sekä kohtisuoruus. NeuroPajan luokittelun mukaan tarvitaan lisäksi, että lehdet ovat kokonaan napaisia, sillä muuten yhden partonipinnan kompleksikoordinaatti ei jatku naapuripinnan koordinaatiksi.

Pitkänen kysyi, ovatko sekä säieradat että partonipinnat minimaalipintoja, kun valokartio viipaloidaan siirtämällä sen reunaa aikajanaa pitkin. Viipalointi on pallomainen rakenne. Säieradat ovat $(t,r)$-puolitasoja, mutta pallo $t=t_0$, $r=r_0$ ei ole minimaalipinta. Sen keskikaarevuusvektorin $H$ pituus on $2/r_0$, ja valon kaltaisissa normaalisuunnissa $l=\partial_t+\partial_r$ ja $n=\partial_t-\partial_r$ sen komponentit ovat

$$
H\cdot l=-\frac{2}{r_0},\qquad H\cdot n=\frac{2}{r_0}.
$$

Suunta $l$ on valokartion generaattori, ja pistetulo $H\cdot l$ on kartion laajeneminen eli pallon alan suhteellinen kasvunopeus $2/r$ generaattoria pitkin. Kartion indusoitu metriikka $-r^2d\Omega^2$ on degeneroitunut, joten minimaalisuus ratkeaa pallon toisesta perusmuodosta $M^4$:ssä, ja sen laajenemisosa ei ole nolla. Kun $r_0$ pidetään kiinteänä ja $t_0=\sqrt{r_0^2+a^2}$, pallo on hyperboloidilla $t^2-r^2=a^2$, ja keskikaarevuus jakautuu hyperboloidin aikasuuntaisen yksikkönormaalin $N$ suuntaiseen osaan ja $H^3$:n sisäiseen osaan,

$$
H\cdot N=-\frac{2}{a},\qquad H\cdot\nu=-\frac{2\coth\rho}{a},\qquad \coth\rho=\frac{t_0}{r_0},
$$

missä $\nu$ on pallon yksikkönormaali $H^3$:ssa. Rajalla $a\to0$ pallo lähestyy valokartion palloa, ja kumpikin osa kasvaa rajatta, mutta $H\cdot H=-4/r_0^2$ pysyy samana.

Pitkänen vastasi 6.11.2026 aamulla, että pallo on minimaalipinta valokartion reunan pintana, koska valokartio on metrisesti pallo ja radiaaliset deformaatiot eivät muuta alaa. Valokartion $t=r$ leikkauksen $r=R(\theta,\phi)$ indusoitu metriikka on

$$
ds^2=-R(\theta,\phi)^2\,d\Omega^2,
$$

koska termit $dt^2-dr^2$ kumoavat toisensa. Jokainen leikkaus on siis konformisesti pyöreä pallo, mikä sopii Pitkäsen konformi-invarianssiin. Ala $\int R^2\,d\Omega$ kuitenkin riippuu $R$:stä, ja generaattorin $l$ suuntainen toinen perusmuoto on $R\,d\Omega^2$, joten laajeneminen $2/R$ ei häviä millään leikkauksella. Pallo on alan minimi niiden leikkausten joukossa, joilla on sama keskisäde $\int R\,d\Omega$, sillä Cauchyn ja Schwarzin epäyhtälö antaa $\int R^2\,d\Omega\ge(\int R\,d\Omega)^2/4\pi$. Tasainen siirto ulospäin kasvattaa alaa. Hyperboloidin koordinaateissa $(r,\theta,\phi)$ pätee $g_{rr}=a^2/(a^2+r^2)\to0$, mutta $g^{rr}=(a^2+r^2)/a^2$ ja $\Gamma^r{}_{\theta\theta}=-r(a^2+r^2)/a^2$ kasvavat rajatta, kun $a\to0$. Alaindeksillä kirjoitettu komponentti $g_{rr}\Gamma^r{}_{\theta\theta}=-r$ pysyy äärellisenä, joten radiaalisen osan raja riippuu siitä, mikä komponentti on kyseessä. Valokartion oma toinen perusmuoto on nolla, kun toinen sen suunnista on generaattori, koska generaattorit ovat valon kaltaisia geodeeseja. Kulmasuuntien jälki $2/R$ ei häviä. NeuroPaja lähetti nämä laskut Pitkäselle 7.11.2026.

Yleinen tulos seuraa napaisuudesta. Kokonaan napaisella pinnalla $B^n{}_{ab}=\lambda_n g_{ab}$, joten minimaalisuus antaa $\lambda_n=0$, ja pinta on taso. Jos H-J-rakenteen kaikki säieradat ja partonipinnat ovat $M^4$:n minimaalipintoja, ne ovat siis tasoja. Partonipinnan $P$ läpi kulkevat säieradat ovat silloin saman tason yhdensuuntaisia siirtoja, ja muut partonipinnat ovat $P$:n yhdensuuntaisia siirtoja. Rakenne on paikallisesti litteä tulo $M^2\times E^2$. Muissa rakenteissa vain toinen perhe voi koostua minimaalipinnoista.

Hyperboloidilla oleva pinta ei ole koskaan $M^4$:n minimaalipinta. Hyperboloidin toinen perusmuoto on sen metriikka jaettuna $a$:lla, joten

$$
H_{M^4}=H_{H^3}+\frac{2}{a}\,N .
$$

Esimerkiksi $H^3$:n geodeettisella tasolla $H_{H^3}=0$, mutta $M^4$:ssä keskikaarevuusvektorin pituus on $2/a$. Sama koskee Jordanin käyrän rajaamia minimaalikiekkoja, jotka eivät myöskään ole napaisia.

Pitkäsen mukaan suunnistusongelma poistuu, jos Jordanin käyrän rajaama alue on pallonpuoliskolla. Lasku tukee tätä. Tasossa $(t,z)$ koordinaatti $u=t-r$ on puolitasolla $z>0$ sama kuin $t-z$ ja puolitasolla $z<0$ sama kuin $t+z$, joten koko taso ei ole yksi säierata, jolla $u$ ja $v$ olisivat sileitä valokoordinaatteja. Kun aikajana poistetaan ja $w$ rajataan pallonpuoliskolle, mikään säierata ei jatku aikajanan yli. Aikajana ei kuitenkaan erota $u$:ta $v$:stä, sillä $U$-käyrät lähtevät siitä ja $V$-käyrät päättyvät siihen. Timantissa, jonka kärjet ovat $t=0$ ja $t=t_1$, peilaus $t\to t_1-t$ vie koordinaatin $u$ koordinaatiksi $t_1-v$. Pallomainen rakenne on siksi geometrisesti symmetrinen $u$:n ja $v$:n vaihdossa. Peilaus vaihtaa kuitenkin myös timantin tulevan ja menneen reunan, joten avoin kysymys on, tuleeko $u$-$v$-epäsymmetria nollaenergiaontologiasta.

Pitkänen kysyi myös ryhmän $\Gamma$ äärellisestä aliryhmästä ja Platonin kappaleista. Oletetaan, että $\Gamma$ toimii vapaasti ja diskreetisti niin, että $H^3/\Gamma$ on hyperbolinen monisto. Cartanin kiintopistelauseen mukaan $H^3$:n isometrioiden äärellinen ryhmä kiinnittää aina pisteen, joten $\Gamma$:ssa ei ole epätriviaaleja äärellisiä aliryhmiä. Platonin kappaleiden kiertoryhmät ovat tessellaation koko symmetriaryhmän $G$ solujen keskipisteiden stabilisaattoreita, ja äärellinen ryhmä $G/\Gamma$ toimii $H^3/\Gamma$:n isometrioina, kun $\Gamma$ on $G$:n torsioton normaali aliryhmä. Monitahokkaan tahot ovat $H^3$:n geodeettisten tasojen paloja ja siten minimaalipintoja $H^3$:ssa. Saman H-J-rakenteen partonipinnat ovat jokaisessa $H^3$:ssa yhdensuuntaisia pintoja, joten yhden solun tahot eivät voi kaikki olla saman rakenteen partonipintoja.

#### Artikkeliluonnos 6.11.2026

Pitkänen lähetti 6.11.2026 artikkeliluonnoksen *Problems with Holography = Holomorphy Principle* ja pyysi tarkistamaan sen kaavat. NeuroPaja lähetti tarkistuksen hänelle. Tarkistuksessa syntyi kolme laskua, jotka täydentävät edellä olevaa säiejännityksen käsittelyä.

Arvolla $\Lambda=1/r^2+k/L_p^2$ pallon, jonka säde on $r$, jännitys on

$$
T=\frac{\Lambda\,4\pi r^2-4\pi}{8\pi G}=\frac{k\,r^2}{2G\,L_p^2}.
$$

Tuotteella $M^1\times X^2\times S^1$, jossa $S^1$:n pituus on $L$, energia on $(\Lambda S-2\pi\chi)L/(8\pi G)$, joten se on positiivinen täsmälleen, kun $S>2\pi\chi/\Lambda$. Pallon topologialla raja on $S>4\pi/\Lambda$. Sijoitus $G_0=x^2G$, $\hbar_0=\hbar/x^2$ säilyttää tulon $\hbar G$ ja siten Planckin pituuden, kun taas sijoitus $G_0=R^2/\hbar$ arvolla $R=x\,l_P$ tekee Planckin pituudesta luvun $R$.

Testit ovat tiedostoissa [test-hj-classification.mac](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-hj-classification.mac) ja [test-interior-string.mac](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-interior-string.mac).

### Pitkäsen vastaukset 8.11.2026

Pitkänen vastasi 8.11.2026, että valokartion reunan isometriaryhmä on ääretön ja vastaa poikkileikkauksen konformimuunnoksia. Hän arveli, että paikallinen radiaalinen deformaatio voidaan aina muuntaa isometriaksi, ja lisäsi artikkeliin perustelun, jonka mukaan pallo on minimaalipinta, kun degeneroituneen metriikan käänteiskomponentiksi valitaan $g^{rr}=0$. Pallon kompleksikoordinaatissa $z$ valokartion reunan $t=r$ metriikka on

$$
ds^2=-r^2\,\frac{4\,dz\,d\bar z}{(1+\lvert z\rvert^2)^2}.
$$

Jokaisella holomorfisella funktiolla $f$, jonka derivaatta ei häviä, kuvaus

$$
z\mapsto f(z),\qquad r\mapsto r\,\frac{1+\lvert f\rvert^2}{(1+\lvert z\rvert^2)\,\lvert f'(z)\rvert}
$$

säilyttää tämän metriikan. Jos $f$ riippuu myös $r$:stä, metriikkaan tulee $dr$:n sisältäviä termejä, joten isometriassa $f$ ei riipu $r$:stä. Leikkaus $r=R(\theta,\phi)$ on pallon $r=r_0$ kuva tällaisessa isometriassa täsmälleen silloin, kun sen Gaussin kaarevuus

$$
K=\frac{1-\Delta\log R}{R^2}
$$

on $1/r_0^2$. Tässä $\Delta$ on yksikköpallon Laplacen operaattori. Koko pallolla nämä leikkaukset ovat boostattuja palloja $R=r_0/(\cosh\beta-\sinh\beta\cos\theta)$. Ne ovat hypertasojen $t\cosh\beta-z\sinh\beta=r_0$ leikkauksia, ja niiden ala on $4\pi r_0^2$. Pienellä deformaatiolla $R=r_0(1+\epsilon h)$ pätee ensimmäisessä kertaluvussa $r_0^2K=1-\epsilon(\Delta h+2h)$, joten isometrisiä ovat vain pallofunktiot, joilla $l=1$. Vakioskaalaus $r\mapsto\lambda r$ muuttaa kaarevuuden arvoon $1/(\lambda r_0)^2$, joten mikään konformikuvaus ei kompensoi sitä, kun $\lambda\ne1$.

Valokartion reunan metriikka $q=r^2\,d\Omega^2$ muuttuu generaattorin $l=\partial_r$ suunnassa, sillä

$$
\mathcal L_l\,q=\frac{2}{r}\,q.
$$

Degeneroituneella metriikalla on vääntymätön konnektio, joka säilyttää metriikan, vain jos $\mathcal L_l q=0$. Jos nimittäin $\nabla q=0$ ja $q(l,\cdot)=0$, niin $q(\nabla_X l,Y)=0$, ja vääntymättömyyden avulla $(\mathcal L_l q)(X,Y)=q(\nabla_X l,Y)+q(X,\nabla_Y l)=0$. Kupeli kutsuu ehtoa $\mathcal L_l q=0$ stationaarisuudeksi. Valinnalla $g^{rr}=0$ lasketut Christoffelin symbolit eivät siksi säilytä metriikkaa $q$, ja esimerkiksi $\nabla_\theta q_{r\theta}=-r$. Alan ensimmäinen variaatio $\delta A=\int(2/R)\,\delta R\,R^2\,d\Omega$ ei riipu tästä valinnasta. Uudelleenskaalatulle metriikalle $d\Omega^2$ pätee $\mathcal L_l\,d\Omega^2=0$, ja siinä jokaisen leikkauksen ala on $4\pi$. Pitkäsen tulos pätee siis täsmälleen tässä konformisessa mitassa.

Inversio, jonka keskipiste on valokartiolla, vie valokartion valon kaltaiseksi hypertasoksi, ja kuvan metriikka ei riipu säteestä. Valon kaltaisen hypertason $t-z=u_0$ leikkauksen $t+z=V(x,y)$ metriikka on $-(dx^2+dy^2)$ jokaisella funktiolla $V$, joten siirrot generaattoreiden suuntaan ovat isometrioita. Leikkauksen keskikaarevuusvektori on valon kaltainen ja verrannollinen vektoriin $(\Delta V)\,l$, joten leikkaus on $M^4$:n minimaalipinta täsmälleen, kun $V$ on harmoninen. Horosfäärirakenteen partonipinnat ovat tällaisia leikkauksia, sillä niillä $t+z=(u_0v_0+x^2+y^2)/u_0$. Horosfäärirakenteessa partonipinnan ala ei siis muutu generaattoreiden suuntaisissa deformaatioissa.

Pitkänen huomasi, että hänen lisäehtonsa sanoo Kähler-virran olevan valon kaltainen. Pinnoilla $\xi^k=f^k(u,w)$ virralla ei ole yläindeksistä komponenttia $j^u$ missään H-J-rakenteessa, jonka indusoidulla metriikalla $g_{vv}=g_{vw}=0$, ja

$$
j\cdot j=-P\big((j^x)^2+(j^y)^2\big),
$$

missä $P$ on poikittainen metriikka. Virta on siis valon kaltainen täsmälleen silloin, kun sen poikittainen osa häviää, ja silloin koko Lorentzin 4-voima häviää. Pinnoilla $\xi^k=f^k(w)$ poikittainen virta häviää täsmälleen, kun $J_{w\bar w}/g_{w\bar w}$ ei riipu koordinaatista $w$. Pallomaisen rakenteen suoralla ja kartioleikkauksella koko virta häviää, vaikka $J_{w\bar w}\ne0$. Laplacen ehto $J_{w\bar w}=0$ on siis riittävä mutta ei välttämätön, ja valon kaltaisuus sallii pallomaisessa rakenteessa myös suoran ja kartioleikkauksen.

Puolipallolla, jonka reuna on geodeesi, sekä Gauss–Bonnet-termi että tilavuustermi ovat puolet pallon arvoista. Jännitys $(\Lambda R^2-1)/4G$ on siksi ei-negatiivinen täsmälleen, kun $\Lambda\ge1/R^2$, kuten pallolla. Arvo $1/(2R^2)$ syntyy, jos puolipallon Gauss–Bonnet-termi yhdistetään koko pallon tilavuustermiin.

NeuroPaja lähetti nämä laskut Pitkäselle 8.11.2026.

### Artikkelin viimeistely

Pitkäsen artikkeliluonnoksen luvuissa 3.3 ja 3.4 kaksi olemassaolokieltoa nojasi Geminin vastauksiin. NeuroPaja ehdotti 8.11.2026 illalla niiden tilalle kahta lyhyttä laskua. Avaruuden kaltaisen pinnan indusoitu metriikka on etumerkkiä vaille riemannilainen. Kun keskikaarevuusvektori $H$ on toisen perusmuodon jälki, Minkowskin lineaarisen koordinaatin $m^k$ Laplacen operaattori pinnalla antaa keskikaarevuusvektorin komponentin,

$$
\Delta m^k=H^k.
$$

Minimaalipinnalla jokainen $m^k$ on siis harmoninen, ja suljetulla pinnalla harmoninen funktio on maksimiperiaatteen mukaan vakio. $M^4$:ssä ei siksi ole suljettuja avaruuden kaltaisia minimaalipintoja. Hyperboloidin $H^3(a)$ minimaalipinnan keskikaarevuusvektori $M^4$:ssä on $(2/a)N$, missä $N$ on hyperboloidin tulevaisuuteen osoittava yksikkönormaali, joten

$$
\Delta m^0=\frac{2m^0}{a^2}>0.
$$

Suljetulla pinnalla $m^0$:n maksimikohdassa pitäisi olla $\Delta m^0\le0$, joten $H^3$:ssa ei ole suljettuja minimaalipintoja. NeuroPaja ehdotti samalla lähdeviitteitä. Suljettujen hyperbolisten 3-monistojen minimaalipinnat perustuvat Schoenin ja Yaun, Sacksin ja Uhlenbeckin, Freedmanin, Hassin ja Scottin sekä Kahnin ja Markovicin töihin. Jordanin käyrän rajaama minimaalinen taso perustuu Andersonin vuoden 1983 artikkeliin ja Coskunuzerin korjaukseen.

Pinnalla $M^1\times X^2\times S^1$ ympyrän $S^1$ pituus $2\pi R$ kertoo sekä tilavuustermin että kaarevuustermin. Tilavuustermi on $(\Lambda S/4G)R$, kun $S$ on pinnan $X^2$ ala. Pallon topologialla kaarevuustermi on jännitys $-1/(2G)$ kerrottuna pituudella $2\pi R$. Energia on

$$
E=\frac{(\Lambda S-4\pi)R}{4G},
$$

ja se on positiivinen täsmälleen, kun $S>4\pi/\Lambda$.

Pitkänen vastasi 9.11.2026, että hän lisäsi molemmat laskut ja lähdeviitteet artikkeliin ja yhtenäisti luvun 4.2.1 energiakaavat. Luvun 3.5 rajasta $a\to0$ hän kirjoitti kommentin, jonka mukaan rajan ei tarvitse olla jatkuva. Puolipallolle ei hänen mukaansa käytetä koko pallon tilavuustermiä, joten puolipallon raja on $\Lambda\ge1/R^2$ kuten pallolla.

Pitkänen ehdotti luvussa 3.4.2, että $H^3$ viipaloidaan minimaalisilla kiekoilla, joiden reunat ovat äärettömyyspallon ympyröitä, joilla napakulma $\theta$ on vakio. NeuroPajan 9.11.2026 lähettämän laskun mukaan ehdotus toimii. Ympyrää $\theta$ vastaa hyperboloidimallissa taso

$$
m^3=m^0\tanh s,\qquad \tanh s=\cos\theta.
$$

Taso on $H^3(\tau)$:n ja kärjen kautta kulkevan hypertason leikkaus, joten se on $H^3$:n totaalisesti geodeettinen taso. Jokainen $H^3(\tau)$:n piste on täsmälleen yhdellä tasolla, koska suhde $m^3/m^0$ on välillä $(-1,1)$. Sama hypertasojen perhe viipaloi jokaisen $H^3(\tau)$:n ja siten koko valokartion sisäosan. Tasoja vastaan kohtisuorat pinnat ovat $m^1=u\tau$, $m^2=v\tau$, missä $u$ ja $v$ ovat vakioita. Kukin niistä on kartio sellaisen $H^3$:n käyrän yli, joka pysyy vakioetäisyydellä $d$ akselista $m^1=m^2=0$, kun $\sinh d=\sqrt{u^2+v^2}$. Kartion keskikaarevuusvektori $M^4$:ssä on avaruuden kaltainen, ja sen pituus on

$$
\lvert H\rvert=\frac{\tanh d}{\tau}.
$$

Viipaloinnissa partonipinnat ovat siis minimaalisia $H^3$:ssa, mutta säiepinnat ovat $M^4$:n minimaalipintoja vain akselilla. Kartio koostuu kärjestä lähtevistä suorista, mutta se on minimaalinen vain, jos sen pohjakäyrä on $H^3$:n geodeesi.

Luvun 3.5 alan laskuun NeuroPaja lisäsi, että leikkauksen $r_M=R(\theta,\phi)$ metriikka $R^2\,d\Omega^2$ ja ala $\int R^2\,d\Omega$ käyttävät vain metriikan kovariantteja komponentteja. Lasku pätee siksi sekä valinnalla $g^{rr}=0$ että valinnalla $g^{rr}=\infty$. Arvolla $\Lambda=1/L_p^2$ edellä oleva energia on

$$
E=\frac{(S-4\pi L_p^2)R}{4GL_p^2}.
$$

Pitkänen lähetti 10.11.2026 uuden tiivistelmän ja johdannon. Niiden mukaan H-H-periaatteen universaalisuus kaatuu kahdessa testatussa tapauksessa, Kähler-vaikutuksella ja kaarevuusskalaarilla. Kaarevuusskalaari ei kuulu perusvaikutukseen. Kähler-vaikutuksen kaatuminen on vakavampi ongelma, koska twistorinosto antaa vaikutukseksi Kähler-vaikutuksen ja tilavuustermin summan. Korjauksena on ehto, jonka mukaan $CP_2$:n Kähler-funktio toteuttaa pinnalla poikittaisen kaksiulotteisen Laplacen yhtälön. Tiivistelmän mukaan ehto tekee Kähler-virran poikittaisen osan nollaksi singulaaristen pintojen ulkopuolella, ja silloin virta on valon kaltainen. Tämä on sopusoinnussa 8.11.2026 laskun kanssa, jonka mukaan H-J-ansatsin pinnoilla

$$
j\cdot j=-P\big((j^x)^2+(j^y)^2\big).
$$

Johdanto perustelee TGD:n yksikäsitteisyyden Hitchinin lauseella, jonka mukaan vain $M^4$:llä ja $CP_2$:lla on Kähler-rakenteinen twistoriavaruus. Hitchinin lause koskee kompakteja itseduaaleja neliulotteisia avaruuksia, ja niistä Kähler-rakenteinen twistoriavaruus on vain avaruuksilla $S^4$ ja $CP_2$. NeuroPaja kysyi 10.11.2026, miten $M^4$ tulee perusteluun mukaan.

Testit ovat tiedostossa [test-hj-classification.mac](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-hj-classification.mac) ja puolipallon ja energian osalta tiedostossa [test-interior-string.mac](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-interior-string.mac).

## Tarkistus ja rajat

Maxima-testit ovat tiedostoissa [test-interior-curvature.mac](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-interior-curvature.mac), [test-interior-energy.mac](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-interior-energy.mac) ja [test-interior-string.mac](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-interior-string.mac). Erilliset Python-skriptit ovat kansiossa [scripts/sisaosa](https://github.com/markomanninen/tgd-geometry-lab/tree/main/scripts/sisaosa). OpenAI:n Codex tarkisti tulokset riippumattomasti kahdessa kierroksessa. Jännityksen kaava, avoin poikkileikkaus, tuotteen epävakaus, minimipintaperhe, genuksen $g$ lehti ja polynomiupotus vahvistuivat. Yleiset väitteet rajattiin tällä sivulla olevaan muotoon. Holomorfista $X^6$:ta koskevaa johtopäätöstä tarkistus ei vahvistanut, ja se on siksi kirjattu yhden esimerkin tulokseksi.

Auki ovat nämä kohdat:

- Ovatko pallomaiset pinnat ja genuksen $g$ lehti sallittuja H-J-pintoja.
- Miten kaksilehtinen vuoputki, jonka poikkileikkaus on suljettu, toteutuu Laplacen ehdon ja minimaalipintaehdon kanssa.
- Reunatermin johto yleisille upotuksille.
- Holomorfisen $X^6$:n yleinen tapaus.
- Riittääkö Pitkäselle virran valon kaltaisuus, joka pallomaisessa rakenteessa sallii suoran ja kartioleikkauksen mutta litteässä rakenteessa vain Kähler-tyhjiön $\xi(u)$.
- Mistä $u$:n ja $v$:n epäsymmetria tulee pallomaisessa rakenteessa, joka on kausaalisessa timantissa symmetrinen niiden vaihdossa.
- Miten $M^4$ liittyy Hitchinin lauseeseen, joka antaa Kähler-rakenteisen twistoriavaruuden vain avaruuksille $S^4$ ja $CP_2$.

Pitkäsen vastaukset 5.11.2026 ja 6.11.2026 ratkaisivat kolme aiemmin tällä listalla ollutta kohtaa. Kohtisuoruusehto toteutuu H-J-rakenteessa, jonka lehdet ovat kokonaan napaisia. Säieradoilta ei vaadita minimaalisuutta. Einsteinin tensorin tyyppijako on sama $\{u,w\}$ ja $\{v,\bar w\}$, jota NeuroPajan lasku käyttää.
