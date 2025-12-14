from controlador_paginas import (
    listar_paginas,
    apagar_pagina,
    substituir_bloco_descricao
)

from ia_decisora import decidir_acao
from criar_paginas import criar_pagina
from ia_texto import gerar_descricao_html

def menu():
    print("\n=== CONSOLE DE CONTROLE ===")
    print("1 - Listar páginas")
    print("2 - Apagar página")
    print("3 - IA decidir (criar ou editar)")
    print("4 - IA editar SOMENTE a descrição")
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
            produto = input("Nome do produto: ").strip()
            nicho = input("Nicho do produto: ").strip()

            acao = decidir_acao(produto)
            print(f"\n🤖 IA sugere: {acao.upper()} a página")

            confirmar = input("Deseja continuar? (s/n): ").strip().lower()
            if confirmar != "s":
                print("❎ Ação cancelada.")
                continue

            if acao == "criar":
                criar_pagina({"produto": produto, "nicho": nicho, "link_afiliado": "#"})
                print("✅ Página criada.")
            else:
                # Se for editar, por enquanto só substitui a descrição
                bloco = gerar_descricao_html(produto, nicho)
                ok, msg = substituir_bloco_descricao(produto, bloco)
                print("✅" if ok else "❌", msg)

        elif escolha == "4":
            produto = input("Nome do produto: ").strip()
            nicho = input("Nicho do produto: ").strip()

            bloco = gerar_descricao_html(produto, nicho)

            print("\n=== NOVA DESCRIÇÃO (IA) ===")
            print(bloco)

            confirmar = input("\nAplicar essa descrição na página? (s/n): ").strip().lower()
            if confirmar != "s":
                print("❎ Alteração cancelada.")
                continue

            ok, msg = substituir_bloco_descricao(produto, bloco)
            print("✅" if ok else "❌", msg)

        elif escolha == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    executar()
