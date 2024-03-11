import os
import pandas as pd
from dict_variables import dict_type_variables
from holi import *
from analyse_nombre import *


def main():
    dossier = '../Foppa'  # Remplacez cela par le chemin réel vers votre dossier de fichiers CSV
    print("Liste des variables :")
    cpt = 1  # Initialisation du compteur
    index_a_variable = {}  # Dictionnaire pour mapper le numéro (cpt) à la clé de dict_type_variables

    for variable, nature in dict_type_variables.items():
        print(str(cpt) + f" - {g1}" + str(variable) + f"{g0} (" + str(nature) + ")")
        index_a_variable[str(cpt)] = variable  # Associe le compteur actuel à la clé 'variable'
        cpt += 1

    var = '0'
    while not (var.isdigit() and 0 < int(var) <= len(index_a_variable)):
        var = str(input("\nVariable a analyser : \n"))
    
    variable_choisie = index_a_variable[var]

    print(f"Variable choisie : {variable_choisie}")

    analyser(variable_choisie)

if __name__ == "__main__":
    g0 = RGB() # couleur blanc
    g1 = RGB(0, 255, 0) # couleur vert
    main()