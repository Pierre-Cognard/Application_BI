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

def plot_filtered_violin(data, cat_var, num_var, cat_filter=None, num_filter=None):

    # Filtrer le dataframe si des filtres catégoriels ou numériques sont fournis
    if cat_filter:
        data = data[data[cat_filter[0]] == cat_filter[1]]
    if num_filter:
        data = data[data[num_filter[0]] < num_filter[1]]

    # Vérifier si le DataFrame filtré n'est pas vide
    if not data.empty:

       
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



# Exemple d'utilisation de la fonction:
plot_filtered_violin(
    data=merged_df,
    cat_var='city',  # Variable catégorielle pour l'axe des x
    num_var='awardPrice',  # Variable numérique pour l'axe des y
    cat_filter=('city', 'PARIS'),  # Filtrer pour le département '84'
    num_filter=('awardPrice', 10000000)  # Filtrer pour les prix inférieurs à 200000
)




