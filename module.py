class Mesure ():
    "L'objet Mesure comprend les informations sur une mesure prise à partir d'un capteur de mesure(capteur de distance ou servomoteur)."
    
    def __init__(self, dateHeureMesure, dataMesure, type):
        self.dateHeureMesure = dateHeureMesure
        self.dataMesure = dataMesure
        self.type = type
        
    def __repr__(self):
        return f'"{self.dateHeureMesure}","{self.type}"'
    
    def afficherMesure(self):
        affichage_date = "Date et l'heure de mesure: " + str(self.dateHeureMesure) + "\r\n"
        affichage_dataMesure = "Données de mesure: " + str(self.dataMesure) + "\r\n"
        affichage_type = "Type de la mesure: " + self.type # peut-être «distance» ou «angle»
        
        return affichage_date + affichage_dataMesure + affichage_type