from __future__ import absolute_import, unicode_literals
from usuario import users_service
__author__ = 'Matheus'

def index(_write_tmpl):
    users = users_service.get_all_users().fetch()
    lista = []
    i = 0
    for user in users:
        user = user.to_dict()
        if "@" in user['nome']:
            user['nome'], __ = user['nome'].split("@")
        lista.append(user)
        user['indice'] = i
        i += 1
    _write_tmpl('templates/listar.html', {'lista':lista})