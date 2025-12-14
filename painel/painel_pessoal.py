from pathlib import Path
import re

BASE_DIR = Path(__file__).resolve().parent.parent
PRODUTOS_DIR = BASE_DIR / "docs" / "produtos"

def extrair_info(html):
    def pegar(label):
        padrao = rf"<strong>{label}:</strong>\s*(.*?)</p>"
        m = re.search(padrao, html, re.IGNORECASE)
        return m.group(1).strip() if m else "—"

    return {
        "macro": pegar("Macro-nicho"),
        "subnicho": pegar("Subnicho")
    }

def listar_produtos():
    print("\n📊 PAINEL PESSOAL — VISÃO GERAL\n")

    arquivos = list(PRODUTOS_DIR.glob("*.html"))

    if not arquivos:
        print("Nenhum produto encontrado.")
        return

    for i, arq in enumerate(arquivos, 1):
        html = arq.read_text(encoding="utf-8", errors="ignore")
        info = extrair_info(html)

        print(f"{i}. {arq.name}")
        print(f"   Macro-nicho : {info['macro']}")
        print(f"   Subnicho    : {info['subnicho']}")
        print("-" * 40)

if __name__ == "__main__":
    listar_produtos()
