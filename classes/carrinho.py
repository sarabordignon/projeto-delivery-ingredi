from sqlalchemy import Column, Integer, String
from database import Base

class Carrinho(Base):
    __tablename__ = "Carrinho"

    codigo_carrinho = Column(Integer, primary_key=True, index=True)
    data_criacao = Column(String(50), nullable=False)
    status = Column(String(50), nullable=False)
    cpf = Column(Integer, nullable=False)

