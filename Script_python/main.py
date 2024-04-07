from holi import *
from analyse_nombre import *
from analyse_varchar import *
import tkinter as tk
import ui
from threading import Thread


def main():
    global fig
    root = tk.Tk()
    app = ui.App(root) # creation de l'interface tkinter

    app.analyser_all("Foppa") # lancement thread analyse de toutes les variables
    #app.analyser_all("Foppa_clean")

    #app.analyse_variables("Foppa_clean") # lancement thread analyse de toutes les variables

    #thread = Thread(target = analyser_toutes_les_variables, args=("Foppa",))
    #thread.start()


    #thread.join()

    """thread2 = Thread(target = app.analyser_toutes_les_variables, args=("Foppa_clean",))
    thread2.start()"""





    root.mainloop()


if __name__ == "__main__":
    main()