class Personnage:
    def __init__(self,age:int=14):
        self.age = age
    
    def afficherAge(self):
        return self.age

    def bonjour():
        return "Hello"
    
    def modifierAge(self,age:int):
        self.age = age

class Eleve(Personnage):
    def __init__(self,age=14):
        super().__init__(age)
    
    def allerEnCours(self):
        return "Je vais en cours"
    
    def afficherAge(self):
        return f"J'ai {self.age} ans"

class Professeur(Personnage):
    def __init__(self, age,matiere):
        super().__init__(age)
        self.__matiereEnseignee = matiere
    #def __init__(self,
    
    def enseigner():
        return "Le cours va commencer"

if __name__ == "__main__":
    Nico = Personnage()
    Ulys = Eleve()
    print(Ulys.afficherAge())
    