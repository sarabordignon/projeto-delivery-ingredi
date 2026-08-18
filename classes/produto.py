from sqlalchemy import Column, String, Numeric
from database import Base

class Produto(Base):
    __tablename__ = "Produto"

    codigo_barra = Column(String(20), primary_key=True)
    nome = Column(String(100), nullable=False)
    und_medida = Column(String(10), nullable=False)
    preco_und = Column(Numeric(10, 2), nullable=False)
    categoria = Column(String(50), nullable=False)
    cnpj = Column(String(18), nullable=False)
