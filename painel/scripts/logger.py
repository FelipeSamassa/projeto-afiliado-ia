import json
import os
from datetime import datetime

LOG_PATH = os.path.join(
    os.path.dirname(__file__),
    "../data/logs.json"
)

def registrar_log(acao, produto, nicho=None, modo_ia=None, status="ok", detalhe=None):
    if not os.path.exists(LOG_PATH):
        logs = []
    else:
        with open(LOG_PATH, "r", encoding="utf-8") as f:
            logs = json.load(f)

    evento = {
        "data_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "acao": acao,
        "produto": produto,
        "nicho": nicho,
        "modo_ia": modo_ia,
        "status": status,
        "detalhe": detalhe
    }

    logs.append(evento)

    with open(LOG_PATH, "w", encoding="utf-8") as f:
        json.dump(logs, f, ensure_ascii=False, indent=2)
