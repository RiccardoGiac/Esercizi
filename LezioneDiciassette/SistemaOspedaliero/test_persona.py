#Riccardo Giacalone

import unittest

from dottore import Dottore
from fatture import Fattura
from paziente import Paziente
from persona import Persona

class TestPersona(unittest.TestCase):

    def setUp(self) -> None:
        
        self.p1: Persona = Persona(first_name="Giovanni",last_name="Giorgio")
        self.p1.age = 31

    def test_attributi(self):

        self.assertEqual(self.p1.getName(),"Giovanni","Errore nel nome")
        self.assertEqual(self.p1.getLastname(),"Giorgio","Errore nel cognome")
        self.assertEqual(self.p1.getAge(),31, "Errore nell'eta")

    def test_cambioAttributi(self):
        
        self.p1.setName("Paolo")
        self.assertEqual(self.p1.getName(),"Paolo","Errore nel cambio nome")
        self.p1.setLastName("Rossi")
        self.assertEqual(self.p1.getLastname(),"Rossi","Errore nel cambio cognome")
        self.p1.setAge(20)
        self.assertEqual(self.p1.getAge(),20,"Errore nel cambio eta")


class TestDottore(unittest.TestCase):

    def setUp(self) -> None:

        self.d1: Dottore = Dottore(first_name="Giorgio",last_name="Giovanni",
                                   specialization="QuelloChePassaIlBisturi",parcel=150.0)
    
    def test_attributi(self):

        self.assertEqual(self.d1.getName(),"Giorgio","Errore nel nome del Dottore")
        self.assertEqual(self.d1.getLastname(),"Giovanni","Errore nel cognome del Dottore")
        self.assertEqual(self.d1.getAge(),31,"Errore nell'eta del Dottore")
        self.assertEqual(self.d1.getParcel(), 150.0,"Errore nella parcella del dottore")
    
    def test_validDoctor(self):

        self.d1.age = 31
        self.assertEqual(self.d1.isAValidDoctor())
        self.d1.age = 20
        self.assertEqual(self.d1.isAValidDoctor())


class TestPaziente(unittest.TestCase):

    def setUp(self) -> None:

        self.pa1: Paziente = Paziente(first_name="Carlo",last_name="Carlini",
                                      id_code="24A")

    def test_attributi(self):
        
        self.pa1.age = 20
        self.assertEqual(self.pa1.getName(),"Carlo","Errore nel nome del Dottore")
        self.assertEqual(self.pa1.getLastname(),"Carlini","Errore nel cognome del Dottore")
        self.assertEqual(self.pa1.getAge(),20)
        self.assertEqual(self.pa1.getIdCode(),"24A")   

class TestFattura(unittest.TestCase):

    def setUp(self) -> None:
        
        self.d: Dottore = Dottore("Giorgio","Rossi","Cardiologo",150.0)
        self.d.setAge(55)
        self.p: list[Paziente] = [Paziente(first_name="Giovanni",
                                                  last_name="Verdi",
                                                  id_code="33B",),
                                         Paziente(first_name="Rosaria",
                                                  last_name="Franchi",
                                                  id_code="22A")]
        self.f: Fattura = Fattura(self.p,self.d)

    def test_attributi(self):
        
        self.assertEqual(self.f.fatture,2)
        self.assertEqual(self.f.getSalary(),300.0)

    def test_add_patient(self):

        paziente: Paziente = Paziente("Luca","Nervi","LL4")
        self.f.addPatient(paziente)
        self.assertEqual(self.f.getFatture(),3)
        self.assertEqual(self.f.getSalary(),450.0)

    def test_remove_patient(self):

        self.f.removePatient("22A")
        self.assertEqual(self.f.getFatture(),1)
        self.assertEqual(self.f.getSalary(),150.0)
        
                                                        
        



if __name__ == "__main__":
    unittest.main()   
