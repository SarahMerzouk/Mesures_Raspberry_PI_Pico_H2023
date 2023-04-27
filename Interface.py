from time import sleep
from tkinter import ttk
import tkinter as tk
import serial
import datetime

# ouvrir le port serie pour le connexion
#s = serial.Serial("COM3")

class Interface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Merzouk Sarah _ TP_Synthèse")
        self.geometry("400x400")
        
        # bouton pour démarrer le système de captation de distance et d'angle
        self.btn_demarrer = tk.Button(self, text="Démarrer le système de captation", width = 30)
        self.btn_demarrer["command"] = self.btn_demarrerCaptation_click
        self.btn_demarrer.pack()
        
        # label pour afficher qu'il faut choisir une mesure
        self.lbl_choixMesure = tk.Label(self, text="Veuillez choisir ce que vous voulez mesurer:")
        self.lbl_choixMesure.pack()
        # boutons radio pour choisir si on veut mesurer la distance ou l'angle
        rbtn_var = tk.IntVar()
        self.btnRadio_distance = tk.Radiobutton(self, 
               text="Mesurer la distance",
               padx = 20, 
               variable= rbtn_var, 
               value=1)
        self.btnRadio_distance["command"] = self.rbtn_mesurerDistance_click
        self.btnRadio_distance.pack()
        
        self.btnRadio_angle = tk.Radiobutton(self, 
               text="Mesurer l'angle",
               padx = 20, 
               variable=rbtn_var, 
               value=2)
        self.btnRadio_angle["command"] = self.rbtn_mesurerAngle_click
        self.btnRadio_angle.pack()
        
    def btn_demarrerCaptation_click(self):
        pass
    
    def rbtn_mesurerDistance_click(self):
        pass
           
    def rbtn_mesurerAngle_click(zelf):
        pass
    
if __name__ == "__main__":
    app = Interface()
    app.mainloop()
