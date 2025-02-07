class Carte:
    def __init__(self,valeur,couleur,points=0):
        self.valeur = valeur
        self.couleur = couleur
        self.points = points
        if self.valeur in [2,3,4,5,6,7,8,9,10]:
            self.points = self.valeur
        if self.valeur in ["J","Q","K"]:
            self.points = 10
        if self.valeur == "A":
            points = int(input(""))




class Jeu:
    def __init__(self,paquet:list):
        self.paquet = paquet

    def ajouterCarte(self,carte):
        self.paquet.append(carte)

    trA = Carte("A","trefle")
    coA = Carte("A","coeur") 
    caA = Carte("A","carreau")
    piA = Carte("A","pique")
    ajouterCarte(trA)
    ajouterCarte(coA)
    ajouterCarte(caA)
    ajouterCarte(piA)

    tr2 = Carte("2","trefle") 
    co2 = Carte("2","coeur") 
    ca2 = Carte("2","carreau")
    pi2 = Carte("2","pique")  
    ajouterCarte(tr2)
    ajouterCarte(co2)
    ajouterCarte(ca2)
    ajouterCarte(pi2)

    tr3 = Carte("3","trefle") 
    co3 = Carte("3","coeur") 
    ca3 = Carte("3","carreau")
    pi3 = Carte("3","pique")  
    ajouterCarte(tr3)
    ajouterCarte(co3)
    ajouterCarte(ca3)
    ajouterCarte(pi3)

    tr4 = Carte("4","trefle") 
    co4 = Carte("4","coeur") 
    ca4 = Carte("4","carreau")
    pi4 = Carte("4","pique")  
    ajouterCarte(tr4)
    ajouterCarte(co4)
    ajouterCarte(ca4)
    ajouterCarte(pi4)

    tr5 = Carte("5","trefle")  
    co5 = Carte("5","coeur") 
    ca5 = Carte("5","carreau")
    pi5 = Carte("5","pique")  
    ajouterCarte(tr5)
    ajouterCarte(co5)
    ajouterCarte(ca5)
    ajouterCarte(pi5)

    tr6 = Carte("6","trefle")  
    co6 = Carte("6","coeur") 
    ca6 = Carte("6","carreau")
    pi6 = Carte("6","pique")  
    ajouterCarte(tr6)
    ajouterCarte(co6)
    ajouterCarte(ca6)
    ajouterCarte(pi6)

    tr7 = Carte("7","trefle")  
    co7 = Carte("7","coeur") 
    ca7 = Carte("7","carreau")
    pi7 = Carte("7","pique")  
    ajouterCarte(tr7)
    ajouterCarte(co7)
    ajouterCarte(ca7)
    ajouterCarte(pi7)

    tr8 = Carte("8","trefle")  
    co8 = Carte("8","coeur") 
    ca8 = Carte("8","carreau")
    pi8 = Carte("8","pique")  
    ajouterCarte(tr8)
    ajouterCarte(co8)
    ajouterCarte(ca8)
    ajouterCarte(pi8)

    tr9 = Carte("9","trefle")  
    co9 = Carte("9","coeur") 
    ca9 = Carte("9","carreau")
    pi9 = Carte("9","pique")  
    ajouterCarte(tr9)
    ajouterCarte(co9)
    ajouterCarte(ca9)
    ajouterCarte(pi9)

    tr10 = Carte("10","trefle")  
    co10 = Carte("10","coeur")
    ca10 = Carte("10","carreau")
    pi10 = Carte("10","pique") 
    ajouterCarte(tr10)
    ajouterCarte(co10)
    ajouterCarte(ca10)
    ajouterCarte(pi10)

    trJ = Carte("J","trefle")  
    coJ = Carte("J","coeur")
    caJ = Carte("J","carreau")
    piJ = Carte("J","pique") 
    ajouterCarte(trJ)
    ajouterCarte(coJ)
    ajouterCarte(caJ)
    ajouterCarte(piJ)

    trQ = Carte("Q","trefle")  
    coQ = Carte("Q","coeur")
    caQ = Carte("Q","carreau")
    piQ = Carte("Q","pique") 
    ajouterCarte(trQ)
    ajouterCarte(coQ)
    ajouterCarte(caQ)
    ajouterCarte(piQ)

    trK = Carte("K","trefle")  
    coK = Carte("K","coeur")
    caK = Carte("K","carreau")
    piK = Carte("K","pique")
    ajouterCarte(trK)
    ajouterCarte(coK)
    ajouterCarte(caK)
    ajouterCarte(piK)