from ia_texto import chamar_ia_analise

def analisar_nichos(objetivo):
    prompt = f"""
Você é um analista de mercado digital para afiliados iniciantes.

Objetivo do usuário:
{objetivo}

Analise e retorne:
1. 3 nichos promissores para começar
2. Para cada nicho, informe:
   - tipo de produto ideal (curso, assinatura, físico)
   - nível de concorrência (baixo/médio/alto)
   - facilidade de venda para iniciante
   - motivo resumido
3. Diga qual nicho você recomenda começar AGORA
4. Diga se algum nicho deve ser evitado

Formato de resposta:
- Texto claro
- Listas
- Sem enrolação
"""
    return chamar_ia_analise(prompt)
