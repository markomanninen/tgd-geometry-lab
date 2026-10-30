"""MkDocs hooks for the public site."""
from pathlib import Path


def on_config(config):
    """Add an Explainerit section as soon as docs/explainerit/ has pages."""
    root = Path(config["docs_dir"]) / "explainerit"
    pages = sorted(p.name for p in root.glob("*.md")) if root.is_dir() else []
    if not pages:
        return config
    pages.sort(key=lambda name: name != "index.md")
    section = [f"explainerit/{name}" for name in pages]
    # before the notebooks, which stay last
    config["nav"].insert(len(config["nav"]) - 1, {"Explainerit": section})
    return config


def on_page_markdown(markdown, page, config, files):
    """Single pages read better without a left sidebar holding one link."""
    if not page.file.src_path.startswith(("notebooks/", "explainerit/")):
        page.meta.setdefault("hide", ["navigation"])
    return markdown
