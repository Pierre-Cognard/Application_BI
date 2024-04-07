import pandas as pd
import numpy as np
from scipy.spatial import cKDTree
from multiprocessing import Pool

# Charger les données
agents = pd.read_csv('../../Foppa_clean/Agents.csv')
geonames = pd.read_csv('../../geonames-all-cities-with-a-population-500.csv', delimiter=';')
geonames['Coordinates'] = list(zip(geonames['Latitude'], geonames['Longitude']))
geonames_tree = cKDTree(geonames['Coordinates'].tolist())

# Dictionnaire pour les codes de pays
country_codes = {
    'France': 'FR',
    'Italy': 'IT',
    'Spain': 'ES',
    'Germany': 'DE',
    'United Kingdom': 'GB',
    'United States': 'US',
    'Canada': 'CA',
    'Australia': 'AU',
    'Brazil': 'BR',
    'India': 'IN',
    'China': 'CN',
    'Russia': 'RU',
    'Japan': 'JP',
    'South Korea': 'KR',
    'Mexico': 'MX',
    'Sweden': 'SE',
    'Norway': 'NO',
    'Poland': 'PL',
    'Netherlands': 'NL',
    'Belgium': 'BE',
    'Switzerland': 'CH',
    'Turkey': 'TR',
    'Saudi Arabia': 'SA',
    'South Africa': 'ZA',
    'Nigeria': 'NG',
    'Egypt': 'EG',
    'Brazil': 'BR',
    'Argentina': 'AR',
    'Chile': 'CL',
    'Peru': 'PE',
    'Colombia': 'CO',
    'Venezuela': 'VE',
    'Malaysia': 'MY',
    'Singapore': 'SG',
    'Indonesia': 'ID',
    'Thailand': 'TH',
    'Vietnam': 'VN',
    'Philippines': 'PH',
    'Pakistan': 'PK',
    'Bangladesh': 'BD',
    'Iran': 'IR',
    'Iraq': 'IQ',
    'Afghanistan': 'AF',
    'United Arab Emirates': 'AE',
    'Israel': 'IL',
    'Qatar': 'QA',
    'New Zealand': 'NZ',
    'Ireland': 'IE',
    'Portugal': 'PT',
    'Greece': 'GR',
    'Hungary': 'HU',
    'Austria': 'AT',
    'Czech Republic': 'CZ',
    'Romania': 'RO',
    'Denmark': 'DK',
    'Finland': 'FI',
    'Slovakia': 'SK',
    'Bulgaria': 'BG',
    'Croatia': 'HR',
    'Lithuania': 'LT',
    'Slovenia': 'SI',
    'Estonia': 'EE',
    'Latvia': 'LV',
    'Luxembourg': 'LU',
    'Cyprus': 'CY',
    'Malta': 'MT',
    'Iceland': 'IS',
    'Monaco': 'MC',
    'Liechtenstein': 'LI',
    'Norway': 'NO',
    'Sweden': 'SE',
    'Finland': 'FI',
}


def find_country(args):
    city, lat, lon = args
    city = city.lower()  # Convertir la ville en minuscule

    matching_countries = geonames[geonames['Name'].str.lower() == city]['Country'].unique()
    if len(matching_countries) == 1:
        country_name = matching_countries[0]
        return country_codes.get(country_name, 'Unknown')

    if not np.isnan(lat) and not np.isnan(lon) and np.isfinite(lat) and np.isfinite(lon):
        try:
            distance, index = geonames_tree.query((lat, lon))
            country_name = geonames.iloc[index]['Country']
            return country_codes.get(country_name, 'Unknown')
        except Exception as e:
            return 'Unknown'
    else:
        return 'Unknown'

# Préparer les données pour le multiprocessing
data_to_process = agents[agents['country'].isna() & agents['latitude'].notna() & agents['longitude'].notna()][['city', 'latitude', 'longitude']].apply(tuple, axis=1).tolist()
indices_to_update = agents.index[agents['country'].isna() & agents['latitude'].notna() & agents['longitude'].notna()].tolist()

if __name__ == '__main__':
    with Pool(processes=8) as pool:
        results = pool.map(find_country, data_to_process)
    pool.join()

    # Vérifier que la longueur des résultats correspond aux indices à mettre à jour
    assert len(results) == len(indices_to_update), "Le nombre de résultats ne correspond pas aux indices à mettre à jour"

    # Mise à jour des résultats dans le DataFrame
    agents.loc[indices_to_update, 'country'] = results

    # Sauvegarder les résultats
    agents.to_csv('../../Foppa_clean/Agents_updated.csv', index=False)
