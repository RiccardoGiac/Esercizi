class Banca:

    def __init__(self,nome:str, simbolo:str) -> None:
        self.nome: str = nome
        self.simbolo: str = simbolo
        self.lista_filiali : list[Filiale] = []

class Filiale:

    filiali_create = 0

    def __init__(self,codice:str,indirizzo:str,banca:Banca) -> None:
        
        self.codice = codice
        self.indirizzo = indirizzo
        self.banca = 
        
        Filiale.filiali_create += 1

    classmethod
    def totale_filiali_create(cls)-> int:
        return cls.filiali_create

unicredit: Banca = Banca("Unicredit", "UCG")
intesa: Banca = Banca("Intesa San Paolo", "ISP")
filiale_unicredit_1:Filiale = Filiale("UCG01","Via Sierra Nevada 60,Roma,Italia",unicredit)

print(filiale_unicredit_1.banca.nome)#cosi printa il nome unicredit
print(filiale_unicredit_1.banca) # così printa dove è pos in memoria l'oggetto

