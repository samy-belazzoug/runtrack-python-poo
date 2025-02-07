class Personnage:
    def __init__(self,nom:str=0,vie:int=10):
        self.nom = nom 
        self.vie = vie
        
    def get_vie(self):
        return self.vie
    def set_vie(self,valeur):
        self.vie = valeur

    def attaquer(self,adversaire,points):
        adversaire = Personnage
        print(f"{adversaire} a été touché")
        return adversaire.get_vie() - points        

class Jeu:

    liste = []
    def ajouterPersonnage(personnage:Personnage):
        global liste
        return liste.append(personnage)

    def choisirNiveau(niveau:int):
        global liste
        if niveau == 1:
            for personnages in liste:
                personnages.set_vie(200)
        if niveau == 2:
            for personnages in liste:
                personnages.set_vie(100)
        if niveau == 3:
            for personnages in liste:
                personnages.set_vie(50)
    
    def lancerJeu(Niveau):
        Niveau = Jeu.choisirNiveau(Niveau)
        joueur1 = Personnage("Joueur 1",Niveau)
        joueur2 = Personnage("Joueur 2",Niveau)
        Jeu.ajouterPersonnage(joueur1)
        Jeu.ajouterPersonnage(joueur2)

    def checkWin():
        if Personnage.get_vie == 0:
            print("L'adversaire a gagner... Tu reviendra plus fort !")