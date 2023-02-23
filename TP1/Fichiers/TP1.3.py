# Ecrit la somme des nombres à partir d'un nombre donnée

def Somme():
    print("/Ecrit la somme des nombres a partir d'un nombre donnee/")
    i = 1
    result = 0
    somme = ""
    while True:                                                                         # Tant que number n'est pas un nombre
        try:
            number = int(input("Rentrez seulement un nombre positif ou negatif : "))
            break
        except:
            print("Seulement les nombres positifs ou négatifs sont autorises !")

    if number < 0:                                                                      # Si number est négatif
        while i <= abs(number):
            if i == abs(number):
                somme = "- " + somme + str(i)
            else:
                somme = somme + str(i) + " - "
            result += i
            i += 1
    else:                                                                               # Si number est positif
        while i <= number:
            if i == number:
                somme = somme + str(i)
            else:
                somme = somme + str(i) + " + "
            result += i
            i += 1

    print("La somme des entiers positifs jusqu'a ce nombre est egale a : ")
    if number < 0:
        print(somme, "= -", result)
        print("-", result, "=", somme)
    else:
        print(somme, "=", result)
        print(result, "=", somme)


Somme()

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
            Somme()
        elif option == 2:
            exec(open("TP1_Menu.py").read())
        else:
            print('Les seuls choix possible sont 1 ou 2.')
