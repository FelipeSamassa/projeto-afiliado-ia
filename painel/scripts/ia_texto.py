import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def gerar_descricao_html(produto, nicho):
    prompt = f"""
Crie APENAS a seção de descrição (HTML) para uma página de review.

Produto: {produto}
Nicho: {nicho}

Regras:
- Retorne somente HTML (ex: <p>...</p><p>...</p>)
- 2 a 4 parágrafos curtos
- Linguagem clara e direta
- Não faça promessas irreais
- Sem links e sem botão (isso fica fora)
"""

    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Você é um redator profissional focado em clareza e ética."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return resp.choices[0].message.content
