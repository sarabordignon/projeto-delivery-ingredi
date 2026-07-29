class Pagamento:
    def __init__(self, id_pagamento, tipo_pagamento, valor, status_pagamento, data_pagamento, nota_fiscal):
        self.id_pagamento = id_pagamento
        self.tipo_pagamento = tipo_pagamento
        self.valor= valor
        self.status_pagamento = status_pagamento
        self.data_pagamento = data_pagamento
        self.nota_fiscal = nota_fiscal

    def alterar_tipo_pagamento(self, alterar_pagamento):
        self.tipo_pagamento = alterar_pagamento
        print("forma de pagamento alterada!")
 
pagamento1 = Pagamento("1", "pix", "22R$", "aprovado", "22-04-2026", "1245")
print(pagamento1.valor)

pagamento1.alterar_tipo_pagamento("cartão")
print(pagamento1.tipo_pagamento)
