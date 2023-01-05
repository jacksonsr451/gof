from src.factory_method.empresa import Empresa
from src.factory_method.prodtuto_x_salada import ProdutoXSalada


class Lanchonete(Empresa):

    def cadastrar_x_salada(self, produto: str, valor: float, descricao: str) -> ProdutoXSalada:
        return ProdutoXSalada(produto=produto, valor=valor, descricao=descricao)
