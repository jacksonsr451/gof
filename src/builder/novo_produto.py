from src.builder.produto_builder import ProdutoBuilder


class NovoProduto:
    def __init__(self, tipo: str, valor: str, descricao: str) -> None:
        self.tipo: str = tipo
        self.valor: str = valor
        self.descricao: str = descricao

    def cadastrar_produto(self, builder: ProdutoBuilder) -> ProdutoBuilder:
        builder.set_tipo(self.tipo)
        builder.set_valor(self.valor)
        builder.set_descricao(self.descricao)
        return builder
