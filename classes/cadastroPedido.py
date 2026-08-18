from database import SessionLocal
from pedido import Pedido

session = SessionLocal()

novo_pedido= Pedido(numero_pedido = 5, data_pedido = "2020/10/10", status_pedido = "produção", valor_total = 200.00, endereco_entrega = "rua 123",status_entrega = "esperando", data_prevista_entrega = "2020/10/10", data_realizada_entrega = "2020/10/10", cpf = "111.222.333-44", codigo_carrinho = "CAR001")
session.add(novo_pedido)
session.commit()
print("Pedido inserido!")

session.close()