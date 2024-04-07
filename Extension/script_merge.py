import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.cluster import KMeans
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import seaborn as sns

# Chargement des données (chemins à ajuster selon l'emplacement de vos fichiers)
data = pd.read_csv('../Autres_Sources/df_agents_merged_activity.csv')
lots_df = pd.read_csv('../Foppa/Lots.csv')
lot_buyers_df = pd.read_csv('../Foppa/LotBuyers.csv')
lot_suppliers_df = pd.read_csv('../Foppa/LotSuppliers.csv')
criteria_df = pd.read_csv('../Foppa/Criteria.csv')

# Fusion des DataFrames
lots_with_agents_df = pd.merge(lots_df, lot_buyers_df[['lotId', 'agentId']], on='lotId', how='left')
merged_df = pd.merge(lots_with_agents_df, data, on='agentId', how='left')

# Compter la fréquence des codes d'activité
activity_frequency = merged_df['activitePrincipaleEtablissement'].value_counts()

# Afficher les codes les plus fréquents
print(activity_frequency.head())

# Créez un graphique en barres des activités principales les plus fréquentes.
plt.figure(figsize=(10, 6))
activity_frequency.head(15).plot(kind='bar', color='skyblue')  # Les 10 codes d'activité les plus fréquents.
plt.title('Top 10 des activités principales des établissements')
plt.xlabel('Code d\'activité principale')
plt.ylabel('Nombre d\'établissements')
plt.xticks(rotation=45)
plt.tight_layout()  # Ajuste automatiquement les paramètres de la subplot.
plt.show()