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
        
        self.banconote: list = [500.0,200.0,100.0,50.0,20.0,10.0,5.0]
        self.monete: list = [2.0,1.0,0.5,0.2,0.1,0.05,0.02,0.01]

        
        for e in self.banconote:
            while self.importo > e:
                self.importo - e
                


        
