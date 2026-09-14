from sqlalchemy import Column, String
from database import Base

class Mercado(Base):
    __tablename__ = "Mercado"

    cnpj = Column(String(18), primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    endereco = Column(String(200), nullable=False)
    contato = Column(String(20), nullable=False)
