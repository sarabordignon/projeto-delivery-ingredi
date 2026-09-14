from sqlalchemy import Column, Integer, String
from database import Base

class Pedido(Base):
    __tablename__ = "Pedido"

    numero_pedido = Column(String(50), primary_key=True, index=True)
    data_pedido = Column(String(100), nullable=False)
    status_pedido = Column(String(100), nullable=False)
    valor_total = Column(String(100), nullable=False)
    endereco_entrega = Column(String(100), nullable=False)
    status_entrega = Column(String(100), nullable=False)
    data_prevista_entrega = Column(String(100), nullable=False)
    data_realizada_entrega = Column(String(100), nullable=False)
    cpf = Column(String(100), nullable=False)
    codigo_carrinho = Column(String(100), nullable=False)
