# Calcule la surface d'un trapeze

def Surface_Trapeze():
    print("/Calcule la surface d'un trapeze/")
    grande_base = (input("Rentrez la valeur de la Grande base du trapeze : "))
    petite_base = (input("Rentrez la valeur de la petite base du trapeze : "))
    hauteur = (input("Rentrez la valeur de la hauteur du trapeze : "))
    while not grande_base.isdigit() or not petite_base.isdigit() or not hauteur.isdigit():      # Tant que les entrées ne sont pas toutes des entiers/nombres
        print("Seulement les chiffres sont autorises !")
        grande_base = (input("Rentrez la valeur de la Grande base du trapeze : "))
        petite_base = (input("Rentrez la valeur de la petite base du trapeze : "))
        hauteur = (input("Rentrez la valeur de la hauteur du trapeze : "))

    grande_base = int(grande_base)
    petite_base = int(petite_base)
    hauteur = int(hauteur)
    resultat = (grande_base + petite_base) * hauteur * 1 / 2
    print("L'aire du trapeze est de : ", resultat)


Surface_Trapeze()

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
            Surface_Trapeze()
        elif option == 2:
            exec(open("TP1_Menu.py").read())
        else:
            print('Les seuls choix possible sont 1 ou 2.')
