__author__ = 'Matheus'

from model import Usuario

def get_all_users():
    return Usuario.query()
