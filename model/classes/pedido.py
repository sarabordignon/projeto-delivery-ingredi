class Pedido:
    def __init__(self, numero_pedido, data_pedido, status_pedido, valor_total, endereco_entrega, status_entrega, data_prevista_entrega, data_realizada_entrega):
        self.numero_pedido = numero_pedido
        self.data_pedido = data_pedido
        self.status_pedido = status_pedido
        self.valor_total = valor_total
        self.endereco_entrega = endereco_entrega
        self.status_entrega = status_entrega
        self.data_prevista_entrega = data_prevista_entrega
        self.data_realizada_entrega = data_realizada_entrega

    def cancelar(self, status_novo):
        self.status_pedido = status_novo
        print("novo status adicionado!")


pedido1 = Pedido("1", "26-04-2026", "pendente", "99R$", "Rua 3", "pendente", "27-04-2026", "ainda não realizada")
print(pedido1.valor_total)

pedido1.cancelar("cancelado")
print(pedido1.status_pedido)





