import sqlite3

class BaseDeDonnees():
    "Base de données pour stocker ma table qui contient toutes mes mesures prises"
    
    def __init__(self, dataBase):
        self.dataBase = dataBase
        
    def create_table(self):
        self.connexion = sqlite3.connect(self.dataBase)
        
        # création d'un curseur
        cur = self.connexion.cursor()
        
        # exécution du selection existance de la table sur le curseur
        cur.execute("""SELECT count(name) FROM sqlite_master
                        WHERE type='table' AND name='MESURES'""")
                
        # vérifier si la table existe
        if cur.fetchone()[0] == 1:
            print("La table existe déjà.")
        else:
            tableMesures = """CREATE TABLE MESURES (
                                    ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                    DATE_MESURE TEXT NOT NULL,
                                    TYPE TEXT NOT NULL,
                                    DATA FLOAT NOT NULL);"""
            print("Création de la table")
            
            # créer la table MESURES     
            self.connexion.execute(tableMesures)

        cur.close()
        
        # fermer la base de données        
        self.connexion.close()
    
    def insertInto_table(self, date, description, donnees):
        try :  
            self.connexion = sqlite3.connect(self.dataBase)
                      
            # création d'un curseur
            cur = self.connexion.cursor()
            
            # paramètres
            sql_param =""" INSERT INTO MESURES (DATE_MESURE, TYPE, DATA) VALUES (?,?,?)"""
            data_param = (date, description, donnees)
            
            # exécution de la requêtre d'insertion
            cur.execute(sql_param, data_param)
            
            # sauvegarde des données
            self.connexion.commit()
            print("Enregistrements ajoutés dans la table.")
            
            # fermeture du curseur
            cur.close()
        
        except sqlite3.Error as error:
            print("Erreur de connexion à la base de données", error)
        finally:
            # fermer la base de données
            if self.connexion:
                self.connexion.close()
                