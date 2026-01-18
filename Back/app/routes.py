from flask import Blueprint, jsonify, request
from app.dataBase.db import get_connection 

bp = Blueprint('main', __name__)


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

        if r[6] is not None:  # máquina
            falha["maquina"] = {
                "id": r[6],
                "nome": r[7],
                "setor": r[8]
            }

        if r[9] is not None:  # equipamento
            falha["equipamento"] = {
                "id": r[9],
                "nome": r[10],
                "setor": r[11]
            }

        resultado.append(falha)

    return jsonify(resultado)
