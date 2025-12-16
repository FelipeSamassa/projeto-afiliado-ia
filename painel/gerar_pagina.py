from pathlib import Path
from ia_gerador import gerar_conteudo
from seo_keywords import gerar_palavras_chave

# Caminhos base
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE = BASE_DIR / "template_base_neutra.html"
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
    # ===== DADOS DO PRODUTO =====
    produto = "Curso Completo de Excel"
    tema = "Excel para trabalho"
    link = "https://go.hotmart.com/F103401870R"

    # ===== SEO (SUGESTÃO DA IA) =====
    palavras = gerar_palavras_chave(produto, tema)

    print("\n🔑 PALAVRAS-CHAVE SUGERIDAS:\n")
    print(palavras)

    input("\n➡️ Pressione ENTER para continuar com a criação da página...")

    # ===== CONTEÚDO =====
    conteudo = gerar_conteudo(produto, tema)

    dados = {
        "NOME_ARQUIVO": "Curso_Excel_IA.html",
        "TITULO_PAGINA": f"{produto} – Vale a pena?",
        "DESCRICAO_SEO": f"{produto} vale a pena? Veja se funciona.",
        "HEADLINE": conteudo["HEADLINE"],
        "SUBHEADLINE": conteudo["SUBHEADLINE"],
        "INTRO_SEO": f"Veja se o {produto} realmente vale a pena, como funciona e se é indicado para quem quer aprender {tema}.",
        "PARA_QUEM_E": "<li>Iniciantes</li>",
        "PARA_QUEM_NAO_E": "<li>Usuários avançados</li>",
        "BENEFICIOS": conteudo["BENEFICIOS"],
        "NOME_PRODUTO": produto,
        "DESCRICAO_PRODUTO": conteudo["DESCRICAO_PRODUTO"],
        "MICROTEXTO_CONFIANCA": conteudo["MICROTEXTO_CONFIANCA"],
        "TEXTO_CTA": conteudo["TEXTO_CTA"],
        "LINK_AFILIADO": link,
        "FAQ": ""
    }

    gerar_pagina(dados)
