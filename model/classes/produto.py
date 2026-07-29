class Produto:
    def __init__(self, codigo_barra, nome, unidade_medida, preco_unidade, categoria):
        self.codigo_barra = codigo_barra
        self.nome = nome
        self.unidade_medida = unidade_medida
        self.preco_unidade = preco_unidade
        self.categoria= categoria

    def alterar_preco(self, novo_preco):
        self.preco_unidade = novo_preco
        print("preço alterado!")

produto1 = Produto("1312421", "farinha", "kg", "23R$", "doce")
print(produto1.nome)

produto1.alterar_preco("15,90R$")
print(produto1.preco_unidade)