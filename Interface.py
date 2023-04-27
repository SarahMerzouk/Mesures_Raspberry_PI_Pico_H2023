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
        self.geometry("400x330")
        
        # bouton pour démarrer le système de captation de distance et d'angle
        self.btn_demarrer = tk.Button(self, text="Démarrer le système de captation", width = 30)
        self.btn_demarrer["command"] = self.btn_demarrerCaptation_click
        self.btn_demarrer.pack()
        
        # label pour afficher qu'il faut choisir une mesure
        self.lbl_choixMesure = tk.Label(self, text="Veuillez choisir ce que vous voulez mesurer:")
        self.lbl_choixMesure.pack()
        
        # boutons radio pour choisir si on veut mesurer la distance ou l'angle (inactif au début)
        self.rbtn_var = tk.IntVar()
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

        # label pour la mesure
        self.lbl_mesure = tk.Label(self, text="Écrire si c'est la mesure d'une distance ou d'un angle:")
        self.lbl_mesure.pack()
        
        # champ texte pour saisir la description de la mesure (si c'est une distance ou un angle) (inactif au début)
        self.txt_description = tk.Text(self, width=30, height=1, state="disabled")
        self.txt_description.pack()

        # label pour afficher l'angle à envoyer au pico, si c'est une angle qu'on mesure
        self.lbl_nombreAngle = tk.Label(self, text="Angle:")
        self.lbl_nombreAngle.pack()
        
        # champ texte pour saisir l'angle, si c'est un angle qu'on mesure (inactif si on ne clique pas sur le bouton radion pour mesure l'angle)
        self.txt_angle = tk.Text(self, width=3, height=1, state="disabled")
        self.txt_angle.pack()
        
        # la listBox qui contient les mesures soit des distances, soit des angles
        self.list_mesures = tk.Listbox(self, height=5, width=40, selectmode=tk.SINGLE, selectbackground="blue")
        self.list_mesures.pack()
        self.list_mesures.bind("<<ListboxSelect>>")
        
        # bouton pour prendre la mesure (inactif au début)
        self.btn_mesurer = tk.Button(self, text="Prendre la mesure", width = 30, state="disabled")
        self.btn_mesurer["command"] = self.btn_prendreMesure_click
        self.btn_mesurer.pack()
        
        # une étiquette qui affiche si le système de captation est activé ou désactivé
        self.lbl_etat_systeme = tk.Label(self, text="DÉSACTIVÉ", fg="red")
        self.lbl_etat_systeme.pack(side="bottom")
        
    def btn_demarrerCaptation_click(self):
        
        # activer mes radios boutons, mon champ description et mon bouton
        self.btnRadio_distance.config(state="active")
        self.btnRadio_angle.config(state="active")
        self.txt_description.config(state="normal")
        self.btn_mesurer.config(state="active")
        self.lbl_etat_systeme.config(text="ACTIVÉ", fg="green")
    
    def rbtn_mesurerDistance_click(self):
        pass
           
    def rbtn_mesurerAngle_click(zelf):
        pass
    
    def btn_prendreMesure_click(self):
        pass
    
if __name__ == "__main__":
    app = Interface()
    app.mainloop()
