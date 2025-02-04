class Rectangle:
    def __init__(self,longueur,largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        """Getter de l'attribut privé longueur"""
        return self.__longueur

    def get_largeur(self):
        """Getter de l'attribut privé largeur"""
        return self.__largeur

    def set_longueur(self,valeur):
        """Setter de l'attribut privé longueur"""
        self.__longueur = valeur
    
    def set_largeur(self,valeur):
        """Setter de l'attribut privé largeur"""
        self.__largeur = valeur

if __name__ == "__main__":
    rect = Rectangle(10,5)
    rect.set_longueur(15)
    rect.set_largeur(9)
    print(rect.get_longueur())
    print(rect.get_largeur())