import os
import json

BASE_DIR = os.path.dirname(__file__)
NICHO_DIR = os.path.join(BASE_DIR, "../../nicho")
DATA_JSON = os.path.join(BASE_DIR, "../data/produtos.json")

# ===============================
# UTILIDADES
# ===============================
def nome_arquivo(produto):
    return produto.replace(" ", "_") + ".html"

def caminho_pagina(produto):
    return os.path.join(NICHO_DIR, nome_arquivo(produto))

# ===============================
# AÇÕES
# ===============================
def listar_paginas():
    if not os.path.exists(NICHO_DIR):
        return []

    return [
        f for f in os.listdir(NICHO_DIR)
        if f.endswith(".html")
    ]

def apagar_pagina(produto):
    path = caminho_pagina(produto)

    if os.path.exists(path):
        os.remove(path)
        return True

    return False

def atualizar_pagina(produto, novo_html):
    path = caminho_pagina(produto)

    if not os.path.exists(path):
        return False

    with open(path, "w", encoding="utf-8") as f:
        f.write(novo_html)

    return True

def ler_produtos():
    if not os.path.exists(DATA_JSON):
        return []

    with open(DATA_JSON, "r", encoding="utf-8") as f:
        return json.load(f)

def editar_pagina(produto, novo_conteudo):
    path = caminho_pagina(produto)

    if not os.path.exists(path):
        return False

    with open(path, "w", encoding="utf-8") as f:
        f.write(novo_conteudo)

    return True
