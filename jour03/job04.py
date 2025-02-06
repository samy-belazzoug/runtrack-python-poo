class Joueur:
    def __init__(self,nom,numero,position,buts:int=0,assists:int=0,jaunes:int=0,rouges:int=0):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts = buts
        self.assists = assists
        self.jaunes = jaunes
        self.rouges = rouges
    
    def nom(self):
        return self.nom
    def numero(self):
        return self.numero
    def position(self):
        return self.position
    
    def setNom(self,valeur):
        self.nom = valeur
    def setNumero(self,valeur):
        self.numero = valeur
    def setPosition(self,valeur):
        self.position += valeur
    
    def setButs(self,valeur):
        self.buts = valeur
    def setAssists(self,valeur):
        self.assists = valeur
    def setJaunes(self,valeur):
        self.jaunes += valeur
    def setRouges(self,valeur):
        self.rouges += valeur

    def marquerUnBut(self):
        self.buts += 1
    
    def effectuerUnePasseDecisive(self):
        self.assists += 1
    
    def recevoirUnCartonJaune(self):
        self.jaunes += 1

    def recevoirUnCartonRouge(self):
        self.rouges += 1
    
    def afficherStatistiques(self):
        print(f"Voici les statistiques de {self.nom} :\nPosition : {self.position} ({self.numero})\nG/A : {self.buts+self.assists} ({self.buts} buts/{self.assists} passes dé)\nCartons jaunes : {self.jaunes}\nCartons rouges : {self.rouges}")

class Equipe:
    def __init__(self,nom:str,joueurs:list=[]):
        self.nom = nom 
        self.joueurs = joueurs

    def ajouterJoueur(self,joueur:Joueur):
        self.joueurs.append(joueur)

    def afficherStatistiquesJoueurs(self):
        [print(Joueur.afficherStatistiques(self.joueurs[i])) for i in range(len(self.joueurs))]
    
    def mettreAJourStatistiquesJoueur(self,joueur:Joueur,attribut:str,valeur):
        if attribut == "nom":
            joueur.setNom(valeur)
        if attribut == "numero":
            joueur.setNumero(valeur)
        if attribut == "position":
            joueur.setPosition(valeur)
        if attribut == "buts":
            joueur.setNom(valeur)
        if attribut == "assists":
            joueur.setNom(valeur)
        if attribut == "jaunes":
            joueur.setNom(valeur)
        if attribut == "rouges":
            joueur.setNom(valeur)       

        
if __name__ == "__main__":
    greenwood = Joueur("greenwood",10,11,0,0,0,0)
    mbemba = Joueur("mbemba",3,3,0,0,0,0)
    henrique = Joueur("henrique",20,7,0,0,0,0)
    rongier = Joueur("rongier",8,5,0,0,0,0)
    hojberg = Joueur("hojberg",6,6)
    
    olympique_marseille = Equipe("Olympique de Marseille")
    olympique_marseille.ajouterJoueur(greenwood)
    olympique_marseille.ajouterJoueur(mbemba)
    olympique_marseille.ajouterJoueur(henrique)
    olympique_marseille.ajouterJoueur(rongier)
    olympique_marseille.ajouterJoueur(hojberg)
    rongier.effectuerUnePasseDecisive
    greenwood.marquerUnBut()
    henrique.recevoirUnCartonJaune()
    rongier.marquerUnBut()
    rongier.recevoirUnCartonRouge()
    olympique_marseille.mettreAJourStatistiquesJoueur(hojberg,"nom","kondogbia")
    olympique_marseille.afficherStatistiquesJoueurs()