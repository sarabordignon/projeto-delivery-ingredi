class Receita:
    def __init__(self, codigo_receita, nome, modo_preparo, tempo_preparo, porcoes):
        self.codigo_receita = codigo_receita
        self.nome = nome
        self.modo_preparo = modo_preparo
        self.tempo_preparo = tempo_preparo
        self.porcoes = porcoes

    def reduzir_porcoes(self):
        self.porcoes //= 2
        print("reduzido pela metade!")

receita1 = Receita(1, "bolo", "batido", "9 minutos", 90)
print(receita1.nome)

receita1.reduzir_porcoes()
print(receita1.porcoes)