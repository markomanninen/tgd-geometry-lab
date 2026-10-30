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

## Spinorit (Vaihe IV)

CP₂ ei ole spin-monisto; TGD:ssä spinoriyhteys kytketään Kähler-potentiaaliin: kerroin $k=1$ kvarkeille ja $k=3$ leptoneille (Pitkänen). Tämä toteutetaan issuessa #19.

## Ekstremaalit (vertailukohteet)

- **Massattomat ekstremaalit:** CP₂-koordinaatit mielivaltaisia funktioita muuttujista $u=k\cdot m$ ja $w=\varepsilon\cdot m$ ($k$ valon kaltainen, $\varepsilon\perp k$); minimipintoja ja käytännössä minkä tahansa yleisesti kovariantin toiminnan ekstremaaleja.
- **Kosmiset säikeet** $X^2\times Y^2$: $X^2\subset M^4$ minimipinta, $Y^2$ homologisesti epätriviaali kompleksinen pinta.
- **Tyhjiöekstremaalit** $M^4\times Y^2$, $Y^2$ Lagrangen pinta ($J=0$), sekä CP₂-tyyppiset tyhjiöekstremaalit.
- Tunnetuille ratkaisuille Kähler-virta $j^\alpha=D_\beta J^{\alpha\beta}$ häviää tai on valon kaltainen.
