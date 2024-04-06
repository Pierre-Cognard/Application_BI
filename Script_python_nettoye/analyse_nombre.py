import csv
import matplotlib.pyplot as plt
import numpy as np
import requests
from dict_variables import *
import time
from holi import *
import warnings

warnings.filterwarnings("ignore")

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

def generer_graphique(data, champ, log, affichage):
    text = ""
    somme = 0 # nb de valeur pour le champ

    valeurs_analysees, min_val, max_val = analyser_valeurs(data, champ)

    for valeur, occurence in valeurs_analysees.items():
        if occurence != 0:
            somme += occurence

    text = print_or_save(affichage, text, "\n======= Infos =======")
    text = print_or_save(affichage, text, f"Nombre de ligne : {bleue}"+str(len(data)))
    text = print_or_save(affichage, text, f"{g0}Nombre valeur pour {g1}{champ}{g0} : {bleue}"+str(somme))
    text = print_or_save(affichage, text, f"{g0}Taux de valeurs manquantes : {orange}{str(round(100-(somme/len(data))*100,2))}%{g0}")
    text = print_or_save(affichage, text, "=====================")

    valeurs = [float(d[champ]) for d in data if d[champ] != ""]
    moyenne = np.mean(valeurs)
    mediane = np.median(valeurs)
    ecart_type = np.std(valeurs)

    text = print_or_save(affichage, text, "\n===== Statistiques =====")
    text = print_or_save(affichage, text, f"Moyenne de {g1}{champ}{g0}: {round(moyenne,2)}")
    text = print_or_save(affichage, text, f"Mediane de {g1}{champ}{g0}: {round(mediane,2)}")
    text = print_or_save(affichage, text, f"Ecart type de {g1}{champ}{g0}: {round(ecart_type,2)}")
    text = print_or_save(affichage, text, "========================")

    for valeur, occurence in valeurs_analysees.items():
        if occurence != 0:
            text = print_or_save(affichage, text, f"Valeur: {g1}{valeur}{g0} | Occurences: {g1}{occurence}{g0}")
    
    if champ == "sirett":
        validator = Siret()
        valid_count = 0
        invalid_count = 0
        invalid_sirets = []
        for d in data:
            if d[champ] != "" and validator.is_valid(d[champ]):
                valid_count += 1
            elif d[champ] != "":
                invalid_count += 1
                invalid_sirets.append(d[champ])

        
        total_count = valid_count + invalid_count
        print(f"Pourcentage de SIRET valides : {valid_count / total_count * 100:.2f}%")
        print(f"Pourcentage de SIRET invalides : {invalid_count / total_count * 100:.2f}%")
        # Stockage des SIRET invalides dans un fichier texte
        with open("siret_invalides.txt", "w") as file:
            file.write("SIRET invalides :\n")
            for siret in invalid_sirets:
                file.write(siret + "\n")
        
        true_count, false_count = count_validity(invalid_sirets)
        print("Nombre de SIRET valides par API:", true_count)
        print("Nombre de SIRET invalides par API:", false_count)

    plage_de_donnees = max_val - min_val

    # Définissez la largeur en pourcentage
    largeur_en_pourcentage = 0.5

    # Calculez la largeur en fonction de la plage de données
    largeur = largeur_en_pourcentage / 100 * plage_de_donnees

    if affichage:
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
    else:
        fig, ax = plt.subplots()
        ax.bar(valeurs_analysees.keys(), valeurs_analysees.values(), width=largeur)
        ax.set_xlabel(champ)
        if log:
            ax.set_yscale('log')  # Utilisez une échelle logarithmique pour l'axe y
            ax.set_ylabel('Occurences (log scale)')
        else:
            ax.set_ylabel('Occurences')
        ax.set_title('Répartition des valeurs de ' + champ)
        return fig, text

class Siret:
    SIRET_LENGTH = 14

    def is_valid(self, siret: str) -> bool:
        siret = siret.strip() if siret else ""
        if not siret.isdigit() or len(siret) != self.SIRET_LENGTH:
            return False

        total = 0
        for i in range(self.SIRET_LENGTH):
            temp = int(siret[i]) * (2 if i % 2 == 0 else 1)
            temp = temp - 9 if temp > 9 else temp
            total += temp

        return total % 10 == 0

def is_siret_valid(siret):
    url = f"https://api.insee.fr/entreprises/sirene/V3/siret/{siret}"
    headers = {
        "Authorization": "Bearer 870e79f3-ad71-398e-b0b4-04a485b1a7ea"
    }
    response = requests.get(url, headers=headers)
    time.sleep(0.5)  # Pause de 2 secondes max api
    print(response)
    if response.status_code == 200:
        data = response.json()
        return not data.get('error', False)
    return False

def count_validity(sirets):
    true_count = 0
    false_count = 0
    for siret in sirets:
        if is_siret_valid(siret):
            true_count += 1
        else:
            false_count += 1
    return true_count, false_count


"""if __name__ == "__main__":
    fichier_csv = "../Foppa/Agents.csv"
    champs = ['zipcode']  # Champs à analyser
    data = lire_fichier_csv(fichier_csv)
    for champ in champs:
        generer_graphique(data, champ)"""

def print_or_save(affichage, data, text):
    if affichage:
        print(text)
    else:
        data += text+"\n"
    return data

def analyser_nombre(champ):
    file = dict_type_variables[champ]["File"]
    log = dict_type_variables[champ]["Log"]
    fichier_csv = "../Foppa/"+file
    data = lire_fichier_csv(fichier_csv)
    generer_graphique(data, champ, log, True)

def analyser_nombre_all(champ):
    file = dict_type_variables[champ]["File"]
    log = dict_type_variables[champ]["Log"]
    fichier_csv = "../Foppa/"+file
    data = lire_fichier_csv(fichier_csv)
    return generer_graphique(data, champ, log, False)
