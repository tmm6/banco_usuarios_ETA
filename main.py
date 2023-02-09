from src.models.store import Store
from src.models.usuario import Usuario
from src.service.service_usuario import ServiceUsuario

#usuario = Usuario('Alucard', 'O que matou o dracula')
#print(usuario.nome)
#print(usuario.profissao)


store = Store()
print(store.bd)

# Adicionar alguns usuarios.
service = ServiceUsuario()
result = service.add_usuario('Alucard', 'Buscando um sentido para vida')
print(result)
print('Nome ' + service.store.bd[0].nome)
print('Profissão: ' + service.store.bd[0].profissao)
print('\n')

result = service.add_usuario('Diana', 'Mulher-Maravilha')
print(result)
print('Nome ' + service.store.bd[1].nome)
print('Profissão: ' + service.store.bd[1].profissao)
print('\n')

result = service.add_usuario('Peter Park', 'Fotógrafo')
print(result)
print('Nome ' + service.store.bd[2].nome)
print('Profissão: ' + service.store.bd[2].profissao)
print('\n')

# Editar um usuario
## Usuario invalido
result = service.edit_usuario('Dr. Strange', 'Sung Jin-woo', 'Monarca das sombras')
print(result)
print('\n')
## Usuario valido
result = service.edit_usuario('Peter Parker', 'Sung Jin-woo', 'Monarca das sombras')
print(result)
print('Nome ' + service.store.bd[2].nome)
print('Profissão: ' + service.store.bd[2].profissao)
print('\n')


print(service.search_usuario_nome('Alucard'))
print(service.search_usuario_nome('Dracula'))
print('\n')

# Excluir um usuario
## Usuario nao existe
result = service.del_usuario('Dracula')
print(result)
print('\n')
## Usuario existe
result = service.del_usuario('Alucard')
print(result)
print('\n')
# Neste caso o primeiro usuario da lista sera Diana
print(service.store.bd[0].nome)
