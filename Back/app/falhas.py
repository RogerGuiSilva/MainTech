# app/falhas.py
from app.dataBase.db import get_connection

def inserir_falha(descricao, tipo, gravidade, data_ocorrencia, status, maquina_id=None, equipamento_id=None):
    
    if maquina_id is None and equipamento_id is None:
        return "Erro: informe maquina_id ou equipamento_id"


    if not descricao or not tipo or not gravidade or not data_ocorrencia or not status:
        return "Erro: descricao, tipo, gravidade, data_ocorrencia e status são obrigatórios"

    conn = get_connection()
    cursor = conn.cursor()

    
    if maquina_id is not None:
        cursor.execute("SELECT id FROM maquinas WHERE id = ?", (maquina_id,))
        if cursor.fetchone() is None:
            conn.close()
            return f"Erro: Máquina com ID {maquina_id} não existe"

    
    if equipamento_id is not None:
        cursor.execute("SELECT id FROM equipamentos WHERE id = ?", (equipamento_id,))
        if cursor.fetchone() is None:
            conn.close()
            return f"Erro: Equipamento com ID {equipamento_id} não existe"

    cursor.execute("""
    INSERT INTO falhas (descricao, tipo, gravidade, data_ocorrencia, status, maquina_id, equipamento_id)
    VALUES (?, ?, ?, ?, ?, ?, ?)
""", (descricao, tipo, gravidade, data_ocorrencia, status, maquina_id, equipamento_id))

    conn.commit()

    falha_id = cursor.lastrowid   
    conn.close()

    return falha_id
