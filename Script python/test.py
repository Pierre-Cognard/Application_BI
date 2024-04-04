import tkinter as tk
from PIL import Image, ImageTk

print(f"images/variables_individuelles/country.png")

fenetre = tk.Tk()
 
## Ouverture du fichier
image = Image.open('images/variables_individuelles/country.png')
## Remplace PhotoImage de Tkinter par celui de PIL
photo = ImageTk.PhotoImage(image)
 
label = tk.Label(fenetre, image=photo)
label.pack()
 
fenetre.mainloop()