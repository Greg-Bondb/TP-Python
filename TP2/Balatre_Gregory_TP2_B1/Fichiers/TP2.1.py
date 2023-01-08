#Algorithme qui demande successivement 10 nombres à l’utilisateur, et qui lui dit ensuite quel était le plus grand nombres.
def Le_plus_grand():
    print("/Algorithme qui demande successivement 10 nombres a l'utilisateur, et qui lui dit ensuite quel etait le plus grand nombres./")
    i = 0
    reponse = 0
    list = []
    rang = 0
    while i < 10:
        try:
            print("Entrez le nombre numero", i+1, ":", end=' ')
            list.append(float(input()))
            if reponse < list[i]:
                reponse = list[i]
                rang = i+1
                i += 1
            else:
                i += 1
        except:
            print("Seulement les chiffres sont acceptes.")

    print(reponse, "est le plus grand nombre que vous aillez donne.")
    print("C'etait le nombre numero :", rang)


Le_plus_grand()

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
            Le_plus_grand()
        elif option == 2:
            exec(open("TP2_Menu.py").read())
        else:
            print('Les seuls choix possible sont 1 ou 2.')
