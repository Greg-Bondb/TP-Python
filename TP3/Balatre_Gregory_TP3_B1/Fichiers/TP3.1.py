# fonction qui calcule la suite de Syracuse pour un nombre N donnée
def Syracuse():
    print("\nLa suite de Syracuse est definie de la maniere suivante : pour tout N > 0, U0 = N et Un+1 = Un/2 si Un est pair et 3Un + 1 si un est impair.")
    while True:
        try:
            N = int(input("Rentrez la valeur de N :"))
            if N > 0:
               break
            else:
                print("Vous n'avez pas choisi un nombre > 0")
        except:
            print("Seulement les chiffres sont acceptes.")

    n = 0
    print("U", n, "=", float(N))
    # vérifie si N est pair ou impair
    while N != 1:
        if N % 2 == 0:
            N = N/2
        else:
            N = 3 * N + 1
        n += 1
        print("U", n, "=", N)


Syracuse()

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
            Syracuse()
        elif option == 2:
            exec(open("TP3_Menu.py").read())
        else:
            print('Les seuls choix possible sont 1 ou 2.')
