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
    def information(self):
        print("\nVoici vos informations :")
        print(f"Votre nom : {self.nom}\nVotre prenom : {self.prenom}\nVotre adresse : {self.adresse}\nVotre numero de telephone : {self.numero}")
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

# création de la classe Etudiant
class Etudiant(Personne):
    def __init__(self, matiere, note, nom, prenom, adresse, numero):
        self.matiere = matiere
        self.note = note
        self.dico = {}
        super().__init__(nom, prenom, adresse, numero)

    # fonction qui permet de créer une matiere ou d'ajouter des notes au personnage
    def notation(self):
        while True:
            try:
                self.matiere = str(input("\nNom de la matiere :"))
                self.note = float(input("Note :"))
                break
            except:
                print("La matiere doit etre un string et la note un int ou un float !")
        if self.matiere in self.dico:
            i = 0
            tab = self.note
            tableau = self.dico[self.matiere]
            while i < 1:
                tableau.append(tab)
                i += 1
            self.dico[self.matiere] = tableau
        else:
            tab = [self.note]
            self.dico[self.matiere] = tab
        print(f"Vous avez ajoute la note de {self.note} pour la matiere {self.matiere} a {str(self.nom)}")
        time.sleep(3)

    # fonction qui affiche les notes du personngae
    def affichage(self):
        if self.dico == {}:
            print("Vous n'avez pas de notes")
        else:
            for i in self.dico.keys():
                print(i, ":", self.dico[i])

    # fonction qui supprime les notes du personnage
    def suppr(self):
        if self.dico == {}:
            print("Vous n'avez pas de notes")
            return
        while True:
            try:
                print("Voici les matieres disponibles : ")
                for i in self.dico.keys():
                    print("-", i)
                self.matiere = str(input("\nA quelle matiere voulez vous acceder :"))
                print(f"Voici les notes disponibles pour cette matiere: {self.dico[self.matiere]}")
                self.note = float(input("Quelle note voulez vous supprimer : "))
                if self.note in self.dico[self.matiere]:
                    self.dico[self.matiere].remove(self.note)
                    # supprime la matiere si il n'y a plus de note
                    if not self.dico[self.matiere]:
                        del(self.dico[self.matiere])
                    print(f"Vous avez supprime le note de {self.note} a {self.prenom} {self.nom}")
                    time.sleep(3)
                    break
            except:
                print("Vous n'avez pas choisi des entrees valides !")

    # fonction menu de la classe Personne
    def Menu(self):
        while True:
            print("\n1) Ajouter une nouvelle note \n2) afficher les notes \n3) supprimer une note \n4) revenir en arriere")
            try:
                n = int(input("Quel choix voulez vous faire :"))
                if n == 1:
                    self.notation()
                elif n == 2:
                    self.affichage()
                elif n == 3:
                    self.suppr()
                elif n == 4:
                    self.__repr__()
                else:
                    print("Vous n'avez pas choisi un nombre compris entre 1 et 4.\n")
            except:
                print("Seulement les chiffres sont acceptes.\n")

    # fonction menu de la classe Etudiant
    def __repr__(self):
        while True:
            print("\n0) quitter l'exercice\n1) creer un personnage\n2) modifier le personnage\n3) afficher le personnage\n4) Notes du personnage")
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
                    self.information()
                elif n == 4 and type(self.nom) == str:
                    self.Menu()
                else:
                    print("Commencez d'abord par vous identifier !")
            except:
                print("Seulement les chiffres sont acceptes !")

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
                print(Etudiant(str, float, str, str, str, int))
            elif option == 2:
                exec(open("TP3_Menu.py").read())
            else:
                print('Les seuls choix possible sont 1 ou 2.')


print(Etudiant(str, float, str, str, str, int))