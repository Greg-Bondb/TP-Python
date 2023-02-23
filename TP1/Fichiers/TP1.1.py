# Transforme un caractère en un nombre et un entier en caractère.

def Types_predefinis():
    print("/Transforme un caractere en un nombre et un entier en caractere/")
    caractere = str(input("Choississez un caractere : "))       # Prend un caractère en entrée et le transforme en en un nombre
    while len(caractere) != 1:
        print("Vous n'avez pas choisi un caractere !")
        caractere = str(input("Choississez un caractere : "))
    print(caractere, "vaut", (ord(caractere)))
    entier = (input("Choississez un entier : "))                # Prend un entier en entrée
    while not entier.isdigit():                                 # Tant que l'entrée n'est pas égale à un entier/nombre
        print("Vous n'avez pas choisi un entier !")
        entier = (input("Choississez un entier : "))
    print(int(entier), "vaut", (chr(int(entier))))


Types_predefinis()

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
            Types_predefinis()
        elif option == 2:
            exec(open("TP1_Menu.py").read())
        else:
            print('Les seuls choix possible sont 1 ou 2.')
