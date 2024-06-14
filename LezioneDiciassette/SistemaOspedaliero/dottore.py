#Riccardo Giacalone

from persona import Persona

class Dottore(Persona):

    def __init__(self, first_name: str, last_name: str,specialization:str,parcel:float) -> None:
        super().__init__(first_name, last_name)
        self.parcel: float = parcel
        

        if isinstance(specialization,str):
            self.specialization: str = specialization
        else:
            self.specialization = None
            print("La specializzazione inserita non è una str")

        if isinstance(parcel,float):
            self.parcel: str = parcel
        else:
            self.parcel = None
            print("La parcella inserita non è un float")
        
    
    def setSpecialization(self,specialization):
        if isinstance(specialization,str):
            self.specialization = specialization
        else:
            print("La specializzazione inserita non è una str")

    def setParcel(self,parcel):
        if isinstance(parcel,float):
            self.parcel = parcel
        else:
            print("La parcella inserita non è un float")

    def getSpecialization(self)-> str:
        return self.specialization
    
    def getParcel(self)-> float:
        return self.parcel
    
    def isAValidDoctor(self):
        if self.age > 30:
            print(f"Doctor {self.first_name} {self.last_name} is valid!")
        else:
            print(f"Doctor {self.first_name} {self.last_name} is not valid!")
        
    def doctorGreet(self):
        self.greet()
        print(f"Sono un medico {self.specialization}")
    


