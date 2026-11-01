"""Create labels, milestones (M1-M8) and issues for the development plan.

Run once:  python3 scripts/seed_tracking.py
Idempotent for labels and milestones (existing ones are reused); issues are
skipped if an issue with the same title already exists.
Requires an authenticated `gh` CLI with access to the repository.
"""
import json
import subprocess

REPO = "markomanninen/tgd-geometry-lab"


def gh(method, path, **fields):
    args = ["gh", "api", "-X", method, f"repos/{REPO}/{path}"]
    for k, v in fields.items():
        if isinstance(v, list):
            for item in v:
                args += ["-f", f"{k}[]={item}"]
        elif isinstance(v, int) and not isinstance(v, bool):
            args += ["-F", f"{k}={v}"]
        else:
            args += ["-f", f"{k}={v}"]
    out = subprocess.run(args, capture_output=True, text=True)
    if out.returncode != 0:
        raise RuntimeError(out.stderr + out.stdout)
    return json.loads(out.stdout) if out.stdout.strip() else None


def get_all(path):
    out = subprocess.run(["gh", "api", "--paginate", f"repos/{REPO}/{path}"],
                         capture_output=True, text=True, check=True)
    txt = out.stdout.replace("][", ",")
    return json.loads(txt) if txt.strip() else []


LABELS = {
    "infra": ("5319e7", "Ympäristö, CI, lataaja, työkalut"),
    "cp2": ("1d76db", "CP2-geometria (Fubini–Study, kartat)"),
    "muodot": ("0e8a16", "Differentiaalimuodot"),
    "geometria": ("006b75", "Yhteydet, kaarevuus, Cartan"),
    "clifford": ("b60205", "Clifford-algebra, vielbein, spin-yhteys"),
    "upotus": ("fbca04", "M4 x CP2 -upotusgeometria"),
    "tgd-dynamiikka": ("d93f0b", "Vaikutus, variaatio, kenttäyhtälöt"),
    "analyysi": ("c5def5", "Ratkaisut, numeriikka, visualisointi"),
    "testit": ("bfd4f2", "Testit ja validointi"),
    "colab": ("f9d0c4", "Colab-kirjat"),
    "dokumentaatio": ("0075ca", "Dokumentaatio"),
    "fysiikka": ("7057ff", "TGD:n fysikaalinen tulkinta"),
}

MILESTONES = [
    ("M1 Maxima- ja Clifford-ympäristö", "Valmis kun: peruslaskenta toimii. Vaihe I.1"),
    ("M2 CP2-metriikka", "Valmis kun: Fubini–Study-tulokset täsmäävät. Vaihe II"),
    ("M3 Differentiaalimuodot", "Valmis kun: muoto-operaatiot ja d^2=0 toimivat. Vaihe III"),
    ("M4 Yhteydet ja kaarevuus", "Valmis kun: kaarevuus-, Bianchi- ja torsiotestit läpäisty. Vaiheet IV.1-2, V"),
    ("M5 Clifford-geometria", "Valmis kun: paikalliset kehykset ja spin-yhteys toimivat. Vaihe IV.3-5"),
    ("M6 Upotusgeometria", "Valmis kun: indusoitu geometria ja Gauss–Codazzi toimivat. Vaiheet I.3-4, VI"),
    ("M7 TGD:n vaikutusintegraali", "Valmis kun: variaatioyhtälöt muodostuvat upotuskoordinaattien suhteen. Vaihe VII"),
    ("M8 Ratkaisuanalyysi", "Valmis kun: ensimmäiset testattavat ratkaisut saatu. Vaihe VIII"),
]

# (milestone index, title, labels, done, body)
ISSUES = [
    # ---- M1
    (1, "Step 1.1: Maxima-lataaja ja laskentakonventiot", ["infra", "dokumentaatio"], True,
     "`tgd-lab.mac` lataa moduulit; konventiot kirjattu `docs/konventiot.md`."),
    (1, "Colab-testiympäristö (kirja 01) ja tgdlab.py-silta", ["infra", "colab"], True,
     "Lanyonin Colab-esimerkin mallin mukainen asennus + testisarja + Maxima→LaTeX-silta."),
    (1, "GitHub Actions: testit jokaisesta muutoksesta", ["infra", "testit"], True,
     "`.github/workflows/tests.yml` ajaa `scripts/run_tests.sh` Prodanovin clifford-paketin kanssa."),
    (1, "Step 1.2: define_manifold / define_metric -rajapinta", ["infra", "geometria"], True,
     "`core/metric.mac`: metric_inverse, metric_determinant, signatuuri, transform_02."),
    # ---- M2
    (2, "Step 2.1–2.3: CP2 Fubini–Study-metriikka Kähler-potentiaalista", ["cp2"], True,
     "Testit: symmetria, det g = 16/(1+ρ²)^6, positiividefiniittisyys, käänteismatriisi."),
    (2, "Step 2.5: Kähler-rakenne ω, J ja dω = 0", ["cp2", "muodot"], True,
     "Testit: J² = −1, JᵀgJ = g, dω = 0, ∇J = 0, ω∧ω/2 = vol."),
    (2, "Step 2.4: karttasiirtymä Z0 ↔ Z1", ["cp2"], True,
     "Siirtokuvauksella vedetty metriikka = FS-kaava uudessa kartassa (testattu)."),
    (2, "Step 2.4: kartta Z2 ≠ 0 ja kaikki siirtymät", ["cp2", "testit"], False,
     "- [ ] `cp2_chart2_to_chart0()`\n- [ ] siirtymät Z1 ↔ Z2\n- [ ] testi: metriikka ja kaarevuusinvariantit säilyvät kaikissa karttapareissa\n\nValmis kun kaikki kolme karttaa ja siirtymät on testattu."),
    (2, "cp2.mac vertailutesti: Ric = 3g, R = 12, holomorfinen leikkauskaarevuus 2", ["cp2", "testit"], True,
     "Normalisointi ds² = 2h dz dz̄ (R² = 1): K ∈ [1/2, 2]. Ks. docs/konventiot.md."),
    (2, "CP2-säde R² ja TGD:n normalisoinnin varmistus", ["cp2", "fysiikka", "dokumentaatio"], False,
     "- [ ] Vertaa `cp2_R2`-skaalausta Pitkäsen konventioon (s_kl, J_kl normalisointi)\n- [ ] Lisää testi Ric = 3g/R² mielivaltaisella R²:lla\n- [ ] Kirjaa konventiot.md:hen\n\nValmis kun TGD-kirjallisuuden normalisointi on toistettavissa parametrilla."),
    # ---- M3
    (3, "Step 3.1–3.3: muodot, ulkotulo ja ulkoderivaatta", ["muodot"], True,
     "Testit: antisymmetria, d² = 0 (0- ja 1-muodot), asteittainen Leibniz."),
    (3, "Step 3.4: Hodge-tähti ja sisätulo", ["muodot"], True,
     "Testit: ⋆⋆ = +1 (R⁴, 2-muodot), ⋆⋆ = −1 (Minkowski)."),
    (3, "Step 3.5: differentiaalimuotojen integraalit (symbolinen)", ["muodot"], False,
     "- [ ] integraalilausekkeen muodostus p-muodosta ja parametrisoinnista\n- [ ] Stokes-testi yksinkertaisella alueella\n- [ ] CP1:n Kähler-vuo ∫ω (homologinen testi)\n\nValmis kun Stokesin lause tarkistuu symbolisesti esimerkissä."),
    # ---- M4
    (4, "Step 4.1–4.2: Christoffel ja kovariantti derivaatta", ["geometria"], True,
     "Testit: Γ symmetrinen, ∇g = 0 (S² ja CP2), ∇J = 0."),
    (4, "Step 5.1–5.2, 5.4: Riemann, Ricci, Bianchi", ["geometria"], True,
     "Testit: algebralliset symmetriat, Bianchi I, kontrahoitu Bianchi II."),
    (4, "Step 5.3: Cartanin rakenneyhtälöt ja torsio", ["geometria"], False,
     "- [ ] `geometry/cartan.mac`: yhteys-1-muodot ω^a_b kehyksestä\n- [ ] kaarevuus-2-muodot Ω = dω + ω∧ω\n- [ ] torsio T^a = de^a + ω^a_b ∧ e^b\n- [ ] testi: T = 0 Levi-Civitalle; Ω vastaa Riemannin tensoria (S² ja CP2)\n\nValmis kun Cartan- ja koordinaattikaarevuus täsmäävät. Riippuu vielbein-issuesta."),
    # ---- M5
    (5, "Clifford-relaatiot Prodanovin paketilla", ["clifford", "testit"], True,
     "Testit: Cl(4,0) ja Cl(1,3)."),
    (5, "Step 4.3: ortonormaalit kehykset (vielbein) CP2:lle ja H:lle", ["clifford", "geometria"], False,
     "- [ ] `algebra/vielbein.mac`: e^a_μ annetusta metriikasta (Cholesky / CP2:lle unitaarinen kehys)\n- [ ] testi: g = eᵀ η e\n- [ ] H = M4 × CP2 lohkokehys\n\nValmis kun kehys toimii CP2:lle ja H:lle."),
    (5, "Step 4.4: spin-yhteys ortonormaalista kehyksestä", ["clifford", "geometria"], False,
     "- [ ] ω_μ^{ab} kehyksestä ja Christoffelista\n- [ ] testi: antisymmetria ω^{ab} = −ω^{ba}\n- [ ] CP2:n spin- vs spin^c-rakenne (CP2 ei ole spin-monisto → Kähler-kytkentä tarvitaan)\n\nValmis kun spin-yhteys täsmää Cartan-moduulin kanssa."),
    (5, "Step 4.5: paikalliset gammamatriisit γ^μ = e_a^μ γ^a kaarevalla monistolla", ["clifford"], False,
     "- [ ] Prodanovin cliffordin generaattorit paikallisessa kehyksessä\n- [ ] testi: {γ^μ, γ^ν} = 2g^{μν}\n- [ ] Dirac-operaattorin symbolinen muoto (alku)\n\nValmis kun Clifford-relaatio toimii kaarevalla metriikalla."),
    # ---- M6
    (6, "Step 6.1–6.3: H = M4 × CP2, indusoitu metriikka ja Kähler-muoto", ["upotus"], True,
     "Testit: signatuuri (1,7), kanoninen M4 (g = m, J = 0)."),
    (6, "Vertailuupotukset: kosminen säie ja massaton ekstremaali", ["upotus", "fysiikka", "testit"], True,
     "Kosminen säie: J_ab J^ab = 2. ME: J ≠ 0, g^{uu} = 0, J² = 0, J∧J = 0."),
    (6, "Step 6.4: normaalikehys ja toinen perusmuoto", ["upotus", "geometria"], False,
     "- [ ] normaalivektorit (Gram–Schmidt H:n metriikalla)\n- [ ] B^k_{αβ} = D_α ∂_β h^k ja keskikaarevuus H^k = g^{αβ}B^k_{αβ}\n- [ ] testi: tunnettu pinta R³:ssa (pallo, sylinteri)\n\nValmis kun minimipintaehto H^k = 0 voidaan tarkistaa upotukselle."),
    (6, "Step 6.5: Gaussin, Codazzin ja Riccin yhtälöt", ["upotus", "geometria", "testit"], False,
     "- [ ] Gauss: sisäinen kaarevuus = ympäröivä + B·B -termit\n- [ ] Codazzi ja Ricci (normaalikimppu)\n- [ ] testit pallolla R³:ssa ja kosmisella säikeellä\n\nValmis kun identiteetit tarkistuvat symbolisesti."),
    # ---- M7
    (7, "Step 7.1: vaikutustiheydet L_K, L_V ja J∧J", ["tgd-dynamiikka"], True,
     "`tgd/action.mac`; kertoimet c_K, c_V symbolisina."),
    (7, "Step 7.3: Euler–Lagrange-moottori", ["tgd-dynamiikka", "testit"], True,
     "Testit: aaltoyhtälö, minimipintayhtälö tilavuusvaikutuksesta."),
    (7, "Step 7.2: L_TGD:n variaatio upotuskoordinaattien h^k suhteen", ["tgd-dynamiikka", "fysiikka"], False,
     "- [ ] kentät = upotuskoordinaatit (M4-projektio tai CP2-koordinaatit QFT-rajalla)\n- [ ] EL-yhtälöt L = (c_K J·J + c_V)√|g|:stä\n- [ ] vertailu Pitkäsen kovarianttiin muotoon D_α(T^{αβ}∂_β h^k) + J-termit = 0\n\nValmis kun yhtälöt muodostuvat ja täsmäävät kovarianttiin muotoon."),
    (7, "Tarkistus: kosminen säie ja ME ovat ekstremaaleja", ["tgd-dynamiikka", "fysiikka", "testit"], False,
     "- [ ] sijoita vertailuupotukset kenttäyhtälöihin → 0\n- [ ] minimipintaehto H^k = 0 ME:lle\n\nValmis kun molemmat läpäisevät testin. Riippuu L_TGD-variaatiosta ja toisesta perusmuodosta."),
    (7, "Step 7.4: Noether-virrat ja säilymislait", ["tgd-dynamiikka"], False,
     "- [ ] virrat H:n isometrioista (Poincaré, SU(3)) indusoituina\n- [ ] divergenssin tarkistus ratkaisuilla\n\nValmis kun säilyminen tarkistuu vertailuupotuksilla."),
    (7, "Step 7.5: karakteristinen analyysi Lanyonin calcev-tyyliin", ["tgd-dynamiikka", "analyysi"], False,
     "- [ ] kvasilineaarinen muoto linearisoidulle kenttäyhtälölle\n- [ ] karakteristinen matriisi, ominaisarvot/-vektorit (vrt. LanyonScripts eqnsys)\n- [ ] milloin hyperbolinen analyysi soveltuu\n\nValmis kun yksi TGD-yhtälöjärjestelmä on analysoitu Lanyonin tapaan."),
    # ---- M8
    (8, "Step 8.1–8.2: symmetriset erikoistapaukset ja analyyttiset ratkaisut", ["analyysi", "fysiikka"], False,
     "- [ ] CP2-tyyppiset tyhjiöekstremaalit\n- [ ] Lagrangen pintojen tyhjiöekstremaalit\n- [ ] pallosymmetriset ansatsit\n\nValmis kun vähintään yksi uusi ratkaisu on tarkistettu."),
    (8, "Step 8.4–8.5: numeriikka ja visualisointi Pythonilla", ["analyysi", "colab"], False,
     "- [ ] Maxima-lausekkeet → NumPy (lambdify-tyyli)\n- [ ] kuvaajat CP2-projektioista ja indusoiduista kentistä\n- [ ] Colab-kirja 04\n\nValmis kun kirja 04 tuottaa kuvat ratkaisusta."),
    # ---- docs (no milestone)
    (None, "Lanyon-launch-videon transkriptio ja tavoitteet dokumenttiin", ["dokumentaatio"], False,
     "Videota https://youtu.be/gSH50n-9ZLk ei saatu haettua automaattisesti.\n- [ ] liitä transkriptio\n- [ ] päivitä kehityssuunnitelman Lanyon-osio (verifioitu laskenta, spesifikaatio → koodi + Lean-todistus)"),
    (None, "Manninen (2024) TGD-historian keskeiset kaavat vertailutesteiksi", ["dokumentaatio", "fysiikka", "testit"], False,
     "Kirjasta *Through the Wormhole on Spacetime Surface* (2024): S = S_K + S_V, g_αβ = h_kl ∂h∂h, J_αβ, minimipinnat, twistorinosto.\n- [ ] poimi jokaisesta kaavasta testattava väite\n- [ ] linkitä testit dokumenttiin"),
]


def main():
    existing_labels = {l["name"] for l in get_all("labels")}
    for name, (color, desc) in LABELS.items():
        if name not in existing_labels:
            gh("POST", "labels", name=name, color=color, description=desc)
    ms = {m["title"]: m["number"] for m in get_all("milestones?state=all")}
    for title, desc in MILESTONES:
        if title not in ms:
            ms[title] = gh("POST", "milestones", title=title, description=desc)["number"]
    ms_by_idx = {i + 1: ms[t] for i, (t, _) in enumerate(MILESTONES)}
    existing = {i["title"]: i["number"] for i in get_all("issues?state=all&per_page=100")}
    created = []
    for mi, title, labels, done, body in ISSUES:
        if title in existing:
            num = existing[title]
        else:
            kw = dict(title=title, body=body, labels=labels)
            if mi:
                kw["milestone"] = ms_by_idx[mi]
            num = gh("POST", "issues", **kw)["number"]
            if done:
                gh("PATCH", f"issues/{num}", state="closed", state_reason="completed")
        created.append((num, title, done))
    for num, title, done in created:
        print(f"#{num:<3} {'✅' if done else '⬜'} {title}")
    for i in range(1, 9):
        m = gh("GET", f"milestones/{ms_by_idx[i]}")
        print(f"{m['title']}: {m['closed_issues']}/{m['open_issues'] + m['closed_issues']}")


if __name__ == "__main__":
    main()
