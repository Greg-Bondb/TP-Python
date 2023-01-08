# merci d'importer la bibliotheque random
import random


# fonction qui simule le jeu des allumettes avec un ordinateur
def Allumette():
    print("\nLa regle : il y a plusieurs allumettes (autant qu'on le veut) et on en retire 1,2 ou 3 et celui qui prend la derniere a perdu.")
    while True:
        try:
            name = input("Entrez votre nom :")
            n = int(input("Nombre d'allumettes de depart :"))
            if n > 0:
                break
            else:
                print("Vous n'avez pas choisi un nombre positif")
        except:
            print("Seulement les chiffres sont acceptes.")

    # utilise l'aléatoire pour savoir qui commence
    if random.randint(1, 2) == 1:
        # joueur
        turn = 1
    else:
        # ordinateur
        turn = 2
    nb = 0

    while True:
        # enleve le nombre d'allumettes choisie au tour précédant
        n -= nb
        alu = "|" * n
        if turn == 1:
            # win du joueur
            if alu == "":
                print("l'ordinateur a perdu :-(")
                print(name, " a gagne :-)")
                break
            # tour du joueur
            while True:
                try:
                    nb = int(input("Combien d'allumettes voulez vous enlevez :"))
                    if nb > n:
                        print("Vous ne pouvez pas enlevez plus d'allumettes qu'il n'en reste")
                    elif 4 > nb > 0:
                        break
                    else:
                        print("Vous n'avez pas choisi un nombre comprit entre 1 et 3")
                except:
                    print("Seulement les chiffres sont acceptes.")
            print(alu, name, "enleve", nb)
            turn += 1
        # tour de l'ordinateur
        else:
            # win de l'ordinatuer
            if alu == "":
                print(name, "a perdu :-(")
                print("l'ordinateur a gagne :-)")
                break
            # stratégie ordinateur
            elif n == 4:
                nb = 3
            elif n == 3:
                nb = 2
            elif n == 2:
                nb = 1
            else:
                nb = random.randint(1, 3)
            print(alu, "ordinateur enleve", nb)
            turn -= 1


Allumette()

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
            Allumette()
        elif option == 2:
            exec(open("TP3_Menu.py").read())
        else:
            print('Les seuls choix possible sont 1 ou 2.')
