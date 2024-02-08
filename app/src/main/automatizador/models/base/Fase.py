# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy.orm import relationship, joinedload
from src.main.automatizador.configurations.config import app_active, app_config
from sqlalchemy.orm import backref

from src.main.automatizador.models.base.Subfase import Subfase

config = app_config[app_active]
db = SQLAlchemy(config.APP)


class Fase(db.Model):
    __tablename__ = 'fase'
    id = db.Column('id_fase', db.Integer, primary_key=True)
    descricao = db.Column('descricao_fase', db.String(40), unique=True, nullable=False)
    fk_sub_fase = db.Column('id_sub_fase', db.Integer, db.ForeignKey(Subfase.id))
    subfase = relationship(Subfase)


    def get_total_fases(self):
        try:
            res = db.session.query(func.count(Fase.id)).first()
        except Exception as e:
            res = []
            print(e)
        finally:
            db.session.close()
            return res

    def get_fases(self, page, per_page, order, colum):
        try:
            if page is None and per_page is None:
                res = db.session.query(Fase).options(joinedload(Fase.subfase)).all()
            else:
                toOrder = db.asc(Fase.descricao)
                if order=="desc":
                    toOrder = db.desc(Fase.descricao)
                res = db.session.query(Fase).options(joinedload(Fase.subfase)).order_by(toOrder).paginate(page=int(page), per_page=int(per_page))
        except Exception as e:
            res = []
            print(e)
        finally:
            db.session.close()
            return res

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
            db.session.query(Fase).filter(Fase.id == self.id).delete()
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return False

    def find(self):
        try:
            res = db.session.query(Fase).filter(Fase.id == self.id).options(joinedload(Fase.subfase)).first()
        except Exception as e:
            res = []
            print(e)
        finally:
            db.session.close()
            return res

    def find_by_descricao(self):
        try:
            res = db.session.query(Fase).filter(Fase.descricao == self.descricao).options(joinedload(Fase.subfase)).first()
        except Exception as e:
            res = []
            print(e)
        finally:
            db.session.close()
            return res

    def update(self, obj):
        try:
            db.session.query(Fase).filter(Fase.id == self.id).update(obj)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            db.session.rollback()
            return False


    def obj_to_dict(self):  # for build json format
        return {
            "id": self.id,
            "descricao": self.descricao,
            'subfase': {
                'id': self.subfase.id,
                'descricao': self.subfase.descricao,
            }
        }

    def __repr__(self):
        return '%s	-	%s' % (self.id, self.descricao)