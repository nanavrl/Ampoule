from tkinter import *

def inverser():
    lampeEteinte = c1.itemcget(m0, "state")=="hidden" # connaitre l'état de la lampe
    if lampeEteinte :
           c1.itemconfigure(m0, state='normal')       # montrer l'image i0 lampe allumée
           c1.itemconfigure(m1, state='hidden')       # cacher l'image i1
    else :
           c1.itemconfigure(m0, state='hidden')       # cacher l'image i0
           c1.itemconfigure(m1, state='normal')       # montrer l'image i1 lampe éteinte

fenetre = Tk()                                        # créer la fenêtre
c1 = Canvas(fenetre, height=150,  width=100 )         # definir la zone de dessin
c1.pack()
i0 = PhotoImage(file="Off107x128.png")                # charger la photo "Off107x128.png"
i1 = PhotoImage(file="On107x128.png")                 # charger la photo "On107x128.png"
m1=c1.create_image(0, 0, anchor=NW, image=i1)         # ajouter la photo i1 au canvas c1
m0=c1.create_image(0, 0, anchor=NW, image=i0)         # supperposer photo i0
Button(fenetre, text='On/Off', command=inverser).pack()  # Appeler le sous-programme allumer
fenetre.mainloop()                          # Affiche la fenêtre en boucle
