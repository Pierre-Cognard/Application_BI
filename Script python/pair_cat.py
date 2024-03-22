#Analyse Paire de variable numérique et catégorielle: 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats

# Chargement des données
agents_df = pd.read_csv('../Foppa/Agents.csv')
lots_df = pd.read_csv('../Foppa/Lots.csv')
lot_buyers_df = pd.read_csv('../Foppa/LotBuyers.csv')
lot_suppliers_df = pd.read_csv('../Foppa/LotSuppliers.csv') # Utilisez cette ligne si vous travaillez avec les fournisseurs

# Fusion de lots_df avec lot_buyers_df pour obtenir le prix de chaque lot avec son agentId
lots_with_agents_df = pd.merge(lots_df, lot_buyers_df, on='lotId')
lots_with_agents_df = pd.merge(lots_df, lot_suppliers_df, on='lotId')
# Fusion du résultat avec agents_df pour obtenir le département de chaque agent
merged_df = pd.merge(lots_with_agents_df, agents_df, on='agentId')

print(merged_df.head())

def plot_filtered_violin(data, cat_var1, cat_var2, cat1_filter=None, cat2_filter=None):

    # Filtrer le dataframe si des filtres catégoriels ou numériques sont fournis
    if cat1_filter:
        data = data[data[cat1_filter[0]] == cat1_filter[1]]
    if cat2_filter:
        data = data[data[cat2_filter[0]] == cat2_filter[1]]

    # Vérifier si le DataFrame filtré n'est pas vide
    if not data.empty:
        # Pour afficher le compte de chaque combinaison de 'region' et 'activity_domain':
        plt.figure(figsize=(12, 8))
        sns.countplot(x=cat_var1, hue=cat_var2, data=data)
        plt.title(f'Distribution de {cat_var1} par {cat_var2}')
        plt.xlabel(cat_var1)
        plt.ylabel(cat_var2)
        plt.xticks(rotation=45)  # Rotation des étiquettes si elles sont trop longues
        plt.tight_layout()  # Ajustement automatique pour éviter le chevauchement des étiquettes
        plt.show()
    else:
        print(f"Aucune donnée trouvée pour les filtres fournis: {cat1_filter}, {cat2_filter}")

# Exemple d'utilisation de la fonction:
plot_filtered_violin(
    data=merged_df,
    cat_var1='typeOfContract',  # Variable catégorielle pour l'axe des x
    cat_var2='onBehalf',  # Variable categorielle num 2 ( celle qu'on compare ) pour l'axe des y
    cat1_filter=('city', 'PARIS'),  # Filtrer pour le département '84'
    #cat2_filter=('onBehalf', 1)  
)
