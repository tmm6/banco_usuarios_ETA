from src.models.store import Store
from src.models.usuario import Usuario


class ServiceUsuario:
    def __init__(self):
        self.store = Store()

    def add_usuario(self, nome, profissao):
        if nome != None and profissao != None:
            if type(nome) == str and type(profissao) == str:
                usuario = Usuario(nome, profissao)
                self.store.bd.append(usuario)
            else:
                return 'Usuario invalido'
        else:
            return 'Usuario invalido'
        return 'Usuario adicionado'

    def edit_usuario(self, nome, nome_novo, profissao):
        if nome != None:
            for usuario in self.store.bd:
                if usuario.nome == nome:
                    index = self.store.bd.index(usuario)
                    print(index)
                    usuario_editado = Usuario(nome_novo, profissao)
                    self.store.bd[index] = usuario_editado
                    return 'Usuario atualizado'
            return 'Usuario invalido'
        else:
            return 'Usuario invalido'


    def del_usuario(self, nome):
        if nome != None:
            for usuario in self.store.bd:
                if usuario.nome == nome:
                    self.store.bd.remove(usuario)
                    return 'Usuario removido'
            return 'Usuario invalido'
        else:
            return 'Usuario invalido'

