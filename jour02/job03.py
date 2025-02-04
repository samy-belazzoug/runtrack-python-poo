class Livre:
    def __init__(self,titre:str,auteur:str,nb_pages:int,disponible:bool=True):
        self.__titre = titre 
        self.__auteur = auteur
        self.__nb_pages = nb_pages
        self.__disponible = disponible
    
    def get_titre(self):
        """Getter de l'attribut privé titre"""
        return self.__titre

    def get_auteur(self):
        """Getter de l'attribut privé auteur"""
        return self.__auteur

    def get_nb_pages(self):
        """Getter de l'attribut privé nb_pages"""
        if self.__nb_pages >=0:
            return self.__nb_pages
        else:
            return TypeError ("Tu ne peux pas avoir un nombre de pages negatif.. Tu n'es pas la physique.")

    def set_titre(self,valeur):
        """Setter de l'attribut privé titre"""
        self.__titre = valeur
    
    def set_auteur(self,valeur):
        """Setter de l'attribut privé auteur"""
        self.__auteur = valeur

    def set_nb_pages(self,valeur):
        """Setter de l'attribut privé nb_pages"""
        if self.__nb_pages >=0:
            self.get_nb_pages = valeur
        else:
            return TypeError ("Tu ne peux pas avoir un nombre de pages negatif.. Tu n'es pas la physique.")

    def verification(self):
        """Méthode qui verifie l'êtat de disponible (getter de disponible)."""
        return self.__disponible == True
    
    def emprunter(self):
        """Methode qui emprunte le livre, le rendant indisponible"""
        if self.verification() == True:
            print("Le livre a été emprunté.")
            self.__disponible = False
        else:
            print("Le livre n'est toujours pas disponible..")

    def rendre(self):
        """Methode qui fait l'inverse de la méthode emprunter."""
        if self.verification() == False:
            print("Le livre a été rendu")
            self.__disponible = True
        else:
            print("Le livre n'a pas été emprunté.")

if __name__ == "__main__":
    book = Livre("Don Quichotte","Miguel de Cervantes",-1)
    print(book.get_nb_pages())
    book.emprunter()
    print(book.verification())
    book.rendre()
    book.rendre()