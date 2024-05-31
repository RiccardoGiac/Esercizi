#Riccardo Giacalone

class Libro:

    def __init__(self,titolo:str, autore:str, prestito:bool = False) -> None:
        self.titolo: str = titolo
        self.autore: str = autore
        self.prestito: bool = prestito


class Biblioteca:

    def __init__(self,lista_libri: list[Libro] = []) -> None:
        self.lista_libri:list[Libro] = lista_libri

    def aggiungi_libro(self,libro:Libro):
        self.lista_libri.append(libro)
        print("Libro aggiunto alla biblioteca.")

    def presta_libro(self,titolo:str):
        for libro in self.lista_libri:
            if libro.titolo == titolo and libro.prestito == False:
                libro.prestito = True
                print(f"Il libro {titolo} è stato preso in prestito.")
            elif libro.titolo != titolo:
                continue
            else:
                print(f"Il libro {titolo} non è disponibile per il prestito")

    def restituisci_libro(self,titolo:str):
        for libro in self.lista_libri:
            if libro.titolo == titolo and libro.prestito == True:
                libro.prestito = False
                print(f"Il libro {titolo} è stato restituito.")
            elif libro.titolo != titolo:
                continue
            else:
                print(f"Errore, libro non trovato.")

    def mostra_libri_disponibili(self):
        print("Ecco la lista di libri disponibili:\n")
        for libro in self.lista_libri:
            if libro.prestito == False:
                print(libro.titolo)
            elif libro.prestito == True:
                continue
            else:
                print("Non ci sono libri disponibili.")

libro1: Libro = Libro("Divina Commedia","Dante Alighieri",prestito=False)
libro2: Libro = Libro("Promessi sposi","Alessandro Manzoni", prestito=False)
bbt1:Biblioteca = Biblioteca()
bbt1.aggiungi_libro(libro2)
bbt1.aggiungi_libro(libro1)
bbt1.mostra_libri_disponibili()
bbt1.presta_libro("Divina Commedia")
bbt1.mostra_libri_disponibili()
bbt1.restituisci_libro("Divina Commedia")
bbt1.mostra_libri_disponibili()



