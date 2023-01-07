from abc import ABC


class Produto(ABC):
    tipo: str
    valor: float
    descricao: str

    def exibe_produto(self) -> str:
        produto = (
            '\n\ntipo: {}\n'.format(self.tipo)
            + 'valor: R${}\n'.format(self.valor)
            + 'descrição: {}\n'.format(self.descricao)
        )
        print(produto)
