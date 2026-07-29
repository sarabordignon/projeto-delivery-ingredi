class Refeicao:
    def __init__(self, quantidade):
        self.quantidade = quantidade

    def alterar_quantidade(self, nova_quantidade):
        self.quantidade = nova_quantidade
        print("nova quantidade adicionada!")
    

refeicao1 = Refeicao("1")
print(refeicao1.quantidade)

refeicao1.alterar_quantidade("27")
print(refeicao1.quantidade)


