class Ville:
    def __init__(self,nom,habitants):
        self.__nom = nom
        self.__habitants = habitants
    
    def get_nom(self):
        return self.__nom

    def get_habitants(self):
        return self.__habitants
    
    def set_habitants(self,valeur):
        self.__habitants = valeur
    
    def __repr__(self):
        return f"Population de la ville de {self.__nom}: {self.__habitants} habitants"
    
class Personne:
    def __init__(self,nom,age,objet:Ville):
        self.__nom = nom
        self.__age = age
        self.__objet = objet
    
    def ajouterPopulation(self):
        x = int(self.__objet.get_habitants())
        #print(type(x))
        x += 1
        y = self.__objet.set_habitants(x)
        return f"Mise a jour de la population de la Ville de {self.__objet.get_nom()} {self.__objet.get_habitants()} habitants"

p = Ville("Paris",1000000)
m = Ville("Marseille",861635)

j = Personne("John",45,p)
my = Personne("Myrtille",4,p)
c = Personne("Chloé",18,m)
print(p)
print(m)
j.ajouterPopulation()
print(my.ajouterPopulation())
print(c.ajouterPopulation())