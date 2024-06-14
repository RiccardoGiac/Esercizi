#Riccardo Giacalone

from persona import Persona

class Paziente(Persona):

    def __init__(self, first_name: str, last_name: str,id_code:str) -> None:
        super().__init__(first_name, last_name)

        self.id_code:str = id_code

    
    def setIdCode(self,idCode):
        self.id_code = idCode
    
    def getIdCode(self)-> str:
        return self.id_code
    
    def patient_info(self):
        print(f"Paziente: {self.first_name} {self.last_name}\nID:{self.id_code}")



