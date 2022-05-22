from tkinter import *  # pour créer les fenêtre
import os  # pour aller chercher un fichier
import sqlite3  # pour accéder à la base de donnée
from tkinter import messagebox
import webbrowser
from turtle import color, textinput
import random
from tkinter import filedialog  # ouvrir un fichier

# ajout des variables
global nomsJoueurs
nomsJoueurs = ["Jean", "Jeanne"]

global resultot
resultot = 21

global frame1
frame1 = Frame

global labelPoints
labelPoints = Label

global imageFleche
imageFleche = "C:\\Users\\chris\\OneDrive\\Images\\fleche.png"

totMatches = [21.00]


# Pour changer la couleur du texte dans Label
def randomColor():
    colors = ["red", "orange", "green", "blue", "indigo", "violet"]
    labelResultat.config(text=str(joueur), font=('Goudy Old Style0', 30), \
                         bg="moccasin", fg=random.choice(colors))


# Pour choisir un nom de joueur de façon aléatoire et l'afficher
def lancer(nomsJoueurs):
    canvas.destroy()
    global joueur
    labelCtaki.config(text="C'est à vous, ", font=('Goudy Old Style', 30), \
                      bg="moccasin", fg="slategrey", bd=1)
    labelCtaki.place(x=45, y=95)
    colors = ["red", "orange", "green", "blue", "indigo", "violet"]
    joueur = random.choice(nomsJoueurs)
    print(joueur)
    labelResultat.config(fg=random.choice(colors))
    labelResultat.config(text=str(joueur), font=('Goudy Old Style', 30), \
                         bg="moccasin")

    labelResultat.place(x=110, y=185)
    return joueur


# pour afficher le résultat allumettes restantes
def result():
    labelCtaki.config(text="", font=('Goudy Old Style', 30), \
                      bg="moccasin", fg="slategrey", bd=1)
    tot = (choix.get())
    resultot = totMatches[0] - tot
    resultot = int(resultot)
    if resultot <= 0:
        labelResultat.config(text="")
        labelCtaki.config(text="")
        # BoutonLancer.destroy()
        labelResultat.config(text="Vous avez perdu..." + str(joueur))

    elif resultot > 1:
        labelResultat.config(text="Il reste " + str(resultot) + " allumettes.")
    else:
        labelResultat.config(text="Il reste " + str(resultot) + " allumette.")
    totMatches[0] = resultot


# work in progress
def interfaceDepart():
    root.mainloop


# creation de la fenêtre
root = Tk()
root.geometry('600x450')
root.title("Le jeu des allumettes")
#os.chdir("C:\\Users\\chris\\OneDrive\\Images")  # appelle de l'endroit ou se trouve le fichier
#root.iconbitmap("allumettes.ico")
root.config(background="moccasin")

# interfaceDepart()

label_title = Label(root, text="Bienvenue au jeu des allumettes", \
                    font=('Showcard Gothic', 20), bg="antiquewhite", fg="darkorange", bd=1, relief=RIDGE)
label_title.place(x=60, y=8)

# creation d'image
width = 65
heigt = 55
#image = PhotoImage(file=imageFleche)
#image.zoom(10)  # importer l'image, personnalisation zoom=taille de l'image.
#image.subsample(62)  # sub=pattern
canvas = Canvas(root, width=width, height=heigt)  # espace pour dessiner un composant graphique (images ,formes, ...)
#canvas.create_image(width / 2.5, heigt / 1.9, image=image)  # pour avoir le centre de l'image
canvas.place(x=220, y=90)

# création boutons radio
choix = DoubleVar(value=1)
match = Frame(root)
match.place(x=70, y=270)
match.config(bg="#FF9966")
for name, value in [
    ('- 1 allumette ', 1),
    ('- 2 allumettes', 2),
    ('- 3 allumettes', 3),
]:
    matches = Radiobutton(match, bg="#FF9966", font=("Berlin Sans Fb", 18), \
                          text=name, variable=choix, value=value)
    matches.grid()

# création du boutton lancer
BoutonLancer = Button(root, bg="#66FF99", font=("Berlin Sans Fb", 22), \
                      text='Lancer', width=8, height=2, command=lambda: lancer(nomsJoueurs))
BoutonLancer.place(x=350, y=80)
# Label indication joueur

labelCtaki = Label(root, text="Appuyer\n     sur\n           Lancer", \
                   font=("Arial", 20), bg="moccasin", fg="mediumblue", bd=1)
labelCtaki.place(x=5, y=75)
# Résultat du random joueur
labelResultat = StringVar()
labelResultat = ""
labelResultat = Label(root, font=(15), bg='moccasin', fg='black')
labelResultat.place(x=330, y=300)

# création du boutton Confirmer
buttonConfirm = Button(root, text='Confirmer', font=("Berlin Sans Fb", 22), \
                       width=10, height=1, command=result)
buttonConfirm.place(x=330, y=270)

# création du boutton Quitter
buttonQuitter = Button(root, text=' Quitter ', bg="tomato", \
                       font=('Franklin Gothic Demi', 12), width=6, height=1, \
                       command=root.destroy)
buttonQuitter.place(x=480, y=400)
# bouton réinitialiser
buttonInitialiser = Button(root, text="Recommencer", bg="lightcyan", \
                           font=('Franklin Gothic Demi', 12), width=12, height=1, command=interfaceDepart)
buttonInitialiser.place(x=300, y=400)

choix.set(None)  # Désactiver les coches au départ
root.mainloop()



# -----------------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------

