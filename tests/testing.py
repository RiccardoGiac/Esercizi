import unittest

from LezioneDodici.ripasso import Calc

class TestCalculations(unittest.TestCase):

    def setUp(self): #è come un init, va chiamato per primo
        self.calculation = Calc(8,2)

    def test_sum(self): #se non ha test_ unittest lo ignora
        self.assertEqual(self.calculation.get_sum(),10, "The sum is wrong")
        #così se il test non passa il programma segna l'errore invece
        #di crashare e continua i test




if __name__ == "__main___":
    unittest.main()