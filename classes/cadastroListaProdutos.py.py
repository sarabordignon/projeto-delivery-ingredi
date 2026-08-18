
from database import SessionLocal
from listaProdutos import ListaProdutos


session = SessionLocal()


nova_lista_produtos = ListaProdutos(
    codigo_carrinho="CAR001",codigo_barra="7891000200207",quantidade=2,preco_unitario="5.20")
session.add(nova_lista_produtos)
session.commit()


print("Lista de produto inserida!")


session.close()


