
from flask import request, Response, json

from src.main.automatizador.services.base.SubFaseService import SubFaseService


def routes_subfases(app):
    @app.route("/subfases", methods=['GET'])
    def subfases():
        subfase_service = SubFaseService()
        result = subfase_service.list_subfase()
        return Response(json.dumps(result, ensure_ascii=False), mimetype='application/json')

    @app.route("/subfase", methods=['POST', 'GET', 'PATCH'])
    def subfase():
        result = ''
        json = request.json
        subfase_service = SubFaseService()
        if request.method == 'POST':
            result = subfase_service.save_subfase(json)
        elif request.method == 'GET':
            result = subfase_service.find_subfase_by_id(request.json)
        elif request.method == 'PATCH':
            result = subfase_service.update_subfase(json)
        return Response(result, mimetype='application/json')

    @app.route("/subfase", methods=['DELETE'])
    def delete_subfase():
        descricao = request.json
        subfase_service = SubFaseService()
        return subfase_service.delete_subfase(descricao)