from src.factory_method.produto import Produto


class ProdutoXSalada(Produto):
    def __init__(self, produto: str, valor: float, descricao: str) -> None:
        super().__init__(produto, valor, descricao)

    def exibe_produto(self) -> str:
        produto = (
            '\n\nproduto: {}\n'.format(self.get_tipo())
            + 'valor: R${}\n'.format(self.get_valor())
            + 'descrição: {}\n'.format(self.get_descricao())
        )
        print(produto)
