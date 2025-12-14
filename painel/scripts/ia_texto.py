import os
from dotenv import load_dotenv

from config import MODO_IA_PADRAO

# -------- IA SIMULADA (ZERO CUSTO) --------
def gerar_descricao_simulada(produto, nicho):
    return f"""
<p>
O <strong>{produto}</strong> é um produto voltado para quem deseja evoluir no nicho de
<strong>{nicho}</strong>, buscando mais clareza, organização e resultados práticos.
</p>

<p>
Ele se destaca por oferecer uma abordagem direta, com foco em aplicação real
e aprendizado progressivo, sem promessas irreais.
</p>
"""

# -------- IA REAL (OPCIONAL) --------
def gerar_descricao_real(produto, nicho):
    load_dotenv()

    try:
        from openai import OpenAI
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        prompt = f"""
Crie APENAS a seção de descrição (HTML) para uma página de review.

Produto: {produto}
Nicho: {nicho}

Regras:
- Retorne somente HTML (<p>...</p>)
- 2 a 4 parágrafos
- Linguagem clara e ética
- Sem links e sem CTA
"""

        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Você é um redator profissional."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.6
        )

        return resp.choices[0].message.content

    except Exception as e:
        print("⚠️ Falha na IA real, usando IA simulada.")
        print(f"Detalhe: {e}")
        return gerar_descricao_simulada(produto, nicho)

# -------- FUNÇÃO PRINCIPAL --------
def gerar_descricao_html(produto, nicho, forcar_modo=None):
    modo = forcar_modo or MODO_IA_PADRAO

    if modo == "real":
        return gerar_descricao_real(produto, nicho)

    return gerar_descricao_simulada(produto, nicho)
