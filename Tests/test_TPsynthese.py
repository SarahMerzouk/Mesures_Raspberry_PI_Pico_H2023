import unittest
from BaseDeDonnees import BaseDeDonnees
from module import Mesure
import datetime

class test_TesterTPsynthese(unittest.TestCase):
    
    # tester si les deux objets sont du même type
    def test_creerObjetMesure(self):
        mesure1 = Mesure(datetime.datetime.now(), 20, "distance")
        mesure2 = Mesure(datetime.datetime.now(), 20, "angle")

        self.assertNotEqual(mesure1, mesure2)
    
    # tester si la base de données existe
    def test_creerUneBaseDeDonnes(self):
        base = BaseDeDonnees("mesuresBD.db")
        
        if base.dataBase == "mesuresBD.db" :
            existe = True
        else :
            existe = False
        
        self.assertTrue(existe)
        
if __name__ == "__name__":
    unittest.main()