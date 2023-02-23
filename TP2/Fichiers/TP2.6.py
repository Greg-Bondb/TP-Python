# Merci d'importer le package math (permet d'effectuer des opérations mathématiques plus complexe)
import math

#Code de la fonctions exponentielle et du sinus
def Exponentielle():
    print("/Code de la fonctions exponentielle et du sinus./")
    while True:
        try:
            print("Ce script calcule la fonction e puissance x")
            x = float(input("Entrez x :"))
            break
        except:
            print("Seulement les chiffres sont acceptes.")
    n = 0
    F = (x**n)/(Factorielle(n))
    result = F

    while n < 100:
        if n == 0:
            result = result
        else:
            result = result + (x**n)/(Factorielle(n))
        n = n + 1

    print("Le resultat de l'integrale de la fonction e puissance,", x, "est", result)
    print("Le résultat trouve par la bibliotheque math:", math.exp(x))

def Sinus():
    while True:
        try:
            print("\nCe Script calcule la fonction sin x")
            x = float(input("Entrez x :"))
            break
        except:
            print("Seulement les chiffres sont acceptes.")
    n = 1
    result = x

    while n < 50:
        n = n + 1
        var0 = (-1)**(n - 1)
        var1 = (x**((2 * n) - 1))
        var2 = Factorielle((2 * n) - 1)
        result = result + (var0*(var1/var2))

    print("Le résultat trouvé par la fonction:", result)
    print("Le résultat trouvé par la bibliothèque math:", math.sin(x))

#Algorithme pour faire la factorielle d'un nombre (on peut aussi utiliser math.factorial avec la bibliothèque math).
def Factorielle(nb):
    facto = 1
    i = 1
    while i <= nb:
        facto = facto * i
        i += 1
    return facto


Exponentielle()
Sinus()

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
            Exponentielle()
            Sinus()
        elif option == 2:
            exec(open("TP2_Menu.py").read())
        else:
            print('Les seuls choix possible sont 1 ou 2.')
