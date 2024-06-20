#Riccardo Giacalone

from film import Film

class Azione(Film):

    def __init__(self, id: int, title: str) -> None:
        super().__init__(id, title)
        self.genere: str = "Azione"
        self.penale: float = 3.0
    
    def getGenere(self)-> str:
        return self.genere
    def getPenale(self)-> float:
        return self.penale
    
    def calcolaPenaleRitardo(self,giorni:float):
        return self.penale * giorni
    
class Commedia(Film):

    def __init__(self, id: int, title: str) -> None:
        super().__init__(id, title)
        self.genere: str = "Commedia"
        self.penale: float = 2.50
    
    def getGenere(self)-> str:
        return self.genere
    def getPenale(self)-> float:
        return self.penale
    
    def calcolaPenaleRitardo(self,giorni:float):
        return self.penale * giorni
    
class Drama(Film):

    def __init__(self, id: int, title: str) -> None:
        super().__init__(id, title)
        self.genere: str = "Drama"
        self.penale: float = 2.0
    
    def getGenere(self)-> str:
        return self.genere
    def getPenale(self)-> float:
        return self.penale
    
    def calcolaPenaleRitardo(self,giorni:float):
        return self.penale * giorni