from src.builder.humburquer import Humburquer
from src.builder.produto import Produto
from src.builder.produto_builder import ProdutoBuilder


class HumburquerBuilder(ProdutoBuilder):
    produto: Produto = Humburquer()

    def set_tipo(self, tipo: str) -> None:
        self.produto.tipo = tipo

    def set_valor(self, valor: float) -> None:
        self.produto.valor = valor

    def set_descricao(self, descricao: str) -> None:
        self.produto.descricao = descricao

    def get_produto(self) -> Produto:
        return self.produto
