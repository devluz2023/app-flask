from src.main.automatizador.models.base.Subfase import Subfase

class SubFaseService:
    def __init__(self):
        self.sub_fase_model = Subfase()

    def list_subfase(self):
         subfases = self.sub_fase_model.get_subfases()
         return [item.obj_to_dict() for item in subfases]

    def find_sufbase(self, id):
        self.fase_model = Subfase()
        self.fase_model.find()
        return self.fase_model


    def save_subfase(self, faseRequest):
        descricao = faseRequest['descricao']
        self.sub_fase_model = Subfase(descricao=descricao)
        return self.sub_fase_model.save()

    def delete_subfase(self, faseRequest):
        descricao = faseRequest['descricao']
        id = faseRequest['id']
        self.fase_model = Subfase(id=id, descricao=descricao)
        self.fase_model.delete()

    def update_subfase(self,subfaseRequest):
        descricao = subfaseRequest['descricao']
        id = subfaseRequest['id']
        self.fase_model = Subfase(id=id, descricao=descricao)
        result = self.fase_model.update()
        return result
