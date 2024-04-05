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

   # Filtrer le dataframe si des filtres catégoriels sont fournis
    if cat1_filter:
        if isinstance(cat1_filter[1], list):  # Si c'est une liste
            data = data[data[cat1_filter[0]].isin(cat1_filter[1])]
        else:  # Si c'est une valeur unique
            data = data[data[cat1_filter[0]] == cat1_filter[1]]
    if cat2_filter:
        if isinstance(cat2_filter[1], list):  # Si c'est une liste
            data = data[data[cat2_filter[0]].isin(cat2_filter[1])]
        else:  # Si c'est une valeur unique
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
        #plt.tight_layout()  # Ajustement automatique pour éviter le chevauchement des étiquettes
        plt.show()


        #data = data.sample(frac=0.1, random_state=1)  # Ajustez frac= selon la fraction souhaitée

        # Test du Chi-carré d'indépendance
        contingency_table = pd.crosstab(data[cat_var1], data[cat_var2])
        chi2, p, dof, expected = stats.chi2_contingency(contingency_table)
        print(f"Test du Chi-carré: chi2 = {chi2:.2f}, p-value = {p:.4f}")

        # Test exact de Fisher pour les tableaux 2x2
        if contingency_table.shape[0] == 2 and contingency_table.shape[1] == 2:
            _, p_fisher = stats.fisher_exact(contingency_table)
            print(f"Test exact de Fisher: p-value = {p_fisher:.4f}")

    else:
        print(f"Aucune donnée trouvée pour les filtres fournis: {cat1_filter}, {cat2_filter}")


#######
#
# Ces lignes de code permettent de filtrer les données pour ne conserver que 
# les lignes correspondant aux noms de produits ayant un nombre élevé d'annulations.
#
#######
        

#merged_df['cancelled'] = merged_df['cancelled'].astype(int)
#cancelled_df = merged_df[merged_df['cancelled'] == 1]
#cancelled_counts = cancelled_df['name'].value_counts()
#names_with_high_cancellation = cancelled_counts[cancelled_counts > 2].index.tolist()
#filtered_df = merged_df[merged_df['name'].isin(names_with_high_cancellation)]
#print(filtered_df.head())

# Exemple d'utilisation de la fonction:
plot_filtered_violin(
    data=merged_df,
    cat_var1='cancelled',  # Variable catégorielle pour l'axe des x
    cat_var2='typeOfContract',  # Variable categorielle num 2 ( celle qu'on compare ) pour l'axe des y
    cat1_filter=('cancelled', [1]),
    #cat2_filter=('city', ['AVIGNON','LILLE','TARBES', 'LUNEL', 'LYON', 'MARSEILLE', 'NICE']),  # Filtrer pour le département '84'

)
