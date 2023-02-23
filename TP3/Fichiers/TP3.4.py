# merci d'importer la bibliotheque time
import time


# création de la classe Personne
class Personne:
    # initialisation des variables
    def __init__(self, nom, prenom, adresse, numero):
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse
        self.numero = numero

    # fonction pour creer un personnage
    def creation(self):
        while True:
            try:
                self.nom = input("\nQuel est votre nom :")
                self.prenom = input("Quel est votre prenom :")
                self.adresse = input("Quel est votre adresse :")
                self.numero = str(input("Quel est votre numero de telephone :"))
                if self.verifinput(self.nom, self.prenom, self.numero):
                    print("\nVos informations ont bien ete enregistrees.")
                    break
            except:
                print("\nVeillez respecter la syntaxe donnee.")

    # fonction pour modifier un personnage
    def modif(self):
        while True:
            try:
                self.nom = str(input(f"\n(Ancien nom {self.nom}) Votre nouveau nom :"))
                self.prenom = str(input(f"(Ancien nom {self.prenom})Votre nouveau prenom :"))
                self.adresse = input(f"(Ancien nom {self.adresse})Votre nouvelle adresse :")
                self.numero = input(f"(Ancien nom {self.numero})Votre nouveau numero de telephone :")
                if self.verifinput(self.nom, self.prenom, self.numero):
                    print("Vos nouvelles informations ont bien ete enregistrees.")
                    break
            except:
                print("\nVeillez respecter la syntaxe donnee.")

    # fonction pour afficher un personnage
    def affichage(self):
        print("\nVoici vos informations :")
        print(f"Votre nom : {self.nom}\nVotre prenom : {self.prenom}\nVotre adresse : {self.adresse}\nVotre numero : {self.numero}\n")
        time.sleep(3)

    # fonction pour vérifier les informations du personnages
    def verifinput(self, nom, prenom, number):
        tabnum = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        a = 0
        for i in range(len(number)):
            if i == 0 and number[i] == "+":
                a += 0
            elif number[i] not in tabnum:
                a += 1
        if a == 0 and nom.isalpha() is True and prenom.isalpha() is True:
            return True
        else:
            print("\nVeillez respecter la syntaxe donnee.")
            return False

    # fonction menu de la classe Personne
    def __repr__(self):
        while True:
            print("\n0) quitter l'exercice\n1) creer un personnage\n2) modifier le personnage\n3) afficher le personnage")
            try:
                n = int(input("Quel choix voulez vous faire :"))
                if n == 0:
                    self.print_menu()
                elif n == 1 and type(self.nom) == str:
                    rep = str(input(f"vous etes sure de vouloir supprimer {self.prenom} {self.nom} (o/n) :"))
                    if rep == "o" or rep == "O":
                        self.creation()
                elif n == 1 and type(self.nom) != str:
                    self.creation()
                elif n == 2 and type(self.nom) == str:
                    self.modif()
                elif n == 3 and type(self.nom) == str:
                    self.affichage()
                else:
                    print("Commencez d'abord par vous identifier !")
            except:
                print("Seulement les chiffres sont acceptes.")

    # Print le menu avec les choix possible
    def print_menu(self):
        # Liste des options du menu
        menu_options = {
            1: 'Restart',
            2: 'Menu',
        }
        while True:
            print("\n")
            for key in menu_options.keys():
                print(key, ')', menu_options[key])
            option = ''
            try:
                option = int(input('Votre choix: '))
            except:
                print('Seulement les chiffres sont acceptes !')
            if option == 1:  # Redirige l'utilisateur en fonction de son choix
                print(Personne(str, str, str, str))
            elif option == 2:
                exec(open("TP3_Menu.py").read())
            else:
                print('Les seuls choix possible sont 1 ou 2.')


print(Personne(str, str, str, str))