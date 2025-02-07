class Personnage:
    def __init__(self,age:int=14):
        self.age = age
    
    def afficherAge(self):
        return self.age

    def bonjour(self):
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
    def __init__(self,age,matiereEnseignee):
        super().__init__(age)
        self.__matiereEnseignee = matiereEnseignee
    
    def enseigner(self):
        return "Le cours va commencer"

if __name__ == "__main__":
    Nico = Personnage()
    Ulys = Eleve()
    print(Ulys.bonjour())
    print(Ulys.allerEnCours())
    Ulys.modifierAge(15)
    Rodrigo = Professeur(40,"Mathematiques")
    print(Rodrigo.bonjour())
    print(Rodrigo.enseigner())