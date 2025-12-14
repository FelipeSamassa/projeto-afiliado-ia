import json
import os

# Caminho para a pasta nicho
nicho_path = os.path.join(os.path.dirname(__file__), "../../nicho")
os.makedirs(nicho_path, exist_ok=True)

# Função para criar página de produto
def criar_pagina(produto):
    filename = f"{produto['produto'].replace(' ', '_')}.html"
    filepath = os.path.join(nicho_path, filename)

    html_content = f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
      <meta charset="UTF-8">
      <title>{produto['produto']}</title>
    </head>
    <body>
      <h1>{produto['produto']}</h1>
      <p>Nicho: {produto['nicho']}</p>
      <a href="{produto['link_afiliado']}" target="_blank">Comprar agora</a>
    </body>
    </html>
    """

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"✅ Página criada: {filepath}")
