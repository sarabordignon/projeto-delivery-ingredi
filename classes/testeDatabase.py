from database import engine

try: 
    conexao = engine.connect()
    print("Conectou com sucesso!")
    conexao.close()
except Exception as erro:
    print("A conexão falhou!")
    print(erro)
