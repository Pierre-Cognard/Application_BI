import matplotlib.pyplot as plt
import pandas as pd

# Chemin du fichier CSV
file_path = '../Foppa/Agents.csv'

# Lecture des premières lignes du fichier pour comprendre sa structure
df = pd.read_csv(file_path)


# Fonction pour créer un diagramme en barres pour une colonne spécifique
def plot_bar_chart_for_column(dataframe, column_name):
    if column_name in dataframe.columns:
        # Calcul du nombre d'occurrences pour chaque valeur unique dans la colonne
        value_counts = dataframe[column_name].value_counts()


        plt.bar(value_counts.index, value_counts.values)
        plt.xlabel(column_name)
        plt.ylabel('Occurences')
        plt.title('Répartition des valeurs de ' + column_name)
        plt.tight_layout()  # Ajuste automatiquement les sous-plots pour qu'ils tiennent dans la zone de la figure

        plt.show()
    else:
        print(f"La colonne '{column_name}' n'existe pas dans le DataFrame.")

# Exemple d'appel de la fonction
plot_bar_chart_for_column(df, 'name')