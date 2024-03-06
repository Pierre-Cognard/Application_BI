import os
import pandas as pd

def lister_variables_dans_csv(dossier):
    variables = set()  # Utiliser un set pour éviter les doublons
    for fichier in os.listdir(dossier):
        if fichier.endswith('.csv'):  # Vérifier si le fichier est un CSV
            chemin_complet = os.path.join(dossier, fichier)
            try:
                # Lire seulement la première ligne pour obtenir les noms de colonnes
                df = pd.read_csv(chemin_complet, nrows=0)  # nrows=0 signifie aucune ligne de données, juste les en-têtes
                # Ajouter les noms des colonnes au set des variables
                for colonne in df.columns:
                    if "Id" not in colonne and "id" not in colonne:  # Cette vérification est insensible à la casse
                        variables.add(colonne)
            except Exception as e:
                print(f"Erreur lors de la lecture du fichier {fichier}: {e}")
    return variables

# Exemple d'utilisation
dossier = '../Foppa'  # Remplacez cela par le chemin réel vers votre dossier de fichiers CSV
variables = lister_variables_dans_csv(dossier)
print("Liste des variables :")
cpt = 1
for variable in variables:
    print(str(cpt)+" - "+str(variable))
    cpt+=1
