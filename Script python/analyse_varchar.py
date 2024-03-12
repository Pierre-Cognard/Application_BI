import matplotlib.pyplot as plt
import pandas as pd
from dict_variables import *

# Fonction pour créer un diagramme en barres pour une colonne spécifique
def plot_bar_chart_for_column(file_path, column_name, filtrage):
    # Filtrage pour ne conserver que les valeurs avec au moins 5 occurrences

    df = pd.read_csv(file_path)

    if column_name in df.columns:
        # Calcul du nombre d'occurrences pour chaque valeur unique dans la colonne
        value_counts = df[column_name].value_counts()
        valeurs_filtrées = value_counts[value_counts >= filtrage]


        plt.bar(valeurs_filtrées.index, valeurs_filtrées.values)
        plt.xlabel(column_name)
        plt.ylabel('Occurrences')
        plt.title(f'Répartition des valeurs de {column_name} (au moins {filtrage} occurrences)')
        plt.xticks(rotation=45, ha='right')  # Rotation pour une meilleure lisibilité
        plt.tight_layout()  # Ajustement automatique
        plt.show()
    else:
        print(f"La colonne '{column_name}' n'existe pas dans le DataFrame.")


def analyser_varchar(champ,file):
    fichier_csv = "../Foppa/"+file
    plot_bar_chart_for_column(fichier_csv, champ, dict_type_variables[champ]["Seuil"])


#analyser_varchar('name')