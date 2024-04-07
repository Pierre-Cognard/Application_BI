import pandas as pd
from tqdm import tqdm

# Charger la table 'agents'
agents = pd.read_csv('../Foppa_clean/Agents_updated.csv')

# Spécifier les colonnes à charger depuis le fichier Sirene
cols_to_use = ['siret', 'etablissementSiege', 'etatAdministratifEtablissement']

# Estimer le nombre total de lignes dans le fichier pour configurer la barre de progression
total_rows = sum(1 for _ in open('../StockEtablissement_utf8.csv', 'r', encoding='utf-8')) - 1  # Soustraire 1 pour l'en-tête

# Initialiser un DataFrame vide pour les résultats de la fusion
merged_data = pd.DataFrame()

chunksize = 10**5  # Vous pouvez ajuster cela selon votre mémoire disponible

with tqdm(total=total_rows, unit='row') as pbar:
    for chunk in pd.read_csv('../StockEtablissement_utf8.csv', usecols=cols_to_use, chunksize=chunksize):
        # Fusionner le chunk avec la table 'agents' sur 'siret'
        merged_chunk = agents.merge(chunk, on='siret', how='left')
        
        # Ajouter les résultats au DataFrame final
        merged_data = pd.concat([merged_data, merged_chunk], ignore_index=True)
        
        # Mise à jour de la barre de progression
        pbar.update(chunksize)

# Sauvegarder les résultats
merged_data.to_csv('Agents_merged.csv', index=False)
