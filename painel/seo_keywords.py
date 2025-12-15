from ia_texto import chamar_ia_analise

def gerar_palavras_chave(produto, tema):
    prompt = f"""
Gere 10 palavras-chave SEO com intenção de compra
para um produto digital.

Produto: {produto}
Tema principal: {tema}

Regras:
- foco em decisão de compra
- usar termos como: vale a pena, funciona, melhor, curso
- misturar intenção comercial e problema
- retornar apenas uma lista numerada
"""

    resposta = chamar_ia_analise(prompt)
    return resposta
