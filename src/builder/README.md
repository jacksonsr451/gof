# Padrão Builder

Neste padrão encontramos a intenção de separar a construção de um objeto complexo da sua representação do modo que o mesmo processo de construção possa criar diferentes representações.

Com isso o Builder separa a construção do objeto de sua representação.

Diferenças entre Factory e Builder básicamente é que o Factory constroi os objetos de uma só vez, enquanto o Builder faz esse processo gradativamente passo a passo.

Como no Factory criamos nosso produto abstrato

```python
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
```

Logo depois criamos nossos produtos que irão herdar de nosso produto, só que não iremos agregar mais nada de metodos nestes nossos produtos.

```python
from produto import Produto


class Humburquer(Produto):
    """"""


class XSalada(Produto):
    """"""

```

Criamos o builder default para todos os builders que poderemos inserir.

```python
from abc import ABC, abstractmethod

from produto import Produto


class ProdutoBuilder(ABC):
    
    @abstractmethod
    def set_tipo(self, tipo: str) -> None:
        """"""

    @abstractmethod
    def set_valor(self, valor: float) -> None:
        """"""

    @abstractmethod
    def set_descricao(self, descricao: str) -> None:
        """"""

    @abstractmethod
    def get_produto(self) -> Produto:
        """"""
```

Logo em seguida criamos os builders para cada produto a ser inserido em nosso sistema.

```python
from humburquer import Humburquer
from produto import Produto
from produto_builder import ProdutoBuilder


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

```

```python
from produto import Produto
from produto_builder import ProdutoBuilder
from x_salada import XSalada


class XSaladaBuilder(ProdutoBuilder):
    produto: Produto = XSalada()

    def set_tipo(self, tipo: str) -> None:
        self.produto.tipo = tipo

    def set_valor(self, valor: float) -> None:
        self.produto.valor = valor

    def set_descricao(self, descricao: str) -> None:
        self.produto.descricao = descricao

    def get_produto(self) -> Produto:
        return self.produto
```

Por fim, criamos uma classe que possa gerenciar esses builders neste casso de implementação.
Para poder manipular a criação de todos os produtos inseridos.
Nesta classe a somente uma função, a de cadastrar produtos. Com isso no seu construtor ela está recebendo qual é o tipo, valor e descrição de um produto. E em seu metodo cadastrar_produto =, ela recebe o builder default. Com essa condição ao ser chamada e inserido o builder do produto desejado neste methodo, ele irá criar o produto desejado.

```python
from produto_builder import ProdutoBuilder


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
```

Implementação de exemplo:

```python
from humburquer_builder import HumburquerBuilder
from novo_produto import NovoProduto
from x_salada_builder import XSaladaBuilder


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
```

Em nosso terminal, sera apresentado o seguinte resultado.

```bash
tipo: Humburquer
valor: R$10.5
descrição: Novo humburquer



tipo: X-Salada
valor: R$11.5
descrição: Novo X-Salada
```

Padrão builder é indicado para processos complexos, com várias etapas para a produção de um objeto (produto).