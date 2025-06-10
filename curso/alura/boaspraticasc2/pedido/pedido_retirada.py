from pedido.pedido import Pedido


class PedidoRetirada(Pedido):
    def calcula_total(self):
        return sum(item.preco for item in self.itens)
