from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import SessionLocal
from usuario import Usuario
from carrinho import Carrinho
from pedido import Pedido
from receita import Receita
from listaProdutos import ListaProdutos
from mercado import Mercado
from pagamento import Pagamento
from produto import Produto
from refeicao import Refeicao

app = FastAPI()

app.add_middleware (
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/usuario")
def listarUsuario():
    session = SessionLocal()
    usuario = session.query(Usuario).all()
    resultado = [{"cpf": u.cpf, "nome": u.nome, "email": u.email, "telefone": u.telefone, "endereco": u.endereco} for u in usuario]

    session.close()
    return resultado
    

@app.get("/carrinho")
def listarCarrinho():
    session = SessionLocal()
    carrinhos = session.query(Carrinho).all()
    resultado = [{"codigo_carrinho": u.codigo_carrinho,"data_criacao": u.data_criacao, "status": u.status,"cpf": u.cpf }for u in carrinhos]

    session.close()
    return resultado

@app.get("/pedido")
def listarPedido():
    session = SessionLocal()

    pedidos = session.query(Pedido).all()

    resultado = [{
        "numero_pedido": u.numero_pedido,
        "data_pedido": u.data_pedido,
        "status_pedido": u.status_pedido,
        "valor_total": u.valor_total,
        "endereco_entrega": u.endereco_entrega,
        "status_entrega": u.status_entrega,
        "data_prevista_entrega": u.data_prevista_entrega,
        "data_realizada_entrega": u.data_realizada_entrega,
        "cpf": u.cpf,
        "codigo_carrinho": u.codigo_carrinho
    } for u in pedidos]

    session.close()
    return resultado
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