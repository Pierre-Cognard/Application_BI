import pandas as pd
import numpy as np

def replace_non_ints_in_place(csv_file, column_name, replacement_value=""):
    # Charger le fichier CSV
    df = pd.read_csv(csv_file)
    
    # Fonction pour vérifier si une valeur est un entier
    def is_int(val):
        try:
            int(val)
            return True
        except ValueError:
            return False
    
    # Appliquer la fonction pour vérifier les entiers dans la colonne spécifiée
    mask = df[column_name].apply(is_int)

    
    
    # Remplacer les non-entiers par la valeur de remplacement
    df.loc[~mask, column_name] = ""
    
    # Sauvegarder les modifications directement dans le fichier original
    df.to_csv("../Foppa_clean/Lots.csv", index=False)
    #print(f"Les modifications ont été sauvegardées dans test.csv.")

# Utiliser la fonction sur ton fichier CSV et la colonne souhaitée
replace_non_ints_in_place("../Foppa/Lots.csv", "lotsNumber")
