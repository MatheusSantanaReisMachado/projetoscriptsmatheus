from __future__ import absolute_import, unicode_literals
from usuario.model import Usuario
import json
__author__ = 'Matheus'

def index(_write_tmpl):
    usuarios = Usuario.query()
    dct = {'lista_cursos': usuarios.fetch()}
    _write_tmpl('templates/listar.html', dct)

def salvar(_resp, nome, email, google_id):
    usuario = Usuario(nome = nome, email = email, google_id = google_id)
    key = usuario.put()

    json_str = json.dumps({'id':key.id()})

    _resp.write(json_str)

def editar(_resp, idUsuario, nome, email):
    usuario = Usuario.get_by_id(int(idUsuario))

    usuario.nome = nome
    usuario.email = email

    usuario.put()

def remover(_resp, idUsuario):
    usuario = Usuario.get_by_id(int(idUsuario))
    usuario.key.delete()

def listar(_resp):
    json_struct = []

    usuarios = Usuario.query()
    for usu in usuarios:
        json_struct += [{"nome": usu.nome,
                        "email": usu.email,
                        "google_id": usu.google_id,
                        "id": usu.key.id()}]

    json_str = json.dumps(json_struct)
    _resp.write(json_str)

