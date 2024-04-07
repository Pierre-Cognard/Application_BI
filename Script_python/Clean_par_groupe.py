import pandas as pd
from dict_variables import dict_type_variables
from holi import *
from analyse_nombre import *
from analyse_varchar import *
from pathlib import Path
from Levenshtein import ratio
from tqdm import tqdm

# REPRODUCTION DU ANALYSE ALL POUR NETTOYAGE PAR GROUPE A MODIFIER

THIS_FOLDER = Path(__file__).parent.resolve()
PARENT_FOLDER = THIS_FOLDER.parent.resolve()


def regrouper_valeurs_similaires(variable, seuil):
    groupes = {}  # Dictionnaire pour stocker les valeurs regroupées et leur numéro de groupe

    groupes_fusionnés_liste = {}  # Dictionnaire pour stocker les groupes fusionnés contenant au moins deux éléments

    fichier_origine = str(PARENT_FOLDER / 'Foppa_clean' / dict_type_variables[variable]["File"])

    df = pd.read_csv(fichier_origine)
    nouveau_df = df.copy()  # Copie du DataFrame original pour éviter de modifier les données d'origine

    # Calcul du nombre d'occurrences pour chaque valeur unique dans la colonne
    value_counts = df[variable.split(" ")[0]].value_counts()

    # Filtrer les valeurs ayant au moins 10 occurrences
    value_counts = value_counts[value_counts >= 10]

    # Initialisation de la barre de progression
    progress_bar = tqdm(total=len(value_counts), desc="Progression")

    # Vérifie si la colonne "name" contient des valeurs de type objet (texte)
    colonne = variable.split(" ")[0]
    for valeur in value_counts.index:
        # Vérifier si la valeur a déjà été regroupée
        groupe_trouve = False
        for groupe in groupes.keys():
            # Vérifier si le ratio de similarité est supérieur au seuil
            if any(ratio(valeur, val) >= seuil for val in groupe):
                groupes[groupe].append(valeur)
                # Remplacer la valeur dans le DataFrame par le groupe
                groupe_trouve = True

                if len(groupes[groupe]) == 2:
                    groupes_fusionnés_liste[groupe] = [valeur]  # Initialiser la liste avec la première valeur
                    groupes_fusionnés_liste[groupe].append(groupe)  # Ajouter la valeur au groupe fusionné

                else:
                    groupes_fusionnés_liste[groupe].append(valeur)  # Ajouter la valeur au groupe fusionné

                break
        
        # Si la valeur n'a pas été regroupée, créer un nouveau groupe
        if not groupe_trouve:
            groupes[(valeur,)] = [valeur]
        progress_bar.update(1)  # Mettre à jour la barre de progression pour chaque valeur traitée


    # Remplacer chaque valeur par le nom de son groupe dans la colonne du DataFrame
    for groupe, valeurs in groupes.items():
        for valeur in valeurs:
            nouveau_df[colonne].replace(valeur, "/".join(groupe), inplace=True)

    progress_bar.close()  # Fermer la barre de progression


    print("Liste des groupes fusionnés :")
    for groupe, valeurs in groupes_fusionnés_liste.items():
        print(f"Groupe : {groupe}")
        print(f"Valeurs : {valeurs}")

    # Spécifier le chemin pour le nouveau fichier CSV
    chemin_nouveau_fichier = str(PARENT_FOLDER / 'Foppa_clean' / dict_type_variables[variable]["File"])

    # Enregistrer le nouveau fichier CSV avec les valeurs regroupées
    nouveau_df.to_csv(chemin_nouveau_fichier, index=False)

    print("Le nouveau fichier CSV a été créé avec succès.")

    return 1


var_to_chart = {}
open_or_close = {}

cpt = 1  # Initialisation du compteur
index_a_variable = {}  # Dictionnaire pour mapper le numéro (cpt) à la clé de dict_type_variables

for variable, info in dict_type_variables.items():
    index_a_variable[str(cpt)] = variable  # Associe le compteur actuel à la clé 'variable'
    cpt += 1

    # Spécifier le seuil pour la similarité des valeurs
    seuil_similarity = 0.95
    if variable == "address":
        seuil_similarity = 0.99

    if ((info["Type"] == "Textuelle" or info["Type"] == "Categorielle") and info["Grouper"] == True):
        print(f"Analyse de : {g1}" + variable + f"{g0}",end="")
        try:
            regrouper_valeurs_similaires(variable, seuil_similarity)
            print(f" ==> {g1}OK{g0}")
        except Exception as e:
            print(f" ==> {rouge}FAIL{g0}: {e}")

    open_or_close[variable] = 0

print("Analyse terminée")
