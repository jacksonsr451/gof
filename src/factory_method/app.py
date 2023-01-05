from src.factory_method.empresa import Empresa
from src.factory_method.lanchonete import Lanchonete
from src.factory_method.produto import Produto


class App:
    empresa: Empresa
    produto: Produto

    def __init__(self) -> None:
        self.empresa = Lanchonete()

        self.produto = self.empresa.cadastrar_x_salada('X-Salada', 12.25, 'O melhor X-Salada da minha casa!')
        
        self.produto.exibe_produto()


if __name__ == '__main__':
    App()
