import matplotlib.pyplot as plt
import pandas as pd
from dict_variables import *
from holi import *
import warnings
from Levenshtein import ratio
from tqdm import tqdm


warnings.filterwarnings("ignore")

def verifier_chaine(valeur):
    # Suppression des tirets et des espaces
    valeur_nettoyee = valeur.replace("-", "").replace(" ", "")
    # Test si la chaîne est composée uniquement de Y ou uniquement de N
    if all(caractere == "Y" for caractere in valeur_nettoyee):
        return "Y"
    elif all(caractere == "N" for caractere in valeur_nettoyee):
        return "N"
    else:
        return "DEGAGE"
    
def regrouper_valeurs_proches(valeurs_filtrées, seuil):
    groupes = {}  # Dictionnaire pour stocker les valeurs regroupées et leurs occurrences
    groupes_fusionnés_liste = {}  # Dictionnaire pour stocker les groupes fusionnés contenant au moins deux éléments
    index_original = list(valeurs_filtrées.index)
    groupes_fusionnés = 0  # Compteur des groupes fusionnés contenant au moins deux éléments

    for i, valeur in enumerate(index_original):
        groupe_trouvé = False
        for groupe in groupes.keys():
            # Vérifier si la valeur est proche d'une valeur déjà regroupée
            if any(ratio(valeur, val) >= seuil for val in groupe):
                groupes[groupe].append(valeur)
                groupe_trouvé = True
                # Vérifier si le groupe a été fusionné et contient maintenant au moins deux éléments
                if len(groupes[groupe]) == 2:
                    groupes_fusionnés += 1
                    groupes_fusionnés_liste[groupe] = [valeur]  # Initialiser la liste avec la première valeur
                    groupes_fusionnés_liste[groupe].append(groupe)  # Ajouter la valeur au groupe fusionné

                else:
                    groupes_fusionnés_liste[groupe].append(valeur)  # Ajouter la valeur au groupe fusionné
                break
        if not groupe_trouvé:
            groupes[(valeur,)] = [valeur]
    
    print(f"Nombre de groupes fusionnés : {groupes_fusionnés}")
    print("Liste des groupes fusionnés :")
    for groupe, valeurs in groupes_fusionnés_liste.items():
        print(f"Groupe : {groupe}")
        print(f"Valeurs : {valeurs}")

    # Calculer les occurrences des valeurs regroupées
    valeurs_regroupees = {"/".join(groupe): sum(valeurs_filtrées.loc[groupe]) for groupe in groupes.values()}
    
    # Filtrer les valeurs regroupées dont la somme est supérieure à 100
    valeurs_regroupees_filtrees = {groupe: somme for groupe, somme in valeurs_regroupees.items() if somme > 100}

    # Trier les valeurs regroupées dans l'ordre décroissant selon leur somme
    valeurs_regroupees_filtrees_triees = dict(sorted(valeurs_regroupees_filtrees.items(), key=lambda item: item[1], reverse=True))

    
    return valeurs_regroupees_filtrees_triees






# Fonction pour créer un diagramme en barres pour une colonne spécifique
def plot_bar_chart_for_column(file_path, column_name, filtrage, affichage):
    data = ""
    # Filtrage pour ne conserver que les valeurs avec au moins 5 occurrences

    df = pd.read_csv(file_path)

    if column_name == "contractorSme": # Uniquement pour cette variable --> recupère des valeurs en plus
        cpt_y = 0
        cpt_n = 0
        for valeur in df[column_name]:
            if valeur != "" and not pd.isna(valeur) and "-" in valeur:
                if verifier_chaine(valeur) == "Y":
                    cpt_y += 1
                elif verifier_chaine(valeur) == "N":
                    cpt_n += 1


    if column_name in df.columns:
        # Calcul du nombre d'occurrences pour chaque valeur unique dans la colonne
        value_counts = df[column_name].value_counts()

        somme = 0

        for index, valeur in value_counts.items():
            somme += valeur

        
        data = print_or_save(affichage, data, "\n======= Infos =======")
        data = print_or_save(affichage, data, f"Nombre de ligne : {bleue}"+str(len(df)))
        data = print_or_save(affichage, data, f"{g0}Nombre valeur pour {g1}{column_name}{g0} : {bleue}"+str(somme))
        data = print_or_save(affichage, data, f"{g0}Taux de valeurs manquantes : {orange}{str(round(100-(somme/len(df))*100,2))}%{g0}")
        data = print_or_save(affichage, data, "=====================\n")

        #liste={13:0,14:0,15:0,16:0,17:0} # taille des siret

        value_counts = value_counts[value_counts >= 4]

        valeurs_regroupees = regrouper_valeurs_proches(value_counts, seuil=0.95)  # Appel à la fonction de regroupement des valeurs

        for index, valeur in value_counts.items():
            if column_name == "contractorSme":
                if index == "Y":
                    data = print_or_save(affichage, data, f"Index: {g1}{index}{g0} | Valeur: {g1}{valeur} (+{cpt_y}){g0}")
                elif index == "N":
                    data = print_or_save(affichage, data, f"Index: {g1}{index}{g0} | Valeur: {g1}{valeur} (+{cpt_n}){g0}")
                else:
                    data = print_or_save(affichage, data, f"Index: {g1}{index}{g0} | Valeur: {g1}{valeur}{g0}")
            else:
                data = print_or_save(affichage, data, f"Index: {g1}{index}{g0} | Valeur: {g1}{valeur}{g0}")
            #liste[len(str(index))] += 1  # taille des siret
        #print(liste)  # taille des siret

        for groupe, valeur in valeurs_regroupees.items():
            data = print_or_save(affichage, data, f"Group: {g1}{groupe}{g0} | Valeur: {g1}{valeur}{g0}")

                
        if affichage:
            plt.bar(valeurs_regroupees.keys(), valeurs_regroupees.values())
            plt.xlabel(column_name)
            plt.ylabel('Occurrences')
            plt.title(f'Répartition des valeurs de {column_name} (au moins {filtrage} occurrences)')
            plt.xticks(rotation=45, ha='right')  # Rotation pour une meilleure lisibilité
            plt.tight_layout()  # Ajustement automatique
            plt.show()
        else:
            fig, ax = plt.subplots()
            ax.bar(valeurs_regroupees.keys(), valeurs_regroupees.values())
            ax.set_xlabel(column_name)
            ax.set_ylabel('Occurrences')
            ax.set_title(f'Répartition des valeurs de {column_name} (au moins {filtrage} occurrences)')
            #ax.tick_params(axis='x', rotation=45)  # Rotation pour une meilleure lisibilité
            labels = ax.get_xticklabels()
            ax.set_xticklabels(labels, rotation=45, ha='right')
            plt.tight_layout()  # Ajustement automatique
            return fig, data
        
    else:
        print(f"La colonne '{column_name}' n'existe pas dans le DataFrame.")
        return None

def print_or_save(affichage, data, text):
    if affichage:
        print(text)
    else:
        data += text+"\n"
    return data



def analyser_varchar(champ):
    fichier_csv = '../Foppa/'+dict_type_variables[champ]["File"]
    plot_bar_chart_for_column(fichier_csv, champ.split(" ")[0], dict_type_variables[champ]["Seuil"], True)

def analyser_varchar_all(champ):
    fichier_csv = '../Foppa/'+dict_type_variables[champ]["File"]
    return plot_bar_chart_for_column(fichier_csv, champ.split(" ")[0], dict_type_variables[champ]["Seuil"], False)