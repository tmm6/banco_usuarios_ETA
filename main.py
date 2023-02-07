from src.models.store import Store
from src.models.usuario import Usuario
from src.service.service_usuario import ServiceUsuario

#usuario = Usuario('Alucard', 'O que matou o dracula')
#print(usuario.nome)
#print(usuario.profissao)


store = Store()
print(store.bd)

service = ServiceUsuario()
result = service.add_usuario('Alucard', 'Buscando')
print(result)
print(service.store.bd[0].nome)

result = service.edit_usuario('Alucard', 'eitaaa', 'encontrei')
print(result)
print(service.store.bd[0].nome)
print(service.store.bd[0].profissao)



'''

#result = service.del_usuario(service.store.bd[0])
#print(result)
#print(service.store.bd[0].nome)


service = ServiceUsuario()
print(service.store.bd)
result = service.add_usuario('Alucard', 'Buscando')
print(result)

result = service.add_usuario('Alucard', None)
print(result)

result = service.add_usuario(None, 'Buscando')
print(result)

result = service.add_usuario('Alucard', 0)
print(result)

result = service.add_usuario(0, 'Buscando')
print(result)

result = service.add_usuario(usuario.nome, usuario.profissao)
print(result)
print(service.store.bd[0].nome)
print(service.store.bd[0].profissao)

'''