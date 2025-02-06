class CompteBancaire:
    def __init__(self,numero_compte:int,nom:str,prenom:str,solde:float,decouvert:bool=True):
        self.__numero_compte = numero_compte
        self.__nom = nom 
        self.__prenom = prenom 
        self.__solde = solde
        self.decouvert = decouvert

    def afficher(self):
        """Repr de CompteBancaire"""
        return f"Numero de compte : {self.__numero_compte}\nNom-prénom : {self.__nom} {self.__prenom}\nSolde : {self.__solde}"
    
    def afficher_solde(self):
        """Getter de solde"""
        return self.__solde
    
    def versement(self,montant:int):
        """Permet d'ajouter de l'argent au compte"""
        self.__solde += montant
        return self.__solde
    
    def retrait(self,montant:int):
        """Permet de retirer de l'argent du compte"""
        if self.__solde < montant:
            TypeError ("Vous n'êtes pas en capacité financière de retirer cette somme.\nPour être politiquement correcte.")
        self.__solde -= montant
        return self.__solde
    
    def virement(self,compte,montant):
        if self.__solde < montant:
            return f"Pense à ton argent avant de le donner a autrui. Tu ne peux pas donner ce montant."
        self.__solde -= montant
        compte.__solde += montant
        return f"L'argent a bien été viré vers {compte.__nom} {compte.__prenom}"
    
    def agios(self,agios):
        if self.__solde < 0:
            print("Vous avez pas de sous ! Vous allez payer !")
            self.__solde *= agios
    
if __name__ == "__main__":
    rat = CompteBancaire(112213,"Singino","Ratz",15)
    print(rat.afficher())
    print(rat.afficher_solde())
    print(rat.versement(20))
    print(rat.retrait(25))

    singe = CompteBancaire(213112,"Ratonio","Singo",5)
    print(rat.virement(singe,5))
    print(rat.afficher_solde())
    print(singe.afficher_solde())
    print(singe.virement(rat,15))