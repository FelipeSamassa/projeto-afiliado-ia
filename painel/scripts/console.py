from controlador_paginas import (
    listar_paginas,
    apagar_pagina,
    substituir_bloco_descricao
)

from criar_paginas import criar_pagina
from ia_texto import gerar_descricao_html

def menu():
    print("\n=== CONSOLE DE CONTROLE ===")
    print("1 - Listar páginas")
    print("2 - Apagar página")
    print("3 - Criar página (base)")
    print("4 - Editar descrição (IA simulada)")
    print("5 - Editar descrição (IA REAL - gasta crédito)")
    print("0 - Sair")

def executar():
    while True:
        menu()
        escolha = input("Escolha uma opção: ").strip()

        if escolha == "1":
            paginas = listar_paginas()
            print("\nPáginas existentes:")
            for p in paginas:
                print("-", p)

        elif escolha == "2":
            nome = input("Nome do produto (sem .html): ").strip()
            sucesso = apagar_pagina(nome)
            print("✅ Página apagada." if sucesso else "❌ Página não encontrada.")

        elif escolha == "3":
            produto = input("Nome do produto: ").strip()
            nicho = input("Nicho do produto: ").strip()
            criar_pagina({"produto": produto, "nicho": nicho, "link_afiliado": "#"})
            print("✅ Página criada.")

        elif escolha == "4":
            produto = input("Nome do produto: ").strip()
            nicho = input("Nicho do produto: ").strip()
            bloco = gerar_descricao_html(produto, nicho, forcar_modo="simulada")
            ok, msg = substituir_bloco_descricao(produto, bloco)
            print("✅" if ok else "❌", msg)

        elif escolha == "5":
            confirmar = input("⚠️ Isso usará IA real e pode gastar crédito. Continuar? (s/n): ").strip().lower()
            if confirmar != "s":
                print("❎ Cancelado.")
                continue

            produto = input("Nome do produto: ").strip()
            nicho = input("Nicho do produto: ").strip()
            bloco = gerar_descricao_html(produto, nicho, forcar_modo="real")
            ok, msg = substituir_bloco_descricao(produto, bloco)
            print("✅" if ok else "❌", msg)

        elif escolha == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    executar()
