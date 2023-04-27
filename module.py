class Distance ():
    "L'objet distance comprend les informations sur une distance à prise à par le capteur de distance."
    
    def __init__(self, dateHeureMesure, description, dataMesure):
        self.dateHeureMesure = dateHeureMesure
        self.description = description
        self.dataMesure = dataMesure
        
    def __repr__(self):
        return f'"{self.dateHeureMesure}","{self.description}"'
    
    def afficherMesure(self):
        affichage_date = "Date et l'heure de mesure: " + self.dateHeureMesure + "\r\n"
        affichage_description = "Description: " + self.description + "\r\n"
        affichage_dataMesure = "Données de mesure: " + self.dataMesure
        
        return affichage_date + affichage_description + affichage_dataMesure
    
class Angle():
    "L'objet distance comprend les informations sur un angle pris par le servomoteur."
    
    def __init__(self, dateHeureMesure, description, dataMesure):
        self.dateHeureMesure = dateHeureMesure
        self.description = description
        self.dataMesure = dataMesure
        
    def __repr__(self):
        return f'"{self.dateHeureMesure}","{self.description}"'
    
    def afficherMesure(self):
        affichage_date = "Date et l'heure de mesure: " + self.dateHeureMesure + "\r\n"
        affichage_description = "Description: " + self.description + "\r\n"
        affichage_dataMesure = "Données de mesure: " + self.dataMesure
        
        return affichage_date + affichage_description + affichage_dataMesure