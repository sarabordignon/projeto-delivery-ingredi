from sqlalchemy import Column, Integer, String
from database import Base

class Mercado(Base):
    __tablename__ = "Mercado"

    cnpj = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    endereco = Column(String(200), nullable=False)
    contato = Column(Integer, nullable=False)
