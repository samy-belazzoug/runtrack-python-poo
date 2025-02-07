class Vehicule:
    def __init__(self,marque,modele,annee,prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        return f"Voici les informations du vehicule :\nMarque = {self.marque}\nModele = {self.modele}\nAnnée = {self.annee}\nPrix = {self.prix}"
    
    def demarrer(self):
        return "Attention,je roule"

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix,portes=4):
        super().__init__(marque, modele, annee, prix)
        self.portes = portes
    
    def informationsVehicule(self):
        return f"Voici les informations du vehicule :\nMarque = {self.marque}\nModele = {self.modele}\nAnnée = {self.annee}\nPrix = {self.prix}\nNombre de portes = {self.portes}"

    def demarrer(self):
        return "Attention,je pilote"

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix,roues=2):
        super().__init__(marque, modele, annee, prix)
        self.roues = roues

    def informationsVehicule(self):
        return f"Voici les informations du vehicule :\nMarque = {self.marque}\nModele = {self.modele}\nAnnée = {self.annee}\nPrix = {self.prix}\nNombre de roues = {self.roues}"

    def demarrer(self):
        return "Attention pilote préssé, je vais passer en interfile !"

if __name__ == "__main__":
    merco = Voiture("Mercedes","Classe A",2020,18500,4)
    print(merco.informationsVehicule())
    yamaha = Moto("Yamaha","1200Vmax",1987,4500,2)
    print(yamaha.informationsVehicule())
    print(merco.demarrer())
    print(yamaha.demarrer())
