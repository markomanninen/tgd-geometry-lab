# Laskentakonventiot

Kaikki etumerkki- ja normalisointivalinnat ovat tässä yhdessä paikassa. Testit (`tests/`) lukitsevat ne.

## Indeksit ja kaarevuus

| Suure | Määritelmä | Maxima |
|---|---|---|
| Christoffel | $\Gamma^r{}_{mn}=\tfrac12 g^{rs}(\partial_m g_{sn}+\partial_n g_{sm}-\partial_s g_{mn})$ | `Gam[r][m][n]` |
| Riemann | $R^r{}_{smn}=\partial_m\Gamma^r{}_{ns}-\partial_n\Gamma^r{}_{ms}+\Gamma^r{}_{ml}\Gamma^l{}_{ns}-\Gamma^r{}_{nl}\Gamma^l{}_{ms}$ | `Riem[r][s][m][n]` |
| Ricci | $R_{sn}=R^r{}_{srn}$ | `Ric[s,n]` |
| Leikkauskaarevuus | $K(U,V)=R_{abcd}U^aV^bU^cV^d/(|U|^2|V|^2-\langle U,V\rangle^2)$ | `sectional_curvature` |

Vertailu: yksikköpallolla $S^2$ on $\mathrm{Ric}=g$ ja $R=+2$.

## Differentiaalimuodot

- Muoto on lista `[[c, [i1<...<ip]], ...]`, joka tarkoittaa $\sum c\,dx^{i_1}\wedge\cdots\wedge dx^{i_p}$.
- 2-muoto komponenttimatriisista: $F=\tfrac12F_{ab}\,dx^a\wedge dx^b$ (`form_from_matrix`).
- Hodge: $(\star A)_K=\frac{\sqrt{|g|}}{p!}A^J\varepsilon_{JK}$, jossa $\varepsilon_{1\ldots n}=+1$.

## $CP_2$ (Fubini–Study)

- Kartta $Z_0\ne0$, reaalikoordinaatit `cp2_X = [x1, y1, x2, y2]`, $z^k=x_k+iy_k$.
- $K=R^2\log(1+|z|^2)$, $h_{i\bar j}=\partial_i\partial_{\bar j}K$ (Wirtinger-derivaatat).
- **TGD-normalisointi (Pitkänen), oletus:** $ds^2=R^2\,\partial_a\partial_{\bar b}K\,d\xi^a d\bar\xi^b$, eli
  $ds^2/R^2=(dr^2+r^2\sigma_3^2)/F^2+r^2(\sigma_1^2+\sigma_2^2)/F$, $F=1+r^2$. Maximassa `cp2_metric_factor : 1/2`
  (reaalimetriikka $\tfrac12\cdot 2h_{i\bar j}dz^id\bar z^j$).
- **Kähler-muoto** $J=\tfrac{i}{2}h_{i\bar j}\,dz^i\wedge d\bar z^j$ (sama kerroin), kompleksirakenne $J^a{}_b=g^{ac}J_{cb}$, $J_{kl}J^{kl}=4$.
- Kun $R^2=1$: $\mathrm{Ric}=6g$, $R=24$, holomorfinen leikkauskaarevuus $4$, $K\in[1,4]$, $\mathrm{Vol}(CP_2)=\pi^2/2$,
  $CP_1\subset CP_2$ on pallo, jonka säde on $1/2$. Yleisellä säteellä $\mathrm{Ric}=6g/R^2$.
- **Vertailuarvo:** CP₂-tyyppisen tyhjiöekstremaalin Kähler-toiminta $S_K=\pi/(8\alpha_K)$, kun
  $L_K=\frac{1}{4g_K^2}J_{\alpha\beta}J^{\alpha\beta}\sqrt g$ ja $\alpha_K=g_K^2/4\pi$ (Pitkänen, hep-ph/9510361). Tämä lukitsee normalisoinnin testinä.

Vaihtoehto `cp2_metric_factor : 1` antaa normalisoinnin $ds^2=2h_{i\bar j}dz^id\bar z^j$ (metriikka kaksinkertainen): $\mathrm{Ric}=3g$, $R=12$, $H=2$, $K\in[1/2,2]$. Kirjasto käytti sitä ennen 30.10.2026. TGD:n $CP_2$-säde $R$ tulee mukaan kertoimena `cp2_R2`.

## $H=M^4\times CP_2$

- `H_X = [t, x, y, z, x1, y1, x2, y2]`.
- $m=\mathrm{diag}(1,-1,-1,-1)$, $h_{kl}=m_{kl}\oplus(\texttt{cp2\_sign}\cdot s_{kl})$, oletuksena `cp2_sign = -1` → signatuuri $(1,7)$.
- $J_H=0\oplus\omega_{CP_2}$.

## Toiminta

$$L_{TGD}=\left(c_K\,J_{\alpha\beta}J^{\alpha\beta}+c_V\right)\sqrt{|g|}.$$

Kertoimet ovat symbolisia. Pitkäsen määritelmä on $L_K=\frac{1}{4g_K^2}J^{\mu\nu}J_{\mu\nu}\sqrt g$, $\alpha_K=g_K^2/4\pi$; tämä tuottaa arvon $S_K(CP_2)=\pi/(8\alpha_K)$ (testattu). Manninen (2024, s. 34) kirjoittaa kertoimeksi $1/(2\alpha_K)$, mikä antaisi eri arvon – kirjan kaava kannattaa tarkistaa. Twistorinostossa $S=S_K+S_V$ (+ instantonitermi), ja M⁴:n Kähler-osan vaikutus on häviävän pieni (~10⁻¹⁷ elektronille), joten se jätetään toistaiseksi pois. Variaatio tehdään upotuskoordinaattien $h^k$ suhteen.

**Kenttäyhtälöt.** Kun $f=c_KJ_{\alpha\beta}J^{\alpha\beta}+c_V$,

$$T^{\alpha\beta}=\tfrac12 f g^{\alpha\beta}-2c_KJ^{\alpha}{}_{\gamma}J^{\beta\gamma},\qquad j^\beta=D_\alpha J^{\alpha\beta},$$

$$\frac{\delta S}{\delta h^k}=-2\sqrt{|g|}\left[h_{kl}D_\alpha\left(T^{\alpha\beta}\partial_\beta h^l\right)+2c_K\,j^\beta J_{kl}\partial_\beta h^l\right].$$

Johto käyttää ehtoa $dJ=0$. Testi vertaa muotoa suoraan määritelmästä laskettuun arvoon $\partial L/\partial h^k-\partial_\alpha\,\partial L/\partial(\partial_\alpha h^k)$. Kertoimet pysyvät symbolisina, joten mitään etumerkkiä ei ole kiinnitetty.

## Kehykset ja Cartan-muodot

- Kehys on matriisi `E[a,m]` $=e^a{}_\mu$ (rivi = litteä indeksi), ja $g=E^T\eta E$. Käänteiskehys on `frame_inverse(E)` $=e_a{}^\mu$.
- $CP_2$:n unitaarinen kehys on sileä koko kartassa $Z_0\ne0$: $\theta^1=\frac{\sqrt D}{F}\bigl(dz^1-\frac{z^1\bar z^2}{D}dz^2\bigr)$, $\theta^2=\frac{dz^2}{\sqrt{FD}}$, $D=1+|z^2|^2$, $e^{1,2}=\mathrm{Re},\mathrm{Im}\,\theta^1$, $e^{3,4}=\mathrm{Re},\mathrm{Im}\,\theta^2$. Tällöin $J=e^1\wedge e^2+e^3\wedge e^4$.
- $H$:n litteä metriikka on `H_eta()` $=\mathrm{diag}(1,-1,\ldots,-1)$, ja kehys on $\mathbb 1_4\oplus e_{CP_2}$.
- $T^a=de^a+\omega^a{}_b\wedge e^b$, $\Omega^a{}_b=d\omega^a{}_b+\omega^a{}_c\wedge\omega^c{}_b=\tfrac12 e^a{}_\rho e_b{}^\sigma R^\rho{}_{\sigma\mu\nu}dx^\mu\wedge dx^\nu$.
- `connection_forms` laskee yhteyden pelkästä kehyksestä, `spin_connection` kehyksestä ja Christoffeleista: $\omega_\mu{}^a{}_b=e^a{}_\rho(\partial_\mu e_b{}^\rho+\Gamma^\rho{}_{\mu\lambda}e_b{}^\lambda)$. Reitit tarkistavat toisensa.

## Spinorit (Vaihe IV)

- Litteät gammat: $\{\gamma_a,\gamma_b\}=2\eta_{ab}$. Kaarevat: $\gamma^\mu=e_a{}^\mu\gamma^a$, $\{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}$.
- $D_\mu=\partial_\mu+\tfrac14\omega_{\mu ab}\gamma^a\gamma^b+ikA_\mu$, jossa $dA=J$ ja $A=\tfrac12\sum_k(x_kdy_k-y_kdx_k)/F$ (kun $R^2=1$).
- CP₂ ei ole spin-monisto; TGD:ssä spinoriyhteys kytketään Kähler-potentiaaliin: kerroin $k=1$ kvarkeille ja $k=3$ leptoneille (Pitkänen). Tällä normalisoinnilla testit vahvistavat:
  - unitaarisessa kehyksessä $S^+$-lohkon yhteys on $\mathrm{diag}(3iA,-3iA)$, joten $k=3$ antaa kovariantisti vakion spinorin ($\nu_R$),
  - $\tfrac12\gamma^\mu\gamma^\nu F_{\mu\nu}=-R/4=-6$, eli $\slashed D^2=\nabla^2-R/4+\tfrac{ik}{2}J_{\mu\nu}\gamma^\mu\gamma^\nu$,
  - $S^+$:n vuo yli $CP_1$:n on $(k\pm3)/2$ ($\int_{CP_1}J=\pi$), kokonaisluku täsmälleen parittomilla $k$.

## Toinen perusmuoto

$B^k{}_{\alpha\beta}=D_\alpha\partial_\beta h^k=\partial_\alpha\partial_\beta h^k-\Gamma^\gamma{}_{\alpha\beta}\partial_\gamma h^k+\bar\Gamma^k{}_{lm}\partial_\alpha h^l\partial_\beta h^m$ ja $H^k=g^{\alpha\beta}B^k{}_{\alpha\beta}$. Etumerkkivertailu: $R^3$:n $\rho$-säteisellä pallolla $B^k{}_{ab}=-g_{ab}n^k/\rho$. Gauss: $R_{abcd}=\bar R(t_a,t_b,t_c,t_d)+\langle B_{ac},B_{bd}\rangle-\langle B_{ad},B_{bc}\rangle$. Normaalikentät tehdään projektorilla $P^k{}_l=\delta^k_l-g^{ab}t_a^kt_{bl}$, jolloin neliöjuuria ei tarvita.

## Ekstremaalit (vertailukohteet)

- **Massattomat ekstremaalit:** Pitkäsen ansatsi on $s^k=f^k(u,v)$, $u=k\cdot m$, $v=\varepsilon\cdot m$, $k$ valon kaltainen, $\varepsilon\perp k$. Lähteen mukaan (*Extremals of the Kähler Action*, 2024) ME:t ovat "in their simplest form at least" minimipintoja. Laskettu tilanne (`tests/test-field-equations.mac`, valokartioparametrit, $x$ poikittainen, $w=x+iy$):

| Ansatsi | Kähler-termi $c_K$ | Tilavuustermi $c_V$ |
|---|---|---|
| $s^k(u)$, mielivaltaiset funktiot | 0 | 0 |
| $s^k(u,x)$, mielivaltaiset funktiot | 0 ($T^{\alpha\beta}\propto k^\alpha k^\beta$, $j^\alpha\propto k^\alpha$) | $\ne0$ |
| $z^1=\tan(x)\,e^{ia(u)}$, $z^2=0$ (geodeesi, jonka suunta kääntyy $u$:n mukana) | 0, kun $J_{ux}\ne0$ ja $j^v\ne0$ | 0 |
| holomorfinen $w$:ssä, esim. $z^1=w/2$ | $\ne0$ | 0 |

  Yleinen $f^k(u,v)$ on siis Kähler-toiminnan ekstremaali mutta ei minimipinta. Se, mikä näistä on ME:n määritelmä toiminnalle $S_K+S_V$, on kysymys Matille (#28).
- **Kosmiset säikeet** $X^2\times Y^2$: $X^2\subset M^4$ minimipinta, $Y^2$ homologisesti epätriviaali kompleksinen pinta.
- **Tyhjiöekstremaalit** $M^4\times Y^2$, $Y^2$ Lagrangen pinta ($J=0$), sekä CP₂-tyyppiset tyhjiöekstremaalit.
- Tunnetuille ratkaisuille Kähler-virta $j^\alpha=D_\beta J^{\alpha\beta}$ häviää tai on valon kaltainen.
