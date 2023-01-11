from src.abstract_factory.empresa import Empresa
from src.abstract_factory.produto_humburquer import ProdutoHumburquer
from src.abstract_factory.produto_x_salada import ProdutoXSalada


class Lanchonete(Empresa):
    def cadastrar_x_salada(
        self, produto: str, valor: float, descricao: str
    ) -> ProdutoXSalada:
        return ProdutoXSalada(
            produto=produto, valor=valor, descricao=descricao
        )

    def cadastrar_humburquer(
        self, produto: str, valor: float, descricao: str
    ) -> ProdutoHumburquer:
        return ProdutoHumburquer(produto, valor, descricao)
