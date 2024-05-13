class Animal:

    def __init__(self,nome, specie, eta) -> None:
        self.specie : str = specie
        self.eta : int = eta
        self.nome: str = nome

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(nome = {self.nome}, specie= {self.specie}, eta = {self.eta}"
    
    def speak():
        pass

class Person(Animal):

    def __init__(self, specie, eta, nome : str, cognome : str, cf : str) -> None:
        super().__init__(specie, eta) # si può mettere anche ("homo sapiens", eta) togliendo specie dall'init sopra e sotto
        self.nome : str = nome
        self.cognome : str = cognome
        self.cf : str = cf

    def __str__(self) -> str:
        return super().__str__() + f"cf = {self.cf} cognome = {self.cognome}"

    def speak(self):
        return f"Ciao mi chiamo {self.nome}"

class Cat(Animal):

    def __init__(self, eta, nome : str) -> None:
        super().__init__("Felidae", eta)
        self.nome : str = nome
    
    def speak(self):
        return f"Meow"

class Rabbit(Animal):

    def __init__(self, eta, nome : str) -> None:
        super().__init__("Leporidae", eta)
        self.nome : str = nome



class Student(Person):

    def __init__(self, nome:str, cognome:str, cf: str, matricola : str) -> None:
        super().__init__(nome, cognome, cf)
        self.matricola : str = matricola