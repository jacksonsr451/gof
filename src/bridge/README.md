# Padrão Bridge

O padrão Bridge tem por intenção desacoplar uma abstração da sua implementação, de modo que as duas possam variar independentemente.

Com isso ela separa a interface do objeto de sua implementação.

Para implementar este exemplo, criei duas classes abstratas - Frutas e Implementacao:

São duas classes isoladas uma que irá representar as nossas abstrações e a outra para a implementações.

A classe Implementacao contém somente um metodo, implementa, que sera responsavel por nossa implementação.

```python
from abc import ABC, abstractmethod


class Implementacao(ABC):
    
    @abstractmethod
    def implementa(self) -> None:
        """"""
```

A classe Frutas, recebe em seu construtor a Implementacao e em um metodo execute ela chama o metodo implementa de Implementacao. 

```python
from abc import ABC, abstractmethod

from implementacao import Implementacao


class Frutas(ABC):
    executa_implementacao: Implementacao

    def __init__(self, executa_implementacao: Implementacao) -> None:
        self.executa_implementacao = executa_implementacao

    @abstractmethod
    def execute(self) -> None:
        """"""
```

Com essas duas classes prontas criei os dois objetos abstrados para o exemplo, Maca e Banana.
Veja que são objetos abstratos mas não são classes abstratas, e em ambas é recebido em seu construtor a Implementacao.

```python
from frutas import Frutas
from implementacao import Implementacao


class Maca(Frutas):
    def __init__(self, executa_implementacao: Implementacao) -> None:
        super().__init__(executa_implementacao)

    def execute(self) -> None:
        self.executa_implementacao.implementa()


class Banana(Frutas):
    def __init__(self, executa_implementacao: Implementacao) -> None:
        super().__init__(executa_implementacao)

    def execute(self) -> None:
        self.executa_implementacao.implementa()
```

Agora montando as classes de implementação, que neste caso é bem simples.
No metodo implementa de cada uma delas, estarei printando somente algo referente a implementação do objeto abstrato.

```python
from implementacao import Implementacao


class MacaImplementacao(Implementacao):
    def implementa(self) -> None:
        print('Implementando a fruta maçã!')


class BananaImplementacao(Implementacao):
    def implementa(self) -> None:
        print('Implementando a fruta banana!')
```

Rodando nossa aplicação:

```python 
from banana import Banana
from banana_implementacao import BananaImplementacao
from frutas import Frutas
from maca import Maca
from maca_implementacao import MacaImplementacao


class App:
    def __init__(self) -> None:
        banana: Frutas = Banana(BananaImplementacao())

        maca: Frutas = Maca(MacaImplementacao())

        banana.execute()

        maca.execute()


if __name__ == '__main__':
    App()
```

O resultado será:

```bash
Implementando a fruta banana!
Implementando a fruta maçã!
```

O padrão bridge deixara bem isolado a abstração da implementação, e se necessário alterar qualquer um deles de forma isolada, não irá impactar no resultado final.
