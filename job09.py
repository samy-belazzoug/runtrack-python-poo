class Produit:
    def __init__(self,nom:str,prixHT,TVA=1.20):
        self.nom = nom 
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        return self.prixHT * self.TVA
    

    def afficher(self):
        return f"Nom du produit : {self.nom}\nPrix (HT) : {self.prixHT}\nTVA : {self.TVA}"
    
if __name__ == "__main__":
    ferrari = Produit("458 Italia",210000)
    print(ferrari.CalculerPrixTTC())
    nike = Produit("Terrascape",185)
    print(nike.CalculerPrixTTC())
    panzani = Produit("Spaghetti",1.70)
    print(panzani.CalculerPrixTTC())
