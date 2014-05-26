from mock.mock import Mock
from base import GAETestCase

from web import listar


from usuario.model import Usuario
import json

class RestTests(GAETestCase):
    
    def test_listar(self):
        usuario = Usuario(nome='teste', email='teste@teste.tst', google_id=123)
        usuario.put()
        usuarios = Usuario.query().fetch()
        lista_dict = [{"nome": usu.nome, "email": usu.email, "google_id": usu.google_id, "id": usu.key.id()} for usu in usuarios]
        resposta_mock = Mock()
        listar.listar(resposta_mock)
        json_str = json.dumps(lista_dict)
        resposta_mock.write.assert_called_once_with(json_str)

    def test_salvar(self):
        resp = Mock()
        rest.salvar(resp, 'teste', 'teste@teste.com', 1234)
        lista = Usuario.query().fetch()
        self.assertEquals(1, len(lista))
        usuario = lista[0]
        self.assertEqual('teste', usuario.firstname)
        self.assertEqual('teste@teste.com', usuario.email)

