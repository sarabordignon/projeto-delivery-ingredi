from database import SessionLocal
from produto import Produto

session = SessionLocal()

novo_produto = Produto(codigo_barra="7891000300453",ome="Farinha",und_medida="KG",preco_und=20.00,categoria="Farinha",cnpj="12.345.678/0001-90")

session.add(novo_produto)
session.commit()

print("Produto inserido!")

session.close()