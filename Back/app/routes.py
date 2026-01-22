from flask import Blueprint, jsonify, request
from app.dataBase.db import get_connection
from app.falhas import inserir_falha

bp = Blueprint("main", __name__)

STATUS_VALIDOS = {
    "ABERTA",
    "EM_ANALISE",
    "EM_MANUTENCAO",
    "PARADA",
    "PLANEJADA",
    "RESOLVIDA",
    "CANCELADA"
}

TRANSICOES_VALIDAS = {
    "ABERTA": {"EM_ANALISE", "EM_MANUTENCAO", "PARADA", "CANCELADA"},
    "EM_ANALISE": {"EM_MANUTENCAO", "PARADA", "CANCELADA", "RESOLVIDA"},
    "EM_MANUTENCAO": {"RESOLVIDA", "PARADA", "CANCELADA"},
    "PARADA": {"EM_MANUTENCAO", "EM_ANALISE", "RESOLVIDA", "CANCELADA"},
    "PLANEJADA": {"ABERTA", "CANCELADA"},
    "RESOLVIDA": set(),
    "CANCELADA": set()
}


def montar_falha_com_join(cursor, falha_id: int):
    cursor.execute("""
        SELECT 
            f.id, f.descricao, f.tipo, f.gravidade, f.status, f.data_ocorrencia,
            m.id, m.nome, m.setor,
            e.id, e.nome, e.setor
        FROM falhas f
        LEFT JOIN maquinas m ON f.maquina_id = m.id
        LEFT JOIN equipamentos e ON f.equipamento_id = e.id
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
        falha["maquina"] = {"id": r[6], "nome": r[7], "setor": r[8]}

    if r[9] is not None:
        falha["equipamento"] = {"id": r[9], "nome": r[10], "setor": r[11]}

    return falha


@bp.route("/equipamentos", methods=["POST"])
def criar_equipamentos():
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "JSON não enviado"}), 400

    campos_obrigatorios = ["nome", "setor", "tipo", "status"]
    for campo in campos_obrigatorios:
        if campo not in dados or not dados[campo]:
            return jsonify({"erro": f"Campo '{campo}' é obrigatório"}), 400

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO equipamentos (nome, setor, tipo, status)
        VALUES (?, ?, ?, ?)
    """, (dados["nome"], dados["setor"], dados["tipo"], dados["status"]))
    conn.commit()
    conn.close()

    return jsonify({"mensagem": "Equipamento cadastrado com sucesso"}), 201


@bp.route("/equipamentos", methods=["GET"])
def get_equipamentos():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM equipamentos")
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


@bp.route("/maquinas", methods=["POST"])
def criar_maquinas():
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "JSON não enviado"}), 400

    campos_obrigatorios = ["nome", "setor", "tipo", "status"]
    for campo in campos_obrigatorios:
        if campo not in dados or not dados[campo]:
            return jsonify({"erro": f"Campo '{campo}' é obrigatório"}), 400

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO maquinas (nome, setor, tipo, status)
        VALUES (?, ?, ?, ?)
    """, (dados["nome"], dados["setor"], dados["tipo"], dados["status"]))
    conn.commit()
    conn.close()

    return jsonify({"mensagem": "Máquina cadastrada com sucesso"}), 201


@bp.route("/maquinas", methods=["GET"])
def get_maquinas():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM maquinas")
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


@bp.route("/falhas", methods=["GET"])
def listar_falhas():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            f.id, f.descricao, f.tipo, f.gravidade, f.status, f.data_ocorrencia,
            m.id, m.nome, m.setor,
            e.id, e.nome, e.setor
        FROM falhas f
        LEFT JOIN maquinas m ON f.maquina_id = m.id
        LEFT JOIN equipamentos e ON f.equipamento_id = e.id
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
            falha["maquina"] = {"id": r[6], "nome": r[7], "setor": r[8]}

        if r[9] is not None:
            falha["equipamento"] = {"id": r[9], "nome": r[10], "setor": r[11]}

        resultado.append(falha)

    return jsonify(resultado)


@bp.route("/falhas", methods=["POST"])
def criar_falha():
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "JSON não enviado"}), 400

    campos_obrigatorios = ["descricao", "tipo", "gravidade", "data_ocorrencia", "status"]
    for campo in campos_obrigatorios:
        if campo not in dados or not dados[campo]:
            return jsonify({"erro": f"Campo '{campo}' é obrigatório"}), 400

    status = str(dados["status"]).strip().upper()
    if status not in STATUS_VALIDOS:
        return jsonify({"erro": f"Status inválido. Use um destes: {sorted(STATUS_VALIDOS)}"}), 400

    maquina_id = dados.get("maquina_id")
    equipamento_id = dados.get("equipamento_id")

    if maquina_id is None and equipamento_id is None:
        return jsonify({"erro": "Informe 'maquina_id' OU 'equipamento_id'"}), 400

    if maquina_id is not None and equipamento_id is not None:
        return jsonify({"erro": "Envie apenas um: 'maquina_id' OU 'equipamento_id'"}), 400

    resp = inserir_falha(
        descricao=dados["descricao"],
        tipo=dados["tipo"],
        gravidade=dados["gravidade"],
        data_ocorrencia=dados["data_ocorrencia"],
        status=status,
        maquina_id=maquina_id,
        equipamento_id=equipamento_id
    )

    if isinstance(resp, str) and resp.startswith("Erro"):
        return jsonify({"erro": resp}), 400

    falha_id = resp

    conn = get_connection()
    cursor = conn.cursor()
    falha = montar_falha_com_join(cursor, falha_id)
    conn.close()

    return jsonify(falha), 201


@bp.route("/falhas/<int:falha_id>/status", methods=["PATCH"])
def atualizar_status_falha(falha_id):
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "JSON não enviado"}), 400

    if "status" not in dados or not str(dados["status"]).strip():
        return jsonify({"erro": "Campo 'status' é obrigatório"}), 400

    novo_status = str(dados["status"]).strip().upper()

    if novo_status not in STATUS_VALIDOS:
        return jsonify({"erro": f"Status inválido. Use um destes: {sorted(STATUS_VALIDOS)}"}), 400

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT status FROM falhas WHERE id = ?", (falha_id,))
    row = cursor.fetchone()

    if row is None:
        conn.close()
        return jsonify({"erro": f"Falha {falha_id} não encontrada"}), 404

    status_atual = (row[0] or "").strip().upper()

    if status_atual not in STATUS_VALIDOS:
        conn.close()
        return jsonify({"erro": f"Status atual inválido no banco: '{row[0]}'"}), 500

    if novo_status == status_atual:
        falha = montar_falha_com_join(cursor, falha_id)
        conn.close()
        return jsonify(falha), 200

    permitidos = TRANSICOES_VALIDAS.get(status_atual, set())
    if novo_status not in permitidos:
        conn.close()
        return jsonify({
            "erro": f"Transição inválida: {status_atual} -> {novo_status}",
            "permitidos": sorted(list(permitidos))
        }), 400

    cursor.execute("UPDATE falhas SET status = ? WHERE id = ?", (novo_status, falha_id))
    conn.commit()

    falha = montar_falha_com_join(cursor, falha_id)
    conn.close()

    return jsonify(falha), 200


@bp.route("/falhas/<int:falha_id>", methods=["GET"])
def obter_falha(falha_id):
  
    conn = get_connection()
    cursor = conn.cursor()

   
    falha = montar_falha_com_join(cursor, falha_id)

   
    conn.close()

    
    if falha is None:
        return jsonify({"erro": f"Falha {falha_id} não encontrada"}), 404

 
    return jsonify(falha), 200


@bp.route("/falhas/<int:falha_id>", methods=["DELETE"])
def deletar_falha(falha_id):
  
    conn = get_connection()
    cursor = conn.cursor()

    
    falha = montar_falha_com_join(cursor, falha_id)

 
    if falha is None:
        conn.close()
        return jsonify({"erro": f"Falha {falha_id} não encontrada"}), 404

   
    cursor.execute("DELETE FROM falhas WHERE id = ?", (falha_id,))
    conn.commit()

 
    conn.close()

    return jsonify({
        "mensagem": "Falha removida com sucesso",
        "falha": falha
    }), 200



@bp.route("/falhas/<int:falha_id>", methods=["PUT"])
def atualizar_falha(falha_id):
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "JSON não enviado"}), 400

    if "maquina_id" in dados or "equipamento_id" in dados:
        return jsonify({"erro": "Não é permitido alterar maquina_id/equipamento_id por este endpoint"}), 400

    campos_permitidos = {"descricao", "tipo", "gravidade", "status", "data_ocorrencia"}
    updates = {k: v for k, v in dados.items() if k in campos_permitidos and v is not None}

    if not updates:
        return jsonify({"erro": "Envie ao menos um campo para atualizar: descricao, tipo, gravidade, status, data_ocorrencia"}), 400

    if "status" in updates:
        novo_status = str(updates["status"]).strip().upper()
        if novo_status not in STATUS_VALIDOS:
            return jsonify({"erro": f"Status inválido. Use um destes: {sorted(STATUS_VALIDOS)}"}), 400
        updates["status"] = novo_status

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM falhas WHERE id = ?", (falha_id,))
    if cursor.fetchone() is None:
        conn.close()
        return jsonify({"erro": f"Falha {falha_id} não encontrada"}), 404

    set_clause = ", ".join([f"{campo} = ?" for campo in updates.keys()])
    valores = list(updates.values()) + [falha_id]

    cursor.execute(f"UPDATE falhas SET {set_clause} WHERE id = ?", valores)
    conn.commit()

    falha = montar_falha_com_join(cursor, falha_id)
    conn.close()

    return jsonify(falha), 200
