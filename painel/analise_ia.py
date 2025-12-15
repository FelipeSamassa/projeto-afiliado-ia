from analise_site import gerar_relatorio_base
from ia_texto import chamar_ia_analise
import json

def executar_analise():
    relatorio = gerar_relatorio_base()

    prompt = f"""
Você é um analista de negócios digitais e afiliados.

Analise os dados do site abaixo e responda SEMPRE nos seguintes tópicos:

1. Visão geral do site
2. Avaliação de nichos e subnichos
3. Risco de duplicação ou canibalização
4. Oportunidades claras de novos produtos
5. Alertas importantes
6. Próxima ação recomendada

Dados do site:
{json.dumps(relatorio, indent=2)}
"""

    resposta = chamar_ia_analise(prompt)

    print("\n🧠 ANÁLISE ESTRATÉGICA DA IA\n")
    print(resposta)

if __name__ == "__main__":
    executar_analise()
