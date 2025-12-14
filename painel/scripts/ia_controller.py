import json
import os

# Caminho correto para o JSON
caminho_json = os.path.join(os.path.dirname(__file__), "../data/produtos.json")

# Carrega produtos
with open(caminho_json, "r") as f:
    produtos = json.load(f)

# Simula análise da IA
for p in produtos:
    if p["status"] == "pendente":
        print(f"IA: Produto '{p['produto']}' sugere: Vender agora")
        resposta = input("Você aprova? (s/n): ").strip().lower()
        if resposta == "s":
            p["status"] = "aprovado"
            print(f"Produto '{p['produto']}' aprovado!")
        else:
            p["status"] = "rejeitado"
            print(f"Produto '{p['produto']}' rejeitado!")

# Salva alterações
with open(caminho_json, "w") as f:
    json.dump(produtos, f, indent=2)

print("\n✅ Todos os produtos foram processados. Você pode atualizar o painel no navegador.")

