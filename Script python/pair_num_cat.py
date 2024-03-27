#Analyse Paire de variable numérique et catégorielle: 

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
# Chargement des données
agents_df = pd.read_csv('../Foppa/Agents.csv')
lots_df = pd.read_csv('../Foppa/Lots.csv')
lot_buyers_df = pd.read_csv('../Foppa/LotBuyers.csv')
lot_suppliers_df = pd.read_csv('../Foppa/LotSuppliers.csv') # Utilisez cette ligne si vous travaillez avec les fournisseurs


criteria_df = pd.read_csv('../Foppa/Criteria.csv')


# Fusion de lots_df avec lot_buyers_df pour obtenir le prix de chaque lot avec son agentId
lots_with_agents_df = pd.merge(lots_df, lot_buyers_df, on='lotId')
lots_with_agents_df = pd.merge(lots_df, lot_suppliers_df, on='lotId')
# Fusion du résultat avec agents_df pour obtenir le département de chaque agent
merged_df = pd.merge(lots_with_agents_df, agents_df, on='agentId')
merged_df = pd.merge(lots_df, criteria_df, on='lotId')



# Assurez-vous que vos DataFrames sont correctement chargés et fusionnés comme dans votre script initial

def anova_test(data, cat_var, num_var):
    """
    Effectue une ANOVA pour tester si les moyennes du num_var diffèrent entre les groupes définis par cat_var.
    """
    data = data.sample(frac=0.1, random_state=1)  # Ajustez frac= selon la fraction souhaitée

    data = data.dropna(subset=[cat_var, num_var])

    formula = f'{num_var} ~ C({cat_var})'
    model = ols(formula, data=data).fit()
    anova_results = sm.stats.anova_lm(model, typ=2)
    print(anova_results)

def point_biserial_correlation(data, binary_var, num_var):
    """
    Calcule le coefficient de corrélation de point bisériel entre une variable binaire et une variable numérique.
    """
    data = data.dropna(subset=[binary_var, num_var])
    binary_numeric = data[binary_var].apply(lambda x: 1 if x == data[binary_var].unique()[0] else 0)
    correlation_coef, p_value = stats.pointbiserialr(binary_numeric, data[num_var])
    print(f'Coefficient de corrélation de point bisériel: {correlation_coef:.2f}, Valeur-p: {p_value:.3f}')
    if p_value < 0.05:
        print("La corrélation est statistiquement significative.")
    else:
        print("La corrélation n'est pas statistiquement significative.")




def plot_filtered_violin(data, cat_var, num_var, cat_filter=None, num_filter=None):


    # Filtrer le dataframe si des filtres catégoriels ou numériques sont fournis
    if cat_filter and isinstance(cat_filter[1], list):
        data = data[data[cat_filter[0]].isin(cat_filter[1])]
    if num_filter:
        data = data[data[num_filter[0]] < num_filter[1]]

    # Vérifier si le DataFrame filtré n'est pas vide
    if not data.empty:

        print(data.head())

       
        # Création du violin plot pour la distribution de la variable numérique
        plt.figure(figsize=(10, 6))
        sns.violinplot(x=cat_var, y=num_var, data=data, inner="point")
        sns.pointplot(x=cat_var, y=num_var, data=data, color='black', markers='_', errorbar='sd')  # Utilise ci='sd' pour montrer l'écart-type
        plt.title(f'Distribution de {num_var} par {cat_var}')
        plt.xlabel(cat_var)
        plt.ylabel(num_var)
        plt.tight_layout()  # Ajustement automatique pour éviter le chevauchement des étiquettes
        plt.show()
    else:
        print(f"Aucune donnée trouvée pour les filtres fournis: {cat_filter}, {num_filter}")



# Utilisation de l'ANOVA
print("Résultats de l'ANOVA :")
anova_test(data=merged_df, cat_var='type', num_var='weight')


# Pour utiliser le coefficient de corrélation de point bisériel, assurez-vous que votre variable catégorielle est binaire.
# Si 'binary_var' est votre variable binaire et 'num_var' est votre variable numérique, utilisez :
#point_biserial_correlation(data=merged_df, binary_var='VotreVariableBinaire', num_var='awardPrice')

# Exemple d'utilisation de la fonction:
plot_filtered_violin(
    data=merged_df,
    cat_var='type',  # Variable catégorielle pour l'axe des x
    num_var='weight',  # Variable numérique pour l'axe des y
    cat_filter=('type', ['PRICE','DELAY','TECHNICAL','ENVIRONMENTAL','SOCIAL','OTHER'])  # Liste des villes à inclure
    #num_filter=('awardPrice', 10000000)  # Filtrer pour les prix inférieurs à 200000
)




