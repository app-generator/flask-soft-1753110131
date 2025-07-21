# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from email.policy import default
from apps import db
from sqlalchemy.exc import SQLAlchemyError
from apps.exceptions.exception import InvalidUsage
import datetime as dt
from sqlalchemy.orm import relationship
from enum import Enum

class CURRENCY_TYPE(Enum):
    usd = 'usd'
    eur = 'eur'

class Product(db.Model):

    __tablename__ = 'products'

    id            = db.Column(db.Integer,      primary_key=True)
    name          = db.Column(db.String(128),  nullable=False)
    info          = db.Column(db.Text,         nullable=True)
    price         = db.Column(db.Integer,      nullable=False)
    currency      = db.Column(db.Enum(CURRENCY_TYPE), default=CURRENCY_TYPE.usd, nullable=False)

    date_created  = db.Column(db.DateTime,     default=dt.datetime.utcnow())
    date_modified = db.Column(db.DateTime,     default=db.func.current_timestamp(),
                                               onupdate=db.func.current_timestamp())
    
    def __init__(self, **kwargs):
        super(Product, self).__init__(**kwargs)

    def __repr__(self):
        return f"{self.name} / ${self.price}"

    @classmethod
    def find_by_id(cls, _id: int) -> "Product":
        return cls.query.filter_by(id=_id).first() 

    def save(self) -> None:
        try:
            db.session.add(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            db.session.close()
            error = str(e.__dict__['orig'])
            raise InvalidUsage(error, 422)

    def delete(self) -> None:
        try:
            db.session.delete(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            db.session.close()
            error = str(e.__dict__['orig'])
            raise InvalidUsage(error, 422)
        return


#__MODELS__
class Usuario(db.Model):

    __tablename__ = 'Usuario'

    id = db.Column(db.Integer, primary_key=True)

    #__Usuario_FIELDS__
    nome = db.Column(db.String(255),  nullable=True)
    usuario = db.Column(db.String(255),  nullable=True)
    email = db.Column(db.String(255),  nullable=True)
    senha = db.Column(db.String(255),  nullable=True)
    foto = db.Column(db.String(255),  nullable=True)
    setor = db.Column(db.String(255),  nullable=True)
    admin = db.Column(db.Boolean, nullable=True)
    diaria = db.Column(db.Boolean, nullable=True)
    ativo = db.Column(db.Boolean, nullable=True)
    data = db.Column(db.DateTime, default=db.func.current_timestamp())
    id = db.Column(db.Integer, nullable=True)

    #__Usuario_FIELDS__END

    def __init__(self, **kwargs):
        super(Usuario, self).__init__(**kwargs)


class Entidades(db.Model):

    __tablename__ = 'Entidades'

    id = db.Column(db.Integer, primary_key=True)

    #__Entidades_FIELDS__
    id = db.Column(db.Integer, nullable=True)
    tipo = db.Column(db.String(255),  nullable=True)
    ativo = db.Column(db.Boolean, nullable=True)

    #__Entidades_FIELDS__END

    def __init__(self, **kwargs):
        super(Entidades, self).__init__(**kwargs)


class Registro_Viagens(db.Model):

    __tablename__ = 'Registro_Viagens'

    id = db.Column(db.Integer, primary_key=True)

    #__Registro_Viagens_FIELDS__
    data_inicio = db.Column(db.DateTime, default=db.func.current_timestamp())
    data_fim = db.Column(db.DateTime, default=db.func.current_timestamp())
    tipo_viagem = db.Column(db.String(255),  nullable=True)
    n_diaria = db.Column(db.String(255),  nullable=True)
    v_diaria = db.Column(db.String(255),  nullable=True)
    descricao = db.Column(db.Text, nullable=True)
    n_intranet = db.Column(db.String(255),  nullable=True)
    veiculo = db.Column(db.String(255),  nullable=True)
    placa = db.Column(db.String(255),  nullable=True)
    km_inicial = db.Column(db.String(255),  nullable=True)
    km_final = db.Column(db.String(255),  nullable=True)
    n_combustivel = db.Column(db.String(255),  nullable=True)
    total_gasto = db.Column(db.String(255),  nullable=True)
    ativo = db.Column(db.Boolean, nullable=True)
    data = db.Column(db.DateTime, default=db.func.current_timestamp())

    #__Registro_Viagens_FIELDS__END

    def __init__(self, **kwargs):
        super(Registro_Viagens, self).__init__(**kwargs)



#__MODELS__END
