import os
import pandas as pd
from dict_variables import dict_type_variables
from holi import *
from analyse_nombre import *
from analyse_varchar import *
import tkinter as tk

bdd = ""

def on_button_click(base):
    global bdd, root
    bdd = base
    root.destroy()

def main():
    global bdd, root
    root = tk.Tk()
    root.title("Choix de la base de données")

    button_size = 10

    label = tk.Label(root, text="Choix de la base de données")
    label.grid(row=0,column=0,columnspan=2,pady=5,padx=5) # Ajout de marge au-dessus et en dessous du label

    # Création du premier bouton
    button1 = tk.Button(root, text="Foppa", command=lambda: on_button_click("Foppa"))
    button1.config(height=button_size, width=button_size+7,bg="blue")  # Taille carrée
    button1.grid(row=1,column=0,pady=5, padx=5)

    # Création du deuxième bouton
    button2 = tk.Button(root, text="Foppa_clean", command=lambda: on_button_click("Foppa_clean"))
    button2.config(height=button_size, width=button_size+7,bg="blue")  # Taille carrée
    button2.grid(row=1,column=1,pady=5, padx=5)

    # Boucle principale de Tkinter
    root.mainloop()

    dossier = '../Foppa' 
    print("Liste des variables :")
    cpt = 1  # Initialisation du compteur
    index_a_variable = {}  # Dictionnaire pour mapper le numéro (cpt) à la clé de dict_type_variables

    for variable, info in dict_type_variables.items():
        print(str(cpt) + f" - {g1}" + str(variable) + f"{g0} (" + str(info["Type"]) + ")")
        index_a_variable[str(cpt)] = variable  # Associe le compteur actuel à la clé 'variable'
        cpt += 1

    var = '0'
    while not (var.isdigit() and 0 < int(var) <= len(index_a_variable)):
        var = str(input("\nVariable a analyser : \n"))
    
    variable_choisie = index_a_variable[var]
    type_variable = dict_type_variables[variable_choisie]["Type"]

    print(f"Variable choisie : {g1}{variable_choisie}{g0} dans {g1}{bdd}{g0}")
    print("Analyse en cours....")

    if (type_variable == "Numérique"):
        analyser_nombre(variable_choisie.split(" ")[0],bdd)

    elif (type_variable == "Textuelle" or type_variable == "Categorielle"):
        analyser_varchar(variable_choisie,bdd)


if __name__ == "__main__":
    main()