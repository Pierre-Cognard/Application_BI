import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats


# Chargement des données
agents_df = pd.read_csv('../Foppa/Agents.csv')
lots_df = pd.read_csv('../Foppa/Lots.csv')
criteria_df = pd.read_csv('../Foppa/Criteria.csv')

merged_df = pd.merge(lots_df, criteria_df, on='lotId')

def plot_scatter_with_correlation(data, num_var1, num_var2):
    """
    Affiche un nuage de points entre deux variables numériques et calcule leur coefficient de corrélation de Pearson.
    """
    # Créer un nuage de points

    # Calculer et afficher le coefficient de corrélation de Pearson
    data_cleaned = data.dropna(subset=[num_var1, num_var2])

    pearson_coef, pearson_p_value = stats.pearsonr(data_cleaned[num_var1], data_cleaned[num_var2])
    spearman_coef, spearman_p_value = stats.spearmanr(data_cleaned[num_var1], data_cleaned[num_var2])

    print(f'Coefficient de corrélation de Pearson: {pearson_coef:.2f}, Valeur-p: {pearson_p_value:.3f}')
    if pearson_p_value < 0.05:
        print("La corrélation de Pearson est statistiquement significative.")
    else:
        print("La corrélation de Pearson n'est pas statistiquement significative.")

    print(f'Coefficient de corrélation de Spearman: {spearman_coef:.2f}, Valeur-p: {spearman_p_value:.3f}')
    if spearman_p_value < 0.05:
        print("La corrélation de Spearman est statistiquement significative.")
    else:
        print("La corrélation de Spearman n'est pas statistiquement significative.")



    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=num_var1, y=num_var2, data=data)
    plt.title(f'Nuage de points entre {num_var1} et {num_var2}')
    plt.xlabel(num_var1)
    plt.ylabel(num_var2)
    plt.show()
    
    

# Exemple d'utilisation de la nouvelle fonction
plot_scatter_with_correlation(
    data=merged_df,
    num_var1='contractDuration',  # Remplacez par le nom de votre première variable numérique
    num_var2='publicityDuration'   # Remplacez par le nom de votre seconde variable numérique
)
