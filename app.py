from flask import Flask, request, jsonify, send_from_directory
import json
import os
from painel.scripts.criar_paginas import criar_pagina

app = Flask(__name__, static_folder="painel", static_url_path="/painel")

# Caminho do JSON
json_path = os.path.join("painel", "data", "produtos.json")

# Serve index.html do painel
@app.route("/")
def painel():
    return send_from_directory("painel", "index.html")

# Endpoint para listar produtos
@app.route("/produtos", methods=["GET"])
def listar_produtos():
    with open(json_path, "r", encoding="utf-8") as f:
        produtos = json.load(f)
    return jsonify(produtos)

# Endpoint para aprovar/rejeitar produto
@app.route("/produto/atualizar", methods=["POST"])
def atualizar_produto():
    dados = request.json
    produto_id = dados["id"]
    acao = dados["acao"]

    with open(json_path, "r", encoding="utf-8") as f:
        produtos = json.load(f)

    for p in produtos:
        if p["id"] == produto_id:
            p["status"] = "aprovado" if acao == "aprovar" else "rejeitado"
            # Cria página automaticamente se aprovado
            if acao == "aprovar":
                criar_pagina(p)
            break

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(produtos, f, indent=2, ensure_ascii=False)

    return jsonify({"sucesso": True})

if __name__ == "__main__":
    app.run(debug=True)
