import json
import os

# Caminho para a pasta nicho
nicho_path = os.path.join(os.path.dirname(__file__), "../../nicho")
os.makedirs(nicho_path, exist_ok=True)

# Garante que a pasta CSS exista
css_path = os.path.join(nicho_path, "css")
os.makedirs(css_path, exist_ok=True)

# Crie style.css básico se não existir
css_file = os.path.join(css_path, "style.css")
if not os.path.exists(css_file):
    with open(css_file, "w", encoding="utf-8") as f:
        f.write("""
body {
  font-family: Arial, sans-serif;
  margin: 20px;
}
h1 {
  color: #2c3e50;
}
a {
  display: inline-block;
  margin-top: 10px;
  padding: 10px 15px;
  background-color: #27ae60;
  color: white;
  text-decoration: none;
  border-radius: 5px;
}
""")

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
  <link rel="stylesheet" href="css/style.css">
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
