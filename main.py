from fastapi import FastAPI 

#cria a aplicação
app = FastAPI()


@app.get("/usuario")
def usuario():
    return {"cpf: " "123456789" " | "
            "nome: " "Sara" " | "
            "email: " "sara123@gmail.com" " | "
            "telefone: " "123456789" " | "
            "endereço: " "rua das flores 123" " | "
            "senha: " "12345"}

@app.get("/carrinho")
def carrinho():
    return {"codigo carrinho: " "1" " | "
            "data de criação: " "10/03/2026" " | "
            "status: " "vazio" " | "
            "cpf: " "123456789"}

@app.get("/pedido")
def pedido():
    return {"numero do pedido: " "1" " | "
            "data pedido: " "07/08/2026" " | "
            "status pedido: " "produção" " | "
            "valor total: " "100 reais" " | "
            "endereço: " "rua 123" " | "
            "status entrega: " "em espera" " | "
            "data prevista: " "07/08/2026 as 7:00" " | "
            "data da entrega: " "07/08/2026 as 6:50" " | "
            "cpf: " "12345678" " | "
            "codigo carrinho: " "1"}

@app.get("/lista")
def lista_produtos():
    return {"codigo carrinho: " "1" " | "
            "codigo barra: " "1" " | "
            "quantidade: " "1und" " | "
            "preço unitario: " "1 real"}

@app.get("/produto")
def produto():
    return {"codigo barra: " "1" " | "
            "nome: " "arroz" " | "
            "unidade medida: " "1kg" " | "
            "preço unidade: " "1 real" " | "
            "categoria: " "grãos" " | "
            "cnpj: " "123456"}

@app.get("/refeicao")
def refeicao():
    return {"codigo barras: " "1" " | "
            "codigo receita: " "1" " | "
            "quantidade: " "1" }

@app.get("/mercado")
def mercado():
    return {"cnpj: " "123456" " | "
            "nome: " "bigbom" " | "
            "endereço: " "centro" " | "
            "contato: " "98765"}

@app.get("/pagamento")
def pagamento():
    return {"id pagamento: " "1" " | "
            "tipo: " "pix" " | "
            "valor: " "100 reais" " | "
            "status: " "autorizado" " | "
            "data do pagamento: " "10/05/2026" " | "
            "nota fiscal: " "176364" " | "
            "numero pedido: " "1"}


@app.get("/receita")
def receita():
    return {"codigo receita: " "1" " | "
            "nome: " "bolo" " | "
            "modo preparo: " "bata no liquidificador" " | "
            "tempo preparo: " "9min" " | "
            "porções: " "1kg"}