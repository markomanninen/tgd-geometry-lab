"""Generate the Colab notebooks in notebooks/ (run: python3 scripts/build_notebooks.py)."""
import nbformat as nbf
from pathlib import Path

REPO = "markomanninen/tgd-geometry-lab"
OUT = Path(__file__).resolve().parent.parent / "notebooks"

def badge(name):
    url = f"https://colab.research.google.com/github/{REPO}/blob/main/notebooks/{name}"
    return f"[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]({url})"

SETUP = r'''# Asennus: Maxima, tämä repositorio ja Dimiter Prodanovin clifford-paketti.
# Colabissa ajo kestää noin minuutin. Paikallisesti asetetaan TGD_ROOT / CLIFFORD_PATH.
import os, sys, shutil
ROOT = os.environ.get("TGD_ROOT", "/content/tgd-geometry-lab")
CLI  = os.environ.get("CLIFFORD_PATH", "/content/clifford")
if not shutil.which("maxima"):
    !apt-get -qq update > /dev/null && apt-get -qq install -y maxima > /dev/null
if not os.path.exists(ROOT):
    !git clone -q --depth 1 https://github.com/markomanninen/tgd-geometry-lab.git {ROOT}
if not os.path.exists(CLI):
    !git clone -q --depth 1 https://github.com/dprodanov/clifford.git {CLI}
sys.path.insert(0, ROOT + "/notebooks")
from tgdlab import Lab
lab = Lab(ROOT, CLI)
!maxima --version 2>/dev/null | tail -1'''

def nb(cells):
    n = nbf.v4.new_notebook()
    n.metadata = {"kernelspec": {"name": "python3", "display_name": "Python 3"},
                  "language_info": {"name": "python"}, "colab": {"provenance": []}}
    n.cells = [nbf.v4.new_markdown_cell(c[1]) if c[0] == "md" else nbf.v4.new_code_cell(c[1])
               for c in cells]
    # the install cell is for Colab; the public site leaves it out
    for cell in n.cells:
        if cell.source == SETUP:
            cell.metadata["tags"] = ["site-hidden"]
    return n

# ---------------------------------------------------------------- 01
nb01 = nb([
("md", f"""# 01 · Ympäristö ja testit

{badge("01_ymparisto_ja_testit.ipynb")}

Tämä kirja on rakennettu Lanyonin Colab-esimerkin (*Run LanyonScripts in Colab*) mallin mukaan. Siinä ovat
väliaikainen Ubuntu-ajoympäristö, GNU Maxima, Prodanovin `clifford`/`cliffordan` -paketit ja
skriptien ajo omissa Maxima-prosesseissaan.

Erona Lanyonin esimerkkiin on, että jokainen moduuli tarkistetaan **automaattisilla testeillä**
(tunnetut identiteetit kuten $d^2=0$, $d\\omega=0$, $\\mathrm{{Ric}}=3g$, Bianchi), jotta
laskentakirjaston virheet eivät sekoitu TGD:n fysikaalisiin oletuksiin (välitavoite M1)."""),
("code", SETUP),
("md", "## Testisarja\n\nAjaa kaikki `tests/`-hakemiston testit (metriikka, kaarevuus, muodot, $CP_2$, upotus, vaikutus, Clifford)."),
("code", "ok = lab.tests()\nprint('KAIKKI TESTIT LÄPI' if ok else 'TESTEJÄ EPÄONNISTUI')"),
("md", """## Clifford-algebra (Prodanov)

Sama paketti kuin LanyonScriptsissä. Tarkistetaan Clifford-relaatiot
$\\gamma_a\\gamma_b+\\gamma_b\\gamma_a = 2\\eta_{ab}$ signatuurilla $(1,3)$."""),
("code", r'''print(lab.values("clifford(g, 1, 3)$",
    ["g[1] . g[1]", "g[2] . g[2]", "g[1] . g[2] + g[2] . g[1]", "g[3] . g[4] + g[4] . g[3]"],
    load_clifford=True))'''),
("md", """## Vertailu LanyonScriptsin esimerkkeihin

Tämä vaihe on valinnainen. Siinä ajetaan Lanyonin kuusi virtausfysiikan esimerkkiä (Burgers, matala vesi, Euler, Maxwell, MHD)
samalla tavalla kuin alkuperäisessä kirjassa. Ne käyttävät samaa Maxima–Clifford-pohjaa,
jonka päälle TGD Geometry Lab rakentaa differentiaaligeometrian."""),
("code", r'''RUN_LANYON = os.environ.get("RUN_LANYON", "1") == "1"   # aseta 0 ohittaaksesi
if RUN_LANYON:
    import subprocess
    from pathlib import Path
    L = Path("/content/LanyonScripts")
    if not L.exists():
        !git clone -q --depth 1 https://github.com/lanyonai/LanyonScripts.git {L}
    for f in ["burgers.mac", "shallow-water.mac", "isoeuler.mac", "euler.mac", "maxwell.mac", "ideal-mhd.mac"]:
        code = (f'file_search_maxima: append(file_search_maxima, ["{CLI}/###.{{mac,wxm}}", "{CLI}/$$$.{{mac,wxm}}"])$ '
                f'load("{L}/eqnsys/{f}")$ print("LANYON_SCRIPT_FINISHED")$')
        p = subprocess.run(["maxima", "--very-quiet", f"--batch-string={code}"],
                           capture_output=True, text=True, timeout=300)
        print(f"{f:20s}", "OK" if "LANYON_SCRIPT_FINISHED" in p.stdout else "VIRHE")'''),
])

# ---------------------------------------------------------------- 02
CP2 = "G : cp2_metric()$ W : cp2_kahler_matrix()$ Jc : cp2_complex_structure(G, W)$ "
CURV = CP2 + "Gam : christoffel(G, cp2_X)$ Riem : riemann(Gam, cp2_X)$ Rl : riemann_lower(G, Riem)$ Ric : ricci(Riem)$ "
nb02 = nb([
("md", f"""# 02 · $CP_2$ ja Fubini–Study-geometria

{badge("02_cp2_fubini_study.ipynb")}

Kirja kuuluu vaiheeseen II ja välitavoitteeseen **M2** (sekä M3–M4 $CP_2$:n osalta), ja se on ensimmäinen vertailutesti `spaces/cp2.mac`.

Kartassa $Z_0\\neq 0$ on $z^1=Z_1/Z_0,\\ z^2=Z_2/Z_0$, ja reaalikoordinaatit ovat $(x_1,y_1,x_2,y_2)$, $z^k=x_k+i\\,y_k$.

$$K=\\log(1+|z^1|^2+|z^2|^2),\\qquad h_{{i\\bar j}}=\\partial_i\\partial_{{\\bar j}}K,\\qquad
ds^2 = h_{{i\\bar j}}\\,dz^i d\\bar z^j,\\qquad J = \\tfrac{{i}}{{2}}\\,h_{{i\\bar j}}\\,dz^i\\wedge d\\bar z^j\\quad(\\text{{TGD-normalisointi, Pitkänen}}).$$"""),
("code", SETUP),
("md", "## Kähler-potentiaali ja hermiittinen metriikka $h_{i\\bar j}$"),
("code", r'''lab.show("H : cp2_hermitian_metric()$", [
  ("K", "cp2_kahler_potential()"),
  ("h_{1\\bar 1}", "factor(H[1,1])"),
  ("h_{1\\bar 2}", "factor(H[1,2])"),
  ("\\det h", "factor(determinant(H))")])'''),
("md", "## Reaalinen metriikka $g_{ab}$, determinantti ja käänteismetriikka"),
("code", f'''lab.show("{CP2}", [
  ("g_{{x_1x_1}}", "factor(G[1,1])"),
  ("g_{{x_1x_2}}", "factor(G[1,3])"),
  ("g_{{x_1y_2}}", "factor(G[1,4])"),
  ("\\\\det g", "factor(determinant(G))"),
  ("g^{{x_1x_1}}", "factor(mat_inverse(G)[1,1])")])'''),
("md", """## Kähler-rakenne

Kähler-muoto $\\omega$, kompleksirakenne $J^a{}_b=g^{ac}\\omega_{cb}$ ja tarkistukset
$J^2=-1$, $J^TgJ=g$, $d\\omega=0$ sekä $\\omega\\wedge\\omega/2=\\mathrm{vol}$."""),
("code", f'''lab.show("{CP2} om : form_from_matrix(W)$", [
  ("\\\\omega_{{x_1y_1}}", "factor(W[1,2])"),
  ("J^2+1", "tgd_msimp(Jc . Jc + ident(4))"),
  ("d\\\\omega\\\\ (\\\\text{{termit}})", "dform(om, cp2_X)"),
  ("\\\\tfrac12\\\\,\\\\omega\\\\wedge\\\\omega", "factor(top_coef(wedge(om, om))/2)"),
  ("\\\\sqrt{{\\\\det g}}", "factor(radcan(sqrt(factor(determinant(G)))))")])'''),
("md", """## Yhteys ja kaarevuus

Levi-Civita-yhteys, Riemannin ja Riccin tensorit. Tuloksena $CP_2$ on Kähler–Einstein,
$\\mathrm{Ric}=6g$, $R=24$, ja holomorfinen leikkauskaarevuus on vakio $4$ ja
leikkauskaarevuus vaihtelee välillä $[1,\\,4]$ (TGD-normalisointi, $R^2=1$). Lopuksi CP₂-tyyppisen
tyhjiöekstremaalin Kähler-vaikutus $S_K=\\pi/(8\\alpha_K)$ – Pitkäsen tunnettu arvo."""),
("code", f'''lab.show("{CURV} e1:[1,0,0,0]$ Je1 : list_matrix_entries(Jc . transpose(matrix(e1)))$", [
  ("\\\\Gamma^{{x_1}}{{}}_{{x_1x_1}}", "factor(Gam[1][1][1])"),
  ("\\\\mathrm{{Ric}}-6g", "tgd_msimp(Ric - 6*G)"),
  ("R", "scalar_curvature(G, Ric)"),
  ("K(e_{{x_1}},Je_{{x_1}})", "sectional_curvature(G, Rl, e1, Je1)"),
  ("K(e_{{x_1}},e_{{x_2}})|_0", "subst([x1=0,y1=0,x2=0,y2=0], sectional_curvature(G, Rl, [1,0,0,0], [0,0,1,0]))"),
  ("\\\\nabla J\\\\ \\\\text{{(kaikki nollia?)}}", "nested_zero_p(cov_deriv_11(Jc, Gam, cp2_X))")])'''),
("md", "### CP₂-tyyppisen ekstremaalin vaikutus TGD:n vertailuarvona\n\n$S_K=\\frac{1}{4g_K^2}\\int J_{kl}J^{kl}\\sqrt g\\,d^4x$, $\\alpha_K=g_K^2/4\\pi$."),
("code", f'''lab.show("{CP2}", [
  ("J_{{kl}}J^{{kl}}", "kahler_invariant(G, W)"),
  ("\\\\mathrm{{Vol}}(CP_2)", "2*%pi^2*integrate(r^3/(1+r^2)^3, r, 0, inf)"),
  ("S_K", "ratsimp(subst(gK2=4*%pi*alpha[K], 2*%pi^2*integrate(r^3*kahler_invariant(G, W)/(1+r^2)^3, r, 0, inf)/(4*gK2)))")])'''),
("md", """## Koordinaattikarttojen vaihto (Step 2.4)

Kartassa $Z_1\\neq0$ on $w^1=Z_0/Z_1,\\ w^2=Z_2/Z_1$, jolloin $z^1=1/w^1$, $z^2=w^2/w^1$.
Siirtokuvauksella vedetty metriikka on sama Fubini–Study-kaava uudessa kartassa."""),
("code", f'''lab.show("{CP2} Gc1 : transform_02(G, cp2_X, cp2_W, cp2_chart1_to_chart0())$", [
  ("x(w)", "cp2_chart1_to_chart0()"),
  ("g'-g_{{FS}}(w)", "tgd_msimp(Gc1 - cp2_metric_in_chart(cp2_W))")])'''),
])

# ---------------------------------------------------------------- 03
H = "GH : H_metric()$ JH : H_kahler()$ "
nb03 = nb([
("md", f"""# 03 · Upotusgeometria $H=M^4\\times CP_2$ ja vaikutusintegraali

{badge("03_upotus_ja_vaikutus.ipynb")}

Vaiheet I.4, VI ja VII (välitavoitteet M6–M7, alkuvaihe). Aika-avaruuspinta $X^4\\subset H$ annetaan
upotuskoordinaatteina $h^k(\\xi)$, ja indusoidut suureet ovat

$$g_{{\\alpha\\beta}} = h_{{kl}}\\,\\partial_\\alpha h^k\\,\\partial_\\beta h^l,\\qquad
J_{{\\alpha\\beta}} = J_{{kl}}\\,\\partial_\\alpha h^k\\,\\partial_\\beta h^l .$$

Konventiona on $h_{{kl}} = m_{{kl}} - s_{{kl}}$, $m=\\mathrm{{diag}}(1,-1,-1,-1)$, $s$ = Fubini–Study ($R^2=1$),
joten $H$:n signatuuri on $(1,7)$. Dynaamiset muuttujat ovat upotuskoordinaatit $h^k$ –
indusoitua metriikkaa ja Kähler-muotoa ei varioida erikseen."""),
("code", SETUP),
("md", "## Kanoninen $M^4$-upotus\n\n$h=(\\xi^0,\\ldots,\\xi^3,\\ p)$, jossa $p$ on vakiopiste $CP_2$:ssa. Indusoitu metriikka on Minkowski ja $J=0$ (tyhjiöekstremaali)."),
("code", f'''lab.show("{H} xi:[t0,t1,t2,t3]$ e0:[t0,t1,t2,t3,0,0,0,0]$", [
  ("g_{{\\\\alpha\\\\beta}}", "induced_metric(GH, H_X, e0, xi)"),
  ("J_{{\\\\alpha\\\\beta}}", "induced_kahler_form(JH, H_X, e0, xi)")])'''),
("md", """## Kosminen säie $X^2\\times Y^2$

$(t,z)$ vapaina, $Y^2=CP_1=\\{z^2=0\\}\\subset CP_2$ (homologisesti epätriviaali kompleksinen pallo).
Tuloksena on vakiosuuruinen magneettinen Kähler-kenttä, jolle $J_{\\alpha\\beta}J^{\\alpha\\beta}=2$."""),
("code", f'''lab.show("{H} xs:[tt0,zz0,aa,bb]$ eCS:[tt0,0,0,zz0,aa,bb,0,0]$ g:induced_metric(GH,H_X,eCS,xs)$ J:induced_kahler_form(JH,H_X,eCS,xs)$", [
  ("g_{{\\\\alpha\\\\beta}}", "factor(g)"),
  ("J_{{ab}}", "factor(J[3,4])"),
  ("J_{{\\\\alpha\\\\beta}}J^{{\\\\alpha\\\\beta}}", "kahler_invariant(g, J)"),
  ("\\\\sqrt{{|g|}}", "factor(sqrt_abs_det(g))")])'''),
("md", """## Massaton ekstremaali (ME-tyyppinen ansatsi)

Valokartioparametrit $\\xi=(u,v,x,y)$, $t=(u+v)/2$, $z=(v-u)/2$. $CP_2$-koordinaatit riippuvat vain $u=t-z$:stä
ja poikittaisesta $x$:stä. Indusoitu Kähler-kenttä on nollasta poikkeava mutta *nollakenttä*, koska
$J_{\\alpha\\beta}J^{\\alpha\\beta}=0$ ja $J\\wedge J=0$. Siksi Kähler-vaikutuksen tiheys häviää."""),
("code", f'''lab.show("{H} xl:[uu,vv,xx,yy]$ depends([F1,F2],[uu,xx])$ eME:[(uu+vv)/2,xx,yy,(vv-uu)/2,F1,F2,0,0]$ g:induced_metric(GH,H_X,eME,xl)$ J:induced_kahler_form(JH,H_X,eME,xl)$", [
  ("J_{{ux}}", "factor(J[1,3])"),
  ("g^{{uu}}", "mat_inverse(g)[1,1]"),
  ("J_{{\\\\alpha\\\\beta}}J^{{\\\\alpha\\\\beta}}", "kahler_invariant(g, J)"),
  ("J\\\\wedge J", "tgd_simp(instanton_density(J))")])'''),
("md", """## Euler–Lagrange-moottori (Step 7.3)

`euler_lagrange(L, kentät, muuttujat)` laskee $\\partial L/\\partial\\phi-\\partial_\\alpha\\,\\partial L/\\partial(\\partial_\\alpha\\phi)$.
Tarkistuksena tilavuusvaikutus $\\sqrt{\\det g}$ graafipinnalle $z=f(x,y)$ antaa minimipintayhtälön –
TGD:n tilavuustermin $L_V=k\\sqrt{-g}$ yksinkertaisin analogi."""),
("code", r'''lab.show("depends(fz,[xx,yy])$ gg:induced_metric(ident(3),[X1,X2,X3],[xx,yy,fz],[xx,yy])$ EL:euler_lagrange(sqrt(determinant(gg)),[fz],[xx,yy])$", [
  ("g_{\\alpha\\beta}", "gg"),
  ("\\mathrm{EL}\\cdot(1+f_x^2+f_y^2)^{3/2}", "factor(EL[1]*(1+diff(fz,xx)^2+diff(fz,yy)^2)^(3/2))")])'''),
("md", """## Toinen perusmuoto ja minimipintaehto (Step 6.4)

$B^k{}_{\\alpha\\beta}=D_\\alpha\\partial_\\beta h^k$ ja $H^k=g^{\\alpha\\beta}B^k{}_{\\alpha\\beta}$.
Kompleksiset käyrät ovat minimipintoja myös silloin, kun ne eivät ole totaaligeodeettisia."""),
("code", r'''lab.show("emQ:emb_setup(cp2_metric(),cp2_X,[aa,bb,aa^2-bb^2,2*aa*bb],[aa,bb])$ BQ:second_fundamental_form(emQ)$", [
  ("B^{x_2}{}_{aa}\\ (\\text{kartio } z^2=(z^1)^2)", "factor(BQ[3][1][1])"),
  ("H^k", "mean_curvature(emQ,BQ)")])'''),
("md", """## Kenttäyhtälöt ja ekstremaalit (Step 7.2, #27, #28)

Vaikutuksen $S=\\int(c_KJ_{\\alpha\\beta}J^{\\alpha\\beta}+c_V)\\sqrt{|g|}\\,d^4\\xi$ variaatio upotuskoordinaattien suhteen antaa
$h_{kl}D_\\alpha(T^{\\alpha\\beta}\\partial_\\beta h^l)+2c_K\\,j^\\beta J_{kl}\\partial_\\beta h^l=0$.
Kertoimet ovat symbolisia. Alla Kähler- ja tilavuustermi on eroteltu. ME $s^k(u)$ toteuttaa molemmat, mutta yleisellä
$s^k(u,x)$:llä häviää vain Kähler-termi (ks. `docs/konventiot.md`)."""),
("code", f'''lab.show("{H} xl:[uu,vv,xx,yy]$ meX(s):=append([(uu+vv)/2,xx,yy,(vv-uu)/2],s)$ meEq(s,a,b):=tgd_field_equations(emb_setup(GH,H_X,meX(s),xl),JH,a,b)$ depends([a1,a2,a3,a4],uu)$ depends([F1,F2],[uu,xx])$", [
  ("E[s^k(u)],\\\\ c_K", "meEq([a1,a2,a3,a4],cK,0)"),
  ("E[s^k(u)],\\\\ c_V", "meEq([a1,a2,a3,a4],0,cV)"),
  ("E[s^k(u,x)],\\\\ c_K", "meEq([F1,F2,0,0],cK,0)"),
  ("E[s^1(x)=x],\\\\ c_V", "map(factor,meEq([xx,0,0,0],0,cV))")])'''),
("md", """## Karakteristinen analyysi (Step 7.5)

Lanyonin `calcev`-tyyliin yhtälö kirjoitetaan muotoon $\\partial_tU+A\\,\\partial_xU=0$, ja ominaisarvot ovat rintaman nopeudet. Kosmisen säikeen poikki nopeus
riippuu kertoimista kaavan $s^2=(c_V-2c_K)/(c_V+2c_K)$ mukaan."""),
("code", f'''lab.show("{H} eC:[tt,0,0,zz,aa,bb,0,0]$ xC:[tt,zz,aa,bb]$ pC:[tt=0,zz=0,aa=0,bb=0]$ F:[2,3,7,8]$ Pz:principal_blocks(GH,JH,H_X,eC,xC,pC,F,[1,2],cK,cV,-1)$ Pa:principal_blocks(GH,JH,H_X,eC,xC,pC,F,[1,3],cK,cV,-1)$", [
  ("\\\\det(\\\\ldots)\\\\ \\\\text{{säikeen suuntaan}}", "speed_polynomial(Pz[1][1],Pz[1][2],Pz[2][2],s)"),
  ("\\\\det(\\\\ldots)\\\\ \\\\text{{säikeen poikki}}", "speed_polynomial(Pa[1][1],Pa[1][2],Pa[2][2],s)")])'''),
("md", """## Seuraavat askeleet

* Matilta odotetaan linjausta tilavuustermin kertoimesta (#27) ja ME:n määritelmästä vaikutukselle $S_K+S_V$ (#28).
* Ratkaisugeneraattori (#31) rakennetaan, kun holografia = holomorfia -periaatteen muoto on selvä."""),
])

# ---------------------------------------------------------------- 04
nb04 = nb([
("md", f"""# 04 · Numeriikka ja kuvat

{badge("04_numeriikka_ja_kuvat.ipynb")}

Vaihe VIII, välitavoite **M8**. Maxima laskee lausekkeet, ja `lab.numeric` muuntaa ne NumPy-funktioiksi.
Kirja tarkistaa numeeriset arvot analyyttisiä arvoja vasten ennen kuin piirtää ne."""),
("code", SETUP),
("code", r"""import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

INK, MUTED, GRID = "#0b0b0b", "#52514e", "#e4e3df"
BLUE, ORANGE, AQUA = "#2a78d6", "#eb6834", "#1baf7a"
plt.rcParams.update({
    "figure.dpi": 130, "figure.facecolor": "#fcfcfb", "axes.facecolor": "#fcfcfb",
    "font.size": 10, "axes.edgecolor": GRID, "axes.labelcolor": MUTED, "axes.titlecolor": INK,
    "axes.titlesize": 11, "axes.titlelocation": "left", "axes.spines.top": False,
    "axes.spines.right": False, "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.6,
    "xtick.color": MUTED, "ytick.color": MUTED, "xtick.major.size": 0, "ytick.major.size": 0,
    "lines.linewidth": 2, "lines.solid_capstyle": "round", "legend.frameon": False,
    "legend.labelcolor": MUTED})"""),
("md", """## Yhtälön tyyppi kosmisen säikeen poikki

Karakteristinen analyysi antaa $s^2=(c_V-2c_K)/(c_V+2c_K)$. Lasketaan arvo suoraan Lagrangen funktion toisista derivaatoista
ja verrataan sitä kaavaan. Kuvassa on käytetty suhdetta $c_V/c_K$, ja $c_K>0$. Kertoimien todelliset arvot ovat avoin kysymys (#27)."""),
("code", r"""setup = ("GH:H_metric()$ JH:H_kahler()$ eC:[tt,0,0,zz,aa,bb,0,0]$ xC:[tt,zz,aa,bb]$ "
         "pC:[tt=0,zz=0,aa=0,bb=0]$ F:[2,3,7,8]$ "
         "Pa:principal_blocks(GH,JH,H_X,eC,xC,pC,F,[1,3],1,rr,-1)$")
s2 = lab.numeric(setup, "-Pa[2][2][1,1]/Pa[1][1][1,1]", ["rr"])
r = np.linspace(-6, 6, 1201)
r = r[np.abs(r + 2) > 0.02]
exact = (r - 2)/(r + 2)
assert np.max(np.abs(np.asarray(s2(r), float) - exact)) < 1e-9

fig, ax = plt.subplots(figsize=(7, 3.6))
ax.axvspan(-2, 2, color="#f0efec", zorder=0)
ax.axhline(0, color=MUTED, lw=0.8)
ax.plot(r[r < -2], exact[r < -2], color=BLUE)
ax.plot(r[r > -2], exact[r > -2], color=BLUE)
ax.set_ylim(-3, 3); ax.set_xlim(-6, 6)
ax.set_xlabel("kertoimien suhde $c_V/c_K$"); ax.set_ylabel("$s^2$")
ax.set_title("Kertoimien suhde ratkaisee yhtälön tyypin säikeen poikki")
ax.text(0, 2.3, "elliptinen\n$s^2<0$, kun $|c_V/c_K|<2$", ha="center", va="center", color=MUTED)
ax.text(4, -0.75, "hyperbolinen\n$s^2>0$", ha="center", va="center", color=MUTED)
ax.text(-4, -0.75, "hyperbolinen\n$s^2>0$", ha="center", va="center", color=MUTED)
fig.tight_layout(); plt.show()"""),
("md", """## Kähler-vuo kompleksisten käyrien läpi

Vuo on homologinen, eli se on $CP_1$:n läpi $\\pi$ ja kartion $z^2=(z^1)^2$ läpi $2\\pi$, koska kartion aste on 2.
Lasketaan kummankin vuotiheys Maximalla ja integroidaan se numeerisesti."""),
("code", r"""om = "form_from_matrix(cp2_kahler_matrix())"
d1 = lab.numeric("", f"top_coef(form_pullback({om},cp2_X,[aa,bb,0,0],[aa,bb]))", ["aa", "bb"])
d2 = lab.numeric("", f"top_coef(form_pullback({om},cp2_X,[aa,bb,aa^2-bb^2,2*aa*bb],[aa,bb]))", ["aa", "bb"])

def cumulative_flux(density):
    t = np.linspace(0, np.pi/2 - 1e-5, 200001)
    rho = np.tan(t)
    f = 2*np.pi*rho*np.asarray(density(rho, 0*rho), float)/np.cos(t)**2
    return rho, np.concatenate([[0], np.cumsum((f[1:] + f[:-1])/2*np.diff(t))])

rho, phi1 = cumulative_flux(d1)
rho, phi2 = cumulative_flux(d2)
assert abs(phi1[-1] - np.pi) < 1e-3 and abs(phi2[-1] - 2*np.pi) < 1e-3
assert np.max(np.abs(phi1 - np.pi*rho**2/(1 + rho**2))) < 1e-3
print("vuo CP1:", round(phi1[-1]/np.pi, 5), "pi, vuo kartio:", round(phi2[-1]/np.pi, 5), "pi")

m = rho <= 6
fig, ax = plt.subplots(figsize=(7, 3.6))
ax.axhline(np.pi, color=MUTED, lw=0.8, ls=":"); ax.axhline(2*np.pi, color=MUTED, lw=0.8, ls=":")
ax.plot(rho[m], phi1[m], color=BLUE, label="$CP_1$")
ax.plot(rho[m], phi2[m], color=ORANGE, label="kartio $z^2=(z^1)^2$")
ax.set_yticks([0, np.pi, 2*np.pi]); ax.set_yticklabels(["0", r"$\pi$", r"$2\pi$"])
ax.set_xlim(0, 6); ax.set_ylim(0, 7)
ax.set_xlabel(r"säde $\rho$ kartalla"); ax.set_ylabel("vuo säteen sisällä")
ax.set_title("Kartion Kähler-vuo on kaksinkertainen, koska sen aste on 2")
ax.legend(loc="lower right")
fig.tight_layout(); plt.show()"""),
("md", """## Geodeesi, jonka suunta kääntyy

Ratkaisu $z^1=\\tan(x)\\,e^{ia(u)}$, $z^2=0$ toteuttaa sekä Kähler- että tilavuustermin (`tests/test-field-equations.mac`).
Kuvissa $a(u)=\\sin u$. Indusoitu kenttä on $J_{ux}=-\\tfrac12\\sin(2x)\\,a'(u)$."""),
("code", r"""setup = ("JH:H_kahler()$ xl:[uu,vv,xx,yy]$ s:[tan(xx)*cos(sin(uu)),tan(xx)*sin(sin(uu)),0,0]$ "
         "e:append([(uu+vv)/2,xx,yy,(vv-uu)/2],s)$ Ji:induced_kahler_form(JH,H_X,e,xl)$")
Jux = lab.numeric(setup, "Ji[1,3]", ["uu", "xx"])
u, x = np.meshgrid(np.linspace(0, 4*np.pi, 401), np.linspace(-1.5, 1.5, 241))
vals = np.asarray(Jux(u, x), float)
assert np.max(np.abs(vals + 0.5*np.sin(2*x)*np.cos(u))) < 1e-8

cmap = LinearSegmentedColormap.from_list("div", ["#1c5cab", "#86b6ef", "#f0efec", "#e66767", "#a12b2b"])
fig, ax = plt.subplots(figsize=(7, 3.4))
im = ax.pcolormesh(u, x, vals, cmap=cmap, vmin=-0.5, vmax=0.5, shading="auto", rasterized=True)
ax.grid(False)
ax.set_xlabel("valon kaltainen koordinaatti $u$"); ax.set_ylabel("poikittainen $x$")
ax.set_title("Indusoitu Kähler-kenttä vaihtaa merkkiä sekä $u$:n että $x$:n mukana")
fig.colorbar(im, ax=ax, label="$J_{ux}$", shrink=0.9, ticks=[-0.5, 0, 0.5]).outline.set_visible(False)
fig.tight_layout(); plt.show()"""),
("md", """## $CP_2$-projektio

Kuvassa on pinnan projektio $z^1$-tasoon. Jokaisella $u$:n arvolla piste kulkee geodeesia pitkin origon kautta, ja suunta kääntyy $u$:n mukana."""),
("code", r"""xs = np.linspace(-1.1, 1.1, 201)
fig, ax = plt.subplots(figsize=(4.6, 4.6))
for ui, col, name in [(0.0, BLUE, "$u=0$"), (0.8, ORANGE, "$u=0{,}8$"), (np.pi/2, AQUA, r"$u=\pi/2$")]:
    a = np.sin(ui)
    ax.plot(np.tan(xs)*np.cos(a), np.tan(xs)*np.sin(a), color=col, label=name)
ax.set_aspect("equal"); ax.set_xlim(-2.2, 2.2); ax.set_ylim(-2.2, 2.2)
ax.set_xlabel("Re $z^1$"); ax.set_ylabel("Im $z^1$")
ax.set_title("Geodeesin suunta kääntyy $u$:n mukana")
ax.legend(loc="lower right")
fig.tight_layout(); plt.show()"""),
])

for name, n in [("01_ymparisto_ja_testit.ipynb", nb01), ("02_cp2_fubini_study.ipynb", nb02),
                ("03_upotus_ja_vaikutus.ipynb", nb03), ("04_numeriikka_ja_kuvat.ipynb", nb04)]:
    nbf.write(n, OUT / name)
    print("wrote", name)
