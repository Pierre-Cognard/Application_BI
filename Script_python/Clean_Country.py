import pandas as pd
import numpy as np
from scipy.spatial import cKDTree
from multiprocessing import Pool

# Charger les données
agents = pd.read_csv('../Foppa_clean/Agents.csv')
geonames = pd.read_csv('../Autres_Sources/geonames-all-cities-with-a-population-500.csv', delimiter=';')
geonames['Coordinates'] = list(zip(geonames['Latitude'], geonames['Longitude']))
geonames_tree = cKDTree(geonames['Coordinates'].tolist())


def find_country(args):
    city, lat, lon = args
    city = city.lower() if pd.notna(city) else None

    matching_countries = geonames[geonames['Name'].str.lower() == city]
    if len(matching_countries) == 1:
        country_code = matching_countries['Country Code'].iloc[0]
        print(f"Matched {city} to {country_code}")

        return country_code  # Retourner le code pays directement

    if not np.isnan(lat) and not np.isnan(lon) and np.isfinite(lat) and np.isfinite(lon):
        try:
            distance, index = geonames_tree.query((lat, lon))
            country_code = geonames.iloc[index]['Country Code']
            return country_code
        except Exception as e:
            return 'Unknown'
    

# Préparer les données pour le multiprocessing
data_to_process = agents[agents['country'].isna()][['city', 'latitude', 'longitude']].apply(tuple, axis=1).tolist()
indices_to_update = agents.index[agents['country'].isna()].tolist()

if __name__ == '__main__':
    with Pool(processes=8) as pool:
        results = pool.map(find_country, data_to_process)
    pool.join()

    # Vérifier que la longueur des résultats correspond aux indices à mettre à jour
    assert len(results) == len(indices_to_update), "Le nombre de résultats ne correspond pas aux indices à mettre à jour"
    # Mise à jour des résultats dans le DataFrame
    agents.loc[indices_to_update, 'country'] = results

    # Sauvegarder les résultats
    agents.to_csv('../Foppa_clean/Agents.csv', index=False)
