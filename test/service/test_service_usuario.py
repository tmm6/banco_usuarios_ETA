from src.service.service_usuario import ServiceUsuario


class TestServiceUsuario:
    def test_add_usuario_nome_valido_profissao_valida(self):
        # Setup
        service = ServiceUsuario()
        nome_valido = 'Alucard'
        profissao_valida = 'Buscando um sentido pra vida'
        result_esperado = 'Usuario adicionado'

        # Chamada
        result = service.add_usuario(nome_valido, profissao_valida)

        # Avaliacao
        assert result == result_esperado
        assert service.store.bd[0].nome == nome_valido
        assert service.store.bd[0].profissao == profissao_valida

    # se for para estrutura somente esse serviria
    def test_add_usuario_invalido_profissao_valida(self):
        # Setup
        service = ServiceUsuario()
        nome_valido = None
        profissao_valida = 'Buscando um sentido pra vida'
        result_esperado = 'Usuario invalido'
        store_esperado = []

        # Chamada
        result = service.add_usuario(nome_valido, profissao_valida)

        # Avaliacao
        assert result == result_esperado
        assert service.store.bd == store_esperado

    # DELETAR
    def test_del_usuario_valido(self):
        # Setup
        service = ServiceUsuario()
        nome_valido = 'Alucard'
        profissao_valida = 'Buscando um sentido pra vida'
        result_esperado = 'Usuario removido'
        service.add_usuario(nome_valido, profissao_valida)
        store_esperado = []

        # Chamada
        result = service.del_usuario(nome_valido)

        # Avaliacao
        assert result == result_esperado
        assert service.store.bd == store_esperado

    def test_del_usuario_invalido(self):
        # Setup
        service = ServiceUsuario()
        nome_valido = 'Alucard'
        profissao_valida = 'Buscando um sentido pra vida'
        nome_invalido = 'Filó'
        result_esperado = 'Usuario invalido'
        service.add_usuario(nome_valido, profissao_valida)

        # Chamada
        result = service.del_usuario(nome_invalido)

        # Avaliacao
        assert result == result_esperado
        assert service.store.bd != []
        assert service.store.bd[0].nome == nome_valido
        assert service.store.bd[0].profissao == profissao_valida


    def test_add_usuario_inteiro_profissao_valida(self):
        # Setup
        service = ServiceUsuario()
        nome_valido = 0
        profissao_valida = 'Buscando um sentido pra vida'
        result_esperado = 'Usuario invalido'
        store_esperado = []

        # Chamada
        result = service.add_usuario(nome_valido, profissao_valida)

        # Avaliacao
        assert result == result_esperado
        assert service.store.bd == store_esperado

    # se fosse caminho esse tambem seria necessario
    def test_add_usuario_valido_profissao_invalida(self):
        # Setup
        service = ServiceUsuario()
        nome_valido = 'Alucard'
        profissao_valida = None
        result_esperado = 'Usuario invalido'
        store_esperado = []

        # Chamada
        result = service.add_usuario(nome_valido, profissao_valida)

        # Avaliacao
        assert result == result_esperado
        assert service.store.bd == store_esperado

    def test_add_usuario_valido_profissao_tipo_invalido(self):
        # Setup
        service = ServiceUsuario()
        nome_valido = 'Alucard'
        profissao_invalida = 0
        result_esperado = 'Usuario invalido'
        store_esperado = []

        # Chamada
        result = service.add_usuario(nome_valido, profissao_invalida)

        # Avaliacao
        assert result == result_esperado
        assert service.store.bd == store_esperado

