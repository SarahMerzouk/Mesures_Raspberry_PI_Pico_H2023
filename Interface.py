from time import sleep
from tkinter import ttk
import tkinter as tk
import serial
import datetime
from module import Mesure
from BaseDeDonnees import BaseDeDonnees

# ouvrir le port serie pour le connexion
s = serial.Serial("COM3")

class Interface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Merzouk Sarah _ TP-Synthèse")
        self.geometry("400x250")
        
        # label pour afficher le titre de la page
        self.lbl_titre = tk.Label(self, text="Système de captation de mesures (Distance / Agle)", fg="blue", height=3, font=('Helvetica', 10))
        self.lbl_titre.pack()
        
        # bouton pour démarrer le système de captation de distance et d'angle
        self.btn_demarrer = tk.Button(self, text="Démarrer le système de captation", width = 30)
        self.btn_demarrer["command"] = self.btn_demarrerCaptation_click
        self.btn_demarrer.pack()
        
        # label pour afficher qu'il faut choisir une mesure
        self.lbl_choixMesure = tk.Label(self, text="Veuillez choisir ce que vous voulez mesurer:")
        self.lbl_choixMesure.pack()
        
        # boutons radio pour choisir si on veut mesurer la distance ou l'angle (inactif au début)
        self.rbtn_var = tk.IntVar()
        self.typeMesure = "distance"
        
        self.btnRadio_distance = tk.Radiobutton(self, 
               text="Mesurer la distance",
               padx = 20, 
               variable= self.rbtn_var, 
               value=1,
               state="disabled")
        self.btnRadio_distance["command"] = self.rbtn_mesurerDistance_click
        self.btnRadio_distance.pack()
        
        self.btnRadio_angle = tk.Radiobutton(self, 
               text="Mesurer l'angle",
               padx = 20, 
               variable=self.rbtn_var, 
               value=2,
               state="disabled")
        self.btnRadio_angle["command"] = self.rbtn_mesurerAngle_click
        self.btnRadio_angle.pack()
        self.rbtn_var.set(1)
        
        # bouton pour prendre la mesure (inactif au début)
        self.btn_mesurer = tk.Button(self, text="Prendre la mesure", width = 30, state="disabled")
        self.btn_mesurer["command"] = self.btn_prendreMesure_click
        self.btn_mesurer.pack()
        
        # bouton pour arrêter tout
        self.btn_arreter = tk.Button(self, text="Arrêter", width = 30)
        self.btn_arreter["command"] = self.btn_arreter_click
        self.btn_arreter.pack()
        
        # une étiquette qui affiche si le système de captation est activé ou désactivé
        self.lbl_etat_systeme = tk.Label(self, text="DÉSACTIVÉ", fg="red")
        self.lbl_etat_systeme.pack(side="bottom")
        
    def btn_demarrerCaptation_click(self):        
        # activer mes radios boutons, mon champ description et mon bouton
        self.btnRadio_distance.config(state="active")
        self.btnRadio_angle.config(state="active")
        self.btn_mesurer.config(state="normal")
        self.lbl_etat_systeme.config(text="ACTIVÉ", fg="green")
        
    def btn_arreter_click(self):
        s.write(b"OFF\n") # on mesure la distance
        
        self.btn_demarrer.config(state="disabled")
        self.btn_mesurer.config(state="disabled")
        self.lbl_etat_systeme.config(text="DÉSACTIVÉ", fg="red")
    
    # btn radio distance    
    def rbtn_mesurerDistance_click(self):
        self.typeMesure = "distance" 
    
    # btn radio angle
    def rbtn_mesurerAngle_click(self):
        self.typeMesure = "angle"
    
    def btn_prendreMesure_click(self):
        list_mesures = [] # listes qui contient toutes les mesures
        
        if self.typeMesure == "distance":  
            s.write(b"DISTANCE\n") # on mesure la distance
        
        elif self.typeMesure == "angle":
            s.write(b"ANGLE\n") # on mesure la distance
        
        # récupérer la distance du pico
        data_in = s.readline()
        data = str(data_in)[2:-5]
        
        # création de mon objet Mesure
        mesure = Mesure(datetime.datetime.now(), data, self.typeMesure) 
        list_mesures.append(mesure)
        
        # création de ma base de données
        bd = BaseDeDonnees("mesuresBD.db") # base de données

        # créer ma table
        bd.create_table()

        # insérer mes données
        data = float(mesure.dataMesure)
        dateHeure_string = mesure.dateHeureMesure.isoformat()
        
        bd.insertInto_table(dateHeure_string, mesure.type, data)

if __name__ == "__main__":
    app = Interface()
    app.mainloop()