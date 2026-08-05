from sqlalchemy import Column, Integer, String
from database import Base

class Receita(Base):
    __tablename__ = "Receita"

    codigo_receita = Column(String(50), primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    modo_preparo = Column(String(500), nullable=False)
    tempo_preparo = Column(Integer, nullable=False)
    porcoes = Column(Integer, nullable=False)