import pandas as pd
import numpy as np
from scipy.spatial import cKDTree
from multiprocessing import Pool

# Charger les données
user_data = pd.read_csv('../Foppa_clean/Agents.csv')  # Assurez-vous que le chemin est correct
postal_data = pd.read_csv('../Autres_Sources/geonames-postal-code.csv', delimiter=';')
postal_data['coordinates'] = list(zip(postal_data['latitude'], postal_data['longitude']))
postal_tree = cKDTree(postal_data['coordinates'].tolist())



def find_zipcode(args):
    city, lat, lon, country_code = args
    city = city.lower() if pd.notna(city) else None

    # Étape 1: Recherche par ville
    if city:
        filtered_postal = postal_data[postal_data['place name'].str.lower() == city]
        if not filtered_postal.empty:
            print(f"Matched {city} to {filtered_postal['postal code'].iloc[0]}")
            return filtered_postal['postal code'].iloc[0]


    # Étape 3: Utilisation des coordonnées pour trouver le code postal le plus proche
    if not np.isnan(lat) and not np.isnan(lon) and np.isfinite(lat) and np.isfinite(lon):
        try:
            distance, index = postal_tree.query((lat, lon))
            return postal_data.iloc[index]['postal code']
        except Exception as e:
            print(f"Erreur lors de la recherche spatiale: {e}")
            return 'Unknown'
    return ''  # Retourner 'Unknown' si aucune des méthodes ne trouve de résultat

# Préparer les données pour le multiprocessing
data_to_process = user_data[user_data['zipcode'].isna()][['city', 'latitude', 'longitude', 'country']].apply(tuple, axis=1).tolist()
indices_to_update = user_data.index[user_data['zipcode'].isna()].tolist()

if __name__ == '__main__':
    user_data['zipcode'] = user_data['zipcode'].astype(str)


    with Pool(processes=8) as pool:  # Adaptez le nombre de processus selon les capacités de votre système
        results = pool.map(find_zipcode, data_to_process)
    pool.join()

    # Vérifier que la longueur des résultats correspond aux indices à mettre à jour
    assert len(results) == len(indices_to_update), "Le nombre de résultats ne correspond pas aux indices à mettre à jour"
    # Mise à jour des résultats dans le DataFrame
    user_data.loc[indices_to_update, 'zipcode'] = results

    # Sauvegarder les résultats
    user_data.to_csv('../Foppa_clean/Agents.csv', index=False)
