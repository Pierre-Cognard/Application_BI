import matplotlib.pyplot as plt
import pandas as pd
from dict_variables import *
from holi import *
import warnings

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

# Fonction pour créer un diagramme en barres pour une colonne spécifique
def plot_bar_chart_for_column(file_path, column_name, filtrage, affichage, log):
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

        valeurs_filtrées = value_counts[value_counts >= filtrage]

        #liste={13:0,14:0,15:0,16:0,17:0} # taille des siret

        for index, valeur in valeurs_filtrées.items():
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
                
        plt.bar(valeurs_filtrées.index, valeurs_filtrées.values, log=log)
        plt.xlabel(column_name)
        plt.ylabel('Occurrences')
        plt.title(f'Répartition des valeurs de {column_name} (au moins {filtrage} occurrences)')
        plt.xticks(rotation=45, ha='right')  # Rotation pour une meilleure lisibilité
        plt.tight_layout()  # Ajustement automatique

        if affichage:
            plt.show()
        else:
            plt.savefig(f"images/variables_individuelles/{column_name}.png")
        
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
    plot_bar_chart_for_column(fichier_csv, champ.split(" ")[0], dict_type_variables[champ]["Seuil"], True, dict_type_variables[champ]["Log"])

def analyser_varchar_all(champ):
    fichier_csv = '../Foppa/'+dict_type_variables[champ]["File"]
    return plot_bar_chart_for_column(fichier_csv, champ.split(" ")[0], dict_type_variables[champ]["Seuil"], False, dict_type_variables[champ]["Log"])

