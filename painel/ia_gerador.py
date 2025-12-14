import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def gerar_conteudo(produto, nicho):
    prompt = f"""
Produto: {produto}
Nicho: {nicho}

Retorne APENAS um JSON VÁLIDO, sem texto extra, sem markdown, sem explicações.

Formato obrigatório:

{{
  "HEADLINE": "texto",
  "SUBHEADLINE": "texto",
  "BENEFICIOS": "<li></li>",
  "DESCRICAO_PRODUTO": "<p></p>",
  "MICROTEXTO_CONFIANCA": "texto",
  "TEXTO_CTA": "texto"
}}
"""

    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )

    texto = resp.choices[0].message.content.strip()

    # DEBUG VISUAL (IMPORTANTE)
    print("\n🔎 Resposta bruta da IA:\n")
    print(texto)
    print("\n--- FIM DA RESPOSTA ---\n")

    # Tenta converter para JSON
    try:
        return json.loads(texto)
    except json.JSONDecodeError:
        raise ValueError("❌ A IA não retornou um JSON válido.")
