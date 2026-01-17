from app.dataBase.db import get_connection

def inserir_falhas(descricao, tipo, gravidade, data_ocorrencia, status, maquina_id=None, equipamento_id=None):
    
    if maquina_id is None and equipamento_id is None:
        
        return "Erro: É necessário informar uma máquina ou equipamento"

   
    conn = get_connection()
    cursor = conn.cursor()

    
    if maquina_id is not None:

        cursor.execute("SELECT id FROM maquinas WHERE id=?", (maquina_id,))
        resultado = cursor.fetchone()
        if resultado is None:
            conn.close()
            return f"Erro: Máquina com ID {maquina_id} não existe"



    if equipamento_id is not None:

        cursor.execute("SELECT id FROM equipamentos WHERE id=?", (equipamento_id,))
        resultado = cursor.fetchone()
        if resultado is None:
            conn.close()
            return f"Erro: Equipamento com ID {equipamento_id} não existe"

    

    cursor.execute("""
        INSERT INTO falhas (descricao, tipo, gravidade, data_ocorrencia, status, maquina_id, equipamento_id)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (descricao, tipo, gravidade, data_ocorrencia, status, maquina_id, equipamento_id))


    conn.commit()
    conn.close()

    

    return "Falha inserida com sucesso"
