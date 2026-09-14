from database import SessionLocal
from usuario import Usuario

session = SessionLocal()

novo_usuario = Usuario(
    cpf="4567",
    nome="Gabriel",
    email="gabriel@gmail.com",
    telefone="375757",
    endereco="sao sebastiao",
    senha="123456"
)

session.add(novo_usuario)
session.commit()

print("Usuario inserido!")

session.close()