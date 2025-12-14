from controlador_paginas import (
    listar_paginas,
    apagar_pagina,
    editar_pagina
)

def menu():
    print("\n=== CONSOLE DE CONTROLE ===")
    print("1 - Listar páginas")
    print("2 - Apagar página")
    print("3 - Editar página (texto simples)")
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

            if sucesso:
                print("✅ Página apagada com sucesso.")
            else:
                print("❌ Página não encontrada.")

        elif escolha == "3":
            nome = input("Nome do produto (sem .html): ").strip()
            print("Digite o novo conteúdo HTML (finalize com ENTER):")
            novo_html = input()

            sucesso = editar_pagina(nome, novo_html)

            if sucesso:
                print("✅ Página atualizada.")
            else:
                print("❌ Página não encontrada.")

        elif escolha == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    executar()
