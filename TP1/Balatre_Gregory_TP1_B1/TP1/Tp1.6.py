# Merci d'importer le package math (permet d'effectuer des opérations mathématiques plus complexe)

import math

# Ecrit le logarithme, le sinus et le cosinus d'un entier

def Saisie():
    print("/Ecrit le logarithme, le sinus et le cosinus d'un entier/")
    while True:
        try:
            entier = int(input("Choississez un entier : "))
            break
        except:
            print("Vous n'avez pas choisi un entier (nombre sans virgule) !")

    if entier < 0:
        print("Il n'existe pas de logarithme pour un nombre negatif")
    else:
        print("Le logarithme de cet entier est : ", math.log(int(entier)))

    print("Le sinus de cet entier est de : ", math.sin(int(entier)), "rad")
    print("Le cosinus de cet entier est de : ", math.cos(int(entier)), "rad")


Saisie()

# Liste des options du menu
menu_options = {
    1: 'Restart',
    2: 'Menu',
}

# Print le menu avec les choix possible
def print_menu():
    print("\n")
    for key in menu_options.keys():
        print(key, ')', menu_options[key])


if __name__ == '__main__':
    while (True):
        print_menu()
        option = ''
        try:
            option = int(input('Votre choix: '))
        except:
            print('Seulement les chiffres sont acceptes !')
        # Redirige l'utilisateur en fonction de son choix
        if option == 1:
            Saisie()
        elif option == 2:
            exec(open("TP1_Menu.py").read())
        else:
            print("Les seuls choix possible sont 1 ou 2.")
