CREATE DATABASE DELIVERY;
USE DELIVERY;

CREATE TABLE Usuario (
    cpf         VARCHAR(14)   NOT NULL,
    nome        VARCHAR(100)  NOT NULL,
    email       VARCHAR(100)  NOT NULL,
    telefone    VARCHAR(20)   NOT NULL,
    endereco    VARCHAR(200)  NOT NULL,
    senha       VARCHAR(100)  NOT NULL,
    PRIMARY KEY (cpf)
);

CREATE TABLE Mercado (
    cnpj        VARCHAR(18)   NOT NULL,
    nome        VARCHAR(100)  NOT NULL,
    endereco    VARCHAR(200)  NOT NULL,
    contato     VARCHAR(20)   NOT NULL,
    PRIMARY KEY (cnpj)
);

CREATE TABLE Carrinho (
    codigo_carrinho VARCHAR(20)  NOT NULL,
    data_criacao    DATETIME     NOT NULL,
    status          VARCHAR(20)  NOT NULL,
    cpf             VARCHAR(14)  NOT NULL,
    PRIMARY KEY (codigo_carrinho),
    FOREIGN KEY (cpf) REFERENCES Usuario(cpf)
);

CREATE TABLE Produto (
    codigo_barra  VARCHAR(20)   NOT NULL,
    nome          VARCHAR(100)  NOT NULL,
    und_medida    VARCHAR(10)   NOT NULL,
    preco_und     DECIMAL(10,2) NOT NULL,
    categoria     VARCHAR(50)   NOT NULL,
    cnpj          VARCHAR(18)   NOT NULL,
    PRIMARY KEY (codigo_barra),
    FOREIGN KEY (cnpj) REFERENCES Mercado(cnpj)
);

CREATE TABLE Pedido (
    numero_pedido        VARCHAR(20)   NOT NULL,
    data_pedido           DATETIME     NOT NULL,
    status_pedido         VARCHAR(30)  NOT NULL,
    valor_total            DECIMAL(10,2) NOT NULL,
    endereco_entrega       VARCHAR(200) NOT NULL,
    status_entrega         VARCHAR(30)  NOT NULL,
    data_prevista_entrega  DATETIME     NULL,
    data_realizada_entrega DATETIME     NULL,
    cpf                    VARCHAR(14)  NOT NULL,
    codigo_carrinho        VARCHAR(20)  NOT NULL,
    PRIMARY KEY (numero_pedido),
    FOREIGN KEY (cpf) REFERENCES Usuario(cpf),
    FOREIGN KEY (codigo_carrinho) REFERENCES Carrinho(codigo_carrinho)
);

CREATE TABLE Lista_Produtos (
    codigo_carrinho VARCHAR(20)   NOT NULL,
    codigo_barra    VARCHAR(20)   NOT NULL,
    quantidade      INT           NOT NULL,
    preco_unitario  DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (codigo_carrinho, codigo_barra),
    FOREIGN KEY (codigo_carrinho) REFERENCES Carrinho(codigo_carrinho),
    FOREIGN KEY (codigo_barra) REFERENCES Produto(codigo_barra)
);

CREATE TABLE Pagamento (
    id_pagamento    VARCHAR(20)   NOT NULL,
    tipo_pagamento  VARCHAR(30)   NOT NULL,
    valor           DECIMAL(10,2) NOT NULL,
    status_pagamento VARCHAR(20)  NOT NULL,
    data_pagamento  DATETIME      NOT NULL,
    nota_fiscal     VARCHAR(50)   NULL,
    numero_pedido   VARCHAR(20)   NOT NULL,
    PRIMARY KEY (id_pagamento),
    FOREIGN KEY (numero_pedido) REFERENCES Pedido(numero_pedido),
    UNIQUE (numero_pedido)
);

CREATE TABLE Receita (
    codigo_receita  VARCHAR(20)  NOT NULL,
    nome            VARCHAR(100) NOT NULL,
    modo_preparo    TEXT         NOT NULL,
    tempo_preparo   INT          NOT NULL,
    porcoes         INT          NOT NULL,
    PRIMARY KEY (codigo_receita)
);

CREATE TABLE Refeicao (
    codigo_receita  VARCHAR(20) NOT NULL,
    codigo_barra    VARCHAR(20) NOT NULL,
    quantidade      INT         NOT NULL,
    PRIMARY KEY (codigo_receita, codigo_barra),
    FOREIGN KEY (codigo_receita) REFERENCES Receita(codigo_receita),
    FOREIGN KEY (codigo_barra) REFERENCES Produto(codigo_barra)
);

INSERT INTO Usuario (cpf, nome, email, telefone, endereco, senha) VALUES
('111.222.333-44', 'Maria Silva', 'maria.silva@email.com', '(48) 99123-4567', 'Rua das Flores, 123 - Curitibanos/SC', 'senha123'),
('222.333.444-55', 'Joao Pereira', 'joao.pereira@email.com', '(48) 99887-7665', 'Av. Brasil, 456 - Florianopolis/SC', 'senha456');

INSERT INTO Mercado (cnpj, nome, endereco, contato) VALUES
('12.345.678/0001-90', 'Mercado Sazon Central', 'Rua Comercio, 789 - Curitibanos/SC', '(48) 3241-5566'),
('98.765.432/0001-10', 'Mercado Sazon Filial', 'Av. Industrial, 321 - Florianopolis/SC', '(48) 3255-7788');

INSERT INTO Carrinho (codigo_carrinho, data_criacao, status, cpf) VALUES
('CAR001', '2026-07-20 10:15:00', 'aberto', '111.222.333-44'),
('CAR002', '2026-07-21 14:30:00', 'fechado', '222.333.444-55');

INSERT INTO Produto (codigo_barra, nome, und_medida, preco_und, categoria, cnpj) VALUES
('7891000100103', 'Tomate', 'kg', 6.50, 'Hortifruti', '12.345.678/0001-90'),
('7891000200207', 'Arroz Branco', 'kg', 5.20, 'Graos', '98.765.432/0001-10');

INSERT INTO Pedido (numero_pedido, data_pedido, status_pedido, valor_total, endereco_entrega, status_entrega, data_prevista_entrega, data_realizada_entrega, cpf, codigo_carrinho) VALUES
('PED001', '2026-07-20 11:00:00', 'em producao', 45.60, 'Rua das Flores, 123 - Curitibanos/SC', 'esperando', '2026-07-20 12:30:00', NULL, '111.222.333-44', 'CAR001'),
('PED002', '2026-07-21 15:00:00', 'entregue', 78.90, 'Av. Brasil, 456 - Florianopolis/SC', 'entregue', '2026-07-21 16:00:00', '2026-07-21 15:55:00', '222.333.444-55', 'CAR002');

INSERT INTO Lista_Produtos (codigo_carrinho, codigo_barra, quantidade, preco_unitario) VALUES
('CAR001', '7891000100103', 3, 6.50),
('CAR002', '7891000200207', 5, 5.20);

INSERT INTO Pagamento (id_pagamento, tipo_pagamento, valor, status_pagamento, data_pagamento, nota_fiscal, numero_pedido) VALUES
('PAG001', 'pix', 45.60, 'aprovado', '2026-07-20 11:05:00', 'NF-000123', 'PED001'),
('PAG002', 'cartao_credito', 78.90, 'aprovado', '2026-07-21 15:10:00', 'NF-000124', 'PED002');

INSERT INTO Receita (codigo_receita, nome, modo_preparo, tempo_preparo, porcoes) VALUES
('REC001', 'Molho de Tomate Caseiro', 'Refogue o alho, adicione o tomate picado e cozinhe por 20 minutos em fogo baixo.', 30, 4),
('REC002', 'Arroz Soltinho', 'Refogue o arroz no oleo, adicione agua e sal, cozinhe ate secar.', 25, 4);

INSERT INTO Refeicao (codigo_receita, codigo_barra, quantidade) VALUES
('REC001', '7891000100103', 4),
('REC002', '7891000200207', 2);