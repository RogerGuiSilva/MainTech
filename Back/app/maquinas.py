
from app.dataBase.db import get_connection

def inserir_maquina(nome, setor, tipo, status):
   
    if not nome or not setor or not tipo or not status:
        return "Erro: nome, setor, tipo e status são obrigatórios"

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO maquinas (nome, setor, tipo, status)
        VALUES (?, ?, ?, ?)
    """, (nome, setor, tipo, status))

    conn.commit()
    conn.close()

    return "OK: máquina inserida"
