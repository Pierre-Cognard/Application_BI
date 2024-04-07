import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Fonction pour calculer la distance géographique
def haversine(lat1, lon1, lat2, lon2):
    rad = np.pi / 180
    r = 6371  # Rayon de la Terre en km
    dlat = (lat2 - lat1) * rad
    dlon = (lon2 - lon1) * rad
    a = np.sin(dlat/2)**2 + np.cos(lat1 * rad) * np.cos(lat2 * rad) * np.sin(dlon/2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    return r * c

# Chargement des données
agents = pd.read_csv('../Foppa/Agents.csv')
agents = agents.dropna(subset=['latitude', 'longitude'])

lots = pd.read_csv('../Foppa/Lots.csv')
lots = lots[lots['awardPrice'] <= 100000]
lots = lots.dropna(subset=['awardPrice'])


lot_buyers = pd.read_csv('../Foppa/LotBuyers.csv')
lot_suppliers = pd.read_csv('../Foppa/LotSuppliers.csv')

# Assurer que les identifiants de lot sont présents dans lotSuppliers
#lot_suppliers['lotId'] = [assign lotIds here based on your data organization]

# Fusion des données des acheteurs
merged_buyers = pd.merge(lots, lot_buyers, on='lotId')
merged_buyers = pd.merge(merged_buyers, agents, left_on='agentId', right_on='agentId', suffixes=('', '_buyer'))

# Fusion des données des fournisseurs
merged_suppliers = pd.merge(lots, lot_suppliers, on='lotId')
merged_suppliers = pd.merge(merged_suppliers, agents, left_on='agentId', right_on='agentId', suffixes=('', '_supplier'))

# Calcul de la distance
merged = pd.merge(merged_buyers, merged_suppliers, on='lotId')

print("merged columns:", merged.columns)
# Calcul de la distance entre les acheteurs et les fournisseurs
merged['distance'] = np.vectorize(haversine)(
    merged['latitude_x'], merged['longitude_x'], 
    merged['latitude_y'], merged['longitude_y']
)

# Analyse de la corrélation entre la distance et le montant du contrat
print("Corrélation entre la distance et le montant du contrat:")
print(merged['distance'].corr(merged['contractDuration_x']))

# Visualisation de la relation entre distance et montant du contrat
plt.scatter(merged['distance'], merged['contractDuration_x'], alpha=0.5)
plt.title('Distance vs Prix du contrat')
plt.xlabel('Distance (km)')
plt.ylabel('Durée du contrat (en mois)')
plt.show()
