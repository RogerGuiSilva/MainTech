from flask import Blueprint, jsonify, request
from app.dataBase.db import get_connection
from app.falhas import inserir_falha

bp = Blueprint("main", __name__)




STATUS_FALHA = {
    "ANALISE",
    "MANUTENCAO",
    "RESOLVIDA",
    "CANCELADA"
}

STATUS_MAQUINA = {
    "DISPONIVEL",
    "EM_USO",
    "PARADA"
}

TRANSICOES_VALIDAS = {
    "ANALISE": {
        "MANUTENCAO",
        "RESOLVIDA",
        "CANCELADA"
    },

    "MANUTENCAO": {
        "RESOLVIDA",
        "CANCELADA"
    },

    "RESOLVIDA": set(),

    "CANCELADA": set()
}



def montar_falha_com_join(cursor, falha_id: int):

    cursor.execute("""
        SELECT 
            f.id,
            f.descricao,
            f.tipo,
            f.gravidade,
            f.status,
            f.data_ocorrencia,

            m.id,
            m.nome,
            m.setor,

            e.id,
            e.nome,
            e.setor

        FROM falhas f

        LEFT JOIN maquinas m
            ON f.maquina_id = m.id

        LEFT JOIN equipamentos e
            ON f.equipamento_id = e.id

        WHERE f.id = ?
    """, (falha_id,))

    r = cursor.fetchone()

    if r is None:
        return None

    falha = {
        "id": r[0],
        "descricao": r[1],
        "tipo": r[2],
        "gravidade": r[3],
        "status": r[4],
        "data_ocorrencia": r[5]
    }

    if r[6] is not None:
        falha["maquina"] = {
            "id": r[6],
            "nome": r[7],
            "setor": r[8]
        }

    if r[9] is not None:
        falha["equipamento"] = {
            "id": r[9],
            "nome": r[10],
            "setor": r[11]
        }

    return falha

def atualizar_status_maquina(cursor, maquina_id):

    cursor.execute("""
        SELECT COUNT(*)
        FROM falhas
        WHERE maquina_id = ?
        AND status IN ('ANALISE', 'MANUTENCAO')
    """, (maquina_id,))

    falhas_ativas = cursor.fetchone()[0]

    if falhas_ativas > 0:

        cursor.execute("""
            UPDATE maquinas
            SET status = 'PARADA'
            WHERE id = ?
        """, (maquina_id,))

    else:

        cursor.execute("""
            UPDATE maquinas
            SET status = 'DISPONIVEL'
            WHERE id = ?
        """, (maquina_id,))


@bp.route("/equipamentos", methods=["GET"])
def get_equipamentos():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, nome, setor, tipo, status
        FROM equipamentos
    """)

    rows = cursor.fetchall()

    conn.close()

    equipamentos = []

    for row in rows:

        equipamentos.append({
            "id": row[0],
            "nome": row[1],
            "setor": row[2],
            "tipo": row[3],
            "status": row[4]
        })

    return jsonify(equipamentos)


@bp.route("/equipamentos", methods=["POST"])
def criar_equipamento():

    dados = request.get_json() or {}

    campos = ["nome", "setor", "tipo", "status"]

    for campo in campos:

        if not dados.get(campo):
            return jsonify({
                "erro": f"Campo '{campo}' é obrigatório"
            }), 400

    status = str(dados["status"]).strip().upper()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id
        FROM equipamentos
        WHERE nome = ?
    """, (dados["nome"],))

    if cursor.fetchone():

        conn.close()

        return jsonify({
            "erro": "Equipamento já cadastrado"
        }), 409

    cursor.execute("""
        INSERT INTO equipamentos (nome, setor, tipo, status)
        VALUES (?, ?, ?, ?)
    """, (
        dados["nome"],
        dados["setor"],
        dados["tipo"],
        status
    ))

    conn.commit()
    conn.close()

    return jsonify({
        "mensagem": "Equipamento cadastrado com sucesso"
    }), 201




@bp.route("/maquinas", methods=["GET"])
def get_maquinas():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, nome, setor, tipo, status
        FROM maquinas
    """)

    rows = cursor.fetchall()

    conn.close()

    maquinas = []

    for row in rows:

        maquinas.append({
            "id": row[0],
            "nome": row[1],
            "setor": row[2],
            "tipo": row[3],
            "status": row[4]
        })

    return jsonify(maquinas)


@bp.route("/maquinas", methods=["POST"])
def criar_maquina():

    dados = request.get_json() or {}

    campos = ["nome", "setor", "tipo", "status"]

    for campo in campos:

        if not dados.get(campo):
            return jsonify({
                "erro": f"Campo '{campo}' é obrigatório"
            }), 400

    status = str(dados["status"]).strip().upper()

    if status not in STATUS_MAQUINA:
        return jsonify({
            "erro": f"Status inválido: {sorted(STATUS_MAQUINA)}"
        }), 400

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id
        FROM maquinas
        WHERE nome = ?
    """, (dados["nome"],))

    if cursor.fetchone():

        conn.close()

        return jsonify({
            "erro": "Máquina já cadastrada"
        }), 409

    cursor.execute("""
        INSERT INTO maquinas (nome, setor, tipo, status)
        VALUES (?, ?, ?, ?)
    """, (
        dados["nome"],
        dados["setor"],
        dados["tipo"],
        status
    ))

    conn.commit()
    conn.close()

    return jsonify({
        "mensagem": "Máquina cadastrada com sucesso"
    }), 201




@bp.route("/falhas", methods=["GET"])
def listar_falhas():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            f.id,
            f.descricao,
            f.tipo,
            f.gravidade,
            f.status,
            f.data_ocorrencia,

            m.id,
            m.nome,
            m.setor,

            e.id,
            e.nome,
            e.setor

        FROM falhas f

        LEFT JOIN maquinas m
            ON f.maquina_id = m.id

        LEFT JOIN equipamentos e
            ON f.equipamento_id = e.id

        WHERE f.status NOT IN ('RESOLVIDA', 'CANCELADA')

        ORDER BY f.id DESC
    """)
    
    rows = cursor.fetchall()

    conn.close()

    resultado = []

    for r in rows:

        falha = {
            "id": r[0],
            "descricao": r[1],
            "tipo": r[2],
            "gravidade": r[3],
            "status": r[4],
            "data_ocorrencia": r[5]
        }

        if r[6] is not None:

            falha["maquina"] = {
                "id": r[6],
                "nome": r[7],
                "setor": r[8]
            }

        if r[9] is not None:

            falha["equipamento"] = {
                "id": r[9],
                "nome": r[10],
                "setor": r[11]
            }

        resultado.append(falha)

    return jsonify(resultado)

@bp.route("/falhas/historico", methods=["GET"])
def listar_historico_falhas():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            f.id,
            f.descricao,
            f.tipo,
            f.gravidade,
            f.status,
            f.data_ocorrencia,

            m.id,
            m.nome,
            m.setor,

            e.id,
            e.nome,
            e.setor

        FROM falhas f

        LEFT JOIN maquinas m
            ON f.maquina_id = m.id

        LEFT JOIN equipamentos e
            ON f.equipamento_id = e.id

        WHERE f.status IN ('RESOLVIDA', 'CANCELADA')

        ORDER BY f.id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    resultado = []

    for r in rows:

        falha = {
            "id": r[0],
            "descricao": r[1],
            "tipo": r[2],
            "gravidade": r[3],
            "status": r[4],
            "data_ocorrencia": r[5]
        }

        if r[6] is not None:
            falha["maquina"] = {
                "id": r[6],
                "nome": r[7],
                "setor": r[8]
            }

        if r[9] is not None:
            falha["equipamento"] = {
                "id": r[9],
                "nome": r[10],
                "setor": r[11]
            }

        resultado.append(falha)

    return jsonify(resultado)


@bp.route("/falhas", methods=["POST"])
def criar_falha_route():

    dados = request.get_json() or {}

    campos = [
        "descricao",
        "tipo",
        "gravidade",
        "data_ocorrencia",
        "status"
    ]

    for campo in campos:

        if not dados.get(campo):
            return jsonify({
                "erro": f"Campo '{campo}' é obrigatório"
            }), 400

    status = str(dados["status"]).strip().upper()

    if status not in STATUS_FALHA:

        return jsonify({
            "erro": f"Status inválido: {sorted(STATUS_FALHA)}"
        }), 400

    maquina_id = dados.get("maquina_id")
    equipamento_id = dados.get("equipamento_id")

    if maquina_id is None and equipamento_id is None:

        return jsonify({
            "erro": "Informe maquina_id OU equipamento_id"
        }), 400

    if maquina_id is not None and equipamento_id is not None:

        return jsonify({
            "erro": "Informe apenas maquina_id OU equipamento_id"
        }), 400

    resp = inserir_falha(
        descricao=dados["descricao"],
        tipo=dados["tipo"],
        gravidade=dados["gravidade"],
        data_ocorrencia=dados["data_ocorrencia"],
        status=status,
        maquina_id=maquina_id,
        equipamento_id=equipamento_id
    )

    if isinstance(resp, str):

        return jsonify({
            "erro": resp
        }), 400

    conn = get_connection()
    cursor = conn.cursor()

    atualizar_status_maquina(
        cursor,
        maquina_id,
        
    )

    falha = montar_falha_com_join(cursor, resp)

    conn.commit()
    conn.close()

    return jsonify(falha), 201


@bp.route("/falhas/<int:falha_id>", methods=["GET"])
def obter_falha(falha_id):

    conn = get_connection()
    cursor = conn.cursor()

    falha = montar_falha_com_join(cursor, falha_id)

    conn.close()

    if falha is None:

        return jsonify({
            "erro": "Falha não encontrada"
        }), 404

    return jsonify(falha), 200


@bp.route("/falhas/<int:falha_id>/status", methods=["PATCH"])
def atualizar_status_falha(falha_id):

    dados = request.get_json() or {}

    if "status" not in dados:

        return jsonify({
            "erro": "Campo 'status' é obrigatório"
        }), 400

    novo_status = str(dados["status"]).strip().upper()

    if novo_status not in STATUS_FALHA:

        return jsonify({
            "erro": "Status inválido"
        }), 400

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT status, maquina_id
        FROM falhas
        WHERE id = ?
    """, (falha_id,))

    row = cursor.fetchone()

    if row is None:

        conn.close()

        return jsonify({
            "erro": "Falha não encontrada"
        }), 404

    status_atual = row[0]
    maquina_id = row[1]

    if novo_status != status_atual:

        permitidos = TRANSICOES_VALIDAS.get(
            status_atual,
            set()
        )

        if novo_status not in permitidos:

            conn.close()

            return jsonify({
                "erro": f"Transição inválida: {status_atual} -> {novo_status}",
                "permitidos": sorted(list(permitidos))
            }), 400

    cursor.execute("""
        UPDATE falhas
        SET status = ?
        WHERE id = ?
    """, (
        novo_status,
        falha_id
    ))

    atualizar_status_maquina(
        cursor,
        maquina_id,
        
    )

    falha = montar_falha_com_join(
        cursor,
        falha_id
    )

    conn.commit()
    conn.close()

    return jsonify(falha), 200


@bp.route("/falhas/<int:falha_id>", methods=["PUT"])
def atualizar_falha(falha_id):

    dados = request.get_json() or {}

    if "maquina_id" in dados or "equipamento_id" in dados:

        return jsonify({
            "erro": "Não é permitido alterar maquina_id/equipamento_id"
        }), 400

    campos_permitidos = {
        "descricao",
        "tipo",
        "gravidade",
        "status",
        "data_ocorrencia"
    }

    updates = {
        k: v
        for k, v in dados.items()
        if k in campos_permitidos and v is not None
    }

    if not updates:

        return jsonify({
            "erro": "Nenhum campo válido enviado"
        }), 400

    if "status" in updates:

        status = str(updates["status"]).strip().upper()

        if status not in STATUS_FALHA:

            return jsonify({
                "erro": "Status inválido"
            }), 400

        updates["status"] = status

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT maquina_id
        FROM falhas
        WHERE id = ?
    """, (falha_id,))

    row = cursor.fetchone()

    if row is None:

        conn.close()

        return jsonify({
            "erro": "Falha não encontrada"
        }), 404

    maquina_id = row[0]

    set_clause = ", ".join([
        f"{campo} = ?"
        for campo in updates.keys()
    ])

    valores = list(updates.values()) + [falha_id]

    cursor.execute(f"""
        UPDATE falhas
        SET {set_clause}
        WHERE id = ?
    """, valores)

    if "status" in updates:

        atualizar_status_maquina(
            cursor,
            maquina_id,
            
        )

    falha = montar_falha_com_join(
        cursor,
        falha_id
    )

    conn.commit()
    conn.close()

    return jsonify(falha), 200


@bp.route("/falhas/<int:falha_id>", methods=["DELETE"])
def deletar_falha(falha_id):

    conn = get_connection()
    cursor = conn.cursor()

    falha = montar_falha_com_join(
        cursor,
        falha_id
    )

    if falha is None:

        conn.close()

        return jsonify({
            "erro": "Falha não encontrada"
        }), 404
    
    



    cursor.execute("""
    SELECT maquina_id
    FROM falhas
    WHERE id = ?
""", (falha_id,))

    row = cursor.fetchone()
    maquina_id = row[0] if row else None


    cursor.execute("""
        DELETE FROM falhas
        WHERE id = ?
    """, (falha_id,))

    conn.commit()
    conn.close()

    return jsonify({
        "mensagem": "Falha removida com sucesso",
        "falha": falha
    }), 200

    atualizar_status_maquina(cursor, maquina_id)


    @bp.route("/maquinas/<int:id>", methods=["DELETE"])
    def excluir_maquina(id):

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
        "DELETE FROM maquinas WHERE id = ?",
        (id,)
        )

        conn.commit()
        conn.close()

        return {"mensagem": "Máquina excluída"}
    

@bp.route("/equipamentos/<int:id>", methods=["DELETE"])
def excluir_equipamento(id):

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM equipamentos WHERE id = ?",
        (id,)
    )

    conn.commit()
    conn.close()

    return {"mensagem": "Equipamento excluído"}