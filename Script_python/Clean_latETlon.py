import pandas as pd
import numpy as np
from scipy.spatial import cKDTree
from multiprocessing import Pool

# Charger les données
agents = pd.read_csv('../Foppa_clean/Agents.csv')
geonames = pd.read_csv('../Autres_Sources/geonames-postal-code.csv', delimiter=';')


def find_coordinates(args):
    city, postal_code = args
    city = city.lower() if pd.notna(city) else None

    # Recherche par le nom de la ville
    if city:
        matched_geo = geonames[geonames['place name'].str.lower() == city]
        if not matched_geo.empty:
            print(f"Matched {city} to {matched_geo.iloc[0]['latitude']}, {matched_geo.iloc[0]['longitude']}")
            return matched_geo.iloc[0]['latitude'], matched_geo.iloc[0]['longitude']

    # Recherche par le code postal si la ville n'est pas disponible ou ne donne aucun résultat
    if pd.notna(postal_code):
        matched_geo = geonames[geonames['postal code'] == postal_code]
        if not matched_geo.empty:
            print(f"Matched {postal_code} to {matched_geo.iloc[0]['latitude']}, {matched_geo.iloc[0]['longitude']}")
            return matched_geo.iloc[0]['latitude'], matched_geo.iloc[0]['longitude']

    return np.nan, np.nan  # Retourner NaN pour latitude et longitude si aucune correspondance n'est trouvée


# Préparer les données avec des coordonnées manquantes
missing_coords = agents[(agents['latitude'].isna()) | (agents['longitude'].isna())]
data_to_process = missing_coords[['city', 'zipcode']].apply(tuple, axis=1).tolist()
indices_to_update = missing_coords.index.tolist()

if __name__ == '__main__':
    with Pool(processes=8) as pool:
        results = pool.map(find_coordinates, data_to_process)
    pool.join()

    # Mettre à jour les résultats dans le DataFrame
    for i, (lat, lon) in zip(indices_to_update, results):
        if pd.notna(lat) and pd.notna(lon):
            agents.at[i, 'latitude'] = lat
            agents.at[i, 'longitude'] = lon

    # Sauvegarder les résultats
    agents.to_csv('../Foppa_clean/Agents.csv', index=False)