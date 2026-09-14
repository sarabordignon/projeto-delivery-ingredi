from database import SessionLocal
from mercado import Mercado

session = SessionLocal()

novo_mercado = Mercado(
    cnpj="1234",
    nome="bigbom",
    endereco="centro",
    contato="123456"
)

session.add(novo_mercado)
session.commit()

print("Mercado inserido!")

session.close()