# Merci d'importer le package math (permet d'effectuer des opérations mathématiques plus complexe)
import math

#Programme qui calcule la suite (R n )
def Suite():
    print("/Programme qui calcule la suite (R n )./")
    i = 1
    Rep = 0
    while True:
        try:
            print("La suite (Rn) est la suivante : R1 = racine de 5 et Rn+1 =  racine de (2+Rn)")
            num = int(input("Vous voulez que la fonction s'execute jusqu'a n = "))
            if num >= 1:
                break
        except:
            print("Vous n'avez pas choisi un nombre entier positif.")
    while i <= num:
        if i == 1:
            Rep = math.sqrt(2)
            print("R" + str(i), "=", Rep)
        elif i%10 == 0:
            Rep = math.sqrt(2 + Rep)
            print("R" + str(i), "=", Rep)
        else:
            Rep = math.sqrt(2 + Rep)
        i += 1
    print("Le resultat de R" + str(i-1), "est", Rep)
    print("On remarque que cette suite tant vers le resultat positif de la resolution de l'equation x au carre - x - 2, qui est egal a 2")


Suite()

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
            Suite()
        elif option == 2:
            exec(open("TP2_Menu.py").read())
        else:
            print('Les seuls choix possible sont 1 ou 2.')
