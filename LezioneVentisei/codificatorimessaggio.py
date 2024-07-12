#Riccardo Giacalone

from abc import ABC, abstractmethod

class CodificatoreMessaggio(ABC):

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def codifica(self, testoInChiaro: str):
            pass

class DecodificatoreMessaggio(ABC):

    def __init__(self) -> None:
        super().__init__()

    def decodifica(self,testoCodificato:str):
        pass

class CifratoreAScorrimento(CodificatoreMessaggio,DecodificatoreMessaggio):

    def __init__(self,chiave:int) -> None:
        super().__init__()
        self.chiave:int = chiave

    def codifica(self, testoInChiaro: str):
        alfabeto: str = "abcdefghijklmnopqrstuvwxyz"
        alfabeto = list(alfabeto)
        letteraind: int = 0
        t_cod:list[str] = []

        for c in testoInChiaro:
            if c in alfabeto:
                letteraind = alfabeto.index(c)
            i: int = 0
            while i < self.chiave:
                alfabeto.append(alfabeto.pop(0))
                i += 1
            t_cod.append(alfabeto[letteraind]) 
        
        t_cod = "".join(t_cod)
        return t_cod
    
    def decodifica(self, testoCodificato: str):
        alfabeto: str = "abcdefghijklmnopqrstuvwxyz"
        alfabeto = list(alfabeto)
        letteraind:int = 0
        t_cod:list[str] = []

        for c in testoCodificato:
            if c in alfabeto:
                letteraind = alfabeto.index(c)
            




        

    

ci:CifratoreAScorrimento = CifratoreAScorrimento(3)
print(ci.codifica(testoInChiaro="xyz"))
                              

                     
              