from flask import Blueprint, jsonify
bp = Blueprint ('main', __name__)

@bp.route("/test", methods=["GET"])
def test():
    return jsonify({"message": "back ta rodando"})