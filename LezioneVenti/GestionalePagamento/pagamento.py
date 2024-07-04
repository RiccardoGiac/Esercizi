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
        print(f"Pagamento in contanti di: €{self.importo:.2f}")

    def inPezziDa(self):
        
        self.banconote: list = [500.0,200.0,100.0,50.0,20.0,10.0,5.0]
        self.monete: list = [2.0,1.0,0.5,0.2,0.1,0.05,0.02,0.01]
        d_soldi: dict = {}

        for e in self.banconote:
            count: int = 0
            while self.importo >= e:
                self.importo = self.importo - e
                count += 1
            d_soldi[e] = count

        for e in self.monete:
            count: int = 0
            while self.importo >= e:
                self.importo = self.importo - e
                count += 1
            d_soldi[e] = count    

        for k in d_soldi:

            if d_soldi[k] == 0:
                continue
            elif k >= 5:
                print(f"{d_soldi[k]} banconota/e da {k:.2f} euro")
            else:
                print(f"{d_soldi[k]} moneta/e da {k:.2f} euro")

                
class PagamentoCartaDiCredito(Pagamento):

    def __init__(self, importo:float,nome_cognome:str,data_scad:str,n_carta:int) -> None:
        super().__init__()
        self.importo = importo
        self.nome_cognome = nome_cognome
        self.data_scad = data_scad
        self.n_carta = n_carta

    def dettagli_pagamento(self):
        return (f"Pagamento di: €{self.importo} effettuato con la carta di credito\n"
                f"Nome sulla carta: {self.nome_cognome}\n"
                f"Data di scadenza: {self.data_scad}\n"
                f"Numero della carta: {self.n_carta}")


##TESTS##

pc:PagamentoContanti=PagamentoContanti(1352.02)
pc.inPezziDa()

pcdc:PagamentoCartaDiCredito=PagamentoCartaDiCredito(44.23,"Riccardo",
                                                     "23/12/25","4245235324523")

print(pcdc.dettagli_pagamento())