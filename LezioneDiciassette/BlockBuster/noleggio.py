#Riccardo Giacalone

from film import Film

class Noleggio:

    def __init__(self, film_list:list[Film]):
        self.film_list: list[Film] = film_list
        self.rented_film: dict = {}

    def isAvaible(self, film:Film):
        if film in self.film_list:
            print(f"Il film scelto è disponibile: {film.title}!")
            return True
        else:
            print(f"Il film scelto non è disponibile: {film.title}!")
            return False

    def rentAMovie(self,film:Film,clientID:str):
        if self.isAvaible(film):
            self.film_list.remove(film)
            if clientID not in self.rented_film:
                self.rented_film[clientID] = []
            self.rented_film[clientID].append(film)
            print(f"Il cliente {clientID} ha noleggiato {film.title}!")
        else:
            print(f"Non è possibile noleggiare il film {film.title}!")

    