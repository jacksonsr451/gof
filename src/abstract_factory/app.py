from src.abstract_factory.empresa import Empresa
from src.abstract_factory.lanchonete import Lanchonete
from src.abstract_factory.produto_humburquer import ProdutoHumburquer
from src.abstract_factory.produto_x_salada import ProdutoXSalada


class App:
    empresa: Empresa
    x_salada: ProdutoXSalada
    humburquer: ProdutoHumburquer

    def __init__(self) -> None:
        self.empresa = Lanchonete()

        self.x_salada = self.empresa.cadastrar_x_salada('X-Salada', 12.50, 'O melhor da minha casa!')
        self.humburquer = self.empresa.cadastrar_humburquer('Humburquer', 10.50, 'Humburquer caseiro!')

        self.x_salada.exibe_produto()
        self.humburquer.exibe_produto()


if __name__ == '__main__':
    App()
