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

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


# Usuario

@app.get("/usuario")
def listarUsuario():

    session = SessionLocal()

    usuarios = session.query(Usuario).all()

    resultado = [
        {
            "cpf": u.cpf,
            "nome": u.nome,
            "email": u.email,
            "telefone": u.telefone,
            "endereco": u.endereco
        }
        for u in usuarios
    ]

    session.close()

    return resultado


@app.post("/usuario")
def salvarUsuario(dados: dict):

    session = SessionLocal()

    novo_usuario = Usuario(
        cpf=dados["cpf"],
        nome=dados["nome"],
        email=dados["email"],
        telefone=dados["telefone"],
        endereco=dados["endereco"],
        senha=dados["senha"]
    )

    session.add(novo_usuario)
    session.commit()
    session.close()

    return {"mensagem": "Usuario salvo"}


@app.delete("/usuario/{cpf}")
def excluirUsuario(cpf: str):

    db = SessionLocal()

    usuario = db.query(Usuario).filter(
        Usuario.cpf == cpf
    ).first()

    if usuario is None:
        db.close()
        return {"mensagem": "Usuario nao encontrado"}

    # Busca todos os carrinhos do usuário
    carrinhos = db.query(Carrinho).filter(
        Carrinho.cpf == cpf
    ).all()

    for carrinho in carrinhos:

        # Exclui os itens do carrinho
        db.query(ListaProdutos).filter(
            ListaProdutos.codigo_carrinho == carrinho.codigo_carrinho
        ).delete(synchronize_session=False)

        # Busca pedidos desse carrinho
        pedidos = db.query(Pedido).filter(
            Pedido.codigo_carrinho == carrinho.codigo_carrinho
        ).all()

        for pedido in pedidos:

            # Exclui pagamento do pedido
            db.query(Pagamento).filter(
                Pagamento.numero_pedido == pedido.numero_pedido
            ).delete(synchronize_session=False)

        # Exclui pedidos do carrinho
        db.query(Pedido).filter(
            Pedido.codigo_carrinho == carrinho.codigo_carrinho
        ).delete(synchronize_session=False)

    # Exclui possíveis pedidos do usuário
    # que não estejam associados aos carrinhos
    pedidos_usuario = db.query(Pedido).filter(
        Pedido.cpf == cpf
    ).all()

    for pedido in pedidos_usuario:

        db.query(Pagamento).filter(
            Pagamento.numero_pedido == pedido.numero_pedido
        ).delete(synchronize_session=False)

    db.query(Pedido).filter(
        Pedido.cpf == cpf
    ).delete(synchronize_session=False)

    # Exclui os carrinhos
    db.query(Carrinho).filter(
        Carrinho.cpf == cpf
    ).delete(synchronize_session=False)

    # Finalmente exclui o usuário
    db.delete(usuario)

    db.commit()
    db.close()

    return {"mensagem": "Usuario excluido"}


# Carrinho

@app.get("/carrinho")
def listarCarrinho():

    session = SessionLocal()

    carrinhos = session.query(Carrinho).all()

    resultado = [
        {
            "codigo_carrinho": u.codigo_carrinho,
            "data_criacao": u.data_criacao,
            "status": u.status,
            "cpf": u.cpf
        }
        for u in carrinhos
    ]

    session.close()

    return resultado


@app.post("/carrinho")
def salvarCarrinho(dados: dict):

    session = SessionLocal()

    novo_carrinho = Carrinho(
        codigo_carrinho=dados["codigo_carrinho"],
        data_criacao=dados["data_criacao"],
        status=dados["status"],
        cpf=dados["cpf"]
    )

    session.add(novo_carrinho)
    session.commit()
    session.close()

    return {"mensagem": "Carrinho salvo"}


@app.delete("/carrinho/{codigo_carrinho}")
def excluirCarrinho(codigo_carrinho: str):

    db = SessionLocal()

    carrinho = db.query(Carrinho).filter(
        Carrinho.codigo_carrinho == codigo_carrinho
    ).first()

    if carrinho is None:
        db.close()
        return {"mensagem": "Carrinho nao encontrado"}

    pedidos = db.query(Pedido).filter(
        Pedido.codigo_carrinho == codigo_carrinho
    ).all()

    for pedido in pedidos:

        db.query(Pagamento).filter(
            Pagamento.numero_pedido == pedido.numero_pedido
        ).delete(synchronize_session=False)

    db.query(Pedido).filter(
        Pedido.codigo_carrinho == codigo_carrinho
    ).delete(synchronize_session=False)

    db.query(ListaProdutos).filter(
        ListaProdutos.codigo_carrinho == codigo_carrinho
    ).delete(synchronize_session=False)

    db.query(Carrinho).filter(
        Carrinho.codigo_carrinho == codigo_carrinho
    ).delete(synchronize_session=False)

    db.commit()
    db.close()

    return {"mensagem": "Carrinho excluido"}


# Pedido

@app.get("/pedido")
def listarPedido():

    session = SessionLocal()

    pedidos = session.query(Pedido).all()

    resultado = [
        {
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
        }
        for u in pedidos
    ]

    session.close()

    return resultado


@app.post("/pedido")
def salvarPedido(dados: dict):

    session = SessionLocal()

    novo_pedido = Pedido(
        numero_pedido=dados["numero_pedido"],
        data_pedido=dados["data_pedido"],
        status_pedido=dados["status_pedido"],
        valor_total=dados["valor_total"],
        endereco_entrega=dados["endereco_entrega"],
        status_entrega=dados["status_entrega"],
        data_prevista_entrega=dados["data_prevista_entrega"],
        data_realizada_entrega=dados["data_realizada_entrega"],
        cpf=dados["cpf"],
        codigo_carrinho=dados["codigo_carrinho"]
    )

    session.add(novo_pedido)
    session.commit()
    session.close()

    return {"mensagem": "Pedido salvo"}


@app.delete("/pedido/{numero_pedido}")
def excluirPedido(numero_pedido: str):

    db = SessionLocal()

    pedido = db.query(Pedido).filter(
        Pedido.numero_pedido == numero_pedido
    ).first()

    if pedido is None:
        db.close()
        return {"mensagem": "Pedido nao encontrado"}

    db.query(Pagamento).filter(
        Pagamento.numero_pedido == numero_pedido
    ).delete(synchronize_session=False)

    db.query(Pedido).filter(
        Pedido.numero_pedido == numero_pedido
    ).delete(synchronize_session=False)

    db.commit()
    db.close()

    return {"mensagem": "Pedido excluido"}


# ListaProdutos

@app.get("/lista")
def lista_produtos():

    session = SessionLocal()

    listaProdutos = session.query(ListaProdutos).all()

    resultado = [
        {
            "codigo_carrinho": u.codigo_carrinho,
            "codigo_barra": u.codigo_barra,
            "quantidade": u.quantidade,
            "preco_unitario": u.preco_unitario
        }
        for u in listaProdutos
    ]

    session.close()

    return resultado


@app.post("/lista")
def salvarLista(dados: dict):

    session = SessionLocal()

    nova_lista = ListaProdutos(
        codigo_carrinho=dados["codigo_carrinho"],
        codigo_barra=dados["codigo_barra"],
        quantidade=dados["quantidade"],
        preco_unitario=dados["preco_unitario"]
    )

    session.add(nova_lista)
    session.commit()
    session.close()

    return {"mensagem": "Item salvo"}


@app.delete("/lista/{codigo_carrinho}/{codigo_barra}")
def excluirLista(codigo_carrinho: str, codigo_barra: str):

    db = SessionLocal()

    item = db.query(ListaProdutos).filter(
        ListaProdutos.codigo_carrinho == codigo_carrinho,
        ListaProdutos.codigo_barra == codigo_barra
    ).first()

    if item is None:
        db.close()
        return {"mensagem": "Item nao encontrado"}

    db.query(ListaProdutos).filter(
        ListaProdutos.codigo_carrinho == codigo_carrinho,
        ListaProdutos.codigo_barra == codigo_barra
    ).delete(synchronize_session=False)

    db.commit()
    db.close()

    return {"mensagem": "Item excluido"}


# Produto

@app.get("/produto")
def produto():

    session = SessionLocal()

    produtos = session.query(Produto).all()

    resultado = [
        {
            "codigo_barra": u.codigo_barra,
            "nome": u.nome,
            "und_medida": u.und_medida,
            "preco_und": u.preco_und,
            "categoria": u.categoria,
            "cnpj": u.cnpj
        }
        for u in produtos
    ]

    session.close()

    return resultado


@app.post("/produto")
def salvarProduto(dados: dict):

    session = SessionLocal()

    novo_produto = Produto(
        codigo_barra=dados["codigo_barra"],
        nome=dados["nome"],
        und_medida=dados["und_medida"],
        preco_und=dados["preco_und"],
        categoria=dados["categoria"],
        cnpj=dados["cnpj"]
    )

    session.add(novo_produto)
    session.commit()
    session.close()

    return {"mensagem": "Produto salvo"}


@app.delete("/produto/{codigo_barra}")
def excluirProduto(codigo_barra: str):

    db = SessionLocal()

    produto = db.query(Produto).filter(
        Produto.codigo_barra == codigo_barra
    ).first()

    if produto is None:
        db.close()
        return {"mensagem": "Produto nao encontrado"}

    db.query(ListaProdutos).filter(
        ListaProdutos.codigo_barra == codigo_barra
    ).delete(synchronize_session=False)

    db.query(Refeicao).filter(
        Refeicao.codigo_barra == codigo_barra
    ).delete(synchronize_session=False)

    db.query(Produto).filter(
        Produto.codigo_barra == codigo_barra
    ).delete(synchronize_session=False)

    db.commit()
    db.close()

    return {"mensagem": "Produto excluido"}


# Refeicao

@app.get("/refeicao")
def refeicao():

    session = SessionLocal()

    refeicoes = session.query(Refeicao).all()

    resultado = [
        {
            "codigo_receita": u.codigo_receita,
            "codigo_barra": u.codigo_barra,
            "quantidade": u.quantidade
        }
        for u in refeicoes
    ]

    session.close()

    return resultado


@app.post("/refeicao")
def salvarRefeicao(dados: dict):

    session = SessionLocal()

    nova_refeicao = Refeicao(
        codigo_receita=dados["codigo_receita"],
        codigo_barra=dados["codigo_barra"],
        quantidade=dados["quantidade"]
    )

    session.add(nova_refeicao)
    session.commit()
    session.close()

    return {"mensagem": "Refeicao salva"}


@app.delete("/refeicao/{codigo_receita}/{codigo_barra}")
def excluirRefeicao(codigo_receita: str, codigo_barra: str):

    db = SessionLocal()

    refeicao = db.query(Refeicao).filter(
        Refeicao.codigo_receita == codigo_receita,
        Refeicao.codigo_barra == codigo_barra
    ).first()

    if refeicao is None:
        db.close()
        return {"mensagem": "Refeicao nao encontrada"}

    db.query(Refeicao).filter(
        Refeicao.codigo_receita == codigo_receita,
        Refeicao.codigo_barra == codigo_barra
    ).delete(synchronize_session=False)

    db.commit()
    db.close()

    return {"mensagem": "Refeicao excluida"}


# Mercado

@app.get("/mercado")
def mercado():

    session = SessionLocal()

    mercados = session.query(Mercado).all()

    resultado = [
        {
            "cnpj": u.cnpj,
            "nome": u.nome,
            "endereco": u.endereco,
            "contato": u.contato
        }
        for u in mercados
    ]

    session.close()

    return resultado


@app.post("/mercado")
def salvarMercado(dados: dict):

    session = SessionLocal()

    novo_mercado = Mercado(
        cnpj=dados["cnpj"],
        nome=dados["nome"],
        endereco=dados["endereco"],
        contato=dados["contato"]
    )

    session.add(novo_mercado)
    session.commit()
    session.close()

    return {"mensagem": "Mercado salvo"}


@app.delete("/mercado/{cnpj}")
def excluirMercado(cnpj: str):

    db = SessionLocal()

    mercado = db.query(Mercado).filter(
        Mercado.cnpj == cnpj
    ).first()

    if mercado is None:
        db.close()
        return {"mensagem": "Mercado nao encontrado"}

    produtos = db.query(Produto).filter(
        Produto.cnpj == cnpj
    ).all()

    for produto in produtos:

        db.query(ListaProdutos).filter(
            ListaProdutos.codigo_barra == produto.codigo_barra
        ).delete(synchronize_session=False)

        db.query(Refeicao).filter(
            Refeicao.codigo_barra == produto.codigo_barra
        ).delete(synchronize_session=False)

    db.query(Produto).filter(
        Produto.cnpj == cnpj
    ).delete(synchronize_session=False)

    db.query(Mercado).filter(
        Mercado.cnpj == cnpj
    ).delete(synchronize_session=False)

    db.commit()
    db.close()

    return {"mensagem": "Mercado excluido"}


# Pagamento

@app.get("/pagamento")
def pagamento():

    session = SessionLocal()

    pagamentos = session.query(Pagamento).all()

    resultado = [
        {
            "id_pagamento": u.id_pagamento,
            "tipo_pagamento": u.tipo_pagamento,
            "valor": u.valor,
            "status_pagamento": u.status_pagamento,
            "data_pagamento": u.data_pagamento,
            "nota_fiscal": u.nota_fiscal,
            "numero_pedido": u.numero_pedido
        }
        for u in pagamentos
    ]

    session.close()

    return resultado


@app.post("/pagamento")
def salvarPagamento(dados: dict):

    session = SessionLocal()

    novo_pagamento = Pagamento(
        id_pagamento=dados["id_pagamento"],
        tipo_pagamento=dados["tipo_pagamento"],
        valor=dados["valor"],
        status_pagamento=dados["status_pagamento"],
        data_pagamento=dados["data_pagamento"],
        nota_fiscal=dados["nota_fiscal"],
        numero_pedido=dados["numero_pedido"]
    )

    session.add(novo_pagamento)
    session.commit()
    session.close()

    return {"mensagem": "Pagamento salvo"}


@app.delete("/pagamento/{id_pagamento}")
def excluirPagamento(id_pagamento: str):

    db = SessionLocal()

    pagamento = db.query(Pagamento).filter(
        Pagamento.id_pagamento == id_pagamento
    ).first()

    if pagamento is None:
        db.close()
        return {"mensagem": "Pagamento nao encontrado"}

    db.query(Pagamento).filter(
        Pagamento.id_pagamento == id_pagamento
    ).delete(synchronize_session=False)

    db.commit()
    db.close()

    return {"mensagem": "Pagamento excluido"}


# Receita

@app.get("/receita")
def receita():

    session = SessionLocal()

    receitas = session.query(Receita).all()

    resultado = [
        {
            "codigo_receita": u.codigo_receita,
            "nome": u.nome,
            "modo_preparo": u.modo_preparo,
            "tempo_preparo": u.tempo_preparo,
            "porcoes": u.porcoes
        }
        for u in receitas
    ]

    session.close()

    return resultado


@app.post("/receita")
def salvarReceita(dados: dict):

    session = SessionLocal()

    nova_receita = Receita(
        codigo_receita=dados["codigo_receita"],
        nome=dados["nome"],
        modo_preparo=dados["modo_preparo"],
        tempo_preparo=dados["tempo_preparo"],
        porcoes=dados["porcoes"]
    )

    session.add(nova_receita)
    session.commit()
    session.close()

    return {"mensagem": "Receita salva"}


@app.delete("/receita/{codigo_receita}")
def excluirReceita(codigo_receita: str):

    db = SessionLocal()

    receita = db.query(Receita).filter(
        Receita.codigo_receita == codigo_receita
    ).first()

    if receita is None:
        db.close()
        return {"mensagem": "Receita nao encontrada"}

    db.query(Refeicao).filter(
        Refeicao.codigo_receita == codigo_receita
    ).delete(synchronize_session=False)

    db.query(Receita).filter(
        Receita.codigo_receita == codigo_receita
    ).delete(synchronize_session=False)

    db.commit()
    db.close()

    return {"mensagem": "Receita excluida"}

