#Riccardo Giacalone

class Prodotto:

    def __init__(self, nome:str, quantita:int) -> None:
        self.nome: str = nome
        self.quantita: int = quantita



class Magazzino:

    def __init__(self) -> None:
        self.prodotti: list[Prodotto] = []
    
    def aggiungi_prodotto(self, prodotto:Prodotto):
        self.prodotti.append(prodotto)
    
    def cerca_prodotto(self,nome:str)-> Prodotto:
        for p in self.prodotti:
            if nome == p.nome:
                return p
            else:
                print(f"Il prodotto {nome} non è nell'inventario")

    def verifica_disponibilita(self,nome:str)-> str:
        for p in self.prodotti:
            if nome == p.nome:
                return p.quantita
            else:
                return "Prodotto non disponibile"

mag1:Magazzino = Magazzino()
prod1: Prodotto = Prodotto("Risma di carta",120)
mag1.aggiungi_prodotto(prod1)
print(mag1.cerca_prodotto("Risma di carta"))
print(mag1.verifica_disponibilita("Risma di carta"))
print(mag1.verifica_disponibilita("Risma di cartas"))

