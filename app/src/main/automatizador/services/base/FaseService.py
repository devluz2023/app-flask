from src.main.automatizador.models.base.Fase import Fase, Subfase


class FaseService:
    fase_model: object

    def __init__(self):
        self.fase_model = Fase()

    def get_total_fases(self):
        result = {}
        try:
            res = self.fase_model.get_total_fases()
            result = {
                'total': res._data[0]
            }
            status = 200
        except Exception as e:
            status = 400
            result = []
        finally:
            return {
                'result': result,
                'status': status
            }

    def get_fases(self,  args):
        result = []
        total_elements = {}

        per_page =args.get('per_page')
        order = args.get("order")
        colum = args.get("colum")
        page = args.get('page')

        try:
            pageno = 1
            no_of_records_per_page = 10
            if int(page) != 0:
                pageno = int(page) + 1
            if int(per_page) != 0:
                no_of_records_per_page = int(per_page)
            total = self.fase_model.get_total_fases()
            res = self.fase_model.get_fases(page=pageno, per_page=no_of_records_per_page, order=order, colum=colum)
            for r in res.items:
                result.append({
                    "id": r.id,
                    "descricao": r.descricao,
                    'subfase': {
                        'id': r.subfase.id,
                        'descricao': r.subfase.descricao
                    }
                })

            total_elements = {
                'total': total._data[0]
            }
            status = 200
        except Exception as e:
            print(e)
            result = []
            status = 400
        finally:
            return {
                'result': {'elements': result, 'count': total_elements},
                'status': status
            }

    def find_fase_by_id(self, id):
        result = {}
        try:
            self.fase_model.id = id
            res = self.fase_model.find()
            if res != None:
                result = {
                    "id": res.id,
                    "descricao": res.descricao,
                    'subfase': {
                        'id': res.subfase.id,
                        'descricao': res.subfase.descricao
                    }
                }
            status = 200
        except Exception as e:
            print(e)
            result = []
            status = 400
        finally:
            return {
                'result': result,
                'status': status
            }

    def find_fase_by_descricao(self, descricao):
        result = {}
        try:
            self.fase_model.descricao = descricao
            res = self.fase_model.find_by_descricao()
            if res != None:
                result = {
                    "id": res.id,
                    "descricao": res.descricao,
                    'subfase': {
                        'id': res.subfase.id,
                        'descricao': res.subfase.descricao
                    }
                }
            status = 200
        except Exception as e:
            print(e)
            result = []
            status = 400
        finally:
            return {
                'result': result,
                'status': status
            }

    def delete_fase(self, id):
        self.fase_model.id = id
        try:
            result = self.fase_model.delete()
            status = 200
        except Exception as e:
            print(e)
            result = []
            status = 400
        finally:
            return {
                'result': result,
                'status': status
            }

    def update_fase(self, request):
        self.fase_model.id = request['id']
        try:
            obj = {'descricao': request['descricao'], 'fk_sub_fase': request['fk_sub_fase']}
            status = 200
            result = self.fase_model.update(obj)
        except Exception as e:
            print(e)
            result = []
            status = 400
        finally:
            return {
                'result': result,
                'status': status
            }

    def save_fase(self, faseRequest):
        descricao = faseRequest['descricao']
        fk_sub_fase = faseRequest['fk_sub_fase']
        subfase = Subfase(id=faseRequest['subfase']['id'], descricao=faseRequest['subfase']['descricao'])
        subfase.find()
        self.fase_model = Fase(descricao=descricao, fk_sub_fase=fk_sub_fase)
        try:
            self.fase_model.save()
            status = 200
            result = []
        except Exception as e:
            print(e)
            result = []
            status = 400
        finally:
            return {
                'result': result,
                'status': status
            }
