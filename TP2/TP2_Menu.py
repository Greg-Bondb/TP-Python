# Liste des options du menu

menu_options = {
    1: 'Le plus grand',
    2: 'Le tierce',
    3: 'Second degre',
    4: 'Suite',
    5: 'Surface',
    6: 'Exponentielle',
    7: 'Fibonacci',
    8: 'Golden number',
    9: 'Exit',
}


# Print le menu avec les choix possible
def print_menu():
    for key in menu_options.keys():
        print(key, ')', menu_options[key])


if __name__ == '__main__':
    while (True):
        print_menu()
        option = ''
        try:
            option = int(input('Choississez un exercice: '))
        except:
            print('Seulement les chiffres sont acceptés !')
        if option == 1:                                             # Redirige l'utilisateur en fonction de son choix
            exec(open("Fichiers/TP2.1.py").read())
        elif option == 2:
            exec(open("Fichiers/TP2.2.py").read())
        elif option == 3:
            exec(open("Fichiers/TP2.3.py").read())
        elif option == 4:
            exec(open("Fichiers/TP2.4.py").read())
        elif option == 5:
            exec(open("Fichiers/TP2.5.py").read())
        elif option == 6:
            exec(open("Fichiers/TP2.6.py").read())
        elif option == 7:
            exec(open("Fichiers/TP2.7.py").read())
        elif option == 8:
            exec(open("Fichiers/TP2.8.py").read())
        elif option == 9:
            print('Fin du programme')
            exit()
        else:
            print('Veillez entrer un chiffre compris entre 1 et 8.')
