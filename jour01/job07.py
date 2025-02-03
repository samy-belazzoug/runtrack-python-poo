class Personnage:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def gauche(self):
        """Positionne le personnage vers la gauche"""
        self.x -= 1

    def droite(self):
        """Positionne le personnage vers la droite"""
        self.x += 1
    
    def bas(self):
        """Positionne le personnage vers le bas"""
        self.y -= 1
    
    def haut(self):
        """Positionne le personnage vers le haut"""
        self.y += 1
    
    def position(self)->tuple:
        return (self.x,self.y)
    