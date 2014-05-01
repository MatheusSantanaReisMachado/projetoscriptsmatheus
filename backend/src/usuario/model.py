# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import json
from google.appengine.ext import ndb

__author__ = 'Matheus'

class Usuario (ndb.Model):
    nome = ndb.StringProperty()
    email = ndb.StringProperty()
    google_id = ndb.StringProperty()

    @classmethod
    def query_by_google(cls, google_id):
        return cls.query(cls.google_id == google_id)

def listar(_resp):
    query = Usuario.query().order(-Usuario.nome, -Usuario.email)

    def to_dict(c):
        dct = c.to_dict()
        dct['id'] = str(c.key.id())
        return dct

    lista_de_usuarios = [to_dict(c) for c in query.fetch()]
    lista_de_usuarios = json.dumps(lista_de_usuarios)
    _resp.write(lista_de_usuarios)