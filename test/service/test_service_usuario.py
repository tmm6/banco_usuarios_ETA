import pytest

from src.service.service_usuario import ServiceUsuario


class TestServiceUsuario:

    # Utilizando o recurso de fixture do pytest para reutilizar alguns dados
    # baseado em: https://docs.pytest.org/en/7.1.x/how-to/fixtures.html e
    # https://www.alura.com.br/artigos/montando-cenarios-de-testes-com-o-pytest

    # Mensagem de usuario adicionado
    @pytest.fixture
    def msg_usuario_add(self):
        return 'Usuário adicionado'

    # Mensagem de usuario invalido
    @pytest.fixture
    def msg_invalida(self):
        return 'Usuário inválido'

    # Usuario removido
    @pytest.fixture
    def msg_usuario_del(self):
        return 'Usuário removido'

    # Nome do usuario
    @pytest.fixture
    def nome_usuario(self):
        return 'Alucard'

    # Nome do usuario
    @pytest.fixture
    def profissao(self):
        return 'Buscando um sentido pra vida'

    '''Testes'''
    ## Testes para criacao de um usuario. ##
    # Teste para verificar se o nome e a profissao sao validas.
    def test_add_usuario_nome_valido_profissao_valida(self, nome_usuario, profissao, msg_usuario_add):
        # Setup
        service = ServiceUsuario()

        # Chamada
        result = service.add_usuario(nome_usuario, profissao)

        # Avaliacao
        assert result == msg_usuario_add
        assert service.store.bd[0].nome == nome_usuario
        assert service.store.bd[0].profissao == profissao

    # Teste para verificar o usuario invalido (e.g. usuario == none).
    def test_add_usuario_invalido_profissao_valida(self, profissao, msg_invalida):
        # Setup
        service = ServiceUsuario()
        nome_invalido = None
        store_esperado = []

        # Chamada
        result = service.add_usuario(nome_invalido, profissao)

        # Avaliacao
        assert result == msg_invalida
        assert service.store.bd == store_esperado

    # Teste para verificar o usuario invalido (e.g. profissao == none).
    def test_add_usuario_valido_profissao_invalida(self, nome_usuario, msg_invalida):
        # Setup
        service = ServiceUsuario()
        profissao_invalida = None
        store_esperado = []

        # Chamada
        result = service.add_usuario(nome_usuario, profissao_invalida)

        # Avaliacao
        assert result == msg_invalida
        assert service.store.bd == store_esperado

    # Teste para verificar se o usuario e um numero inteiro (e.g. usuario == 0)
    def test_add_usuario_inteiro_profissao_valida(self, profissao, msg_invalida):
        # Setup
        service = ServiceUsuario()
        nome_valido = 0
        store_esperado = []

        # Chamada
        result = service.add_usuario(nome_valido, profissao)

        # Avaliacao
        assert result == msg_invalida
        assert service.store.bd == store_esperado

    # Teste para verificar se a profissao e um numero inteiro (e.g. profissao == 0)
    def test_add_usuario_valido_profissao_tipo_invalido(self, nome_usuario, msg_invalida):
        # Setup
        service = ServiceUsuario()
        profissao_invalida = 0
        store_esperado = []

        # Chamada
        result = service.add_usuario(nome_usuario, profissao_invalida)

        # Avaliacao
        assert result == msg_invalida
        assert service.store.bd == store_esperado


    ## Testes para excluir um usuario ##
    # Excluir um usuario com sucesso.
    def test_del_usuario_valido(self, nome_usuario, profissao, msg_usuario_del):
        # Setup
        service = ServiceUsuario()
        service.add_usuario(nome_usuario, profissao)
        store_esperado = []

        # Chamada
        result = service.del_usuario(nome_usuario)

        # Avaliacao
        assert result == msg_usuario_del
        assert service.store.bd == store_esperado

    # Teste para verificar quando o usuario e invalido (e.g. nome == none)
    def test_del_usuario_invalido(self, nome_usuario, profissao, msg_invalida):
        # Setup
        service = ServiceUsuario()
        nome_invalido = None
        service.add_usuario(nome_usuario, profissao)

        # Chamada
        result = service.del_usuario(nome_invalido)

        # Avaliacao
        assert result == msg_invalida
        assert service.store.bd != []
        assert service.store.bd[0].nome == nome_usuario
        assert service.store.bd[0].profissao == profissao

    # Teste para verificar quando o usuario nao esta cadastrado
    def test_del_usuario_inexistente(self, nome_usuario, profissao, msg_invalida):
        # Setup
        service = ServiceUsuario()
        nome_inexistente = 'Dracula'
        service.add_usuario(nome_usuario, profissao)

        # Chamada
        result = service.del_usuario(nome_inexistente)

        # Avaliacao
        assert result == msg_invalida
        assert service.store.bd != []
        assert service.store.bd[0].nome == nome_usuario
        assert service.store.bd[0].profissao == profissao