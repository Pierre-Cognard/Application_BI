import tkinter as tk
import tkinter.font as tkFont
from threading import Thread
from dict_variables import dict_type_variables
from analyse_nombre import *
from analyse_varchar import *
import subprocess
import tempfile
from PIL import Image, ImageTk

class App:
    def __init__(self, root):
        root.title("Analyse de la base de données Foppa")
        width=800
        height=610
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        ft = tkFont.Font(family='Arial',size=10)

        # =============== FOPPA BRUTE ===============
        GLabel_659=tk.Label(root,borderwidth=1,relief="groove",font=tkFont.Font(family='Arial',size=12),text="Analyse de la base Foppa brute").place(x=50,y=10,width=300,height=30)
        label_var_indiv=tk.Label(root,borderwidth=1,relief="solid",text="Variables individuelles",font=ft).place(x=75,y=50,width=250,height=30)

        self.liste1=tk.Listbox(root,borderwidth=1,relief="solid",font=ft) # liste var indiv
        self.liste1.place(x=75,y=120,width=150,height=200)

        button1=tk.Button(root,font=ft,text="Afficher \nle graphe",command=self.button1_command) # bouton var indiv
        button1.place(x=235,y=120,width=90,height=200)

        label_pair_var=tk.Label(root,borderwidth=1,relief="solid",text="Paires de variables",font=ft).place(x=75,y=330,width=250,height=30)

        self.liste2=tk.Listbox(root,borderwidth=1,relief="solid",font=ft) # liste pair var
        self.liste2.place(x=75,y=400,width=150,height=200)

        button2=tk.Button(root,font=ft,text="Afficher \nle graphe") # bouton pair de var
        button2.place(x=235,y=400,width=90,height=200)

        # =============== FOPPA NETTOYEE ===============
        GLabel_245=tk.Label(root,borderwidth=1,relief="groove",font=tkFont.Font(family='Arial',size=12),text="Analyse de la base Foppa nettoyée").place(x=450,y=10,width=300,height=30)

        label_var_indiv2=tk.Label(root,borderwidth=1,relief="solid",text="Variables individuelles",font=ft).place(x=475,y=50,width=250,height=30)

        self.liste3=tk.Listbox(root,borderwidth=1,relief="solid",font=ft) # liste var indiv
        self.liste3.place(x=475,y=120,width=150,height=200)

        button3=tk.Button(root,font=ft,text="Afficher \nle graphe",command=self.GButton_114_command) # bouton var indiv
        button3.place(x=635,y=120,width=90,height=200)

        label_pair_var2=tk.Label(root,borderwidth=1,relief="solid",text="Paires de variables",font=ft).place(x=475,y=330,width=250,height=30)

        self.liste4=tk.Listbox(root,borderwidth=1,relief="solid",font=ft) # liste pair var
        self.liste4.place(x=475,y=400,width=150,height=200)

        button4=tk.Button(root,font=ft,text="Afficher \nle graphe") # bouton pair de var
        button4.place(x=635,y=400,width=90,height=200)
        # =============================================

        self.root = root
        self.status_label_1 = tk.Label(root, text="Prêt", font=tkFont.Font(family='Arial', size=10),)
        self.status_label_1.place(x=50, y=85, width=300, height=30) 

        self.status_label_2 = tk.Label(root, text="Prêt", font=tkFont.Font(family='Arial', size=10))
        self.status_label_2.place(x=450, y=85, width=300, height=30)

    def button1_command(self): # bouton "afficher graphes" pour variables individuelles
        variable = self.liste1.get(self.liste1.curselection())
        #print(f"Affichage de : {variable}")

        new_window = tk.Toplevel()
        new_window.title("Affichage de l'image")

        # Chargement de l'image avec PIL
        image = Image.open(f"images/Foppa/variables_individuelles/{variable}.png")
        photo = ImageTk.PhotoImage(image)

        # Création d'un label pour afficher l'image et ajout dans la nouvelle fenêtre
        label = tk.Label(new_window, image=photo)
        label.image = photo 
        label.pack()

        data = self.data_for_variable_foppa[variable]
        open_cmd_and_display_text(data)
    

    def GButton_114_command(self):
        variable = self.liste3.get(self.liste3.curselection())

        print(variable)

        new_window = tk.Toplevel()
        new_window.title("Affichage de l'image")

        # Chargement de l'image avec PIL
        image = Image.open(f"images/Foppa_clean/variables_individuelles/{variable}.png")
        photo = ImageTk.PhotoImage(image)

        # Création d'un label pour afficher l'image et ajout dans la nouvelle fenêtre
        label = tk.Label(new_window, image=photo)
        label.image = photo 
        label.pack()

        data = self.data_for_variable_foppa_clean[variable]
        open_cmd_and_display_text(data)



    def update_status(self, label, text): # mettre a jour le label de status1
        label.config(text = text)
    
    def add_to_list(self,elem,variable): # ajouter la variable a la liste des variables sur l'interface
        elem.insert(tk.END,variable)

    def analyser_all(self, bdd):
        print("analyser_toutes_les_variables")
        thread = Thread(target = self.analyse_full)
        thread.start()
    

        #self.analyser_toutes_les_variables(bdd)

    
    def analyse_full(self):

        self.analyser_toutes_les_variables("Foppa")

        try :
            import Clean_par_groupe
            import Clean_lotsNumber
            import Clean_publicityDuration
            import Clean_Zipcode
            import Clean_latETlon
            import Clean_Country
            print("Nettoyage effectué !")
        except Exception as e:
            print("Erreur pendant le nettoyage !")
            print(e)



        self.analyser_toutes_les_variables("Foppa_clean")


    def analyser_toutes_les_variables(self,bdd): # analyser les variables une a une
        if bdd == "Foppa":
            self.data_for_variable_foppa = {}
        else:
            self.data_for_variable_foppa_clean = {}
        cpt = 1  # Initialisation du compteur
        index_a_variable = {}  # Dictionnaire pour mapper le numéro (cpt) à la clé de dict_type_variables

        for variable, info in dict_type_variables.items():
            index_a_variable[str(cpt)] = variable  # Associe le compteur actuel à la clé 'variable'
            cpt += 1

            if bdd == "Foppa":
                self.update_status(self.status_label_1,"Analyse de "+str(variable)+" en cours...") # update status label
            else:
                self.update_status(self.status_label_2,"Analyse de "+str(variable)+" en cours...") # update status label"""

            if (info["Type"] == "Textuelle" or info["Type"] == "Categorielle"):
                print(f"Analyse de : {g1}" + variable + f"{g0}",end="")
                try :
                    if bdd == "Foppa":
                        self.data_for_variable_foppa[variable] = analyser_varchar_all(variable,bdd)
                        self.add_to_list(self.liste1, variable)
                    else:
                        self.data_for_variable_foppa_clean[variable] = analyser_varchar_all(variable,bdd)
                        self.add_to_list(self.liste3, variable)
                    print(f" ==> {g1}OK{g0}")
                except Exception as e:
                    print(f" ==> {rouge}FAIL{g0}")
                    print(e)

            elif info["Type"] == "Numérique":
                print(f"Analyse de : {g1}" + variable + f"{g0}",end="")
                try :
                    if bdd == "Foppa":
                        self.data_for_variable_foppa[variable] = analyser_nombre_all(variable,bdd)
                        self.add_to_list(self.liste1, variable)
                    else:
                        self.data_for_variable_foppa_clean[variable] = analyser_nombre_all(variable,bdd)
                        self.add_to_list(self.liste3, variable)
                    print(f" ==> {g1}OK{g0}")
                except Exception as e:
                    print(f" ==> {rouge}FAIL{g0}")
                    print(e)
        print("Analyse terminée")

    
    

def open_cmd_and_display_text(text): # ouvrir un cmd et y afficher les info de la variable
    with tempfile.NamedTemporaryFile(delete=False, suffix='.bat', mode='w', newline='\n') as tmpfile:
        tmpfile.write('@echo off\n')
        tmpfile.write('mode con: cols=100 lines=3000\n')
        for line in text.split('\n'):
            safe_line = line.replace('^', '^^').replace('&', '^&').replace('<', '^<').replace('>', '^>').replace('|', '^|').replace('"', '^"')
            # Pour les lignes vides, utilisez "echo.", sinon "echo {safe_line}"
            if not line.strip():  # Vérifie si la ligne est vide ou ne contient que des espaces
                tmpfile.write('echo.\n')
            else:
                tmpfile.write(f'echo {safe_line}\n')
        tmpfile.write('pause > nul\n')
    
    subprocess.run(f'start cmd /k "{tmpfile.name}"', shell=True, check=True)





