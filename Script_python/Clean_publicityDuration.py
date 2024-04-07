import pandas as pd
import numpy as np

def read_csv(csv_file, column_name, replacement_value=""):
    # Charger le fichier CSV
    df = pd.read_csv(csv_file)
    
    df[column_name] = pd.to_numeric(df[column_name], errors='coerce')
    
    df.loc[df[column_name] > 1000, column_name] = replacement_value
    df.loc[df[column_name] < 0, column_name] = replacement_value

    
    
    # Sauvegarder les modifications directement dans le fichier original
    df.to_csv("test.csv", index=False)
    print(f"Les modifications ont été sauvegardées dans test.csv.")

# Utiliser la fonction sur ton fichier CSV et la colonne souhaitée
read_csv("../Foppa_clean/Lots.csv", "publicityDuration")
