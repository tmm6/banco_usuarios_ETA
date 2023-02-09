from src.models.store import Store
from src.models.usuario import Usuario


class ServiceUsuario:

    def __init__(self):
        self.store = Store()
        self.msg_usuario_invalido = 'Usuário inválido'
        self.msg_usuario_adicionado = 'Usuário adicionado'
        self.msg_usuario_removido = 'Usuário removido'
        self.msg_usuario_atualizado = 'Usuário atualizado'


    # Adicioanr usuario
    def add_usuario(self, nome, profissao):
        if nome != None and profissao != None:
            if type(nome) == str and type(profissao) == str:
                usuario = Usuario(nome, profissao)
                self.store.bd.append(usuario)
            else:
                return self.msg_usuario_invalido
        else:
            return self.msg_usuario_invalido
        return self.msg_usuario_adicionado

    # Buscar usuario
    def search_usuario_nome(self, nome):
        if nome is not None:
            for usuario in self.store.bd:
                if usuario.nome == nome:
                    return usuario
            return False
        else:
            return False

    def edit_usuario(self, nome, nome_novo, nova_profissao):
        usuario = self.search_usuario_nome(nome)
        if usuario:
            index = self.store.bd.index(usuario)
            usuario_editado = Usuario(nome_novo, nova_profissao)
            self.store.bd[index] = usuario_editado
            return self.msg_usuario_atualizado
        else:
            return self.msg_usuario_invalido

    # Excluir usuario
    def del_usuario(self, nome):
        usuario = self.search_usuario_nome(nome)
        if usuario:
            self.store.bd.remove(usuario)
            return self.msg_usuario_removido
        else:
            return self.msg_usuario_invalido


