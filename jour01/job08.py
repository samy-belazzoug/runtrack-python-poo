class Cercle:
    def __init__(self,rayon):
        self.rayon = rayon
        
    def changerRayon(self,valeur):
        """Change la valeur du Rayon avec le parametre valeur."""
        self.rayon = valeur

    def circonference(self):
        """Calcule la circonférence (périmètre) du cercle
        Rappel : P = 2r x pi"""
        return (2*self.rayon)*3.14

    def aire(self):
        """Calcule l'aire du cercle
        Rappel : A = 3.14 x r²"""
        return 3.14*(self.rayon**2)
    
    def diametre(self):
        """Calcule le diametre du cercle
        Rappel : d = 2 x r"""
        return 2*self.rayon
    
    def afficherInfos(self):
        return f"Voici quelques informations sur votre cercle :\nRayon : {self.rayon}\Circonférence : {self.circonference()}\n"
