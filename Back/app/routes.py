from flask import Blueprint, jsonify, request
from app.dataBase.db import get_connection
from app.falhas import inserir_falha

bp = Blueprint("main", __name__)


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
        status=dados["status"],
        maquina_id=maquina_id,
        equipamento_id=equipamento_id
    )

    if isinstance(resp, str) and resp.startswith("Erro"):
        return jsonify({"erro": resp}), 400

    falha_id = resp 

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
        WHERE f.id = ?
    """, (falha_id,))
    r = cursor.fetchone()
    conn.close()

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

    return jsonify(falha), 201


@bp.route("/falhas/<int:falha_id>", methods=["PUT"])
def atualizar_falha(falha_id):
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "JSON não enviado"}), 400

    campos_permitidos = {"descricao", "tipo", "gravidade", "status", "data_ocorrencia"}
    updates = {k: v for k, v in dados.items() if k in campos_permitidos and v is not None}

    if not updates:
        return jsonify({"erro": "Envie ao menos um campo para atualizar: descricao, tipo, gravidade, status, data_ocorrencia"}), 400

    if "maquina_id" in dados or "equipamento_id" in dados:
        return jsonify({"erro": "Não é permitido alterar maquina_id/equipamento_id por este endpoint"}), 400

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
    conn.close()

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

    return jsonify(falha), 200
