# Liste des options du menu

menu_options = {
    1: 'Suite de Syracuse',
    2: 'Jeu des allumettes',
    3: '421',
    4: 'Classe Personne',
    5: 'Classe Etudiant',
    6: 'Exit',
}


# Print le menu avec les choix possible
def print_menu():
    for key in menu_options.keys():
        print(key, ')', menu_options[key])


if __name__ == '__main__':
    while (True):
        print("\nListe des exercices disponibles :\n")
        print_menu()
        option = ''
        try:
            option = int(input('Choississez un exercice: '))
        except:
            print('Seulement les chiffres sont acceptés !')
        if option == 1:                                             # Redirige l'utilisateur en fonction de son choix
            exec(open("Fichiers/TP3.1.py").read())
        elif option == 2:
            exec(open("Fichiers/TP3.2.py").read())
        elif option == 3:
            exec(open("Fichiers/TP3.3.py").read())
        elif option == 4:
            exec(open("Fichiers/TP3.4.py").read())
        elif option == 5:
            exec(open("Fichiers/TP3.5.py").read())
        elif option == 6:
            print('Fin du programme')
            exit()
        else:
            print('Veillez entrer un chiffre compris entre 1 et 6.')
