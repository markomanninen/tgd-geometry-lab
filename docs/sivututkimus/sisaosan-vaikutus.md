# Sisäosan vaikutus ja kaarevuusskalaari

Tämä sivu vertaa kahta ehdokasta TGD:n aika-avaruuspinnan sisäosan vaikutukseksi. Matti Pitkänen pohti 2.11.2026, voisiko sisäosassa olla kaarevuusskalaari ja tilavuus, ja hän muotoili ajatuksen kysymyksenä. Toinen ehdokas on pelkkä tilavuus, joka on hänen linjauksensa 1.11.2026. Laskut, lähteiden lukemisen ja päättelyn teki Claude 2.11.2026. Tulokset ovat ehdollisia, koska sisäosan vaikutus on avoin kysymys, ja fysikaalisen tulkinnan ratkaisee Pitkänen.

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

Taulukko näyttää, mitä kukin testi antaa. Jokainen rivi koskee vain mainittua pintaluokkaa, joten taulukko ei ole yleinen konsistenssitodistus kummallekaan ehdokkaalle.

| Testi | R + tilavuus | Pelkkä tilavuus |
|---|---|---|
| Litteän H-J-rakenteen holomorfiset pinnat | Ratkaisuja | Ratkaisuja |
| Pallomainen rakenne, pinnat $\xi(w)$ | Vain suora ja kartioleikkaus | Kaikki holomorfiset pinnat |
| Yksikkövuon tuotesäie, $\Lambda R_C^2\ll 4$ | $T\approx-1/(2G)$ | $T>0$ |
| Hajaantuminen radalla | Riippuu mallista | Ei hajaannu |
| Mistä $G$ tulee | Vaikutuksesta | Fermionisektorista, jos kirjan ennuste pätee |

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

Kuutiokäyrä täyttää Pitkäsen rakenteelliset ehdot, sillä kirjan mukaan $Y^2$ on $CP_2$:n kompleksinen alimonisto. Se ei silti riitä ratkaisuksi. Sen homologiavaraus on kolme, joten yksikkövuon holomorfinen säie on yhä $CP_1$, jolla $T\to-1/(2G)$. Kalibraation mukaan $A(Y)\ge\pi R_C^2$, joten ei-holomorfinen edustaja ei auta tuotteiden joukossa. Kirja myös sijoittaa galaktiset säikeet genukseen $g=0$.

### Etumerkki

Jännityksen negatiivinen osa ei riipu Noether-virran sopimuksesta. Vaikutus $S=-\tfrac{1}{16\pi G}\int\sqrt{\lvert g\rvert}\,(R+2\Lambda)$ supistuu tuotteella Nambu–Goto-muotoon $-T\int\sqrt{\lvert\gamma\rvert}$, ja kerroin $T$ on sama kuin edellä. Tässä käytetään tulosta $R=-2K$. Positiivinen tilavuusenergia kiinnittää vaikutuksen kokonaismerkin, ja de Sitter -ratkaisu kiinnittää suhteellisen merkin. Pitkäsen kaava $\Lambda=3/\alpha^2$ ja tiheys $3/(8\pi G\alpha^2)$ ovat näiden kanssa samaa mieltä.

### Paksuuntuminen

Pitkäsen mukaan kosmiset säikeet paksuuntuvat magneettisiksi vuoputkiksi, joten ohut tuote ei välttämättä kuvaa koko tilannetta. Paksuuntuminen ei auta, jos pinta pysyy muodossa $M^2\times X^2$, jossa $X^2$ on suljettu pinta avaruudessa $E^2\times CP_2$. Minimipinnan $E^2$-projektio on silloin harmoninen funktio suljetulla pinnalla, joten se on vakio, ja pinta pysyy avaruudessa $CP_2$. Reitti jää auki pinnoille, jotka eivät ole tuotteita, ja tällaista ratkaisua ei ole rakennettu. Negatiivinen jännitys on siis osoitettu tuotepinnoille, eikä se ole yleinen kielto.

Kirjassa on myös toinen kaava, $M_{gr}=(1-g)/4G$. Einsteinin tensorin integraali antaa arvon

$$
\frac{1}{8\pi G}\int_{Y^2}\sqrt h\,G^{tt}=\frac{1-g}{2G},
$$

joten kaavoissa on tekijän kaksi ero, ja sen alkuperä on auki.

## Massa

Euklidisella $CP_2$-alueella Einsteinin tensori on $G^{ab}=k\,g^{ab}$, kun $k=6/R_C^2$, joten

$$
P^{ab}=\frac{(\Lambda-k)\,g^{ab}}{8\pi G}.
$$

Radan suuntainen energia on positiivinen, kun $\Lambda<k$. Kenttäyhtälö $(\Lambda-k)\,\Box m^k=0$ pakottaa kuitenkin valonkaltaisen käyrän suoraksi, kun $\Lambda\ne k$, joten sileän kappaleen neliliikemäärä on valonkaltainen. Tämä ei ole ristiriidassa TGD:n kanssa. Pitkäsen kirjan mukaan hiukkaset ovat massattomia kahdeksanulotteisessa mielessä, massa syntyy $p$-adisesta termodynamiikasta, ja kvanttinen neliliikemäärä tulee superkonformiesityksistä.

Lasku tukee tätä muotoa. Mallissa $\xi=t+x^2/2b$ radan ydinvektorin kuva on valonkaltainen avaruudessa $H$, ja siksi $M^2=P_\xi^2$. Neljäulotteinen massa on tässä $CP_2$-liikemäärän osuus, joka on olemassa jo geometriassa, eikä se synny virrasta radan yli. Lasku antaa massan muodon mutta ei sen arvoa.

## Partonirata

Partonirata on pinta, jolla signatuuri vaihtuu Minkowskin signatuurista euklidiseksi. Silloin metriikan yksi ominaisarvo vaihtaa merkkiä, joten sen nollakohdan kertaluku on pariton. Mallissa $g_{tt}=x$ pätee $R=-1/(2x^2)$ radan molemmilla puolilla, ja Pitkäsen linjauksen $\sqrt{\lvert g\rvert}$ kanssa hajaantuvat osat ovat samanmerkkisiä, joten ne eivät kumoa toisiaan. Malli on tarkka, sillä sillä on upotus avaruuteen $M^4\times S^2$, helikoidi kertaa $\mathbb R^2$, joka on sekä minimipinta että vaikutuksen R + tilavuus ekstremaali.

Hajaantuminen riippuu mallista, ja kaksi laskua koskee eri suureita. Gibbons–Hawking–York-reunatermi kumoaa mallissa $g_{tt}=x$ vaikutuksen hajaantuvan osan. Reunatermi riippuu metriikasta, joten K-C-S ei voi korvata sitä. Sen raja riippuu kertaluvusta $a$, jolla $g_{tt}$ häviää, ja arvolla $a\ge3$ se häviää. Linjaus, jonka mukaan radalla on vain K-C-S, sopii siis ilman lisäyksiä vain tähän tapaukseen.

Toinen suure on translaatiovirta. Eräässä sileässä mallissa sen kaarevuusosa hajaantuu kuten $1/\sqrt\delta$, eikä kokeiltu reunatermi poista sitä. Toisessa mallissa normaalivirta on täsmälleen nolla. Tilavuusosan virta häviää radalla kuten $\sqrt\delta$ kaikissa malleissa.

Pitkäsen kaava $4\pi(2-n)$ ei tule radalta, koska geodeettisen kaarevuuden osuus saa siellä painon, joka menee nollaan. Kaava vaatii aikamaisen reunan ja reunatermin.

## Pallomainen rakenne

Pinnoilla $\xi(w)$ ehto $G^{ab}B^k{}_{ab}=0$ vaatii, että $\omega/\rho$ on vakio. Tämä antaa metriikan

$$
ds^2=dt^2-dr^2-(r^2+c)\,d\Omega^2,
$$

joka on $SO(3)$-symmetrinen, joten rajoitus tarkoittaa pallosymmetriaa.

Pinnat $\xi(u,w)$ eivät ole minimipintoja pallomaisessa rakenteessa, sillä

$$
H^\xi=\frac{2r\rho\,\xi_u}{\Phi}.
$$

Holomorfisuus antaa minimipinnan vain litteässä rakenteessa, kuten konventiot jo sanovat. Vaikutuksella R + tilavuus ei löytynyt $u$-riippuvia ratkaisuja, mutta tapausjako on päättelyä ilman testiä. Pinnat $\xi(u,v,w)$ ovat auki.

## Twistoripallo

Tulomallissa avaruudenkaltaisen pallon kaarevuus on $-2/r^2$ ja aikamaisen $+2/r^2$. Pitkäsen kirjan mukaan $M^4$-puolen pallo on aikamainen, joten malli antaa oikean merkin. Todellisella pallokimpulla kaarevuusskalaari on

$$
R(Z)=s+\frac{2}{r^2}-\frac{r^2s^2}{72},
$$

missä $s$ on kannan kaarevuusskalaari ja $r$ kuidun säde. Kaava täsmää tunnettuihin arvoihin. Vakio-osa säilyy muodossa

$$
\Lambda=\frac{1}{R_{cd}^2-r_C^2},
$$

ja vertailu kaavaan $\Lambda=3/\alpha^2$ antaa $\alpha^2=3(R_{cd}^2-r_C^2)$.

Tilavuustermi tulee siis pallon kaarevuudesta ilman Kähler-rakennetta. Einsteinin tensorin $(1,1)$-tyyppisyys ei riipu Kähler-rakenteesta. Holomorfia tarvitsee kohdeavaruuden Kähler-rakenteen, koska se määrää toisen perusmuodon tyypin, mutta se ei tarvitse Kähler-vaikutusta.

Kaavan viimeinen osa on sähköheikon yhteyden vasenkätisen osan Yang–Millsin neliö. Kompleksikäyrillä sillä on sama ensimmäinen variaatio kuin Kähler-termillä, joten kiinteän $X^4$:n yläpuolisessa kimpussa se palauttaa saman esteen, jonka takia sisäosan Kähler-termistä luovuttiin. Holomorfisessa $X^6$:ssa viipale voi riippua pisteestä, ja tätä tapausta ei ole laskettu.

## H-J-rakenne ja torukset

Weierstrass-artikkelin mukaan metriikka on hermiittinen ja tyyppiä $(1,1)$, ja konjugaatio vaihtaa koordinaatit $u$ ja $v$. Artikkelin mukaan partoniratoja ei ole ilman tätä konjugaatiota. Vanhempi yläindeksinen ehto $(\nabla u)^2=(\nabla v)^2=0$ yhdessä viivaelementin (2.4.19) kanssa poistaa ristitermit, jotka alaindeksisessä muodossa ovat mukana.

Pelkkä gradienttiehto sallii minkä tahansa genuksen. Esimerkki on

$$
u,v=t\mp\sqrt{(\rho-R_0)^2+z^2},
$$

jonka lehdet ovat sisäkkäisiä toruksia alueella, joka rajautuu ydinympyrään ja akseliin. Suljetut lehdet pakottaa palloiksi vasta se, että kaikilla lehdillä on yhteinen koordinaatti $w$. Dipolin pinnat eivät kelpaa, koska harmonisen funktion tasa-arvopinnat ovat yhdensuuntaisia vain tasolle, pallolle ja sylinterille.

Multipoliajatus toimii pallolla. Pinta $y^2=F(w)$, jossa $F$ on $n$ vastapistedipolin tulo, on genusta $n-1$. Kenttäyhtälöitä haarapisteissä ei ole laskettu.

## Tarkistus ja rajat

Laskut tehtiin kahdessa vaiheessa. Maxima-testit ovat tiedostoissa [test-interior-curvature.mac](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-interior-curvature.mac), [test-interior-energy.mac](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-interior-energy.mac) ja [test-interior-string.mac](https://github.com/markomanninen/tgd-geometry-lab/blob/main/tests/test-interior-string.mac). Erilliset Python-skriptit ovat kansiossa [scripts/sisaosa](https://github.com/markomanninen/tgd-geometry-lab/tree/main/scripts/sisaosa). OpenAI:n Codex tarkisti pääväitteet riippumattomasti. Jännityksen kaava, pallomaisen rakenteen $H^\xi$, kimpun kaarevuus ja torusesimerkki vahvistuivat, ja se rajasi kaksi väitettä, jotka ovat tällä sivulla rajatussa muodossa.

Auki ovat nämä kohdat:

- Säikeet, jotka eivät ole tuotteita.
- Mistä $T$ saa arvonsa ilman Kähler-termiä, koska $\alpha_K$ ei enää määrää sitä.
- Tekijän kaksi ero kaavassa $M_{gr}$.
- Holomorfinen $X^6$.
- Reunatermin johto muuttujista $\delta h^k$.
