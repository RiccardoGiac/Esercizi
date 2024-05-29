from abc import ABC, abstractmethod

class AbcAnimal(ABC):

    @abstractmethod
    def verso():
        pass

class Cane(AbcAnimal):

    def __init__(self, nome: str) -> None:
        super().__init__()
       
        self.velocita: float = 10.0
        self.nome = nome
    
    def verso(self):
        return print("bau")
    
    def movimento(self,t:int):
        return self.velocita * t

cane_1: Cane = Cane(nome= "Pluto")


class Gatto(AbcAnimal):

    def __init__(self, nome: str) -> None:
        super().__init__()

        self.nome = nome

    def verso(self):
        return print("miao")
    
gatto_1: Gatto = Gatto(nome = "Garfield")

gatto_1.verso()
cane_1.verso()
print(cane_1.movimento(t=10))


