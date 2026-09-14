from database import SessionLocal
from pagamento import Pagamento

session = SessionLocal()

novo_pagamento = Pagamento(id_pagamento = 5, tipo_pagamento = "pix", valor = 200.00, status_pagamento = "pago", data_pagamento = "2020/10/10", nota_fiscal = "hrh2347", numero_pedido = "5")
session.add(novo_pagamento)
session.commit()
print("Pagamento inserida!")

session.close()