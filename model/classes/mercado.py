class Mercado:
    def __init__(self, cnpj, nome, endereco, contato):
        self.cnpj = cnpj
        self.nome = nome
        self.endereco= endereco
        self.contato = contato

    def alterar_contato(self, novo_contato):
        self.contato = novo_contato
        print("novo contato adicionado!")

mercado1 = Mercado("1321412", "mercado do carlos", "Rua 43", "491294122332")
print(mercado1.nome)

mercado1.alterar_contato(3456)
print(mercado1.contato)