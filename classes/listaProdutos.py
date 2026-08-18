
from sqlalchemy import Column, Integer, String
from database import Base


class ListaProdutos(Base):
    __tablename__ = "lista_produtos"

    codigo_carrinho = Column(String(20), primary_key=True, index=True)
    codigo_barra = Column(String(20), primary_key=True, index=True)
    quantidade = Column(Integer, nullable=False)
    preco_unitario = Column(String(20), nullable=False)

    def alterar_preco(self, novo_preco):
        self.preco_unitario = novo_preco
        print("Preço alterado!")



