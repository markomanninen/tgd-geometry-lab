# Sisäosan vaikutus ja kaarevuusskalaari

Tämä sivu vertaa ehdokkaita TGD:n aika-avaruuspinnan sisäosan vaikutukseksi. Sisäosan vaikutus on avoin tutkimuskohde, ja sivu kokoaa, mihin kukin vaihtoehto johtaa. Ehdokkaita on kolme. Pelkkä tilavuus on Matti Pitkäsen linjaus 1.11.2026. Kaarevuusskalaaria ja tilavuutta Pitkänen pohti 2.11.2026 kysymyksenä. Kähler-vaikutusta ja tilavuutta lisäehdolla, jossa $CP_2$:n Kähler-funktio toteuttaa Laplacen yhtälön, hän ehdotti 3.11.2026. Pitkäsen mukaan 4.11.2026 kuva pysyy alkuperäisenä twistorinosto mukaan lukien, ja kaarevuusskalaari on tarpeeton. Laskut, lähteiden lukemisen ja päättelyn teki NeuroPaja 2.–4.11.2026. Tulokset koskevat mainittuja pintaluokkia, ja fysikaalisen tulkinnan tekee Pitkänen.

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

Testit ovat tiedostossa [test-interior-string.mac](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-interior-string.mac).

## Tarkistus ja rajat

Maxima-testit ovat tiedostoissa [test-interior-curvature.mac](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-interior-curvature.mac), [test-interior-energy.mac](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-interior-energy.mac) ja [test-interior-string.mac](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-interior-string.mac). Erilliset Python-skriptit ovat kansiossa [scripts/sisaosa](https://github.com/markomanninen/tgd-geometry-lab/tree/main/scripts/sisaosa). OpenAI:n Codex tarkisti tulokset riippumattomasti kahdessa kierroksessa. Jännityksen kaava, avoin poikkileikkaus, tuotteen epävakaus, minimipintaperhe, genuksen $g$ lehti ja polynomiupotus vahvistuivat. Yleiset väitteet rajattiin tällä sivulla olevaan muotoon. Holomorfista $X^6$:ta koskevaa johtopäätöstä tarkistus ei vahvistanut, ja se on siksi kirjattu yhden esimerkin tulokseksi.

Auki ovat nämä kohdat:

- Ovatko pallomaiset pinnat ja genuksen $g$ lehti sallittuja H-J-pintoja.
- Miten kaksilehtinen vuoputki, jonka poikkileikkaus on suljettu, toteutuu Laplacen ehdon ja minimaalipintaehdon kanssa.
- Reunatermin johto yleisille upotuksille.
- Holomorfisen $X^6$:n yleinen tapaus.
- Hyväksyykö Pitkänen seurauksen, että Laplacen ehdolla kaikki Kähler-kenttä on alueissa, joissa holomorfia rikkoutuu, ja että niiden ulkopuolella pinta on Kähler-tyhjiö.
- Miten säiemaailmanpintojen ja partonipintojen kohtisuoruusehto toteutetaan.
- Hyväksyykö Pitkänen seurauksen, että suljettu minimaalinen partonipinta on $CP_2$-tyyppinen ja pallomaisen jaon pallot eivät ole minimaalipintoja.
