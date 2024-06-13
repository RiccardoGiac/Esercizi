class Specie:
    popolazione: int = 0

    def __init__(self, nome:str, tasso_crescita:float) -> None:
        self.nome: str = nome
        
        self.tasso_crescita: float = tasso_crescita

    def cresci(self):
        popolazione_nuova: int = self.popolazione *(1 + self.tasso_crescita//100)
        self.popolazione = popolazione_nuova

    def anni_per_superare(self,altra_specie: "Specie")-> int:
        c: int = 0
        while self.popolazione < altra_specie.popolazione:
            self.popolazione * self.tasso_crescita // 100
            altra_specie.popolazione * altra_specie.tasso_crescita // 100

        return c

    def getDensita(self,area_kmq: float) -> int:
        d: int = Specie.popolazione // area_kmq
        c: int = 0
        while d < 1:
            d = Specie.popolazione // area_kmq
            c += 1
        return c

            
    
class BufaloKlingon(Specie):


    def __init__(self, nome: str, tasso_crescita: float) -> None:
        super().__init__(nome, tasso_crescita)



class Elefante(Specie):

    def __init__(self, nome: str, tasso_crescita: float) -> None:
        super().__init__(nome, tasso_crescita)



            

# Creazione delle istanze delle specie
bufalo_klingon = BufaloKlingon(100, 15)  # Crea un'istanza di BufaloKlingon con popolazione 100 e tasso di crescita 15%
elefante = Elefante(10, 35)  # Crea un'istanza di Elefante con popolazione 10 e tasso di crescita 35%

# Calcolo degli anni necessari per superare
anni_necessari = elefante.anni_per_superare(bufalo_klingon)  # Calcola gli anni necessari affinché gli elefanti superino i bufali Klingon
print(f"Anni necessari perché la popolazione di elefanti superi quella dei bufali Klingon: {anni_necessari}")

# Calcolo della densità di popolazione per i Bufali Klingon
anni_densita = bufalo_klingon.getDensita(1500)  # Calcola gli anni necessari per raggiungere una densità di 1 bufalo Klingon per km²
print(f"Anni necessari per raggiungere una densità di 1 Bufalo Klingon per km quadrato: {anni_densita}")

        
    