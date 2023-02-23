#Creation de la suite O(n) = F(n+1)/F(n)
def Golden_number():
    print("/Creation de la suite O(n) = F(n+1)/F(n)./")
    listfibo = [0, 1, 1]
    func = []
    while True:
        try:
            print("O(n) = F(n+1)/F(n) avec F(n) qui represente la valeur de Fibonacci a l'ordre n.")
            num = int(input("Choississez la valeur de n = "))
            if num >= 1:
                break
        except:
            print("Vous n'avez pas choisi un nombre positif.")

    while len(listfibo) <= num + 2:
        if len(func) == 1:
            print("O [", len(func), "] = ", func[len(func) - 1])
        n1 = listfibo[len(listfibo) - 1]
        n = listfibo[len(listfibo) - 2]
        listfibo.append(n1 + n)
        func.append(n1 / n)
        if len(func) % 5 == 0 and len(func) != num:
            print("O [", len(func), "] = ", func[len(func) - 1])


    print("O [", len(func), "] = ", func[len(func) - 1])
    print("On remarque que plus n est grand, plus la fonction nous retourne un nombre proche de celui du nombre d'or (~1,618).")


Golden_number()

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
            Golden_number()
        elif option == 2:
            exec(open("TP2_Menu.py").read())
        else:
            print('Les seuls choix possible sont 1 ou 2.')
