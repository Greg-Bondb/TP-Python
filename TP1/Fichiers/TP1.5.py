# Ecrit la table de multiplication d'un nombre donnée

def Multiplication():
    print("/Ecrit la table de multiplication d'un nombre donnee/")
    i = 0
    compteur = 1
    a = 0
    while a == 0:                                                       # Tant que l'entrée n'est pas un nombre positif ou négatif
        number = input("Rentrez un nombre (positif ou negatif): ")
        if number[0] == "-" or number[0].isdigit():
            i += 1
            while i < len(number):
                if number[i].isdigit():
                    i += 1
                else:
                    a = -1
                    i += 1
            a += 1
        else:
            a = 0
    while compteur <= 10:                                               # Permet de print la table de multiplication ligne par ligne
        print(number, "x", compteur, "=", int(number) * compteur)
        compteur += 1


Multiplication()

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
            Multiplication()
        elif option == 2:
            exec(open("TP1_Menu.py").read())
        else:
            print('Les seuls choix possible sont 1 ou 2.')
