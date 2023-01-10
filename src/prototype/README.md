# Padrão Prototype

O padrão prototype tem por sua intenção expecificar os tipos de objetos a serem criados usando uma instância protótipo e criar novos objetos pela cópia deste protótipo.
Este padrão básicamente ira fazer clones de objetos.

Para ver o funcionamento do padrão Prototype, escolhido um estilo de programa que representa uma partitura musical e com suas notas atribuidas.

Criamos então em primeiro momento a NotaMusical.

```python
from abc import ABC, abstractmethod


class NotaMusical(ABC):
    def clone(self):    
        return self

    @abstractmethod
    def desenhar(self) -> None:
        """"""
```
Está classe que irá ficar responsavel por clonar as notas da nossa partitura, nela existe somente 2 metodos (clone, desenhar):
- clone: retorna self, que basicamente retorna a instância do objeto que esta sendo chamado.
- desenhar: retorna o resultado apresentado em tela

O proximo passo é a criação de nossas notas, todas elas irão herdar de NotaMusical.
Em cada notá é aplicado o metodo desenhar, com seus respectivos valores de apresentação. 
Neste caso, cada um imprime qual nota esta sendo chamada.

```python
from src.prototype.nota_musical import NotaMusical


class Do(NotaMusical):
    def desenhar(self) -> None:
        print("DÓ ")

class Re(NotaMusical):
    def desenhar(self) -> None:
        print("RÉ ")

class Mi(NotaMusical):
    def desenhar(self) -> None:
        print("MI ")

class Fa(NotaMusical):
    def desenhar(self) -> None:
        print("FÁ ")

class Sol(NotaMusical):
    def desenhar(self) -> None:
        print("SOL ")

class La(NotaMusical):
    def desenhar(self) -> None:
        print("LÁ ")

class Si(NotaMusical):
    def desenhar(self) -> None:
        print("SI ")
```

Agora criamos a Partitura, que nela contém todas as notas em um dicionário já instânciadas.


```python
from types import NoneType
from do import Do
from fa import Fa
from la import La
from mi import Mi
from nota_musical import NotaMusical
from re import Re
from si import Si
from sol import Sol


class Partitura:
    def __init__(self) -> None:
        self.notas: dict[str, NotaMusical] = dict()

    def caregar_notas(self) -> NoneType:
        self.notas = {
            'Dó': Do(),
            'Ré': Re(),
            'Mi': Mi(),
            'Fá': Fa(),
            'Sol': Sol(),
            'Lá': La(),
            'Si': Si()
        }

    def get_nota(self, nota: str) -> NotaMusical:
        return self.notas.get(nota).clone()
```

Está clase contem 2 metodos, carregar_notas e get_nota:
- carregar_notas: Somente carrega as notas em um dicionario.
- get_notas: Recebe uma string de qual nota irá ser requerida no momento, e retorna a instância dela chamando o metodo clone que somente retorna ela mesma.
  
Com isto, nosso App ficaria desta forma:

```python
from partitura import Partitura


class App:
    def __init__(self) -> None:
        self.partitura = Partitura()

        self.partitura.caregar_notas()

        self.partitura.get_nota('Dó').desenhar()
        self.partitura.get_nota('Ré').desenhar()
        self.partitura.get_nota('Mi').desenhar()
        self.partitura.get_nota('Fá').desenhar()
        self.partitura.get_nota('Fá').desenhar()
        self.partitura.get_nota('Fá').desenhar()
        self.partitura.get_nota('Dó').desenhar()
        self.partitura.get_nota('Ré').desenhar()
        self.partitura.get_nota('Dó').desenhar()
        self.partitura.get_nota('Ré').desenhar()
        self.partitura.get_nota('Ré').desenhar()
        self.partitura.get_nota('Ré').desenhar()


if __name__ == '__main__':
    App()
```

Aonde é instanciado a Partitura, e atravês dela é gerado as instâncias das notas que nela já são incluidas.

Este padrão é utilizado principalmente em jogos, aonde é necessario criar-se vários clones de um mesmo objeto.
