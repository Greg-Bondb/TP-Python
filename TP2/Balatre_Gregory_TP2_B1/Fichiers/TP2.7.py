#Fonction calculant le nombre de Fibonacci d’un nombre
def Fibonacci():
    print("/Fonction calculant le nombre de Fibonacci d'un nombre./")
    list = [0, 1]
    while True:
        try:
            num = int(input("Vous voulez que la suite de Fibonacci s'execute jusqu'a n = "))
            if num >= 0:
                break
        except:
            print("Vous n'avez pas choisi un nombre positif ou neutre.")
    while len(list) <= num:
        n1 = list[len(list)-1]
        n = list[len(list)-2]
        list.append(n1 + n)

    print("F [", num, "] = ", list[num])


Fibonacci()

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
            Fibonacci()
        elif option == 2:
            exec(open("TP2_Menu.py").read())
        else:
            print('Les seuls choix possible sont 1 ou 2.')
