
from flask import Blueprint, jsonify, request
bp = Blueprint ('main', __name__)

@bp.route("/test", methods=["GET"])
def test():
    return jsonify({

        "status": "ok",
        "message": "Eba"
        })

@bp.route("/echo", methods=["POST"])
def echo():
    dados = request.get_json()
    return jsonify ({
        "recebido": dados
    })