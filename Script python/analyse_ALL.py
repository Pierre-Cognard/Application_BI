import os
import pandas as pd
from dict_variables import dict_type_variables
from holi import *
from analyse_nombre import *
from analyse_varchar import *
import tkinter as tk
import subprocess
import tempfile

var_to_chart = {}
data_for_variable = {}
open_or_close = {}


def main():
    global fig
    root = tk.Tk()
    root.title("Variables a analyser")

    cpt = 1  # Initialisation du compteur
    index_a_variable = {}  # Dictionnaire pour mapper le numéro (cpt) à la clé de dict_type_variables

    for variable, info in dict_type_variables.items():
        index_a_variable[str(cpt)] = variable  # Associe le compteur actuel à la clé 'variable'
        cpt += 1

        if (info["Type"] == "Textuelle" or info["Type"] == "Categorielle"):
            print(f"Analyse de : {g1}" + variable + f"{g0}",end="")
            try :
                var_to_chart[variable], data_for_variable[variable] = analyser_varchar_all(variable)
                print(f" ==> {g1}OK{g0}")
            except:
                print(f" ==> {rouge}FAIL{g0}")

        elif info["Type"] == "Numérique" and variable != "tenderNumber":
            print(f"Analyse de : {g1}" + variable + f"{g0}",end="")
            try :
                var_to_chart[variable], data_for_variable[variable] = analyser_nombre_all(variable)
                print(f" ==> {g1}OK{g0}")
            except:
                print(f" ==> {rouge}FAIL{g0}")

        open_or_close[variable] = 0
    


    button_size = 50
    grid_size = 6

    frame = tk.Frame(root)
    frame.pack()

    for i, (key, var_name) in enumerate(index_a_variable.items()):
        row = i // grid_size
        col = i % grid_size
        button = tk.Button(frame, text=var_name, command=lambda vn=var_name: on_button_click(vn))
        button.grid(row=row, column=col, sticky='nsew', padx=2, pady=2)
        # Make the buttons square
        button.config(height=button_size//10, width=button_size//10+15)

    for i in range(grid_size):
        frame.grid_columnconfigure(i, weight=1, uniform="group1")
        frame.grid_rowconfigure(i, weight=1, uniform="group1")

    # Start the Tkinter event loop
    root.mainloop()

def open_cmd_and_display_text(text):
    # Crée un fichier batch temporaire
    with tempfile.NamedTemporaryFile(delete=False, suffix='.bat', mode='w', newline='\n') as tmpfile:
        # S'assure que '@echo off' est la première ligne
        tmpfile.write('@echo off\n')
        for line in text.split('\n'):
            # Échappe les caractères spéciaux potentiels dans 'line'
            safe_line = line.replace('^', '^^').replace('&', '^&').replace('<', '^<').replace('>', '^>').replace('|', '^|').replace('"', '^"')
            tmpfile.write(f'echo {safe_line}\n')
        tmpfile.write('pause > nul\n')  # Ajoute une pause sans afficher "Appuyez sur une touche pour continuer..."
    
    # Exécute le fichier batch dans une nouvelle fenêtre de commande
    subprocess.run(f'start cmd /k "{tmpfile.name}"', shell=True, check=True)

def on_button_click(var_name):
    print(f"Affichage de : {g1}{var_name}{g0}")
    plt.tight_layout()  # Ajustement automatique
    var_to_chart[var_name].show()
    open_cmd_and_display_text(data_for_variable[var_name])

if __name__ == "__main__":
    main()