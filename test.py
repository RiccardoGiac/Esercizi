class Specie:

    def __init__(self, nome:str, popolazione:int, tasso_crescita:float) -> None:
        self.nome: str = nome
        self.popolazione: int = popolazione
        self.tasso_crescita: float = tasso_crescita

    def cresci(self):
        pass

    def anni_per_superare(self,altra_specie: "Specie")-> int:
        pass

    def getDensita(self,area_kmq: float) -> int:
        pass
            
    
class BufaloKlingon(Specie):

    def __init__(self, nome: str, popolazione: int, tasso_crescita: float) -> None:
        super().__init__(nome, popolazione, tasso_crescita)



class Elefante(Specie):

    def __init__(self, nome: str, popolazione: int, tasso_crescita: float) -> None:
        super().__init__(nome, popolazione, tasso_crescita)



            



        
    