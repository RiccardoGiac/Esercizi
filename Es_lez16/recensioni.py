#Riccardo Giacalone

class Media:

    def __init__(self, title: str, reviews: list[int]=[]) -> None:
        self.title: str = title
        self.reviews: list[int] = reviews

    def set_title(self, title: str):
        self.title = title

    def get_title(self)-> str:
        return self.title
    
    def aggiungiValutazione(self, voto: int):
        if voto >= 1 and voto <= 5:
            self.reviews.append(voto)
    
    def getMedia(self)-> float:
        rev_sum: int = 0
        for v in self.reviews:
            rev_sum += v
        return rev_sum / len(self.reviews)
    
    def getRate(self)-> str:
      if self.getMedia() == 5:
          return "Grandioso"
      elif self.getMedia() < 5 and self.getMedia() >= 4:
          return "Bello"
      elif self.getMedia() < 4 and self.getMedia() >= 3:
          return "Normale"
      elif self.getMedia() < 3 and self.getMedia() >= 2:
          return "Brutto"
      elif self.getMedia() < 2 and self.getMedia() >= 1:
          return "Terribile"
      
    def ratePercentage(self,voto: int):
        res_percent: float = 0
        if voto in self.reviews:
           res_percent = self.reviews.count(voto)
           res_percent = (res_percent * 100) / len(self.reviews)
           return res_percent
        
    def recensione(self):
        print(f"{self.title}\nVoto Medio: {self.getMedia()}\nGiudizio: {self.getRate()}\nTerribile: {self.ratePercentage(1)}\nBrutto: {self.ratePercentage(2)}\nNormale: {self.ratePercentage(3)}\nBello: {self.ratePercentage(4)}\nGrandioso: {self.ratePercentage(5)}")


class Film(Media):

    def __init__(self, title: str, reviews: list[int] = []) -> None:
        super().__init__(title, reviews)


######TESTS######

film1: Film = Film(title="Avatar",reviews=[5,4,4,5,5,4,3,5,4,3])
film1.recensione()

print("------------")

film2: Film = Film(title="ClassicoCinepanettone", reviews=[1,2,2,1,3,3,5,1,2,1])
film2.recensione()