from sqlalchemy import Column, String
from database import Base

class Usuario(Base):
    __tablename__ = "Usuario"

    cpf = Column(String(14), primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    telefone = Column(String(20), nullable=False)
    endereco = Column(String(200), nullable=False)
    senha = Column(String(100), nullable=False)

