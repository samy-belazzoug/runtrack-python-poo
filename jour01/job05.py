class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        """Affiche les coordonnées des points"""
        return f"x : {self.x}\ny : {self.y}"

    def afficherX(self):
        """Affiche x"""
        return self.x

    def afficherY(self):
        """Affiche y"""
        return self.y

    def changerX(self,valeur):
        """Change la valeur de l'attribut x avec le parametre valeur"""
        self.x = valeur

    def changerY(self,valeur):
        """Change la valeur de l'attribut y avec le parametre valeur"""
        self.y = valeur