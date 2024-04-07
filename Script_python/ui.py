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

        button2=tk.Button(root,font=ft,text="Afficher \nle graphe",command=self.GButton_114_command) # bouton pair de var
        button2.place(x=235,y=400,width=90,height=200)

        # =============== FOPPA NETTOYEE ===============
        GLabel_245=tk.Label(root,borderwidth=1,relief="groove",font=tkFont.Font(family='Arial',size=12),text="Analyse de la base Foppa nettoyée").place(x=450,y=10,width=300,height=30)

        label_var_indiv2=tk.Label(root,borderwidth=1,relief="solid",text="Variables individuelles",font=ft).place(x=475,y=50,width=250,height=30)

        self.liste3=tk.Listbox(root,borderwidth=1,relief="solid",font=ft) # liste var indiv
        self.liste3.place(x=475,y=120,width=150,height=200)

        button3=tk.Button(root,font=ft,text="Afficher \nle graphe",command=self.button1_command) # bouton var indiv
        button3.place(x=635,y=120,width=90,height=200)

        label_pair_var2=tk.Label(root,borderwidth=1,relief="solid",text="Paires de variables",font=ft).place(x=475,y=330,width=250,height=30)

        self.liste4=tk.Listbox(root,borderwidth=1,relief="solid",font=ft) # liste pair var
        self.liste4.place(x=475,y=400,width=150,height=200)

        button4=tk.Button(root,font=ft,text="Afficher \nle graphe",command=self.GButton_114_command) # bouton pair de var
        button4.place(x=635,y=400,width=90,height=200)
        # =============================================

        self.root = root
        self.status_label_1 = tk.Label(root, text="Prêt", font=tkFont.Font(family='Arial', size=10),)
        self.status_label_1.place(x=50, y=85, width=300, height=30) 

        self.status_label_2 = tk.Label(root, text="Prêt", font=tkFont.Font(family='Arial', size=10))
        self.status_label_2.place(x=50, y=365, width=300, height=30)

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

        data = self.data_for_variable[variable]
        open_cmd_and_display_text(data)
    

    def GButton_114_command(self):
        print("command 114")

    def long_running_task(self):
        print("analyser_toutes_les_variables")
        thread = Thread(target=self.analyser_toutes_les_variables, args=("Foppa",))
        thread.start()

    def update_status(self, text): # mettre a jour le label de status1
        self.status_label_1.config(text=text)
    
    def add_to_list(self,variable): # ajouter la variable a la liste des variables sur l'interface
        self.liste1.insert(tk.END,variable)

    def analyser_toutes_les_variables(self,bdd): # analyser les variables une a une
        self.var_to_chart = {}
        self.data_for_variable = {}
        open_or_close = {}
        cpt = 1  # Initialisation du compteur
        index_a_variable = {}  # Dictionnaire pour mapper le numéro (cpt) à la clé de dict_type_variables

        for variable, info in dict_type_variables.items():
            index_a_variable[str(cpt)] = variable  # Associe le compteur actuel à la clé 'variable'
            cpt += 1
            self.update_status("Analyse de "+str(variable)+" en cours...")

            if (info["Type"] == "Textuelle" or info["Type"] == "Categorielle"):
                print(f"Analyse de : {g1}" + variable + f"{g0}",end="")
                try :
                    self.data_for_variable[variable] = analyser_varchar_all(variable,bdd)
                    print(f" ==> {g1}OK{g0}")
                    self.add_to_list(variable)
                except:
                    print(f" ==> {rouge}FAIL{g0}")

            elif info["Type"] == "Numérique":
                print(f"Analyse de : {g1}" + variable + f"{g0}",end="")
                try :
                    self.data_for_variable[variable] = analyser_nombre_all(variable,bdd)
                    print(f" ==> {g1}OK{g0}")
                    self.add_to_list(variable)
                except:
                    print(f" ==> {rouge}FAIL{g0}")

            open_or_close[variable] = 0
        
        self.update_status("")
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

