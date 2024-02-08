# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy.orm import relationship
from src.main.automatizador.configurations.config import app_active, app_config

config = app_config[app_active]
db = SQLAlchemy(config.APP)


class Subfase(db.Model):
    __tablename__ = 'subfase'
    id = db.Column('id_sub_fase', db.Integer, primary_key=True)
    descricao = db.Column('descricao_sub_fase', db.String(40), unique=True, nullable=False)


    def get_subfases(self):
        try:
            return Subfase.query.all()
        except Exception as e:
            print("Erro ao listar Fases.")
            return []

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return False

    def delete(self):
        try:
            Subfase.query.filter(Subfase.id_sub_fase == self.id_sub_fase).delete()
            return True
        except Exception as e:
            return False

    def find(self):
        try:
            res = db.session.query(Subfase).filter(Subfase.id_sub_fase == self.id_sub_fase).first()
        except Exception as e:
            res = None
            print(e)
        finally:
            db.session.close()
            return res

    def update(self):
        try:
            Subfase.query.update(self)
        except Exception as e:
            print("updated")

    def obj_to_dict(self):  # for build json format
        return {
            "id": self.id,
            "descricao": self.descricao,
        }

    def __repr__(self):
        return '%s	-	%s' % (self.id, self.descricao)