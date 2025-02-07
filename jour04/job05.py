class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self,largeur,hauteur):
        super().__init__()
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur*self.hauteur
    
class Cercle(Forme):
    def __init__(self,radius):
        super().__init__()
        self.radius = radius
    def aire(self):
        return 3.14*(self.radius**2)

if __name__ == "__main__":
    r = Cercle(5)
    print(r.aire())    
    r = Rectangle(5,5)
    print(r.aire())