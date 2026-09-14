from database import SessionLocal
from receita import Receita

session = SessionLocal()

nova_receita= Receita(codigo_receita = "REC003", nome = "bolo", modo_preparo = "misturar", tempo_preparo = 20, porcoes = 5)
session.add(nova_receita)
session.commit()
print("Receita inserida!")

session.close()