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
                data_for_variable[variable] = analyser_varchar_all(variable,"Foppa")
                print(f" ==> {g1}OK{g0}")
            except:
                print(f" ==> {rouge}FAIL{g0}")

        elif info["Type"] == "Numérique":
            print(f"Analyse de : {g1}" + variable + f"{g0}",end="")
            try :
                data_for_variable[variable] = analyser_nombre_all(variable,"Foppa")
                print(f" ==> {g1}OK{g0}")
            except:
                print(f" ==> {rouge}FAIL{g0}")

        open_or_close[variable] = 0
    
    print("Analyse terminée")

    button_size = 50
    grid_size = 6

    frame = tk.Frame(root)
    frame.pack()

    for i, (key, var_name) in enumerate(index_a_variable.items()):
        row = i // grid_size
        col = i % grid_size
        button = tk.Button(frame, text=var_name+"\n("+dict_type_variables[var_name]["Type"]+")", font=("Arial", 12, "bold"), command = lambda vn = var_name: on_button_click(vn))
        button.grid(row=row, column=col, sticky='nsew', padx=2, pady=2)
        button.config(height=button_size//10, width=button_size//10+15)

    for i in range(grid_size):
        frame.grid_columnconfigure(i, weight=1, uniform="group1")
        frame.grid_rowconfigure(i, weight=1, uniform="group1")

    # Start the Tkinter event loop
    root.mainloop()

def open_cmd_and_display_text(text):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.bat', mode='w', newline='\n') as tmpfile:
        tmpfile.write('@echo off\n')
        for line in text.split('\n'):
            safe_line = line.replace('^', '^^').replace('&', '^&').replace('<', '^<').replace('>', '^>').replace('|', '^|').replace('"', '^"')
            # Pour les lignes vides, utilisez "echo.", sinon "echo {safe_line}"
            if not line.strip():  # Vérifie si la ligne est vide ou ne contient que des espaces
                tmpfile.write('echo.\n')
            else:
                tmpfile.write(f'echo {safe_line}\n')
        tmpfile.write('pause > nul\n')
    
    subprocess.run(f'start cmd /k "{tmpfile.name}"', shell=True, check=True)

def on_button_click(var_name):
    print(f"Affichage de : {g1}{var_name}{g0}")
    plt.tight_layout()  # Ajustement automatique
    var_to_chart[var_name].show()
    open_cmd_and_display_text(data_for_variable[var_name])

if __name__ == "__main__":
    main()