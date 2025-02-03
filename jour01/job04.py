class Personne:
    def __init__(self,nom:str,prenom:str):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        """Retourne le nom et prénom de la personne."""
        return f"Je suis {self.prenom} {self.nom}"

if __name__ == "__main__":
    john = Personne("Doe","John")
    print(john.SePresenter())
    jean = Personne("Dupond","Jean")
    print(jean.SePresenter())
    samy = Personne("Belazzoug","Samy")
    print(samy.SePresenter())