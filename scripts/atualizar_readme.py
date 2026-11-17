#!/usr/bin/env python3
"""Atualiza automaticamente a seção de catálogo do README.md do ArmazemDeConhecimento."""

from __future__ import annotations

import glob
import os
import re
from pathlib import Path
from urllib.parse import quote

REPO_ROOT = Path(__file__).resolve().parent.parent
ESTUDOS_DIR = REPO_ROOT / "2.Estudos"
README_PATH = REPO_ROOT / "README.md"
CATALOGO_DIR = REPO_ROOT.parent.parent / "1.Catalogo"

MARKER_START = "<!-- CATALOGO:INICIO -->"
MARKER_END = "<!-- CATALOGO:FIM -->"

CATEGORY_LABELS: dict[str, str] = {
    "Algoritmos": "Algoritmos e Estruturas de Dados",
    "Banco de Dados": "Banco de Dados",
    "Linguagens _Prog/C e C++": "Linguagens de Programação — C e C++",
    "Linguagens _Prog/Java": "Linguagens de Programação — Java",
    "Linguagens _Prog/PHP": "Linguagens de Programação — PHP",
    "Linguagens _Prog/Python": "Linguagens de Programação — Python",
    "Linguagens _Prog/Ruby": "Linguagens de Programação — Ruby",
    "Matemática": "Matemática e Lógica",
    "Metodologia": "Metodologia de Aprendizado",
    "Tecnologias baixo nivel": "Tecnologias de Baixo Nível",
    "Teorico": "Engenharia de Software, Arquitetura e Teoria",
}


def load_vault_metadata() -> dict[str, dict[str, str]]:
    """Lê título e autor das fichas do cofre Obsidian (4-Arquivos/1.Catalogo/), se disponível."""
    metadata: dict[str, dict[str, str]] = {}
    if not CATALOGO_DIR.is_dir():
        return metadata

    for md_path in sorted(glob.glob(str(CATALOGO_DIR / "*.md"))):
        text = Path(md_path).read_text(encoding="utf-8", errors="ignore")
        pdf_matches = set(re.findall(r"\[\[([^\]]+\.pdf)\]\]", text))
        if not pdf_matches:
            continue

        title_match = re.search(r"^#\s+(.+)$", text, flags=re.MULTILINE)
        author_match = re.search(r"^author:\s*(.+)$", text, flags=re.MULTILINE)
        if not author_match:
            author_match = re.search(r"\*\*Autor(?:\s*/\s*Plataforma)?:\*\*\s*(.+)$", text, flags=re.MULTILINE)

        title = title_match.group(1).strip() if title_match else Path(md_path).stem
        author = author_match.group(1).strip().strip('"').strip("'") if author_match else "—"

        for pdf_name in pdf_matches:
            metadata[pdf_name] = {"title": title, "author": author}

    return metadata


def format_size(size_bytes: int) -> str:
    """Formata tamanho em bytes para KB ou MB legível."""
    mb = size_bytes / (1024 * 1024)
    if mb >= 1.0:
        return f"{mb:.1f} MB"
    kb = size_bytes / 1024
    return f"{kb:.0f} KB"


def escape_md(text: str) -> str:
    """Escapa pipes para não quebrar tabelas Markdown."""
    return text.replace("|", "\\|")


def build_catalog_markdown() -> str:
    """Gera o bloco Markdown completo do catálogo a partir de 2.Estudos/."""
    if not ESTUDOS_DIR.is_dir():
        raise FileNotFoundError(f"Diretório não encontrado: {ESTUDOS_DIR}")

    vault_meta = load_vault_metadata()
    grouped: dict[str, list[Path]] = {}
    total_files = 0
    total_bytes = 0

    for pdf_path in sorted(ESTUDOS_DIR.rglob("*.pdf")):
        rel_dir = pdf_path.parent.relative_to(ESTUDOS_DIR).as_posix()
        grouped.setdefault(rel_dir, []).append(pdf_path)
        total_files += 1
        total_bytes += pdf_path.stat().st_size

    lines: list[str] = [
        MARKER_START,
        f"> **Acervo indexado:** **{total_files} PDFs** distribuídos em **{len(grouped)} categorias** ({format_size(total_bytes)} no total).",
        "",
    ]

    ordered_keys = sorted(grouped.keys(), key=lambda k: CATEGORY_LABELS.get(k, k).casefold())
    for rel_dir in ordered_keys:
        files = sorted(grouped[rel_dir], key=lambda p: p.name.casefold())
        heading = CATEGORY_LABELS.get(rel_dir, rel_dir.replace("/", " — "))
        lines.append(f"### {heading} (`2.Estudos/{rel_dir}/`)")
        lines.append("")
        lines.append("| Material | Autor | Tamanho |")
        lines.append("|---|---|---:|")

        for pdf_path in files:
            rel_path = pdf_path.relative_to(REPO_ROOT).as_posix()
            encoded_url = quote(rel_path, safe="/")
            meta = vault_meta.get(pdf_path.name)
            display_name = escape_md(meta["title"]) if meta else escape_md(pdf_path.stem)
            author = escape_md(meta["author"]) if meta else "—"
            size_str = format_size(pdf_path.stat().st_size)
            lines.append(f"| [{display_name}]({encoded_url}) | {author} | {size_str} |")

        lines.append("")

    lines.append(MARKER_END)
    return "\n".join(lines)


def update_readme() -> None:
    """Substitui o bloco entre os marcadores no README.md."""
    readme_text = README_PATH.read_text(encoding="utf-8")
    if MARKER_START not in readme_text or MARKER_END not in readme_text:
        raise ValueError(f"Marcadores {MARKER_START} / {MARKER_END} não encontrados em {README_PATH}")

    catalog_block = build_catalog_markdown()
    pattern = re.compile(rf"{re.escape(MARKER_START)}.*?{re.escape(MARKER_END)}", flags=re.DOTALL)
    updated = pattern.sub(catalog_block, readme_text, count=1)
    README_PATH.write_text(updated, encoding="utf-8")
    print(f"README atualizado com sucesso: {README_PATH}")


if __name__ == "__main__":
    update_readme()
