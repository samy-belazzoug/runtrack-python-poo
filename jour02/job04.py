class Student:
    def __init__(self,nom,prenom,numero_etudiant,nombre_credits=0,level=0):
        self.__nom = nom 
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__nombre_credits = nombre_credits
        #level = self.__level()
        self.__level = self.__student_eval()
    
    def add_credits(self,valeur):
        """Ajoute des crédits"""
        if self.__nombre_credits < 0:
            return TypeError("Credits inférieur à 0.")
        else:
            self.__nombre_credits += valeur
            print(f"Le nombre de credits de {self.__prenom} {self.__nom} est de {self.__nombre_credits} points.")

    def __student_eval(self):
        """En déduis le niveau de l'élève."""
        if self.__nombre_credits >= 90:
            return "Excellent"
        if self.__nombre_credits >= 80:
            return "Très bien"
        if self.__nombre_credits >= 70:
            return "Bien"
        if self.__nombre_credits >= 60:
            return "Passable"
        if self.__nombre_credits < 60:
            return "Insuffisant"

    def student_info(self):
        """Révèle les informations de l'élève."""
        return f"Nom = {self.__nom}\nPrénom = {self.__prenom}\nid = {self.__numero_etudiant}\nNiveau = {self.__student_eval()}"


if __name__ == "__main__":
    john = Student("John","Doe",145,0)
    john.add_credits(30)
    john.add_credits(40)
    print(john.student_info())
