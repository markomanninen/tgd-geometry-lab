"""Small Python bridge for running TGD Geometry Lab (Maxima) from Jupyter/Colab.

Every call starts a fresh Maxima process, loads the library and runs the
given code.  Results are returned as text or rendered as LaTeX.

    from tgdlab import Lab
    lab = Lab()                       # finds repo + clifford automatically
    lab.show(setup="G : cp2_metric()$", items=[("g_{ab}", "G")])
"""
from __future__ import annotations

import os
import re
import shutil
import subprocess
from pathlib import Path

try:
    from IPython.display import Math, Markdown, display
except Exception:  # pragma: no cover - plain python
    display = print
    Math = Markdown = str

MARK = "@@TGD@@"


def _find_root() -> Path:
    cands = [os.environ.get("TGD_ROOT"), "/content/tgd-geometry-lab",
             str(Path(__file__).resolve().parent.parent)]
    for c in cands:
        if c and (Path(c) / "tgd-lab.mac").exists():
            return Path(c)
    raise FileNotFoundError("tgd-geometry-lab not found; set TGD_ROOT")


def _find_clifford() -> Path | None:
    for c in [os.environ.get("CLIFFORD_PATH"), "/content/clifford"]:
        if c and (Path(c) / "clifford.mac").exists():
            return Path(c)
    return None


def _clean_tex(t: str) -> str:
    """Make Maxima's TeX output MathJax/KaTeX friendly."""
    t = t.replace(r"\ifx\endpmatrix\undefined\pmatrix{\else\begin{pmatrix}\fi", r"\begin{pmatrix}")
    t = t.replace(r"\ifx\endpmatrix\undefined}\else\end{pmatrix}\fi", r"\end{pmatrix}")
    t = t.replace(r"\cr \end{pmatrix}", r"\end{pmatrix}").replace(r"\cr", r"\\")
    t = t.replace(r"\mathbf{true}", r"\text{true}").replace(r"\mathbf{false}", r"\text{false}")
    return t


def to_python(expr: str) -> str:
    """Translate Maxima's 1D output to a NumPy expression."""
    e = expr.replace("^", "**").replace("%pi", "pi").replace("%e", "e").replace("%i", "1j")
    return re.sub(r"\s+", "", e)


class Lab:
    def __init__(self, root: str | None = None, clifford: str | None = None,
                 timeout: int = 600):
        if not shutil.which("maxima"):
            raise RuntimeError("Maxima is not installed (apt-get install maxima)")
        self.root = Path(root) if root else _find_root()
        self.clifford = Path(clifford) if clifford else _find_clifford()
        self.timeout = timeout

    # ------------------------------------------------------------------
    def _prelude(self, load_clifford: bool) -> str:
        p = f'tgd_root:"{self.root}"$ '
        if self.clifford:
            p += f'clifford_path:"{self.clifford}"$ '
        p += 'load(sconcat(tgd_root,"/tgd-lab.mac"))$ linel:1000000$ '
        if load_clifford and self.clifford:
            p += 'tgd_load_clifford(clifford_path)$ '
        return p

    def run(self, code: str, load_clifford: bool = False) -> str:
        """Run Maxima code; return the lines printed with marker(...)."""
        code = code.strip()
        full = self._prelude(load_clifford) + code
        out = subprocess.run(["maxima", "--very-quiet", f"--batch-string={full}"],
                             capture_output=True, text=True, timeout=self.timeout)
        text = out.stdout
        if "an error" in text or "incorrect syntax" in text.lower():
            tail = "\n".join(text.splitlines()[-25:])
            raise RuntimeError("Maxima error:\n" + tail)
        return text

    def values(self, setup: str, exprs: list[str], tex: bool = False,
               load_clifford: bool = False) -> list[str]:
        """Evaluate expressions after `setup`; return 1D strings (or TeX)."""
        body = setup.strip() + "\n"
        fn = "tex1" if tex else "string"
        for i, e in enumerate(exprs):
            body += f'print(sconcat("{MARK}{i}{MARK}", {fn}({e})))$\n'
        text = self.run(body, load_clifford=load_clifford)
        res = {}
        for line in text.splitlines():
            line = line.strip()
            if line.startswith(MARK):
                _, idx, val = line.split(MARK, 2)
                res[int(idx)] = val.strip()
        vals = [res.get(i, "<no output>") for i in range(len(exprs))]
        return [_clean_tex(v) for v in vals] if tex else vals

    def numeric(self, setup: str, expr: str, variables: list[str]):
        """Return a NumPy function of `variables` from a Maxima expression."""
        import numpy as np
        code = compile(to_python(self.values(setup, [expr])[0]), "<maxima>", "eval")
        names = {k: getattr(np, k) for k in ("sin", "cos", "tan", "atan", "exp", "log",
                                             "sqrt", "pi", "e", "abs")}
        names.update(sec=lambda v: 1/np.cos(v), csc=lambda v: 1/np.sin(v),
                     cot=lambda v: 1/np.tan(v))

        def f(*args):
            scope = dict(names, **dict(zip(variables, args)))
            return np.broadcast_to(eval(code, {"__builtins__": {}}, scope),
                                   np.broadcast(*args).shape)
        return f

    def show(self, setup: str, items: list[tuple[str, str]],
             load_clifford: bool = False) -> None:
        """Render [(latex_label, maxima_expr), ...] as equations."""
        vals = self.values(setup, [e for _, e in items], tex=True,
                           load_clifford=load_clifford)
        for (label, _), v in zip(items, vals):
            display(Math(f"{label} = {v}" if label else v))

    def tests(self) -> bool:
        """Run the full test suite; print the report; return True if all pass."""
        script = self.root / "scripts" / "run_tests.sh"
        args = ["bash", str(script)] + ([str(self.clifford)] if self.clifford else [])
        p = subprocess.run(args, capture_output=True, text=True, timeout=self.timeout)
        print(p.stdout[-6000:])
        return p.returncode == 0
