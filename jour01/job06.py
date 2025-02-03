class Animal:
    def __init__(self,age=0,prenom=""):
        self.age = age
        self.prenom = prenom
    
    def get_age(self):
        """Permet d'avoir l'age de l'animal."""
        return f"L'age de l'animal {self.age} ans"

    def viellir(self):
        """Permet de faire viellir l'animal d'un an."""
        self.age += 1
        return self.get_age()
    
    def nommer(self,nom:str):
        """Permet de renommer l'animal."""
        self.nom = nom
        return f"L'animal se nomme {self.nom}"

if __name__ == "__main__":
    espece = Animal()
    print(espece.get_age())
    print(espece.viellir())
    print(espece.nommer("Luna"))