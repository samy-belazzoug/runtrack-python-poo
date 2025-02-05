class Commande:
    def __init__(self,numero_commande:int,liste_plats:dict,status_commande:str):
        self.__numero_commande = numero_commande
        self.__liste_plats = liste_plats
        self.__status_commande = status_commande
    
    def ajouter_plat(self,plat:str,prix:float):
        self.__status_commande = "en cours"
        return self.__liste_plats.update({plat:prix})

    def annuler(self):
        self.__liste_plats.clear()
        self.__status_commande = "annulée"
        return self.__status_commande
    
    def total(self)->float:
        self.__status_commande = "en cours"
        total = 0
        for element in self.__liste_plats:
            total += self.__liste_plats[element]
        return total

    def afficher_total(self)->str:
        self.__status_commande = "terminée"
        print(f"Votre commande {self.__numero_commande} :")
        for key in self.__liste_plats:
            total = f"{key} : {self.__liste_plats[key]}€"
            print(total)
        print(f"Total à payer : {self.total()}€")      
    
    def TVA(self):
        return self.total() * 1.20
    
    
    def __repr__(self)->str:
        i = ""
        i += f"{self.__status_commande}"
        for key in self.__liste_plats:
            i +=  f"{key} : {self.__liste_plats[key]}\n"
        i += f"{self.__status_commande}"
        return i 
    

if __name__ == "__main__":
    commande = Commande(113212,{"Tacos" : 7,"Tiramisu" : 2.80},"En cours")
    commande.annuler()
    commande.ajouter_plat("Sandwich Curry",5.50)
    commande.ajouter_plat("Oasis fraise",1.20)
    print(commande.total())
    commande.afficher_total()
    print(commande.TVA())
    print(commande)
