from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PRODUTOS_DIR = BASE_DIR / "docs" / "produtos"

def coletar_paginas():
    paginas = []
    for arq in PRODUTOS_DIR.glob("*.html"):
        paginas.append(arq.name)
    return paginas

def gerar_relatorio_base():
    paginas = coletar_paginas()

    relatorio = {
        "total_paginas": len(paginas),
        "paginas": paginas
    }

    return relatorio

if __name__ == "__main__":
    dados = gerar_relatorio_base()
    print("\n📊 RELATÓRIO BASE DO SITE\n")
    print(f"Total de páginas: {dados['total_paginas']}")
    print("Páginas encontradas:")
    for p in dados["paginas"]:
        print(f"- {p}")
