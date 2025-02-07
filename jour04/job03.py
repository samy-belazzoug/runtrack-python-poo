class Rectangle:
    def __init__(self,longueur,largeur):
        self.__longueur = longueur 
        self.__largeur = largeur
    
    def perimetre(self):
        return (self.__longueur+self.__largeur)*2
    
    def surface(self):
        return self.__longueur*self.__largeur
    
    def getLongueur(self):
        return self.__longueur
    
    def getlargeur(self):
        return self.__largeur
    
    def setLongueur(self,value):
        self.__longueur = value
    
    def setLongueur(self,value):
        self.__largeur = value
    
class parallelepipede(Rectangle):
    def __init__(self, longueur, largeur,hauteur):
        super().__init__(longueur, largeur)
        self.hauteur = hauteur

    def volume(self):
        return self.getLongueur()*self.getlargeur()*self.hauteur

if __name__ == "__main__":
    r = Rectangle(5,6)
    print(r.perimetre())
    print(r.surface())
    p = parallelepipede(5,6,5)
    print(p.volume())