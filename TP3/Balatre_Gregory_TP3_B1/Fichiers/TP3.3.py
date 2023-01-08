# merci d'importer la bibliotheque random
import random


# fonction qui simule le jeu du 421 avec 3 dées
def f421():
    while True:
        try:
            print("\nProgramme qui simule le lancer de 3 des afin d'obtenir en 3 lancers max : 4 2 1")
            n = int(input("Combien de parties voulez vous jouer :"))
            break
        except:
            print("Seulement les chiffres sont acceptes.")

    ran = []
    game = 1
    win = 0
    lose = 0
    # compteur de partie
    while game <= n:
        print("\n")
        compteur = 0
        list = []
        # compteur de tour
        while compteur < 3:
            tabtempo = []
            index = 0
            # choisie le nombre de dée en fonction de de la len de la list 421
            if len(list) == 0:
                ran = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
            elif len(list) == 1:
                ran = [random.randint(1, 6), random.randint(1, 6)]
            elif len(list) == 2:
                ran = [random.randint(1, 6)]
            print('Lancer {} avec {} des : {}   '.format(compteur+1, len(ran), str(ran)[1:-1]), end="")
            # compte le nombre de 4, 2 et 1 dans la liste (permet d'éviter de faire une boucle) et les ajoute si obtenu
            while index < len(ran):
                if ran.count(4) >= 1 and list.count(4) == 0:
                    list.append(4)
                    tabtempo.append(4)
                if ran.count(2) >= 1 and list.count(2) == 0:
                    list.append(2)
                    tabtempo.append(2)
                if ran.count(1) >= 1 and list.count(1) == 0:
                    list.append(1)
                    tabtempo.append(1)
                index += 1
                # met la liste dans l'odre : 4 2 1
                list == list.sort(reverse=True)
            # exprime le résultat du lancé
            if len(tabtempo) == 3:
                print(' je garde {}, {} et {}   '.format(tabtempo[0], tabtempo[1], tabtempo[2]), list)
            elif len(tabtempo) == 2:
                print(' je garde {} et {}   '.format(tabtempo[0], tabtempo[1]), list)
            elif len(tabtempo) == 1:
                print(f' je garde {tabtempo[0]}   ', list)
            else:
                print(' je ne garde rien   ', list)
            compteur += 1
            # win et lose
            if len(list) == 3:
                print("Partie", game, "gagnee en", compteur, "coup")
                win += 1
                break
            elif compteur == 3:
                print("Partie", game, "perdue")
                lose += 1
        game += 1
    # calcule le % de gain
    result = (win/(win+lose))*100
    print('\n Vous avez joue {} parties, {} gagnees pour {} perdue soit {}% de gain.'.format(win+lose, win, lose, round(result, 2)))


f421()

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
        if option == 1:  # Redirige l'utilisateur en fonction de son choix
            f421()
        elif option == 2:
            exec(open("TP3_Menu.py").read())
        else:
            print('Les seuls choix possible sont 1 ou 2.')
