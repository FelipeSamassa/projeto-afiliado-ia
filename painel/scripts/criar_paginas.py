import json
import os

# ===============================
# CAMINHOS
# ===============================
nicho_path = os.path.join(os.path.dirname(__file__), "../../nicho")
os.makedirs(nicho_path, exist_ok=True)

css_path = os.path.join(nicho_path, "css")
os.makedirs(css_path, exist_ok=True)

# ===============================
# CSS PADRÃO (criado automaticamente)
# ===============================
css_file = os.path.join(css_path, "style.css")
if not os.path.exists(css_file):
    with open(css_file, "w", encoding="utf-8") as f:
        f.write("""
body {
  font-family: Arial, Helvetica, sans-serif;
  background: #f7f7f7;
  margin: 0;
  padding: 0;
}

.container {
  max-width: 800px;
  margin: 40px auto;
  background: #ffffff;
  padding: 30px;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.08);
}

h1 {
  color: #2c3e50;
  margin-bottom: 10px;
}

p {
  line-height: 1.6;
  color: #444;
}

.cta {
  display: inline-block;
  margin-top: 20px;
  padding: 14px 22px;
  background-color: #27ae60;
  color: #ffffff;
  text-decoration: none;
  font-weight: bold;
  border-radius: 6px;
}

.cta:hover {
  background-color: #219150;
}

.disclaimer {
  margin-top: 30px;
  font-size: 13px;
  color: #777;
}
""")

# ===============================
# TEXTO DINÂMICO (sem IA ainda)
# ===============================
def gerar_descricao(produto):
    return f"""
O {produto['produto']} é uma solução voltada para quem deseja evoluir no nicho
de {produto['nicho']}. Ele foi desenvolvido para pessoas que buscam um caminho
mais organizado e prático nessa área.

Produtos desse tipo vêm se destacando por entregarem conhecimento aplicável,
principalmente para quem quer resultados reais e consistentes.
"""

# ===============================
# GERADOR DE PÁGINAS
# ===============================
def criar_pagina(produto):
    filename = f"{produto['produto'].replace(' ', '_')}.html"
    filepath = os.path.join(nicho_path, filename)

    html_content = f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>{produto['produto']} | Vale a pena?</title>
  <meta name="description" content="Análise honesta do produto {produto['produto']}. Veja se vale a pena e para quem é indicado.">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <div class="container">
    <h1>{produto['produto']}</h1>

    <p>
      {gerar_descricao(produto)}
    </p>

    <a class="cta" href="{produto['link_afiliado']}" target="_blank">
      Acessar o produto oficial
    </a>

    <div class="disclaimer">
      <p>
        Este site não é o produtor do conteúdo.
        Podemos receber comissão caso você compre pelo link acima,
        sem custo adicional para você.
      </p>
    </div>
  </div>

</body>
</html>
"""

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"✅ Página criada: {filepath}")

# ===============================
# EXECUÇÃO DIRETA (SEM FLASK)
# ===============================
if __name__ == "__main__":
    json_path = os.path.join(os.path.dirname(__file__), "../data/produtos.json")

    if not os.path.exists(json_path):
        print("❌ Arquivo produtos.json não encontrado.")
        exit()

    with open(json_path, "r", encoding="utf-8") as f:
        produtos = json.load(f)

    if not produtos:
        print("⚠️ Nenhum produto encontrado no JSON.")
        exit()

    for produto in produtos:
        criar_pagina(produto)
