from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.data.atendimento_handler import AtendimentoHandler

atendimentos_route_bp = Blueprint("atendimentos_route", __name__)

@atendimentos_route_bp.route("/api/v1/atendimentos/<atend_data>", methods=["GET"])
def get_atendimento(atend_data):
    atend_handler = AtendimentoHandler()

    # Você já tem a data de atendimento como parte da URL, então não precisa acessar request.json
    http_response = atend_handler.find_by_data_consulta(atend_data)
    return jsonify(http_response.body), http_response.status_code
