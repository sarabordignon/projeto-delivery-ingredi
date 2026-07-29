class Carrinho:
    def __init__(self, codigo_carrinho, data_criacao, status):
        self.codigo_carrinho = codigo_carrinho
        self.data_criacao = data_criacao
        self.status = status
        self.quantidade = 0

    def adicionar(self, adicionar):
        self.quantidade += adicionar
        print("adicionou item ao carrinho!")

carrinho1 = Carrinho("1", "29-04-2026", "vazio")
print(carrinho1.status)

carrinho1.adicionar(2)
print(carrinho1.quantidade)