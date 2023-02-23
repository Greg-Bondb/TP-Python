# Merci d'importer le package math (permet d'effectuer des opérations mathématiques plus complexe)
import math

#Trouve les racines d'une équation du second degré.
def Second_degre():
    print("/Trouve les racines d'une equation du second degre./")
    while True:
        try:
            print("Resoudre l'equation du second degre : Ax2 + Bx + C = 0")
            A = int(input("Entrez A :"))
            B = int(input("Entrez B :"))
            C = int(input("Entrez C :"))
            break
        except:
            print("Seulement les chiffres sont acceptes.")
    delta = B**2 - 4 * A * C
    if delta < 0:
        print("Il n'y a pas de racine pour cette equation du second (delta est negatif)")
    elif delta == 0:
        print("Il y a une racine pour cette equation du second (delta est egal a zero)")
        x1 = -B / (2 * A)
        print(x1)
    elif delta > 0:
        print("Il y a deux racines pour cette equation du second (delta est supperieur a zero)")
        x1 = (-B - math.sqrt(delta)) / (2 * A)
        print(x1)
        x2 = (-B + math.sqrt(delta)) / (2 * A)
        print(x2)


Second_degre()

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
        if option == 1:                                         # Redirige l'utilisateur en fonction de son choix
            Second_degre()
        elif option == 2:
            exec(open("TP2_Menu.py").read())
        else:
            print('Les seuls choix possible sont 1 ou 2.')
