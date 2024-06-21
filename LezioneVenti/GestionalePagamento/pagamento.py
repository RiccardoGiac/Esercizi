#Riccardo Giacalone

class Pagamento:

    def __init__(self) -> None:
        pass

    def getImporto(self)-> float:
        return self.importo
    
    def setImporto(self,importo:float):
        self.importo = importo

    def dettagliPagamento(self):
        print(f"Importo del pagamento è : €{self.importo:.2f}")


class PagamentoContanti(Pagamento):

    def __init__(self, importo:float) -> None:
        super().__init__()
        self.importo = importo

    def dettagliPagamento(self):
        print(f"Importo del pagamento in contanti è: €{self.importo:.2f}")

    def inPezziDa(self):
        
