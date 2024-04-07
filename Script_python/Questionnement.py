import pandas as pd

# Chargement des données
lots = pd.read_csv('../Foppa/Lots.csv')

# Affichage des premières lignes pour vérifier la structure des données
print(lots.head())
# Groupe par 'typeOfContract'
grouped = lots.groupby('typeOfContract')

# Calcul du nombre de lots, du montant moyen du contrat et du prix estimé moyen par type de contrat
stats_by_contract_type = grouped.agg({
    'lotId': 'count',  # Nombre de lots
    'awardPrice': 'mean',  # Montant moyen du contrat
    'awardEstimatedPrice': 'mean'  # Prix estimé moyen
}).rename(columns={'lotId': 'Number of Lots', 'awardPrice': 'Average Award Price', 'awardEstimatedPrice': 'Average Estimated Price'})

# Affichage des résultats
print(stats_by_contract_type)

import matplotlib.pyplot as plt

# Graphique pour le nombre de lots par type de contrat
stats_by_contract_type['Number of Lots'].plot(kind='bar', title='Number of Lots by Contract Type')
plt.xlabel('Type of Contract')
plt.ylabel('Number of Lots')
plt.show()

# Graphique pour le montant moyen du contrat par type de contrat
stats_by_contract_type['Average Award Price'].plot(kind='bar', title='Average Award Price by Contract Type')
plt.xlabel('Type of Contract')
plt.ylabel('Average Award Price')
plt.show()