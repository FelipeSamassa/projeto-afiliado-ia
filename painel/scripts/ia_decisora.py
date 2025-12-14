import os
from controlador_paginas import caminho_pagina

def decidir_acao(produto):
    path = caminho_pagina(produto)

    if os.path.exists(path):
        return "editar"
    else:
        return "criar"
