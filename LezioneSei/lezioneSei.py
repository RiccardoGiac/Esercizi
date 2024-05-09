from typing import Any


class Person:

    def __init__(self,name :str,surname:str,date_of_birth: str,gender:str) -> None:
        
        self.name: str = name
        self.surname: str = surname
        self.date_of_birth: str = date_of_birth
        self.gender: str = gender
        #self.codice_fiscale: str = codice_fiscale

    def calcola_eta(self) -> int:

        return 10
    
    #def __eq__(self, value: object) -> bool:
        #return value.codice_fiscale == self.codice_fiscale

person_1 : Person = Person(name="Flavio", 
                           surname= "Giorgi", 
                           date_of_birth="24/12/94",
                           gender="M")

class Dipendente(Person):     #Person superclasse di Dipendente

    def __init__(self, name: str, surname: str, date_of_birth: str, gender: str, ore_lavorate: int) -> None:
        super().__init__(name, surname, date_of_birth, gender)
        self.ore_lavorate: int = ore_lavorate
    
    def calcola_stipendio(self) -> float:
        return 500.0


class Professore(Dipendente):

    def __init__(self, name: str, surname: str, date_of_birth: str, gender: str, ore_lavorate: int,materia_insegnata: str,ore_di_lezione: int) -> None:
        super().__init__(name, surname, date_of_birth, gender, ore_lavorate)
       
        self.materia_insegnata: str = materia_insegnata
        self.ore_di_lezione: int = ore_di_lezione
    
    def __str__(self) -> str:
        return super().__str__()
        #return f"{self.name} ha fatto {self.ore_di_lezione} ore di lezione"
    
    #def __eq__(self, value: object) -> bool:
        #return super().__eq__(value)


professore_1: Professore = Professore(name="Flavio", 
                           surname= "Giorgi", 
                           date_of_birth="24/12/94",
                           gender="M",
                           ore_lavorate=500,
                           materia_insegnata="Python",
                           ore_di_lezione=499)

print(professore_1.ore_di_lezione)

dipendente_1: Dipendente = Dipendente(name="Flavio", 
                           surname= "Giorgi", 
                           date_of_birth="24/12/94",
                           gender="M",
                           ore_lavorate=500)

    

print(person_1.calcola_eta())

print(dipendente_1.ore_lavorate)
print(dipendente_1.name)
print(dipendente_1.calcola_eta())
print(dipendente_1.calcola_stipendio())

#__eq__ serve per testare l'esistenza di due oggetti uguali
#__eq__(person_1,person_2) -> è come scrivere person_1 == person_2
