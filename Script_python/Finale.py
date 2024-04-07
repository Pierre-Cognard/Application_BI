from holi import *
from analyse_nombre import *
from analyse_varchar import *
import tkinter as tk
import ui

def main():
    global fig
    root = tk.Tk()
    app = ui.App(root) # creation de l'interface tkinter

    app.long_running_task() # lancement thread analyse de toutes les variables
    



    root.mainloop()


if __name__ == "__main__":
    main()