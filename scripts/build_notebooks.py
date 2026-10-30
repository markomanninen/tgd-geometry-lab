"""Generate the Colab notebooks in notebooks/ (run: python3 scripts/build_notebooks.py)."""
import nbformat as nbf
from pathlib import Path

REPO = "markomanninen/tgd-geometry-lab"
OUT = Path(__file__).resolve().parent.parent / "notebooks"

def badge(name):
    url = f"https://colab.research.google.com/github/{REPO}/blob/main/notebooks/{name}"
    return f"[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]({url})"

SETUP = r'''# Asennus: Maxima, tämä repositorio ja Dimiter Prodanovin clifford-paketti.
# Colabissa ajo kestää noin minuutin; paikallisesti asetetaan TGD_ROOT / CLIFFORD_PATH.
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
    return n

# ---------------------------------------------------------------- 01
nb01 = nb([
("md", f"""# 01 · Ympäristö ja testit

{badge("01_ymparisto_ja_testit.ipynb")}

Tämä kirja on rakennettu Lanyonin Colab-esimerkin (*Run LanyonScripts in Colab*) mallin mukaan:
väliaikainen Ubuntu-ajoympäristö, GNU Maxima, Prodanovin `clifford`/`cliffordan` -paketit ja
skriptien ajo omissa Maxima-prosesseissaan.

Erona Lanyonin esimerkkiin: jokainen moduuli tarkistetaan **automaattisilla testeillä**
(tunnetut identiteetit kuten $d^2=0$, $d\\omega=0$, $\\mathrm{{Ric}}=3g$, Bianchi), jotta
laskentakirjaston virheet eivät sekoitu TGD:n fysikaalisiin oletuksiin (välitavoite M1)."""),
("code", SETUP),
("md", "## Testisarja\n\nAjaa kaikki `tests/`-hakemiston testit (metriikka, kaarevuus, muodot, $CP_2$, upotus, toiminta, Clifford)."),
("code", "ok = lab.tests()\nprint('KAIKKI TESTIT LÄPI' if ok else 'TESTEJÄ EPÄONNISTUI')"),
("md", """## Clifford-algebra (Prodanov)

Sama paketti kuin LanyonScriptsissä. Tarkistetaan Clifford-relaatiot
$\\gamma_a\\gamma_b+\\gamma_b\\gamma_a = 2\\eta_{ab}$ signatuurilla $(1,3)$."""),
("code", r'''print(lab.values("clifford(g, 1, 3)$",
    ["g[1] . g[1]", "g[2] . g[2]", "g[1] . g[2] + g[2] . g[1]", "g[3] . g[4] + g[4] . g[3]"],
    load_clifford=True))'''),
("md", """## Vertailu: LanyonScriptsin esimerkit

Valinnainen: ajetaan Lanyonin kuusi virtausfysiikan esimerkkiä (Burgers, matala vesi, Euler, Maxwell, MHD)
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
        code = (f'file_search_maxima: append(file_search_maxima, ["{CLI}/$$$.{{mac,wxm}}"])$ '
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

Vaihe II ja välitavoite **M2** (sekä M3–M4 $CP_2$:n osalta): ensimmäinen vertailutesti `spaces/cp2.mac`.

Kartta $Z_0\\neq 0$: $z^1=Z_1/Z_0,\\ z^2=Z_2/Z_0$, reaalikoordinaatit $(x_1,y_1,x_2,y_2)$, $z^k=x_k+i\\,y_k$.

$$K=\\log(1+|z^1|^2+|z^2|^2),\\qquad h_{{i\\bar j}}=\\partial_i\\partial_{{\\bar j}}K,\\qquad
ds^2 = 2\\,h_{{i\\bar j}}\\,dz^i d\\bar z^j,\\qquad \\omega = i\\,h_{{i\\bar j}}\\,dz^i\\wedge d\\bar z^j.$$"""),
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
  ("\\\\sqrt{{\\\\det g}}", "radcan(sqrt(factor(determinant(G))))")])'''),
("md", """## Yhteys ja kaarevuus

Levi-Civita-yhteys, Riemannin ja Riccin tensorit. Tulos: $CP_2$ on Kähler–Einstein,
$\\mathrm{Ric}=3g$, $R=12$; holomorfinen leikkauskaarevuus on vakio $2$ ja
leikkauskaarevuus vaihtelee välillä $[1/2,\\,2]$ (normalisointi $ds^2=2h\\,dz\\,d\\bar z$, $R^2=1$)."""),
("code", f'''lab.show("{CURV} e1:[1,0,0,0]$ Je1 : list_matrix_entries(Jc . transpose(matrix(e1)))$", [
  ("\\\\Gamma^{{x_1}}{{}}_{{x_1x_1}}", "factor(Gam[1][1][1])"),
  ("\\\\mathrm{{Ric}}-3g", "tgd_msimp(Ric - 3*G)"),
  ("R", "scalar_curvature(G, Ric)"),
  ("K(e_{{x_1}},Je_{{x_1}})", "sectional_curvature(G, Rl, e1, Je1)"),
  ("K(e_{{x_1}},e_{{x_2}})|_0", "subst([x1=0,y1=0,x2=0,y2=0], sectional_curvature(G, Rl, [1,0,0,0], [0,0,1,0]))"),
  ("\\\\nabla J\\\\ \\\\text{{(kaikki nollia?)}}", "nested_zero_p(cov_deriv_11(Jc, Gam, cp2_X))")])'''),
("md", """## Koordinaattikarttojen vaihto (Step 2.4)

Kartta $Z_1\\neq0$: $w^1=Z_0/Z_1,\\ w^2=Z_2/Z_1$, jolloin $z^1=1/w^1$, $z^2=w^2/w^1$.
Siirtokuvauksella vedetty metriikka on sama Fubini–Study-kaava uudessa kartassa."""),
("code", f'''lab.show("{CP2} Gc1 : transform_02(G, cp2_X, cp2_W, cp2_chart1_to_chart0())$", [
  ("x(w)", "cp2_chart1_to_chart0()"),
  ("g'-g_{{FS}}(w)", "tgd_msimp(Gc1 - cp2_metric_in_chart(cp2_W))")])'''),
])

# ---------------------------------------------------------------- 03
H = "GH : H_metric()$ JH : H_kahler()$ "
nb03 = nb([
("md", f"""# 03 · Upotusgeometria $H=M^4\\times CP_2$ ja toimintaperiaate

{badge("03_upotus_ja_toiminta.ipynb")}

Vaiheet I.4, VI ja VII (välitavoitteet M6–M7, alkuvaihe). Aika-avaruuspinta $X^4\\subset H$ annetaan
upotuskoordinaatteina $h^k(\\xi)$, ja indusoidut suureet ovat

$$g_{{\\alpha\\beta}} = h_{{kl}}\\,\\partial_\\alpha h^k\\,\\partial_\\beta h^l,\\qquad
J_{{\\alpha\\beta}} = J_{{kl}}\\,\\partial_\\alpha h^k\\,\\partial_\\beta h^l .$$

Konventio: $h_{{kl}} = m_{{kl}} - s_{{kl}}$, $m=\\mathrm{{diag}}(1,-1,-1,-1)$, $s$ = Fubini–Study ($R^2=1$),
joten $H$:n signatuuri on $(1,7)$. Dynaamiset muuttujat ovat upotuskoordinaatit $h^k$ –
indusoitua metriikkaa ja Kähler-muotoa ei varioida erikseen."""),
("code", SETUP),
("md", "## Kanoninen $M^4$-upotus\n\n$h=(\\xi^0,\\ldots,\\xi^3,\\ \\text{vakiopiste } CP_2:ssa)$: indusoitu metriikka on Minkowski ja $J=0$ (tyhjiöekstremaali)."),
("code", f'''lab.show("{H} xi:[t0,t1,t2,t3]$ e0:[t0,t1,t2,t3,0,0,0,0]$", [
  ("g_{{\\\\alpha\\\\beta}}", "induced_metric(GH, H_X, e0, xi)"),
  ("J_{{\\\\alpha\\\\beta}}", "induced_kahler_form(JH, H_X, e0, xi)")])'''),
("md", """## Kosminen säie $X^2\\times Y^2$

$(t,z)$ vapaina, $Y^2=CP_1=\\{z^2=0\\}\\subset CP_2$ (homologisesti epätriviaali kompleksinen pallo).
Tuloksena vakiosuuruinen magneettinen Kähler-kenttä: $J_{\\alpha\\beta}J^{\\alpha\\beta}=2$."""),
("code", f'''lab.show("{H} xs:[tt0,zz0,aa,bb]$ eCS:[tt0,0,0,zz0,aa,bb,0,0]$ g:induced_metric(GH,H_X,eCS,xs)$ J:induced_kahler_form(JH,H_X,eCS,xs)$", [
  ("g_{{\\\\alpha\\\\beta}}", "factor(g)"),
  ("J_{{ab}}", "factor(J[3,4])"),
  ("J_{{\\\\alpha\\\\beta}}J^{{\\\\alpha\\\\beta}}", "kahler_invariant(g, J)"),
  ("\\\\sqrt{{|g|}}", "factor(sqrt_abs_det(g))")])'''),
("md", """## Massaton ekstremaali (ME-tyyppinen ansatsi)

Valokartioparametrit $\\xi=(u,v,x,y)$, $t=(u+v)/2$, $z=(v-u)/2$. $CP_2$-koordinaatit riippuvat vain $u=t-z$:stä
ja poikittaisesta $x$:stä. Indusoitu Kähler-kenttä on nollasta poikkeava mutta *nollakenttä*:
$J_{\\alpha\\beta}J^{\\alpha\\beta}=0$ ja $J\\wedge J=0$ – Kähler-toiminnan tiheys häviää."""),
("code", f'''lab.show("{H} xl:[uu,vv,xx,yy]$ depends([F1,F2],[uu,xx])$ eME:[(uu+vv)/2,xx,yy,(vv-uu)/2,F1,F2,0,0]$ g:induced_metric(GH,H_X,eME,xl)$ J:induced_kahler_form(JH,H_X,eME,xl)$", [
  ("J_{{ux}}", "factor(J[1,3])"),
  ("g^{{uu}}", "mat_inverse(g)[1,1]"),
  ("J_{{\\\\alpha\\\\beta}}J^{{\\\\alpha\\\\beta}}", "kahler_invariant(g, J)"),
  ("J\\\\wedge J", "tgd_simp(instanton_density(J))")])'''),
("md", """## Euler–Lagrange-moottori (Step 7.3)

`euler_lagrange(L, kentät, muuttujat)` laskee $\\partial L/\\partial\\phi-\\partial_\\alpha\\,\\partial L/\\partial(\\partial_\\alpha\\phi)$.
Tarkistus: tilavuustoiminta $\\sqrt{\\det g}$ graafipinnalle $z=f(x,y)$ antaa minimipintayhtälön –
TGD:n tilavuustermin $L_V=k\\sqrt{-g}$ yksinkertaisin analogi."""),
("code", r'''lab.show("depends(fz,[xx,yy])$ gg:induced_metric(ident(3),[X1,X2,X3],[xx,yy,fz],[xx,yy])$ EL:euler_lagrange(sqrt(determinant(gg)),[fz],[xx,yy])$", [
  ("g_{\\alpha\\beta}", "gg"),
  ("\\mathrm{EL}\\cdot(1+f_x^2+f_y^2)^{3/2}", "factor(EL[1]*(1+diff(fz,xx)^2+diff(fz,yy)^2)^(3/2))")])'''),
("md", """## Seuraavat askeleet

* Toiminnan $S=\\int (c_K J_{\\alpha\\beta}J^{\\alpha\\beta}+c_V)\\sqrt{|g|}\\,d^4\\xi$ variointi suoraan
  upotuskoordinaattien $h^k$ suhteen (Vaihe VII, M7).
* Toinen perusmuoto ja Gauss–Codazzi-identiteetit (Step 6.4–6.5).
* Vielbein, spin-yhteys ja Clifford-algebra kaarevalla $CP_2$:lla (Vaihe IV.3–IV.5, M5).
* Kenttäyhtälöiden karakteristinen analyysi Lanyonin `calcev`-tyyliin (Step 7.5)."""),
])

for name, n in [("01_ymparisto_ja_testit.ipynb", nb01), ("02_cp2_fubini_study.ipynb", nb02),
                ("03_upotus_ja_toiminta.ipynb", nb03)]:
    nbf.write(n, OUT / name)
    print("wrote", name)
