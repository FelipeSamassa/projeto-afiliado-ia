from controlador_paginas import (
    listar_paginas,
    apagar_pagina,
    substituir_bloco_descricao
)

from criar_paginas import criar_pagina
from ia_texto import gerar_descricao_html
from logger import registrar_log


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

        # LISTAR PÁGINAS
        if escolha == "1":
            paginas = listar_paginas()
            print("\nPáginas existentes:")
            for p in paginas:
                print("-", p)

        # APAGAR PÁGINA
        elif escolha == "2":
            nome = input("Nome do produto (sem .html): ").strip()
            sucesso = apagar_pagina(nome)

            registrar_log(
                acao="apagar_pagina",
                produto=nome,
                modo_ia="nenhuma",
                status="ok" if sucesso else "erro"
            )

            print("✅ Página apagada." if sucesso else "❌ Página não encontrada.")

        # CRIAR PÁGINA BASE
        elif escolha == "3":
            produto = input("Nome do produto: ").strip()
            nicho = input("Nicho do produto: ").strip()

            criar_pagina({
                "produto": produto,
                "nicho": nicho,
                "link_afiliado": "#"
            })

            registrar_log(
                acao="criar_pagina",
                produto=produto,
                nicho=nicho,
                modo_ia="nenhuma"
            )

            print("✅ Página criada.")

        # EDITAR DESCRIÇÃO (IA SIMULADA)
        elif escolha == "4":
            produto = input("Nome do produto: ").strip()
            nicho = input("Nicho do produto: ").strip()

            bloco = gerar_descricao_html(produto, nicho, forcar_modo="simulada")
            ok, msg = substituir_bloco_descricao(produto, bloco)

            registrar_log(
                acao="editar_descricao",
                produto=produto,
                nicho=nicho,
                modo_ia="simulada",
                status="ok" if ok else "erro",
                detalhe=msg
            )

            print("✅" if ok else "❌", msg)

        # EDITAR DESCRIÇÃO (IA REAL)
        elif escolha == "5":
            confirmar = input(
                "⚠️ Isso usará IA real e pode gastar crédito. Continuar? (s/n): "
            ).strip().lower()

            if confirmar != "s":
                print("❎ Cancelado.")
                continue

            produto = input("Nome do produto: ").strip()
            nicho = input("Nicho do produto: ").strip()

            bloco = gerar_descricao_html(produto, nicho, forcar_modo="real")
            ok, msg = substituir_bloco_descricao(produto, bloco)

            registrar_log(
                acao="editar_descricao",
                produto=produto,
                nicho=nicho,
                modo_ia="real",
                status="ok" if ok else "erro",
                detalhe=msg
            )

            print("✅" if ok else "❌", msg)

        # SAIR
        elif escolha == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    executar()
