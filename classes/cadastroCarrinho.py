from database import SessionLocal
from carrinho import Carrinho 

session = SessionLocal()

novo_carrinho = Carrinho(codigo_carrinho = 3, data_criacao = "2025/03/03", status = "cheio", cpf = "222.333.444-55")
session.add(novo_carrinho)
session.commit()
print("Carrinho inserido!")

session.close()