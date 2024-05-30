#Riccardo Giacalone
class Film:

    def __init__(self,titolo: str, durata:str) -> None:
        self.titolo: str = titolo
        self.durata: str = durata
        




class Sala:

    def __init__(self,n_sala: int, posti_tot:int,
                 posti_pren: int,film_att: Film = None) -> None:
        self.n_sala: int = n_sala
        self.film_att: Film = film_att
        self.posti_tot: int = posti_tot
        self.posti_pren: int = posti_pren
        
    def prenota_posti(self,num_posti:int):
        if self.posti_tot > num_posti:
            self.posti_pren += self.posti_tot - num_posti
            print("Prenotazione confermata")
        else:
            print("Posti non disponibili")

    def posti_disponibili(self)-> int :
        return self.posti_tot - self.posti_pren
    
class Cinema:

    def __init__(self,sale:list[Sala] = []) -> None:
        self.sale: list[Sala] = sale

    def aggiungi_sala(self,sala:Sala):
        self.sale.append(sala)
    
    def prenota_film(self,titolo_film:Film, num_posti:int):
        if self.sale:
            for s in self.sale:
                if s.posti_disponibili() >= num_posti:
                    print(f"Il film {titolo_film.titolo} è stato prenotato nella sala {s.n_sala} per {num_posti} posti.")
                else:
                    print(f"Non ci sono posti disponibili per {titolo_film.titolo}")

avatar:Film = Film("Avatar","3:00")
s1: Sala = Sala(4,200,199,film_att=avatar)
c1: Cinema = Cinema([])
c1.aggiungi_sala(s1)

c1.prenota_film(avatar,1)

        
        




