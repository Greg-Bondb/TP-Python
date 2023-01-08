#Algorithme qui permet de connaître ses chances de gagner au tiercé, quarté, quinté et autres impôts volontaires.
def Le_tierce():
    print("/Algorithme qui permet de connaître ses chances de gagner au tierce, quarte, quinte et autres impots volontaires./")
    while True:
        try:
            n = int(input("Le nombre de chevaux partants :"))
            p = int(input("Le nomber de chevaux joues :"))
            if 0 <= p <= n:
                break
            else:
                print("Vous avez une mise impossible !")
        except:
            print("Seulement les chiffres sont acceptes.")
    X = int((Factorielle(n)) / (Factorielle(n - p)))
    Y = int((Factorielle(n)) / (Factorielle(p) * Factorielle(n - p)))
    print("Dans l'ordre : vous avez 1 chance sur", X, "de gagner")
    print("Dans le desordre : vous avez 1 chance sur", Y, "de gagner")

#Algorithme pour faire la factorielle d'un nombre (on peut aussi utiliser math.factorial avec la bibliothèque math).
def Factorielle(nb):
    facto = 1
    i = 1
    while i <= nb:
        facto = facto * i
        i += 1
    return facto


Le_tierce()

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
            Le_tierce()
        elif option == 2:
            exec(open("TP2_Menu.py").read())
        else:
            print('Les seuls choix possible sont 1 ou 2.')
