import os
import pandas as pd
from dict_variables import variables_dict
from holi import *


def main():
    dossier = '../Foppa'  # Remplacez cela par le chemin réel vers votre dossier de fichiers CSV
    print("Liste des variables :")
    cpt = 1  # Initialisation du compteur
    for variable, nature in variables_dict.items():
        print(str(cpt) + f" - {g1}" + str(variable) + f"{g0} (" + str(nature) + ")")
        cpt += 1

    var = '0'
    while var > '35' or var <= '0':
        var = str(input("\nVariable a analyser : \n"))

if __name__ == "__main__":
    g0 = RGB() # couleur blanc
    g1 = RGB(0, 255, 0) # couleur vert
    main()