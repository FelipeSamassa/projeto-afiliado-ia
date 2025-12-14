import json
from pathlib import Path
from ia_gerador import gerar_conteudo

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE = BASE_DIR / "template_mestre_produto.html"
OUTPUT_DIR = BASE_DIR / "docs" / "produtos"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def gerar_pagina(dados):
    html = TEMPLATE.read_text(encoding="utf-8")

    for chave, valor in dados.items():
        html = html.replace(f"{{{{{chave}}}}}", valor)

    output = OUTPUT_DIR / dados["NOME_ARQUIVO"]
    output.write_text(html, encoding="utf-8")
    print(f"✅ Página criada: {output}")

if __name__ == "__main__":
    produto = "Curso Completo de Excel"
    nicho = "Produtividade e Excel"
    link = "https://go.hotmart.com/F103401870R"

    conteudo = gerar_conteudo(produto, nicho)

    dados = {
        "NOME_ARQUIVO": "Curso_Excel_IA.html",
        "TITULO_PAGINA": f"{produto} – Vale a pena?",
        "DESCRICAO_SEO": f"{produto} vale a pena? Veja como funciona.",
        "HEADLINE": conteudo["HEADLINE"],
        "SUBHEADLINE": conteudo["SUBHEADLINE"],
        "PARA_QUEM_E": "<li>Iniciantes</li>",
        "PARA_QUEM_NAO_E": "<li>Avançados</li>",
        "BENEFICIOS": conteudo["BENEFICIOS"],
        "NOME_PRODUTO": produto,
        "DESCRICAO_PRODUTO": conteudo["DESCRICAO_PRODUTO"],
        "MICROTEXTO_CONFIANCA": conteudo["MICROTEXTO_CONFIANCA"],
        "TEXTO_CTA": conteudo["TEXTO_CTA"],
        "LINK_AFILIADO": link,
        "FAQ": ""
    }

    gerar_pagina(dados)
