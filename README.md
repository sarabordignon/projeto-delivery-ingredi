# Projeto Delivery Ingredi

API de delivery desenvolvida em Python com FastAPI e SQLAlchemy, integrada a um banco de dados MySQL. O projeto é um sistema completo com rotas para usuário, carrinho, pedido, pagamento, estoque e produto, e inclui os diagramas DER e MER da modelagem de dados.

## Funcionalidades

* Cadastro de usuários: criação e gerenciamento de usuários do sistema
* Produtos e mercado: cadastro de produtos, mercados e listas de produtos
* Receitas e refeições: cadastro de receitas e refeições relacionadas aos produtos
* Carrinho: adição de itens ao carrinho de compras
* Pedidos: criação e acompanhamento de pedidos
* Pagamentos: registro dos pagamentos dos pedidos
* Estoque: controle dos itens disponíveis
* Página HTML de cadastro integrada ao back-end
* Modelagem de dados: diagramas DER e MER do banco

## Tecnologias utilizadas

* Python
* FastAPI
* SQLAlchemy
* MySQL
* HTML

## Estrutura do projeto

```
├── main.py
├── database.py
├── testeDatabase.py
│
├── model/
├── controller/
│   └── funcionalidades/
├── classes/
│
├── usuario.py
├── produto.py
├── mercado.py
├── listaProdutos.py
├── receita.py
├── refeicao.py
├── carrinho.py
├── pedido.py
├── pagamento.py
│
├── cadastroUsuario.py
├── cadastroProduto.py
├── cadastroMercado.py
├── cadastroListaProdutos.py.py
├── cadastroReceita.py
├── cadastroRefeicao.py
├── cadastroCarrinho.py
├── cadastroPedido.py
├── cadastroPagamento.py
│
├── index.html
└── cadastro.html
```

## O que pratiquei

* Criação de uma API com FastAPI e definição de rotas
* Mapeamento de classes para tabelas com SQLAlchemy (ORM)
* Conexão do Python com o MySQL
* Modelagem de banco de dados com diagramas DER e MER
* Separação do projeto em camadas (model, controller e classes)
* Integração de páginas HTML com o back-end

## Como executar

1. Clone o repositório:

```
git clone https://github.com/sarabordignon/projeto-delivery-ingredi.git
```

2. Instale as dependências:

```
pip install fastapi uvicorn sqlalchemy pymysql
```

3. Configure a conexão com o MySQL no arquivo `database.py`

4. Execute a API:

```
uvicorn main:app --reload
```

5. Acesse a documentação interativa em `http://localhost:8000/docs`

## Autora

Projeto desenvolvido por Sara Bordignon como parte do curso Jovem Programador
