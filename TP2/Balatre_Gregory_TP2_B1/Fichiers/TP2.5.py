#Script qui calcule la surface sous la courbe de la fonction y = x * x avec des rectangles avec x appartient [a,b] et un pas p
def Surface():
    print("/Script qui calcule la surface sous la courbe de la fonction y = x * x avec des rectangles avec x appartient [a,b] et un pas p./")
    while True:
        try:
            a = int(input("Entrez a :"))
            b = int(input("Entrez b :"))
            p = float(input("Entrez p :"))
            break
        except:
            print("Seulement les chiffres sont acceptes.")
    U0 = a * a * p
    S = U0
    n = 1
    while (a+ p*n < b):
        Un = (a + p * n) * (a + p * n) * p
        S = Un + S
        n = n + 1
    print(" Le resultat de l'integrale de la fonction y = x * x avec", a, "<= x <", b, "et p =", p, "est", S)


Surface()

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
            Surface()
        elif option == 2:
            exec(open("TP2_Menu.py").read())
        else:
            print('Les seuls choix possible sont 1 ou 2.')
