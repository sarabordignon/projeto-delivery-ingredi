from sqlalchemy import Column, Integer, String
from database import Base

class Pagamento(Base):
    __tablename__ = "Pagamento"

    id_pagamento = Column(Integer, primary_key=True, index=True)
    tipo_pagamento = Column(String(50), nullable=False)
    valor = Column(String(50), nullable=False)
    status_pagamento = Column(String(50), nullable=False)
    data_pagamento = Column(String(50), nullable=False)
    nota_fiscal = Column(String(50), nullable=False)
    numero_pedido = Column(String(50), nullable=False)