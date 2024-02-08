from flask import request, Response, json
from flask import Blueprint
from src.main.automatizador.services.base.FaseService import FaseService

faseapp = Blueprint('fases', __name__)


@faseapp.route("/", methods=['GET'])
def lista_fases():
    args = request.args
    fase_controller = FaseService()
    response = fase_controller.get_fases(args = args)
    return Response(json.dumps(response['result'], ensure_ascii=False), mimetype='application/json'), response['status']

@faseapp.route("/", methods=['POST', 'PATCH'])
def save_fase():
    faseController = FaseService()
    req = request.json
    if request.method == 'PATCH':
        response = faseController.update_fase(req)
    elif request.method == 'POST':
        response = faseController.save_fase(req)
    return Response(json.dumps(response['result'], ensure_ascii=False), mimetype='application/json'), response['status']

@faseapp.route("/<int:id>", methods=['GET', 'DELETE'])
def fase(id):
    response = ''
    faseController = FaseService()
    if request.method == 'DELETE':
        response = faseController.delete_fase(id)
    elif request.method == 'GET':
        response = faseController.find_fase_by_id(id)
    return Response(json.dumps(response['result'], ensure_ascii=False), mimetype='application/json'), response['status']

@faseapp.route("/search/<string:descricao>", methods=['GET'])
def search_fase(descricao):
    response = ''
    fase_controller = FaseService()
    if request.method == 'GET':
        response = fase_controller.find_fase_by_descricao(descricao)
    return Response(json.dumps(response['result'], ensure_ascii=False), mimetype='application/json'), response['status']

@faseapp.route("/total", methods=['GET'])
def total():
    fase_controller = FaseService()
    response = fase_controller.get_total_fases()
    return Response(json.dumps(response['result'], ensure_ascii=False), mimetype='application/json'), response['status']