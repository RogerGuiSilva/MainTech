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

