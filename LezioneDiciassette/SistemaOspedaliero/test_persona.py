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
                                   specialization="QuelloChePassaIlBisturi",parcel=150.00)
    
    def test_attributi(self):

        self.assertEqual(self.d1.getName(),"Giorgio","Errore nel nome del Dottore")
        self.assertEqual(self.d1.getLastname(),"Giovanni","Errore nel cognome del Dottore")
        self.assertEqual(self.d1.getAge(),31,"Errore nell'eta del Dottore")
        
    def test_validDoctor(self):

        self.d1.age = 31
        self.assertEqual(self.d1.isAValidDoctor(),print(f"Doctor {self.d1.first_name} {self.d1.last_name} is valid!"),"Errore nella validità del dottore")
        self.d1.age = 20
        self.assertEqual(self.d1.isAValidDoctor(),print(f"Doctor {self.d1.first_name} {self.d1.last_name} is not valid!"),"Errore nella validità del dottore")






if __name__ == "__main__":
    unittest.main()   
