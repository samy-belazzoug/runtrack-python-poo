class Livre:
    def __init__(self,titre:str,auteur:str,nb_pages:int):
        self.__titre = titre 
        self.__auteur = auteur
        self.__nb_pages = nb_pages
    
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

if __name__ == "__main__":
    book = Livre("Don Quichotte","Miguel de Cervantes",-1)
    print(book.get_nb_pages())