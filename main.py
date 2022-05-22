# Fenêtre principale, sera reliée à SQLite

from tkinter import *  # pour créer les fenêtre
from random import randint  # fonction pour générer un nombre aléatoire
import os  # pour aller chercher un fichier
import sqlite3  # pour accéder à la base de donnée
import time  # pour afficher le temps
from tkinter import messagebox
import webbrowser  # import pages internet# pour valider les noms


# Label valider
def valider():
    chn = entryUn.get() + " et " + entryDeux.get() + " !!! \nAppuyer sur commencer... "
    labelValider.config(text="Bonjour " + chn)


# pour effacer les entréees de l'utilisateur
def initialiser():
    labelValider.config(text="")
    entryUn.delete(0, END)
    entryDeux.delete(0, END)
    entryUn.focus_set()


# Pour ouvrir la fenêtre fille contenant le jeu, ne fonctionne pas, work in progress ;)
def NewWindow():
    print ("eeee")
    window.destroy()


# Message box boutton 'quitter'
def ExitApp():
    MsgBox = messagebox.askquestion('Exit game of matches', 'Really quit the game?', icon='error')
    if MsgBox == 'yes':
        window.destroy()
    else:
        messagebox.showinfo('Welcome Back', 'Welcome back to the game!!!')


# pour appeler pages règles jeu des allumettes

def openRules():
    webbrowser.open_new("https://fr.wikipedia.org/wiki/Jeux_de_Nim")


### Créer un objet-connexion à la base de données, à l’aide de la fonction-fabrique connect()

### Créer un autre objet-interface cursor() sur la connexion créée ci-dessus

# Création fenêtre principale

window = Tk()  # création de la fenêtre
window.title("Le jeu des allumettes")  # mettre un titre à la fenêtre
window.geometry("850x580")  # taille de la fenêtre à l'ouverture
window.minsize(480, 360)  # taille min de la fenêtre
# code couleur (https://htmlcolorcodes.com/fr/)
window.config(background="seagreen")  # pour changer la couleur de l'intérieur de la fenêtre

# Pour mettre une image devant le titre de la fenêtre (https://image.online-convert.com/fr/convertir-en-ico) 
# convertit l'image en .ico pour pixels correcte par rapport à la taille de l'image

##os.chdir("C:\\Users\\chris\\OneDrive\\Images")  # appelle de l'endroit ou se trouve le fichier
##window.iconbitmap("allumettes.ico")  # appelle le nom du fichier

# creation d'image
width = 200
heigt = 200
#image = PhotoImage(file="C:\\Users\\chris\\OneDrive\\Images\\allumettes - Copie.png")
#image.zoom(60)  # importer l'image, personnalisation zoom=taille de l'image.
#image.subsample(62)  # sub=pattern

# canvas: espace pour dessiner un composant graphique (images ,formes, ...)
canvas = Canvas(window, width=width, height=heigt, bg="seagreen")

#canvas.create_image(width / 3, heigt / 3, image=image)  # pour avoir le centre de l'image
canvas.grid(row=2, column=4, columnspan=2, padx=100, pady=0, sticky="s")

# Insertion de la date
date = time.strftime('%A,%d/%m/%Y', time.localtime())  # jour de la semaine, date - mois - année
date_jour = Label(window, text=date)
date_jour.grid(row=0, column=1)  # positionnement de la date
date_jour.configure(font=("Berlin Sans Fb", 12), bg="Grey", fg="Yellow", bd=1, relief=RAISED)

# les labels
# Label est un widget utilisé pour implémenter des boîtes d'affichage dans lesquelles vous pouvez placer du texte ou des images.

# Message de bienvenue
label_title = Label(window, text="Bienvenue au jeu des allumettes", font=("Arial", 20), bg="forestgreen", fg="white", \
                    bd=1, relief=SUNKEN)
label_title.grid(row=0, column=2, columnspan=3)
# La méthode grid() | Tkinter Python 3. ==> Gestionnaires de positionnement
# Ce gestionnaire de géométrie organise les widgets dans un tableau à deux dimensions.
# Le widget maître est divisé en un certain nombre de lignes et de colonnes, et
# chaque « cellule » du tableau résultant peut contenir un widget

# Label demande nom des joueurs
labelNul = Label(window, bg="seagreen")  # position  vide
labelNul.grid(row=1)
labelUn = Label(window, text="Joueur 1, entrez votre prénom: ", font=("Arial", 15), bg="forestgreen", fg="darkred",
                bd=1)
labelUn.grid(row=2, column=1, padx=20, pady=60)
labelDeux = Label(window, text="Joueur 2, entrez votre prénom: ", font=("Arial", 15), bg="forestgreen", fg="darkred",
                  bd=1)
labelDeux.grid(row=3, column=1)

# label de la chaîne de validation
labelValider = Label(window, bg="seagreen", font=("Arial", 15), fg="darkred", bd=1)
labelValider.grid(row=5, column=2, columnspan=2, sticky="NESW", padx=10)

# les entrées des noms joueurs
entryUn = Entry(window)
entryUn.grid(row=2, column=2, padx=20, pady=60)
entryDeux = Entry(window)
entryDeux.grid(row=3, column=2)

# les boutons de commande

# bouton 'quitter'
buttonQuitter = Button(window, text=' Quitter ', bg="silver", command=ExitApp)
buttonQuitter.grid(row=4, column=4, padx=10, pady=60)

# bouton 'valider'
buttonValider = Button(window, text=' Valider ', bg="silver", command=valider)
buttonValider.grid(row=4, column=2, padx=10)

# bouton 'initialiser'
buttonInitialiser = Button(window, text=' Réinitialiser ', bg="silver", command=initialiser)
buttonInitialiser.grid(row=4, column=1, padx=10)

# bouton 'commencer', devrait ouvrir la feêtre 'root.Toplevel()', ne fonctionne pas actuellement
buttonBegin = Button(window, text="Commencer", bg="crimson", command=NewWindow)
buttonBegin.grid(row=5, column=4, padx=10, pady=60)

# bouton lien internet, règles du jeu
labelRegle = Button(window, text="Les règles du jeu.", command=openRules)
labelRegle.grid(row=5, column=1, padx=20, pady=60)

# w.mainloop()
window.mainloop()


# ---------------------------------   APRES COFIMER ---------------------------------------------------
print ('reprise main')
import Loop
