from src.builder.humburquer_builder import HumburquerBuilder
from src.builder.novo_produto import NovoProduto
from src.builder.x_salada_builder import XSaladaBuilder


class App:
    def __init__(self) -> None:
        humburquer = (
            NovoProduto('Humburquer', 10.50, 'Novo humburquer')
            .cadastrar_produto(builder=HumburquerBuilder())
            .get_produto()
        )

        x_salada = (
            NovoProduto('X-Salada', 11.50, 'Novo X-Salada')
            .cadastrar_produto(builder=XSaladaBuilder())
            .get_produto()
        )

        humburquer.exibe_produto()

        x_salada.exibe_produto()


if __name__ == '__main__':
    App()
