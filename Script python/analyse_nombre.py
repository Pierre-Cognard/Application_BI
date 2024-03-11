import csv
import matplotlib.pyplot as plt
from dict_variables import dict_fichier_variables

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
    occurrences = {}
    for valeur in valeurs:
        if valeur not in occurrences:
            occurrences[valeur] = 0
        occurrences[valeur] += 1
    return occurrences

def generer_graphique(data, champ):
    valeurs_analysees = analyser_valeurs(data, champ)
    plt.bar(valeurs_analysees.keys(), valeurs_analysees.values())
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

def analyser(champ):
    file = dict_fichier_variables[champ]
    fichier_csv = "../Foppa/"+file
    data = lire_fichier_csv(fichier_csv)
    generer_graphique(data, champ)