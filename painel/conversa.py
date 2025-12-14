from ia_gerador import gerar_conteudo
from gerar_pagina import gerar_pagina

def perguntar(texto):
    return input(f"{texto}: ").strip()

def validar_dados(dados):
    faltando = []
    for campo in ["produto", "nicho", "link"]:
        if not dados.get(campo):
            faltando.append(campo)
    return faltando

def modo_conversa():
    print("\n🧠 MODO CONVERSA — CRIAÇÃO DE PÁGINA\n")

    dados_usuario = {
        "produto": "",
        "nicho": "",
        "link": ""
    }

    while True:
        if not dados_usuario["produto"]:
            dados_usuario["produto"] = perguntar("Digite o NOME DO PRODUTO")

        if not dados_usuario["nicho"]:
            dados_usuario["nicho"] = perguntar("Digite o NICHO")

        if not dados_usuario["link"]:
            dados_usuario["link"] = perguntar("Digite o LINK AFILIADO")

        faltando = validar_dados(dados_usuario)

        if faltando:
            print("\n⚠️ Faltam informações para continuar:")
            for f in faltando:
                print(f"- {f}")
            print("\nVamos completar antes de continuar.\n")
            continue

        print("\n✅ Todas as informações recebidas.")
        print("Gerando conteúdo com IA...\n")

        conteudo = gerar_conteudo(
            dados_usuario["produto"],
            dados_usuario["nicho"]
        )

        dados = {
            "NOME_ARQUIVO": dados_usuario["produto"].replace(" ", "_") + ".html",
            "TITULO_PAGINA": f"{dados_usuario['produto']} – Vale a pena?",
            "DESCRICAO_SEO": f"{dados_usuario['produto']} vale a pena? Veja como funciona.",
            "HEADLINE": conteudo["HEADLINE"],
            "SUBHEADLINE": conteudo["SUBHEADLINE"],
            "PARA_QUEM_E": "<li>Iniciantes</li>",
            "PARA_QUEM_NAO_E": "<li>Avançados</li>",
            "BENEFICIOS": conteudo["BENEFICIOS"],
            "NOME_PRODUTO": dados_usuario["produto"],
            "DESCRICAO_PRODUTO": conteudo["DESCRICAO_PRODUTO"],
            "MICROTEXTO_CONFIANCA": conteudo["MICROTEXTO_CONFIANCA"],
            "TEXTO_CTA": conteudo["TEXTO_CTA"],
            "LINK_AFILIADO": dados_usuario["link"],
            "FAQ": ""
        }

        gerar_pagina(dados)

        print("\n🎉 Página criada com sucesso!")
        break

if __name__ == "__main__":
    modo_conversa()
