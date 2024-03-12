import csv
import matplotlib.pyplot as plt
import numpy as np
from dict_variables import *
from holi import *

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
    return occurrences, min_val, max_val

def generer_graphique(data, champ, log):
    valeurs_analysees, min_val, max_val = analyser_valeurs(data, champ)
    for valeur, occurence in valeurs_analysees.items():
        if occurence != 0:
            print(f"Valeur: {valeur}, Occurences: {occurence}")

    plage_de_donnees = max_val - min_val

    # Définissez la largeur en pourcentage
    largeur_en_pourcentage = 0.5

    # Calculez la largeur en fonction de la plage de données
    largeur = largeur_en_pourcentage / 100 * plage_de_donnees

    print("largeur" , largeur)

    # Maintenant, utilisez cette largeur dans la fonction plt.bar()
    plt.bar(valeurs_analysees.keys(), valeurs_analysees.values(), width=largeur)
    plt.xlabel(champ)
    if log:
        plt.yscale('log')  # Définition de l'échelle logarithmique pour l'axe y
        plt.ylabel('Occurences (log scale)')
    else :
        plt.ylabel('Occurences')
    plt.title('Répartition des valeurs de ' + champ)
    plt.show()

def statistiques_valeurs(data, champ):
    valeurs = [float(d[champ]) for d in data if d[champ] != ""]
    moyenne = np.mean(valeurs)
    mediane = np.median(valeurs)
    ecart_type = np.std(valeurs)

    print(f"Moyenne de {g1}{champ}{g0}: {round(moyenne,2)}")
    print(f"Médiane de {g1}{champ}{g0}: {round(mediane,2)}")
    print(f"Écart type de {g1}{champ}{g0}: {round(ecart_type,2)}")


"""if __name__ == "__main__":
    fichier_csv = "../Foppa/Agents.csv"
    champs = ['zipcode']  # Champs à analyser
    data = lire_fichier_csv(fichier_csv)
    for champ in champs:
        generer_graphique(data, champ)"""

def analyser_nombre(champ):
    file = dict_type_variables[champ]["File"]
    log = dict_type_variables[champ]["Log"]
    fichier_csv = "../Foppa/"+file
    data = lire_fichier_csv(fichier_csv)
    generer_graphique(data, champ, log)
    statistiques_valeurs(data, champ)
