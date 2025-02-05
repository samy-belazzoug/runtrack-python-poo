class Voiture:
    def __init__(self,marque:str,modele:str,annee:int,kilometrage:int,en_marche:bool=False,reservoir:int=0):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = en_marche
        self.__reservoir = reservoir

    def get_marque(self):
        return self.__marque
    
    def get_modele(self):
        return self.__modele
    
    def get_annee(self):
        return self.__annee
    
    def get_kilometrage(self):
        return self.__kilometrage
    
    def get_en_marche(self):
        return self.__en_marche

    
    def set_marque(self,valeur):
        self.__marque = valeur
    
    def set_modele(self,valeur):
        self.__modele = valeur
    
    def set_annee(self,valeur):
        self.__annee = valeur
    
    def set_kilometrage(self,valeur):
        self.__kilometrage = valeur

    def set_en_marche(self,valeur):
        self.__en_marche = valeur
    
    def __verifier_plein(self):
        return self.__reservoir
    
    def demarrer(self):
        if self.__verifier_plein() > 5:
            self.__en_marche = True
        else:
            print("Pas assez de carburant pour démarrer le V8 atmo...")
    
    def arreter(self):
        self.__en_marche = False

    def __verifier_plein(self):
        return self.__reservoir

if __name__ == "__main__":
    my = Voiture("Mercedes","AMG GT BLACK SERIES",2023,2000,False,0)
    my.demarrer()