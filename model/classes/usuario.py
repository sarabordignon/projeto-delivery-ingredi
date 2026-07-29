class Usuario:
    def __init__(self,cpf, nome, email, telefone, endereco, senha):
        self.cpf = cpf
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.endereco = endereco
        self.senha = senha

    def alterar_senha(self, nova_senha):
        self.senha = nova_senha
        print("senha alterada!")

    def exibir_dados(self):
        print(self.nome, self.email)

usuario1 = Usuario("213142112", "carlos", "carlos@gmail.com", "2313122321421", "Rua 3", "carlos123")

usuario1.alterar_senha(1234)
print(usuario1.senha)

usuario1.exibir_dados()
print(usuario1.telefone)



