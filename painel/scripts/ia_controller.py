import json

# Carrega dados iniciais
with open("../data/produtos.json", "r") as file:
    produtos = json.load(file)

# Exemplo simples: imprimir produtos pendentes
for p in produtos:
    if p["status"] == "pendente":
        print(f"Produto pendente: {p['produto']}")
