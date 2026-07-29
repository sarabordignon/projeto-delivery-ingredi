class Lista:
    def __init__(self, quantidade, preco_unitario):
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario

    def alterar_preco(self, novo_preco):
        self.preco_unitario = novo_preco
        print("preço alterado!")

lista1 = Lista("1", "34 R$")
print(lista1.quantidade)

lista1.alterar_preco(2.99)
print(lista1.preco_unitario)