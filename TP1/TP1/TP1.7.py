# Ecrit la mensualité d'un crédit à taux fixe

def Credit():
    print("/Ecrit la mensualites d'un credit a taux fixe/")
    while True:
        try:
            capital = float(input("Montant du capital emprunte :"))
            taux = float(input("Taux annuel (en pourcentage):"))
            annees = float(input("Sur combien d'annees :"))
            if capital <= 0 or taux <= 0 or annees <= 0:
                print("Seulement les chiffres positifs sont acceptes.")
            else:
                break
        except:
            print("Seulement les chiffres positifs sont acceptes.")

    mensuel = (taux/100)/12
    mois = annees * 12
    div = ((1 + mensuel) ** mois) / (((1 + mensuel) ** mois) - 1)
    result = capital * mensuel * div
    print("Vous devez remboursez", round(result, 2), "euros par mois")


Credit()

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
            Credit()
        elif option == 2:
            exec(open("TP1_Menu.py").read())
        else:
            print('Les seuls choix possible sont 1 ou 2.')
