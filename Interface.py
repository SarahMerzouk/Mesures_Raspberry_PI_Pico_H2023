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
        self.geometry("400x250")
        
        # cadres
        frm_debut = tk.Frame(self)
        frm_debut.pack()
        
        frm_distance = tk.Frame(self)
        frm_distance.pack(side="left")
        
        frm_angle = tk.Frame(self)
        frm_angle.pack(side="right")
        
        # bouton pour démarrer le système de captation de distance et d'angle
        self.btn_demarrer = tk.Button(frm_debut, text="Démarrer le système de captation", width = 30)
        self.btn_demarrer["command"] = self.btn_demarrerCaptation_click
        self.btn_demarrer.pack()
        
        # label pour afficher qu'il faut choisir une mesure
        self.lbl_choixMesure = tk.Label(frm_debut, text="Veuillez choisir ce que vous voulez mesurer:")
        self.lbl_choixMesure.pack()
        
        # boutons radio pour choisir si on veut mesurer la distance ou l'angle
        rbtn_var = tk.IntVar()
        self.btnRadio_distance = tk.Radiobutton(frm_debut, 
               text="Mesurer la distance",
               padx = 20, 
               variable= rbtn_var, 
               value=1)
        self.btnRadio_distance["command"] = self.rbtn_mesurerDistance_click
        self.btnRadio_distance.pack()
        
        self.btnRadio_angle = tk.Radiobutton(frm_debut, 
               text="Mesurer l'angle",
               padx = 20, 
               variable=rbtn_var, 
               value=2)
        self.btnRadio_angle["command"] = self.rbtn_mesurerAngle_click
        self.btnRadio_angle.pack()

        # label pour la mesure de la distance
        self.lbl_distance = tk.Label(frm_distance, text="Mesurer la distance:")
        self.lbl_distance.pack()
        
        # champ texte pour saisir la description de la mesure de la distance
        self.txt_description_distance = tk.Text(frm_distance, width=15, height=1, state="disabled")
        self.txt_description_distance.pack()
        
        # label pour la mesure de l'angle
        self.lbl_angle = tk.Label(frm_angle, text="Mesurer l'angle:")
        self.lbl_angle.pack()
        
        # champ texte pour saisir la description de la mesure de l'angle
        self.txt_description_angle = tk.Text(frm_angle, width=15, height=1, state="disabled")
        self.txt_description_angle.pack()
        
        # label pour afficher l'angle à envoyer au pico
        self.lbl_nombreAngle = tk.Label(frm_angle, text="Angle:")
        self.lbl_nombreAngle.pack(side="left")
        
        # champ texte pour saisir l'angle
        self.txt_angle = tk.Text(frm_angle, width=3, height=1, state="disabled")
        self.txt_angle.pack()
        
        # la listBox qui contient les mesures soit des distances, soit des angles
        self.list_mesures = tk.Listbox(self, height=5, width=100, selectmode=tk.SINGLE, selectbackground="blue")
        self.list_mesures.pack()
        self.list_mesures.bind("<<ListboxSelect>>")
        
        # bouton pour prendre la mesure
        self.btn_mesurer = tk.Button(self, text="Prendre la mesure", width = 30, state="disabled")
        self.btn_mesurer["command"] = self.btn_prendreMesure_click
        self.btn_mesurer.pack()
        
        # une étiquette qui affiche si le système de captation est activé ou désactivé
        self.lbl_etat_systeme = tk.Label(self, text="DÉSACTIVÉ", fg="red")
        self.lbl_etat_systeme.pack(side="bottom")
        
    def btn_demarrerCaptation_click(self):
        pass
    
    def rbtn_mesurerDistance_click(self):
        pass
           
    def rbtn_mesurerAngle_click(zelf):
        pass
    
    def btn_prendreMesure_click(self):
        pass
    
if __name__ == "__main__":
    app = Interface()
    app.mainloop()
