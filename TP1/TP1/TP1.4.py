# Ecrit la factorielle d'un nombre donnée

def Factorielle():
    print("/Ecrit la factorielle d'un nombre donnee/")
    i = 1
    result = 1
    somme = ""
    number = input("Rentrez un nombre positifs : ")
    while not number.isdigit():                                         #Tant que l'entrée (number) n'est pas un nombre
        print("Seulement les nombres positifs sont autorises !")
        number = input("Rentrez un nombre positif : ")

    while i <= int(number):
        if i == int(number):
            somme = somme + str(i)
        else:
            somme = somme + str(i) + " x "
        result = result * i
        i += 1

    print("La factorielle de", number, "vaut :")
    print(somme, "=", result)
    print(result, "=", somme)


Factorielle()

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
            Factorielle()
        elif option == 2:
            exec(open("TP1_Menu.py").read())
        else:
            print('Les seuls choix possible sont 1 ou 2.')
