from database import SessionLocal
from refeicao import Refeicao

session = SessionLocal()

nova_refeicao= Refeicao(codigo_receita = "REC002", codigo_barra = 7891000100103, quantidade = 2)
session.add(nova_refeicao)
session.commit()
print("Refeição inserida!")

session.close()