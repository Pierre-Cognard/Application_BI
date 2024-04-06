import os
import pandas as pd
from dict_variables import dict_type_variables
from holi import *
from analyse_nombre import *
from analyse_varchar_nettoye import *


def main():
    dossier = '../Foppa'  # Remplacez cela par le chemin réel vers votre dossier de fichiers CSV
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

    print(f"Variable choisie : {g1}{variable_choisie}{g0}")
    print("Analyse en cours....")

    if (type_variable == "Numérique"):
        analyser_nombre(variable_choisie.split(" ")[0])

    elif (type_variable == "Textuelle" or type_variable == "Categorielle"):
        analyser_varchar(variable_choisie)


if __name__ == "__main__":
    main()