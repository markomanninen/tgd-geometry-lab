# Laskentakonventiot

<p class="lead">Kaikki etumerkki- ja normalisointivalinnat ovat tässä yhdessä paikassa. Testit lukitsevat ne.</p>

## Kaarevuus

### Christoffelin symbolit

Maximassa `Gam[r][m][n]`.

$$
\Gamma^r{}_{mn}=\tfrac12 g^{rs}\left(\partial_m g_{sn}+\partial_n g_{sm}-\partial_s g_{mn}\right)
$$

### Riemannin tensori

Maximassa `Riem[r][s][m][n]`.

$$
R^r{}_{smn}=\partial_m\Gamma^r{}_{ns}-\partial_n\Gamma^r{}_{ms}+\Gamma^r{}_{ml}\Gamma^l{}_{ns}-\Gamma^r{}_{nl}\Gamma^l{}_{ms}
$$

### Ricci ja leikkauskaarevuus

Riccin tensori on `Ric[s,n]`.

$$
R_{sn}=R^r{}_{srn}
$$

Leikkauskaarevuus on `sectional_curvature`.

$$
K(U,V)=\frac{R_{abcd}U^aV^bU^cV^d}{\lVert U\rVert^2\lVert V\rVert^2-\langle U,V\rangle^2}
$$

Etumerkin voi tarkistaa yksikköpallolla $S^2$, jolla $\mathrm{Ric}=g$ ja $R=+2$.

## Differentiaalimuodot

Muoto on lista `[[c, [i1<...<ip]], ...]`, joka tarkoittaa summaa

$$
\sum c\,dx^{i_1}\wedge\cdots\wedge dx^{i_p}.
$$

2-muoto saadaan komponenttimatriisista funktiolla `form_from_matrix`, ja se on

$$
F=\tfrac12F_{ab}\,dx^a\wedge dx^b.
$$

Hodgen tähti määritellään kaavalla

$$
(\star A)_K=\frac{\sqrt{|g|}}{p!}\,A^J\varepsilon_{JK},
$$

jossa $\varepsilon_{1\ldots n}=+1$.

## $CP_2$ (Fubini–Study)

### Koordinaatit

Kartta on $Z_0\ne0$, ja reaalikoordinaatit ovat `cp2_X = [x1, y1, x2, y2]`, jolloin $z^k=x_k+iy_k$.

### Metriikka

Kähler-potentiaali ja hermiittinen metriikka saadaan Wirtinger-derivaatoilla kaavoista

$$
K=R^2\log\left(1+|z|^2\right),\qquad h_{i\bar j}=\partial_i\partial_{\bar j}K.
$$

Oletuksena on Pitkäsen TGD-normalisointi

$$
ds^2=R^2\,\partial_a\partial_{\bar b}K\,d\xi^a d\bar\xi^b,
$$

eli kun $F=1+r^2$,

$$
\frac{ds^2}{R^2}=\frac{dr^2+r^2\sigma_3^2}{F^2}+\frac{r^2(\sigma_1^2+\sigma_2^2)}{F}.
$$

Maximassa tämä on `cp2_metric_factor : 1/2`, eli reaalimetriikka $\tfrac12\cdot 2h_{i\bar j}\,dz^id\bar z^j$. Säde $R$ tulee mukaan kertoimena `cp2_R2`.

### Kähler-muoto

Kähler-muodossa on sama kerroin kuin metriikassa, eli

$$
J=\tfrac{i}{2}\,h_{i\bar j}\,dz^i\wedge d\bar z^j.
$$

Kompleksirakenne on $J^a{}_b=g^{ac}J_{cb}$, ja $J_{kl}J^{kl}=4$.

### Vertailuarvot

Taulukon arvot pätevät, kun $R^2=1$. Yleisellä säteellä $\mathrm{Ric}=6g/R^2$.

| Suure | Arvo |
|---|---|
| Ricci | $\mathrm{Ric}=6g$ |
| Skalaarikaarevuus | $R=24$ |
| Holomorfinen leikkauskaarevuus | $4$ |
| Leikkauskaarevuus | $K\in[1,4]$ |
| Tilavuus | $\mathrm{Vol}(CP_2)=\pi^2/2$ |
| $CP_1\subset CP_2$ | pallo, jonka säde on $1/2$ |

Normalisoinnin lukitsee testinä CP₂-tyyppisen tyhjiöekstremaalin Kähler-vaikutus, jolle Pitkänen antaa arvon (hep-ph/9510361)

$$
S_K=\frac{\pi}{8\alpha_K},\qquad L_K=\frac{1}{4g_K^2}J_{\alpha\beta}J^{\alpha\beta}\sqrt g,\qquad \alpha_K=\frac{g_K^2}{4\pi}.
$$

### Vaihtoehtoinen normalisointi

Asetus `cp2_metric_factor : 1` antaa kaksinkertaisen metriikan $ds^2=2h_{i\bar j}\,dz^id\bar z^j$, jolloin $\mathrm{Ric}=3g$, $R=12$, holomorfinen leikkauskaarevuus on $2$ ja $K\in[1/2,2]$. Kirjasto käytti sitä ennen 30.10.2026.

## $H=M^4\times CP_2$

Koordinaatit ovat `H_X = [t, x, y, z, x1, y1, x2, y2]`.

$$
m=\mathrm{diag}(1,-1,-1,-1),\qquad h_{kl}=m_{kl}\oplus\left(\sigma\, s_{kl}\right),\qquad J_H=0\oplus\omega_{CP_2}.
$$

Etumerkki $\sigma$ on `cp2_sign`, oletuksena $-1$, jolloin signatuuri on $(1,7)$.

## Vaikutus

Englannin sana *action* on suomeksi vaikutus eli vaikutusintegraali, ja se on koko pinnasta laskettu yksi luku. Sama sana on nimessä pienimmän vaikutuksen periaate. Kähler action on siis Kähler-vaikutus. Matti Pitkänen käyttää sanaa vaikutus, ja hänen viestinsä [#35](https://github.com/markomanninen/tgd-geometry-lab/issues/35):ssä toteaa, ettei sana toiminta ole standarditermi. Ryhmän toiminta (*group action*) on eri käsite, ja se säilyy matematiikan terminä.

### Lagrangen tiheys

$$
L_{TGD}=\left(c_K\,J_{\alpha\beta}J^{\alpha\beta}+c_V\right)\sqrt{|g|}
$$

Kertoimet ovat symbolisia, ja variaatio tehdään upotuskoordinaattien $h^k$ suhteen.

### Kertoimet

Pitkäsen määritelmä on

$$
L_K=\frac{1}{4g_K^2}J^{\mu\nu}J_{\mu\nu}\sqrt g,\qquad \alpha_K=\frac{g_K^2}{4\pi}.
$$

Tämä tuottaa testatun arvon $S_K(CP_2)=\pi/(8\alpha_K)$. Arvo seuraa siitä, että $CP_2$:n yli otettu integraali on

$$
\int_{CP_2}J_{\alpha\beta}J^{\alpha\beta}\sqrt g\,d^4x=4\cdot\frac{\pi^2}{2}=2\pi^2.
$$

Integraalin ja arvon $\pi/(8\alpha_K)$ suhde kiinnittää kertoimen, joka on

$$
\frac{1}{16\pi\alpha_K}=\frac{1}{4g_K^2}.
$$

Manninen (2024, s. 33) kirjoittaa kertoimeksi $1/(2\alpha_K)$. Tällä kertoimella sama integraali antaa arvon $\pi^2/\alpha_K$, joka on $8\pi\approx25{,}13$ kertaa arvo $\pi/(8\alpha_K)$. Metriikan toinen normalisointi `cp2_metric_factor : 1` ei selitä eroa, koska integraali kasvaa siinä arvoon $8\pi^2$ ja kertoimien suhde arvoon $32\pi$. Laskut ovat tiedostossa `tests/test-cp2.mac`, ja esseen muut kaavat on koottu [tuloksiin](tulokset.md#mannisen-esseen-kaavat-vertailutesteina).

Twistorinostossa $S=S_K+S_V$ ja lisäksi instantonitermi. Laskut käyttävät oletuksena pelkkää $CP_2$:n Kähler-muotoa, koska $M^4$:n Kähler-osan vaikutus on arvion mukaan häviävän pieni (~10⁻¹⁷ elektronille).

Matti Pitkäsen linjaus 31.10.2026 ([#35](https://github.com/markomanninen/tgd-geometry-lab/issues/35)) on, että $J(M^4)$ ja $J(CP_2)$ antavat vaikutukseen erilliset termit eivätkä summaudu yhdeksi muodoksi. Julkaistuna ratkaisu on [Martin2](https://tgdtheory.fi/public_html/articles/Martin2.pdf):ssa partoniratojen Kähler–Chern–Simons-vaikutukselle, jossa mittabosonien propagaattorit saadaan vain erillisillä termeillä. Viestin mukaan sama koskee sisäosan vaikutusta, jossa magneettiset osat ovat positiivisia sekä $M^4$:ssä että $CP_2$:ssa. Muodolla $J(M^4)$ on vain poikittainen osa. Pitkittäiseen osaan liittyy gradienttina esitettävä mittapotentiaali, joka vastaa Newtonin potentiaalia, ja poikittaisiin vapausasteisiin liittyy gravimagneettinen kenttä. Termin suuruus riippuu sen kertoimesta ja ratkaisun parametreista, ja perusskaala on $CP_2$:n skaala. Rakenteellinen seuraus on laskettu kohdassa [Holografia = holomorfia](#holografia-holomorfia).

Pitkäsen linjaus 1.11.2026 ([#35](https://github.com/markomanninen/tgd-geometry-lab/issues/35)) on, että lisäehtoja ei tuoda, koska minimipintaominaisuudesta ja holografiasta ei haluta luopua. Sisäosan vaikutus on tilavuustermi, ja sisäosan fysiikka on hänen mukaansa puhdasta gravitaatiota kuten AdS/CFT:ssä. Kähler–Chern–Simons-vaikutus on välttämätön, mutta se on mukana vain valon kaltaisilla partonipinnoilla. Partonipintojen ratoihin rajoitettu Diracin vaikutus antaa alkeishiukkasfysiikan. Laskut pitävät kertoimet $c_K$ ja $c_V$ symboleina, joten sisäosan arvo $c_K=0$ kuuluu niiden piiriin, ja kaikki testatut holomorfiset minimipinnat ovat silloin sisäosan ekstremaaleja.

### Kertoimien etumerkki

Matti Pitkäsen linjaus 31.10.2026 ([#27](https://github.com/markomanninen/tgd-geometry-lab/issues/27)) on, että etumerkki ei näy H-H-pintojen eikä Lagrangen minimipintojen kenttäyhtälöissä. Etumerkki vaikuttaa kosmologisen vakion arvoon ja Kähler-funktion eksponenttiin, joka määrittelee WCW:n tyhjiöfunktionaalin. Eksponentissa tilavuusosan on oltava negatiivinen, jotta eksponentti menee nollaan suurilla tilavuuksilla.

Tilavuuskerroin pienenee pitkissä skaaloissa kuten p-adisen pituusskaalan käänteisneliö. Twistorinostossa $1/\alpha_K$ on 6-ulotteisen Kähler-vaikutuksen yhteinen kerroin, joten se ei vaikuta kenttäyhtälöihin. Kompleksisen $\alpha_K$:n vaihetekijän tulkinta on avoin.

Pitkäsen toisessa vastauksessa 31.10.2026 ([#35](https://github.com/markomanninen/tgd-geometry-lab/issues/35)) merkit johdetaan neljästä säännöstä, ja lasku pyydettiin tekemään tässä:

- Sekä Kähler-osan että tilavuusosan on tuotava energiatiheyteen positiivinen osuus.
- Vaikutuksessa $CP_2$:n sähköinen osa on negatiivinen, ja magneettiset osat ovat positiivisia sekä $M^4$:ssä että $CP_2$:ssa.
- Tilavuusosa on positiivinen sekä vaikutuksessa että energiassa.
- Kähler-funktio on $K=-S$, joten tilavuusosa on eksponentissa negatiivinen eikä eksponentti räjähdä.

Ortonormaalissa kehyksessä $J_{\alpha\beta}J^{\alpha\beta}=2(B^2-E^2)$, ja jännitystensori antaa energiatiheydeksi

$$
2T^{tt}=c_V+2c_K\left(B^2+E^2\right).
$$

Noether-virta antaa saman arvon, ja kosmisella säikeellä se on $c_V+2c_K$. Säännöt toteutuvat yhdessä täsmälleen, kun

$$
c_K>0,\qquad c_V>0.
$$

Vaikutuksen yhteinen merkki ei näy kenttäyhtälöissä, mutta jo energian positiivisuus kiinnittää suhteen $c_K/c_V>0$. Normalisointi $c_K=1/(4g_K^2)$ on tämän mukainen. Testit ovat tiedostossa `tests/test-hamilton-jacobi.mac`, ja laskuissa kertoimet pysyvät muuten symbolisina.

Ensimmäisessä vastauksessaan Pitkänen kirjoitti, että magneettinen osa ja tilavuusosa ovat erimerkkisiä ja kilpailevat keskenään. Säännöissä ne ovat samanmerkkisiä. Kilpailu voi syntyä silti putken paksuuden kautta, sillä vuolla $\Phi$ ja poikkipinnalla $A$ jännitys on

$$
T(A)=c_VA+\frac{2c_K\Phi^2}{A}.
$$

Tällä on minimi kohdassa $A^2=2c_K\Phi^2/c_V$ täsmälleen silloin, kun termit ovat samanmerkkisiä. Tämä on yksinkertaistettu malli, mutta sama ajatus on Pitkäsen teksteissä, joiden mukaan tilavuusenergian kasvu johtaa energiaminimiin jollakin vuoputken paksuudella.

### Kenttäyhtälöt

Merkitään $f=c_KJ_{\alpha\beta}J^{\alpha\beta}+c_V$ sekä

$$
T^{\alpha\beta}=\tfrac12 f g^{\alpha\beta}-2c_KJ^{\alpha}{}_{\gamma}J^{\beta\gamma},\qquad j^\beta=D_\alpha J^{\alpha\beta}.
$$

Tällöin

$$
\frac{\delta S}{\delta h^k}=-2\sqrt{|g|}\left[h_{kl}D_\alpha\left(T^{\alpha\beta}\partial_\beta h^l\right)+2c_K\,j^\beta J_{kl}\partial_\beta h^l\right].
$$

Johto käyttää ehtoa $dJ=0$. Testi vertaa muotoa suoraan määritelmästä laskettuun arvoon

$$
\frac{\partial L}{\partial h^k}-\partial_\alpha\frac{\partial L}{\partial(\partial_\alpha h^k)}.
$$

Kertoimet pysyvät symbolisina, joten mitään etumerkkiä ei ole kiinnitetty.

### Noether-virrat

Isometria $K^k$, joka säilyttää sekä metriikan $h_{kl}$ että Kähler-muodon $J_{kl}$, antaa virran

$$
j^\alpha=2T^{\alpha\beta}h_{kl}K^k\partial_\beta h^l+4c_KJ^{\alpha\beta}J_{kl}K^k\partial_\beta h^l.
$$

Jokaiselle pinnalle pätee identiteetti

$$
D_\alpha j^\alpha=2K^k\,\mathrm{Eq}_k,\qquad \mathrm{Eq}_k=h_{kl}D_\alpha\left(T^{\alpha\beta}\partial_\beta h^l\right)+2c_K\,j^\beta J_{kl}\partial_\beta h^l,
$$

joten virta säilyy ratkaisuilla. Isometrioita on 18, eli neljä translaatiota, kuusi Lorentz-generaattoria ja kahdeksan $SU(3)$-generaattoria. Väri-isometria saadaan ryhmän toiminnasta $\delta Z=AZ$, jolloin $\delta z^i=(AZ)_i-z^i(AZ)_0$.

### Karakteristinen analyysi

Kenttäyhtälöiden pääosa pisteessä on $P^{ab}_{ij}\,\partial_a\partial_b u^j$, jossa

$$
P^{ab}_{ij}=\frac{\partial^2 L}{\partial(\partial_a h^i)\,\partial(\partial_b h^j)}.
$$

Kentät $u$ ovat ne upotuskoordinaatit, joita ei ole käytetty pinnan parametreina. Muuttujilla $U=(\partial_tu,\partial_xu)$ yhtälö saa LanyonScriptsin `calcev`-funktiosta tutun muodon $\partial_tU+A\,\partial_xU=0$, jossa

$$
A=\begin{pmatrix}2(P^{tt})^{-1}P^{tx} & (P^{tt})^{-1}P^{xx}\\ -1 & 0\end{pmatrix}.
$$

Rintaman nopeus $s=dx/dt$ toteuttaa yhtälön $\det\left(s^2P^{tt}-2sP^{tx}+P^{xx}\right)=0$. Taulukko kertoo, miten yhtälön tyyppi luokitellaan.

| Tyyppi | Ehto |
|---|---|
| `degenerate` | $P^{tt}$ ei ole kääntyvä |
| `hyperbolic` | nopeudet ovat reaaliset, ja ominaisvektoreita on täysi määrä |
| `weakly_hyperbolic` | nopeudet ovat reaaliset, mutta ominaisvektoreita puuttuu |
| `complex` | jokin nopeus on kompleksinen |

Tulos koskee pääosaa yhdessä pisteessä. Alemman kertaluvun termit eivät ole mukana.

## Kehykset ja Cartan-muodot

### Kehys

Kehys on matriisi `E[a,m]` $=e^a{}_\mu$, jonka rivi on litteä indeksi. Metriikka on $g=E^T\eta E$, ja käänteiskehys on `frame_inverse(E)` $=e_a{}^\mu$.

### $CP_2$:n unitaarinen kehys

Kehys on sileä koko kartassa $Z_0\ne0$. Kun $D=1+|z^2|^2$,

$$
\theta^1=\frac{\sqrt D}{F}\left(dz^1-\frac{z^1\bar z^2}{D}\,dz^2\right),\qquad \theta^2=\frac{dz^2}{\sqrt{FD}}.
$$

Reaalikehys on $e^{1,2}=\mathrm{Re},\mathrm{Im}\,\theta^1$ ja $e^{3,4}=\mathrm{Re},\mathrm{Im}\,\theta^2$. Tällöin

$$
J=e^1\wedge e^2+e^3\wedge e^4.
$$

### $H$:n kehys

Litteä metriikka on `H_eta()` $=\mathrm{diag}(1,-1,\ldots,-1)$, ja kehys on $\mathbb 1_4\oplus e_{CP_2}$.

### Torsio ja kaarevuus

$$
T^a=de^a+\omega^a{}_b\wedge e^b
$$

$$
\Omega^a{}_b=d\omega^a{}_b+\omega^a{}_c\wedge\omega^c{}_b=\tfrac12\, e^a{}_\rho e_b{}^\sigma R^\rho{}_{\sigma\mu\nu}\,dx^\mu\wedge dx^\nu
$$

### Yhteys kahta reittiä

`connection_forms` laskee yhteyden pelkästä kehyksestä, ja `spin_connection` kehyksestä ja Christoffeleista kaavalla

$$
\omega_\mu{}^a{}_b=e^a{}_\rho\left(\partial_\mu e_b{}^\rho+\Gamma^\rho{}_{\mu\lambda}e_b{}^\lambda\right).
$$

Reitit tarkistavat toisensa.

## Spinorit

### Gammamatriisit

$$
\{\gamma_a,\gamma_b\}=2\eta_{ab},\qquad \gamma^\mu=e_a{}^\mu\gamma^a,\qquad \{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}
$$

### Kovariantti derivaatta

$$
D_\mu=\partial_\mu+\tfrac14\,\omega_{\mu ab}\gamma^a\gamma^b+ikA_\mu
$$

Tässä $dA=J$, ja kun $R^2=1$,

$$
A=\frac{1}{2F}\sum_k\left(x_k\,dy_k-y_k\,dx_k\right).
$$

### Kähler-kytkentä

$CP_2$ ei ole spin-monisto. TGD:ssä spinoriyhteys kytketään Kähler-potentiaaliin kertoimella $k=1$ kvarkeille ja $k=3$ leptoneille (Pitkänen). Sektorit vastaavat $H$-spinorien eri kätisyyksiä, ja Pitkäsen viestissä 31.10.2026 kvarkkien kerroin esiintyy myös muodossa $k=-1$. Vuon kokonaislukuisuus on testattu molemmilla merkeillä. Tällä normalisoinnilla testit vahvistavat kolme asiaa.

**Kovariantisti vakio spinori.** Unitaarisessa kehyksessä $S^+$-lohkon yhteys on $\mathrm{diag}(3iA,-3iA)$, joten $k=3$ antaa kovariantisti vakion spinorin $\nu_R$.

**Lichnerowicz-termi.** Spinorikaarevuudelle pätee $\tfrac12\gamma^\mu\gamma^\nu F_{\mu\nu}=-R/4=-6$, eli

$$
\not\!\!D^2=\nabla^2-\frac R4+\frac{ik}{2}J_{\mu\nu}\gamma^\mu\gamma^\nu.
$$

**Vuon kokonaislukuisuus.** Koska $\int_{CP_1}J=\pi$, $S^+$:n vuo yli $CP_1$:n on $(k\pm3)/2$. Se on kokonaisluku täsmälleen parittomilla $k$.

## Toinen perusmuoto

$$
B^k{}_{\alpha\beta}=D_\alpha\partial_\beta h^k=\partial_\alpha\partial_\beta h^k-\Gamma^\gamma{}_{\alpha\beta}\partial_\gamma h^k+\bar\Gamma^k{}_{lm}\,\partial_\alpha h^l\partial_\beta h^m
$$

Keskikaarevuus on $H^k=g^{\alpha\beta}B^k{}_{\alpha\beta}$.

Etumerkin voi tarkistaa $R^3$:n $\rho$-säteisellä pallolla, jolla $B^k{}_{ab}=-g_{ab}n^k/\rho$.

Gaussin yhtälö on

$$
R_{abcd}=\bar R(t_a,t_b,t_c,t_d)+\langle B_{ac},B_{bd}\rangle-\langle B_{ad},B_{bc}\rangle
$$

Normaalikentät tehdään projektorilla

$$
P^k{}_l=\delta^k_l-g^{ab}t_a^k\,t_{bl},
$$

jolloin neliöjuuria ei tarvita.

## Ekstremaalit

### Vertailukohteet

Kosmisessa säikeessä $X^2\times Y^2$ osa $X^2\subset M^4$ on minimipinta, ja $Y^2$ on homologisesti epätriviaali kompleksinen pinta.

Tyhjiöekstremaalissa $M^4\times Y^2$ osa $Y^2$ on Lagrangen pinta, jolla $J=0$. Lisäksi on CP₂-tyyppisiä tyhjiöekstremaaleja.

Tunnetuille ratkaisuille Kähler-virta $j^\alpha=D_\beta J^{\alpha\beta}$ häviää tai on valon kaltainen. Pitkäsen ehdotus yleiseksi ominaisuudeksi on Lorentz-voiman häviäminen, $j\times B=0$.

### Massattomat ekstremaalit

Pitkäsen ansatsi on

$$
s^k=f^k(u,v),\qquad u=k\cdot m,\qquad v=\varepsilon\cdot m,
$$

jossa $k$ on valon kaltainen ja $\varepsilon\perp k$. Lähteen mukaan (*Extremals of the Kähler Action*, 2024) ME:t ovat "in their simplest form at least" minimipintoja.

Taulukossa on laskettu tilanne. Se perustuu testeihin `tests/test-field-equations.mac`, ja parametrit ovat valokartiokoordinaatit $u,v,x,y$ sekä $w=x+iy$.

| Ansatsi | Kähler-termi $c_K$ | Tilavuustermi $c_V$ |
|---|---|---|
| $s^k(u)$ mielivaltaisena | 0 | 0 |
| $s^k(u,x)$ mielivaltaisena | 0 | $\ne0$ |
| $z^1=\tan(x)\,e^{ia(u)}$, $z^2=0$ | 0 | 0 |
| holomorfinen $w$:ssä, esim. $z^1=w/2$ | $\ne0$ | 0 |

Toisella rivillä $T^{\alpha\beta}\propto k^\alpha k^\beta$ ja $j^\alpha\propto k^\alpha$. Kolmas rivi on geodeesi, jonka suunta kääntyy $u$:n mukana, ja sillä $J_{ux}\ne0$ ja $j^v\ne0$.

Yleinen $f^k(u,v)$ on siis Kähler-vaikutuksen ekstremaali mutta ei minimipinta. Taulukon "0" tarkoittaa, että kyseisen termin Euler–Lagrange-osa häviää, ei sitä, että vaikutuksen arvo olisi nolla.

Matti Pitkäsen linjaus 31.10.2026 ([#28](https://github.com/markomanninen/tgd-geometry-lab/issues/28)) on, että ansatsi $s^k=f^k(u,v)$ on johdettu puhtaalle Kähler-vaikutukselle. Vaikutukselle $S_K+S_V$ sen korvaa holografia = holomorfia -ansatsi, jossa holomorfiasta seuraa minimipintaominaisuus.

### Holografia = holomorfia

Pitkäsen muotoilussa (viesti 31.10.2026 ja artikkeli [*Holography = holomorphy vision: analogues of elliptic curves and partonic orbits*](https://tgdtheory.fi/public_html/articles/Weierstrass.pdf)) avaruusaikapinta on kahden kompleksisen funktion yhteinen nollajoukko,

$$
f_1(\xi^1,\xi^2,u,w)=0,\qquad f_2(\xi^1,\xi^2,u,w)=0.
$$

Funktiot ovat analyyttisiä argumenteissaan eivätkä riipu liittokoordinaateista $\bar\xi^k$, $\bar w$ eivätkä toisesta valokartiokoordinaatista $v$. Ne voivat olla polynomeja, rationaalifunktioita tai yleisiä analyyttisiä funktioita, ja jokainen juuri on pinnan yksi lehti. Olennaista on, että $M^4$-projektio on neliulotteinen.

Rakenne edellyttää Hamilton–Jacobi-rakennetta, joka on $M^4$:n integroituva jako pitkittäiseen ja poikittaiseen tangenttitasoon. Pitkäsen kaksi perustapausta on lueteltu alla.

- Litteässä rakenteessa koordinaatit ovat $t\pm z$ ja tason kompleksikoordinaatti $w$.
- Pallomaisessa rakenteessa koordinaatit ovat $t\pm r$ ja pallon $S^2$ stereografinen koordinaatti $w$.

Lagrangen minimipinnat eivät kuulu tähän muotoon, vaan ne ovat oma ratkaisutyyppinsä, jonka kompleksirakenne ei indusoidu $H$:sta. Pitkäsen mukaan molempia tarvitaan. Myöskään $CP_2$-tyyppiset ekstremaalit ja niiden euklidiset deformaatiot eivät palaudu muotoon $(f_1,f_2)=(0,0)$, vaikka ne ovat holomorfisia.

Moduulissa `tgd/solutions.mac` juuret antaa `hh_sheets`, ja testit ovat tiedostossa `tests/test-solutions.mac`.

### Kähler-osa H-H-pinnoilla

Pitkäsen mukaan H-H toteuttaa kenttäyhtälöt erikseen metriikka- ja Kähler-osalle ([*About the relationship of electroweak and strong interactions in the TGD Universe: part I*](https://tgdtheory.fi/public_html/articles/Martin1.pdf), luku 2). Laskenta tarkentaa tätä. Väite riippuu siitä, mikä Kähler-muoto vaikutuksessa on ja mikä Hamilton–Jacobi-rakenne on käytössä.

Olkoon $\xi^k=f^k(u,w)$, ja olkoon $\omega$ Fubini–Study-metriikan vetäisyn kerroin koordinaatissa $w$ yksiköissä, joissa $M^4$:n poikittainen kerroin on $1$. Poikittainen virta häviää täsmälleen, kun Kähler-kulman suure

$$
C=\frac{J_{w\bar w}}{g_{w\bar w}}\propto\frac{\omega}{1+\omega}
$$

ei riipu $w$:stä. Neliulotteisella $M^4$-projektiolla Kähler-osa häviää vain, jos Lorentz 4-voima $f_\beta=j^\alpha J_{\alpha\beta}$ häviää.

Pitkäsen mukaan $j^w$:n ei tarvitse hävitä, kunhan $f_\beta$ häviää, ja H-H takaa tämän. Laskenta osoittaa, että tällä pintaluokalla ehdot ovat samat. Kartassa $(u,v,x,y)$ mikään ei riipu $v$:stä, ja $g_{vv}=g_{vx}=g_{vy}=0$ sekä $J_{v\alpha}=0$. Tästä seuraa $g^{uu}=g^{ux}=g^{uy}=0$ ja edelleen $j^u=0$, joten

$$
f_v=0,\qquad f_x=-j^yJ_{xy},\qquad f_y=j^xJ_{xy}.
$$

Holomorfisella pinnalla $J_{xy}$ on nolla vain siellä, missä $\partial_wf^k=0$, joten $f_\beta=0$ vaatii ehdon $j^w=0$. Pitkäsen kaksi muuta mekanismia johtavat samaan ([*Basic Extremals of the Kähler Action*](http://web.archive.org/web/20161222094333/http://tgdtheory.fi/public_html/pdfpool/class.pdf), 2015, luku 4.2). Instantonivirralla on tällä pintaluokalla vain $v$-komponentti, joten topologisoitu virta $j=\psi j_I$ on ilman poikittaista osaa. Valon kaltaisuus taas tarkoittaa samaa, koska

$$
j^\alpha j_\alpha=-P\left((j^x)^2+(j^y)^2\right),\qquad P=-g_{xx}.
$$

Kahdella viimeisellä kaavalla ei ole oletuksia funktioista $f^k$, joten ne koskevat koko pintaluokkaa.

Pitkäsen artikkelissa perustelu on, että Kähler-muodon variaatio antaa valon kaltaisen virran ja valon kaltaisen vektorin supistuksen, joka häviää ([Martin1](https://tgdtheory.fi/public_html/articles/Martin1.pdf)). Lasku tukee tätä askelta. Jos virta on muotoa $j\propto\partial_v$, supistukset häviävät, koska $J_{v\alpha}=0$ ja $\partial_vh^l=0$ kaikilla $CP_2$-koordinaateilla. Pinnoilla, joilla on $w$-riippuvuus, virralla on kuitenkin myös poikittainen osa, joten oletus ei toteudu niillä.

Sama supistus on jo [vuoden 1981 artikkelin](https://doi.org/10.1007/BF00673694) fotoniratkaisussa (kaava 38), jossa $\Theta=f(k\cdot x)$ ja $\Phi=g(k\cdot x,x_T)$. Koska $\Theta$ riippuu vain muuttujasta $k\cdot x$, Kähler-muodolla ei ole komponenttia $J_{xy}$. Clauden päättelyn mukaan juuri tämä tekee oletuksesta toimivan, sillä silloin suure $C$ on nolla, eikä virralla ole poikittaista osaa.

Vakio $\omega$ tarkoittaisi litteää holomorfista kuvausta kompleksiviivalta $CP_2$:een. Silloin

$$
1+\lvert f^1\rvert^2+\lvert f^2\rvert^2=\lvert h(w)\rvert^2 e^{\omega\lvert w\rvert^2}.
$$

Oikean puolen Hermiten muodon rangi on ääretön ja vasemman puolen enintään kolme, joten $\omega=0$. Tämä on Calabin jäykkyyslause. Litteässä rakenteessa pelkkä $CP_2$:n Kähler-termi ei siis anna yhtään ekstremaalia, jolla on $w$-riippuvuus, ja implisiittifunktiolause vie saman tuloksen jokaisen lehden säännöllisiin pisteisiin.

Jos muotoon lisätään poikittainen $M^4$-osa $\varepsilon\,dx\wedge dy$, pinnalla $\xi^1=w/2$ pätee

$$
E_k(J_{CP_2}+\varepsilon J_{M^4})=(1-\varepsilon)^2\,E_k(J_{CP_2}).
$$

Yhdellä summamuodolla Kähler-osa häviää siis arvolla $\varepsilon=1$, ja silloin $j=0$ ja $J_{\alpha\beta}J^{\alpha\beta}=2$. Tämä on Wirtingerin ehto kompleksikäyrälle tulossa $\mathbb C\times CP_2$.

Pitkäsen linjauksen mukaan muodot ovat kuitenkin erilliset termit, joilla on kertoimet $c_{CP_2}$ ja $c_{M^4}$. Koska $E_k(J_{CP_2})=E_k(J_{M^4})$ kaikilla testatuilla pinnoilla, Kähler-osa on näillä pinnoilla

$$
\left(c_{CP_2}+c_{M^4}\right)E_k(J_{CP_2}).
$$

Molemmat kertoimet ovat etumerkkisääntöjen mukaan positiivisia, joten osa ei häviä näillä pinnoilla.

Pitkäsen käsitys on, että $M^4$:n ja $CP_2$:n osat häviävät erikseen. Laskennassa näin käy kahdessa tapauksessa, jotka ovat litteän rakenteen pinnat $f(u)$ ja pallomaisen rakenteen suora ja kartioleikkaus. Pallomaisessa rakenteessa poikittaiseksi muodoksi on otettu pallon pintamuoto $\rho\,da\wedge db$ vakiokertoimella, joka on suljettu ja kantaa $M^4$:n monopolivarauksen. Martin2:n mukaan muodon suuruus on pallolla $CP_1\subset\delta M^4_+$ verrannollinen säteen neliöön, ja testi kattaa tämän, kun säde on kiinteä. Säteen mukana muuttuva kerroin ei olisi suljettu muoto, joten sitä ei ole laskettu.

Pallomaisessa rakenteessa ehto on toinen. Vetäisyn on oltava verrannollinen pallon metriikkaan, ja Calabin luokittelun mukaan vain suora ja kartioleikkaus toteuttavat tämän. Niillä $j=0$ ja kumpikin osa häviää.

Suoralla indusoitu metriikka on

$$
ds^2=dt^2-dr^2-\left(r^2+\tfrac14\right)d\Omega^2.
$$

Metriikka on sileä kohdassa $r=0$, jossa pallon säde on $1/2$. Kähler-vuo on suoralla $\pi$ ja kartioleikkauksella $2\pi$ jokaisen pallon läpi, ja suoralla $J_{ab}/\lvert g_{ab}\rvert=1/(4r^2+1)$. Vuo on homologisesti epätriviaali, joten kyse on monopolivuosta. Vakiosäteiset leikkaukset kuuluvat [Martin3](https://tgdtheory.fi/public_html/articles/Martin3.pdf):n luokitteluun, jossa partonipinta on käyrä tulossa $CP_1\times CP_2$. Suora on genuksen $0$ käyrä, jolla on yksi lehti yli $CP_1$:n ja aste $1$ pinnassa $CP_2$. Kartioleikkaus on sama käyrä asteella $2$, ja se vastaa Martin3:n esimerkkiä bi-asteista $(1,1)$ ja $(1,1)$.

Pallomaisessa rakenteessa $u=t-r$ ei toimi samalla tavalla kuin litteässä. Valonsäteiden kimppu laajenee, joten

$$
\Box f(t-r)=\frac{2f'(t-r)}{r}\ne0.
$$

Testatuista pinnoista $\xi^1=u$, $\xi^1=u+w$ ja kierretty suora eivät siksi ole minimipintoja tässä rakenteessa, vaikka samat lausekkeet ovat minimipintoja litteässä rakenteessa. Pinnat, jotka eivät riipu $u$:sta, pysyvät minimipintoina.

Matti Pitkänen arvioi sähköpostissaan 1.11.2026, että Kähler-virta häviää minimipinnoilla singulariteetteja lukuun ottamatta, koska toisia kovariantteja derivaattoja sisältävät termit ovat verrannollisia jälkiin. Clauden laskussa $j^b=J_{kl}H^kt^{l\,b}+J_{kl}t^k{}_aB^{l\,ab}$. Ensimmäinen termi on jäljen termi, ja toinen termi ei ole jälki. Tulos on [sivututkimussivulla](sivututkimus/regge-teitelboim.md#matin-vastaus-1112026), ja kysymys on issuessa [#35](https://github.com/markomanninen/tgd-geometry-lab/issues/35).

Toisessa viestissään samana päivänä Pitkänen pitää arvionsa ja pyytää osoittamaan tuloksen suoralla laskulla tai riittävän tiheällä hilalla. Claude laski virran hilalla ilman Maxima-kirjastoa ([`scripts/lattice_kahler_current.py`](https://github.com/markomanninen/tgd-geometry-lab/blob/main/scripts/lattice_kahler_current.py)), ja arvot ovat samat kuin symbolisessa laskussa. Luvut ovat [sivututkimussivulla](sivututkimus/regge-teitelboim.md#matin-toinen-viesti-1112026).

Pitkänen vahvisti 1.11.2026, että virrassa on toinen termi, joka ei häviä, ja korosti, että ratkaisevaa on koko kenttäyhtälö. Testatuilla holomorfisilla minimipinnoilla kenttäyhtälön Kähler-osa on

$$
E_k=2\,j^a\left(J_a^{\ b}t_{bk}+J_{kl}\,t^l_{\ a}\right).
$$

Tämä on hänen kahdeksan ehtonsa $j^\alpha X^k_{\ \alpha}=0$ rakenne etumerkkikonventiota vaille. Ehto ei täyty pinnoilla $\xi^1=w/2$, $\xi^1=uw/3$ ja $\xi^1=2w$. Testit ovat tiedostossa `tests/test-curvature-action.mac`, ja käsittely on [sivututkimussivulla](sivututkimus/regge-teitelboim.md#matin-vastaus-viiteen-kysymykseen).

### Mitkä Hamilton–Jacobi-rakenteet kantavat kaikki holomorfiset funktiot

Pitkänen pitää todennäköisenä, ettei $u=t-r$ riko minimipintaominaisuutta, ja pyysi tarkistamaan asian. Hänen artikkelissaan H-J-rakenteen ehto on ([*Basic Extremals of the Kähler Action*](http://web.archive.org/web/20161222094333/http://tgdtheory.fi/public_html/pdfpool/class.pdf), 2015, kaava 4.22)

$$
\{k\,w\bar w\}=0,\qquad\{k\,{+-}\}=0.
$$

Litteässä rakenteessa ehto pätee. Pallomaisessa rakenteessa poikittainen metriikka $r^2\rho$ riippuu $v$:stä, joten $\{u\,w\bar w\}\ne0$. Lasku ja kaava 4.22 antavat siis saman tuloksen.

Yleisemmin olkoot $u$ reaalinen ja $w$ kompleksinen funktio, joiden gradientit ovat keskenään valon kaltaisia, eli $(\nabla u)^2=\nabla u\cdot\nabla w=(\nabla w)^2=0$. Silloin $\Box F(u,w)=F_u\Box u+F_w\Box w$, joten kaikki holomorfiset funktiot ovat harmonisia täsmälleen, kun $\Box u=\Box w=0$. Bochnerin kaava on

$$
\tfrac12\Box(\nabla u)^2=u_{\alpha\beta}u^{\alpha\beta}+\nabla u\cdot\nabla\Box u.
$$

Ehdoista seuraa $u_{\alpha\beta}u^{\alpha\beta}=0$, jolloin poikittainen Hessen matriisi häviää ja tasopinnat $u=$ vakio ovat valon kaltaisia hypertasoja $k(u)\cdot m=g(u)$. Tason poikittainen koordinaatti on $\zeta=e(u)\cdot m$, ja $\Box\zeta=2e'\cdot\nabla u$. Tämä häviää vain, jos $k'\propto k$, eli hypertasot ovat yhdensuuntaiset. Rakenne on silloin litteä rakenne Poincarén muunnosta ja uudelleenparametrisointia $(u,w)\to(g(u),F(u,w))$ vaille.

Todistus on Clauden päättely oletuksella, että gradientit ovat keskenään valon kaltaisia, ja testit lukitsevat sen vaiheet. Oletus on se, joka tarvitaan holomorfisen funktion supistuksen $g^{\alpha\beta}\partial_\alpha\xi^k\partial_\beta\xi^l=0$ häviämiseen. Saman luvun kohdassa 4.3.3 Pitkänen vaatii $(\nabla S_\pm)^2=0$ ja antaa viivaelementin yleisen muodon (kaava 4.19), joka sallii myös ristitermit,

$$
ds^2=g_{+-}\,dS^+dS^-+g_{w\bar w}\,dw\,d\bar w+g_{+w}\,dS^+dw+g_{+\bar w}\,dS^+d\bar w+g_{-w}\,dS^-dw+g_{-\bar w}\,dS^-d\bar w.
$$

Holomorfinen funktio supistuu yläindeksisten komponenttien $g^{++}$, $g^{+w}$ ja $g^{ww}$ kanssa, ja alaindeksien nollat eivät takaa niiden häviämistä. Viivaelementille pätee

$$
g^{ww}\det g=2\,g_{+-}\,g_{+\bar w}\,g_{-\bar w},
$$

joten komponentit eivät yleensä häviä, kun ristitermejä on molemmilla valokoordinaateilla. Kun ristitermejä on vain koordinaatilla $S^+$, pätee $g^{++}=g^{+w}=g^{ww}=0$. Tällöin gradientit ovat keskenään valon kaltaisia, ja tapaus kuuluu tämän tuloksen piiriin. Tulos ei kata tapausta, jossa ristitermejä on molemmilla puolilla. Lähteen tiedosto on poistunut Pitkäsen sivustolta, ja linkki vie Internet Archiven kopioon.

Jos rajoitutaan funktioihin $F(w)$, luokka on paljon laajempi. Oletuksesta seuraa, että tasopinnat $u=$ vakio ovat täysin napaisia valon kaltaisia hyperpintoja. Minkowskin avaruudessa niitä ovat vain hypertasot ja valokartiot. Rakenne saadaan siis valokartioista, joiden kärki kulkee radalla $z(\tau)$, ja $w$ on säteen suunta, eli

$$
m^\mu=z^\mu(\tau)+r\left(1,\vec n(w)\right).
$$

Tilavuusosa häviää pinnoilla $\xi^k=f^k(w)$ symbolisesti mielivaltaisella radalla $z^\mu(\tau)$, ja hypertasot ovat tapaus, jossa kärki on äärettömyydessä. Tämä vastaa kysymystä H-J-rakenteiden määrästä. Tällä oletuksella rakenteet ovat yhden muuttujan funktioiden perhe. Sama luokka näkyy kirjallisuudessa, jossa ehtojen $\Box y=0$ ja $(\nabla y)^2=0$ ratkaisut vastaavat leikkauksettomia valonsädekongruensseja ([Baird ja Wood](https://arxiv.org/abs/dg-ga/9603005)). Kierteiset kongruenssit, kuten Kerrin kongruenssi, jäävät ulkopuolelle, koska niillä ei ole reaalista koordinaattia $u$.

Kähler-osa on tiukempi. Tasaisesti liikkuvalla kärjellä se häviää suoran Lorentz-muunnetulle versiolle, mutta kiihtyvällä kärjellä testattu suora ei toteuta sitä.

Pitkäsen viestissä 1.11.2026 H-J-rakenne on $M^4$:n tangenttiavaruuden integroituva jako pitkittäiseen hyperkompleksiseen osaan $M^2(x)$ ja poikittaiseen kompleksiseen osaan $E^2(x)$. Fysikaalisesti se olisi hänen mukaansa mittateorian jako pitkittäisiin ja poikittaisiin vapausasteisiin geometrian tasolla. Koordinaattikäyrien $u$ ja $v$ tangentit ovat valon kaltaisia, ja ne saadaan $u$:n ja $v$:n gradienteista. Hän pitää mahdollisena myös käyräviivaisia säteitä.

Merkintä $F(u,w)$ tarkoittaa tässä osiossa pintaa $\xi^k=F^k(u,w)$, jolla $CP_2$-koordinaatit ovat holomorfisia funktioita. Pinta ei siis ole funktion $F$ nollajoukko.

Valon kaltaisen gradientin antamat säteet ovat suoria. Lause koskee vain valon kaltaista gradienttia, sillä esimerkiksi sähköstaattisen potentiaalin voimaviivat ovat kaarevia. Olkoon $k_a=\partial_au$ ja $k^ak_a=0$. Koska $\partial_ak_b$ on symmetrinen, pätee

$$
k^b\partial_bk_a=k^b\partial_ak_b=\tfrac12\partial_a\left(k^bk_b\right)=0.
$$

Kentän integraalikäyrät ovat siis $M^4$:ssä suoria, ja sama koskee gradienttiin verrannollisia kenttiä, koska kertoimen muutos vain parametrisoi käyrän uudelleen. Käyräviivainen valon kaltainen säde, esimerkiksi ruuviviiva, tarvitsee kentän, joka ei ole verrannollinen gradienttiin. Pitkäsen mukaan (1.11.2026) yleisessä H-J-rakenteessa vain koordinaattikäyrän tangentti on valon kaltainen, eli $g_{uu}=g_{vv}=0$, ja $u$ ja $v$ ovat $M^4$:n käyräviivaisia koordinaatteja. Hänen arvionsa mukaan $\nabla S_\pm$ tarkoittaa tätä tangenttia.

Tällaisia koordinaatteja on. Valokartioissa, joiden kärki kulkee radalla $z(\tau)$, säteet ovat suoria ja $\nabla\tau$ on valon kaltainen. Olkoon $l$ säteen suunta. Kun säteen pituus $r$ riippuu parametrista $\tau$ niin, että

$$
\frac{dr}{d\tau}=-\frac{\dot z^2}{2\,\dot z\cdot l},
$$

kiinteän $w$:n käyrä on valon kaltainen, ja kiihtyvällä kärjellä se ei ole suora. Rakenteen ristitermit ovat yhdellä puolella, joten se kuuluu edellä olevaan tapaukseen, ja pinnat $\xi^k=f^k(w)$ ovat minimipintoja.

Aaltorintamat näyttävät, miksi oletus rajaa rakenteet palloihin ja tasoihin. Olkoot $\kappa_1$ ja $\kappa_2$ rintaman pääkaarevuudet. Kun rintama etenee säteitä pitkin matkan $s$, pituudet pääsuunnissa kertautuvat tekijöillä $1+\kappa_1s$ ja $1+\kappa_2s$. Pieni ympyrä muuttuu ellipsiksi, ellei $\kappa_1=\kappa_2$, joten kompleksikoordinaatti ei säily kompleksikoordinaattina koko säteen matkalla. Tämä on täysin napaisuuden sisältö. Epäpallomaisen valolähteen rintamilla säteet ovat suoria, mutta niillä ei ole koordinaattia $w$, joka toteuttaisi ehdot $\nabla u\cdot\nabla w=(\nabla w)^2=0$.

Sylinterikoordinaatit antavat kaksi eri rakennetta. Rakenteessa $(t\pm z,\log\rho+i\phi)$ on $w=\log(x+iy)$, joten se on litteä rakenne uudelleenparametrisoituna. Rakenteessa $(t\pm\rho,z+i\phi)$ on $\nabla u\cdot\nabla w=0$, mutta

$$
(\nabla w)^2=\frac{1-\rho^2}{\rho^2},
$$

ja pinta $\xi^1=(z+i\phi)/2$ ei ole minimipinta. Aaltorintama on siinä sylinteri, jonka pääkaarevuudet ovat $1/\rho$ ja $0$. Pitkänen tarkoitti tätä rakennetta, joten kompleksikoordinaatin valinta jää hänen kanssaan auki. Pitkäsen mukaan H-J-rakenteesta tuskin löytyy kirjallisuutta, ja edellä mainitut leikkauksettomat kongruenssit kattavat vain tapauksen, jossa gradientit ovat keskenään valon kaltaisia.
