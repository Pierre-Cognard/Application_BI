import csv
import matplotlib.pyplot as plt
import numpy as np
from dict_variables import *

def lire_fichier_csv(nom_fichier):
    donnees = []
    with open(nom_fichier, 'r', newline='', encoding='utf-8') as fichier:
        lecteur_csv = csv.DictReader(fichier)
        for ligne in lecteur_csv:
            donnees.append(ligne)
    return donnees

def analyser_valeurs(data, champ):
    valeurs = [float(d[champ]) for d in data if d[champ] != ""]
    valeurs.sort()
    min_val, max_val = min(valeurs), max(valeurs)
    intervalles = np.linspace(min_val, max_val, num=min(100, len(valeurs)), endpoint=True)
    occurrences = {intervalle: 0 for intervalle in intervalles}
    for valeur in valeurs:
        for i in range(len(intervalles) - 1):
            if intervalles[i] <= valeur < intervalles[i+1]:
                occurrences[intervalles[i]] += 1
                break
        else:
            occurrences[intervalles[-1]] += 1
    return occurrences

def generer_graphique(data, champ):
    valeurs_analysees = analyser_valeurs(data, champ)
    for valeur, occurence in valeurs_analysees.items():
        print(f"Valeur: {valeur}, Occurences: {occurence}")
    plt.bar(valeurs_analysees.keys(), valeurs_analysees.values(), width=5)
    plt.xlabel(champ)
    plt.ylabel('Occurences')
    plt.title('Répartition des valeurs de ' + champ)
    plt.show()

"""if __name__ == "__main__":
    fichier_csv = "../Foppa/Agents.csv"
    champs = ['zipcode']  # Champs à analyser
    data = lire_fichier_csv(fichier_csv)
    for champ in champs:
        generer_graphique(data, champ)"""

def analyser_nombre(champ):
    file = dict_type_variables[champ]["File"]
    fichier_csv = "../Foppa/"+file
    data = lire_fichier_csv(fichier_csv)
    generer_graphique(data, champ)
