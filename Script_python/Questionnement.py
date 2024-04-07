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
merged_df = pd.merge(lots_with_agents_df, data[['agentId', 'zipcode', 'department']], on='agentId', how='left')

# Suppression des valeurs manquantes pour les variables utilisées dans le clustering
merged_df.dropna(subset=['zipcode', 'department', 'typeOfContract', 'cpv', 'subContracted'], inplace=True)
merged_df.dropna(subset=['awardPrice', 'contractDuration'], inplace=True)
numeric_features = ['awardPrice', 'contractDuration']
categorical_features = ['zipcode', 'department', 'typeOfContract', 'cpv', 'subContracted']


# Préprocesseur pour encodage One-Hot des variables catégorielles
preprocessor = ColumnTransformer(
    transformers=[
        ('num', Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', StandardScaler())
        ]), numeric_features),
        ('cat', Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ('onehot', OneHotEncoder(handle_unknown='ignore'))
        ]), categorical_features)
    ]
)

# Pipeline de clustering
cluster_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('cluster', KMeans(n_clusters=5, random_state=42))
])

# Application du clustering
cluster_pipeline.fit(merged_df)

# Ajout des étiquettes de cluster au DataFrame
merged_df['cluster'] = cluster_pipeline.named_steps['cluster'].labels_

# Affichage des premières lignes du DataFrame avec clusters
print(merged_df[['cluster', 'zipcode', 'department']].head())

# Utiliser TruncatedSVD pour la réduction de dimensionnalité
svd = TruncatedSVD(n_components=2)
data_svd = svd.fit_transform(cluster_pipeline.named_steps['preprocessor'].transform(merged_df))
# Définition des variables utilisées pour le clustering
variables_used = ['zipcode', 'department', 'typeOfContract', 'cpv', 'subContracted', 'awardPrice', 'contractDuration']

# Statistiques descriptives par cluster pour les variables spécifiques
for i in range(5):
    print(f"\nCluster {i} Statistics:")
    cluster_data = merged_df[merged_df['cluster'] == i][variables_used]  # Restreindre les données aux variables utilisées
    print(cluster_data.describe(include='all').to_string())

# Boxplots pour la variable awardPrice par cluster
plt.figure(figsize=(10, 8))
sns.boxplot(x='cluster', y='awardPrice', data=merged_df)
plt.title('Boxplot de AwardPrice par Cluster')
plt.show()

# Barplots pour une variable catégorielle
category_counts = pd.DataFrame([merged_df.loc[merged_df['cluster'] == i, 'typeOfContract'].value_counts(normalize=True) for i in range(5)])
category_counts.plot(kind='bar', stacked=True)
plt.title('Distribution de TypeOfContract par Cluster')
plt.ylabel('Proportion')
plt.xlabel('Cluster')
plt.show()

# Visualisation des clusters
plt.figure(figsize=(10, 8))
plt.scatter(data_svd[:, 0], data_svd[:, 1], c=merged_df['cluster'], cmap='viridis', alpha=0.5)
plt.colorbar()
plt.title('Visualisation des clusters')
plt.xlabel('Composante SVD 1')
plt.ylabel('Composante SVD 2')
plt.show()

