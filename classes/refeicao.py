from sqlalchemy import Column, Integer, String
from database import Base

class Refeicao(Base):
    __tablename__ = "Refeicao"

    codigo_barra = Column(String(50), primary_key=True, index=True)
    codigo_receita = Column(Integer, primary_key=True, index=True)
    quantidade = Column(Integer, nullable=False)



