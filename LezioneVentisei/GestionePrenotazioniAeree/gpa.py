#Riccardo Giacalone

from abc import ABC, abstractmethod

class Volo(ABC):

    def __init__(self,codice_volo:str,posti_max:int) -> None:
        super().__init__()
        self.prenotazioni: int = 0
        self.codice_volo:str = codice_volo
        self.posti_max: int = posti_max

    @abstractmethod
    def prenota_posto(self):
        pass

    @abstractmethod
    def posti_disponibili(self):
        pass


class VoloCommerciale(Volo):

    def __init__(self, codice_volo: str, posti_max: int) -> None:
        super().__init__(codice_volo, posti_max)
        self.posti_economica: int = (self.posti_max*70) // 100
        self.posti_business: int = (self.posti_max*20) // 100
        self.posti_prima:int = (self.posti_max*10) // 100

        self.prenotazioni_economica:int = 0
        self.prenotazioni_business:int = 0
        self.prenotazioni_prima:int = 0

        self.prenotati: dict[str:int] = {}

        self.prenotati["economica"] = 0
        self.prenotati["business"] = 0
        self.prenotati["prima"] = 0
        
    

    def posti_disponibili(self)->dict[str:int]:
        
        posti_d:dict[str:int] = {}

        posti_d["disponibili"] = self.posti_max
        posti_d["economica"] = self.posti_economica
        posti_d["business"] = self.posti_business
        posti_d["prima"] = self.posti_prima

        return posti_d
        
    def prenota_posto(self,posti:int,classe_servizio:str):

        if classe_servizio in self.posti_disponibili():
            if self.prenotati[classe_servizio] <= self.posti_disponibili[classe_servizio] and (self.prenotati[classe_servizio] + posti) <= self.posti_disponibili[classe_servizio]:
              self.posti_disponibili[classe_servizio] -= posti
              self.posti_disponibili["disponibili"] -= posti
              self.prenotati[classe_servizio] += posti
              print(f"{posti} posti sono stati riservati sul volo {self.codice_volo}")
              self.prenotazioni += posti

            else:
                print(f"Errore, posti non disponibili in {classe_servizio}")
        else:
            print(f"Errore,classe non esistente.")


        