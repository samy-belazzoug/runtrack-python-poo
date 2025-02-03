class Produit:
    def __init__(self,nom:str,prixHT,TVA=1.20):
        self.nom = nom 
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        """Calcule le prix du produit avec la TVA"""
        return self.prixHT * self.TVA
    
    def set_prix(self,valeur):
        """Modifie le prix du produit"""
        self.prixHT = valeur

    def set_nom(self,valeur:str):
        """Modifie le nom du produit"""
        self.nom = valeur
    
    def set_TVA(self,valeur):
        raise TypeError ("Navré de vous dire que vous n'êtes pas le gouvernement.\nCa serait trop beau n'est-ce pas !")
    
    def get_nom(self):
        """Modifie le prix du produit"""
        return self.nom

    def get_prixHT(self):
        """Modifie le nom du produit"""
        return self.prixHT
    
    def get_TVA(self,valeur:str,prixchange=0):
        """Modifie le nom du produit"""
        return self.TVA

    def afficher(self):
        return f"Nom du produit : {self.nom}\nPrix (HT) : {self.prixHT}\nTVA : {self.TVA}"
    
if __name__ == "__main__":
    ferrari = Produit("458 Italia",210000)
    print(ferrari.CalculerPrixTTC())
    ferrari.set_nom("SF90")
    ferrari.set_prix(600000)
    print(ferrari.CalculerPrixTTC())
    
    nike = Produit("Terrascape",185)
    print(nike.CalculerPrixTTC())
    nike.set_nom("Mercurial Superfly 10")
    nike.set_prix(66.49)
    print(nike.CalculerPrixTTC())
    
    panzani = Produit("Spaghetti",1.70)
    print(panzani.CalculerPrixTTC())
    panzani.set_nom("Pesto Verde")
    panzani.set_prix(2.10)      
    print(panzani.CalculerPrixTTC())