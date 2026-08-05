from database import SessionLocal
from usuario import Usuario

session = SessionLocal()

novo_usuario = Usuario(cpf = 1234, nome = "Sara", email = "sara@gmail.com", telefone = 123456, endereco = "centro", senha = "123456")
session.add(novo_usuario)
session.commit()
print("Usuário inserido!")

session.close()