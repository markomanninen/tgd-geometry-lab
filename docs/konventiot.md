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
- **Reaalimetriikka** $ds^2=2h_{i\bar j}\,dz^id\bar z^j$ (symmetrinen tulo).
- **Kähler-muoto** $\omega=i\,h_{i\bar j}\,dz^i\wedge d\bar z^j$, kompleksirakenne $J^a{}_b=g^{ac}\omega_{cb}$.
- Kun $R^2=1$: $\mathrm{Ric}=3g$, $R=12$, holomorfinen leikkauskaarevuus $2$ ja $K\in[1/2,2]$.
  $CP_1\subset CP_2$ on pallo, jonka säde on $1/\sqrt2$.

Monet lähteet käyttävät normalisointia $ds^2=h_{i\bar j}dz^id\bar z^j$, jolloin metriikka on puolet tästä. Koska Ricci-tensori ei muutu metriikan skaalauksessa, saadaan $\mathrm{Ric}=6g$, ja kaarevuudet kaksinkertaistuvat ($H=4$, $K\in[1,4]$). TGD:n $CP_2$-säde $R$ tulee mukaan kertoimena `cp2_R2`.

## $H=M^4\times CP_2$

- `H_X = [t, x, y, z, x1, y1, x2, y2]`.
- $m=\mathrm{diag}(1,-1,-1,-1)$, $h_{kl}=m_{kl}\oplus(\texttt{cp2\_sign}\cdot s_{kl})$, oletuksena `cp2_sign = -1` → signatuuri $(1,7)$.
- $J_H=0\oplus\omega_{CP_2}$.

## Toiminta

$$L_{TGD}=\left(c_K\,J_{\alpha\beta}J^{\alpha\beta}+c_V\right)\sqrt{|g|}.$$

Kertoimet ovat symbolisia. Esimerkiksi Maxwell-analogia antaa $c_K=-1/(4g_K^2)$; Manninen (2024) kirjoittaa kertoimen $1/(2\alpha_K)$:n avulla. Variaatio tehdään upotuskoordinaattien $h^k$ suhteen.
