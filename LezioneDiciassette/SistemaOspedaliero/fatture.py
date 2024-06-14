#Riccardo Giacalone
from dottore import Dottore
from paziente import Paziente

class Fattura:

    def __init__(self, patient:list[Paziente],doctor:Dottore) -> None:

        
        if doctor.isAValidDoctor():
            self.patient: list[Paziente] = patient
            self.doctor: Dottore = doctor
            self.fatture: int = len(patient)
            self.salary:int = 0
        else:
            self.patient = None
            self.doctor = None
            self.fatture = None
            self.salary = None
            print("Impossibile creare la classe fattura poichè il dottore non è valido")

    def getSalary(self)-> float:
        return self.doctor.parcel * len(self.patient)
    
    def getFatture(self)->int:
        self.fatture = len(self.patient)
        return self.fatture
    
    def addPatient(self,newPatient:Paziente):
        self.patient.append(newPatient)
        self.getFatture()
        self.getSalary()
        print(f"Alla lista del dottor {self.doctor.last_name} è stato aggiunto il paziente {newPatient.id_code}")

    def removePatient(self,idCode):
        if self.patient:
            for patient in self.patient:
                if patient.id_code == idCode:
                    self.patient.remove(patient)
                    self.getFatture()
                    self.getSalary()
                    print(f"Alla lista del Dottor {self.doctor.last_name} è stato rimosso il paziente {idCode}")
        else:
            print(f"Errore, lista di pazienti vuota")






