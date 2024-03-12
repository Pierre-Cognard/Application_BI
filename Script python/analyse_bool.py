import matplotlib.pyplot as plt
import pandas as pd
from dict_variables  import *

# Chemin du fichier CSV
file_path = '../Foppa/Agents.csv'

# Lecture des premières lignes du fichier pour comprendre sa structure



def plot_bar_chart_for_categorical_column(file_path, column_name):
    df = pd.read_csv(file_path)

    if column_name in df.columns:
        # Vérifier si les valeurs sont uniquement 0 et 1, ce qui suggère un booléen
        unique_values = df[column_name].unique()
        if set(unique_values).issubset({0, 1}):
            # Mapper 0 et 1 à 'False' et 'True'
            df[column_name] = df[column_name].map({0: 'False', 1: 'True'})
        
        # Calcul du nombre d'occurrences pour chaque valeur unique dans la colonne
        value_counts = df[column_name].value_counts()
       
        # Création du diagramme en barres
        plt.figure(figsize=(8, 4))
        plt.bar(value_counts.index, value_counts.values)
        plt.xlabel(column_name)
        plt.ylabel('Occurrences')
        plt.title(f'Répartition des valeurs de {column_name}')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        print(f"La colonne '{column_name}' n'existe pas dans le DataFrame.")



def analyser_varchar(champ):
    file = dict_fichier_variables[champ]
    fichier_csv = "../Foppa/"+file
    plot_bar_chart_for_categorical_column(fichier_csv, champ)



analyser_varchar('jointProcurement')