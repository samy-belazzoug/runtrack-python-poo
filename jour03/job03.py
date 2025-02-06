class Tache:
    def __init__(self,titre:str,description:str,statut:str="A faire"):
        self.titre = titre 
        self.description = description
        self.statut = statut
    
    def afficherTache(self):
        return self.titre
    
    def afficherStatut(self):
        return self.statut
    
class ListeDeTaches:
    def __init__(self,taches:list=[]):
        self.taches = taches
    
    def ajouterTache(self,tache:Tache):
        return self.taches.append(tache)
    
    def supprimerTache(self,tache:Tache):
        return self.taches.remove(tache)
    
    def marquerCommeFinie(self,tache:Tache):
        tache.statut = "Terminée"

    def afficherListe(self):
        for i in range(len(self.taches)):
            print(Tache.afficherTache(self.taches[i]))
    
    def filterListe(self):
        print("Taches à faire : ")
        for i in range(len(self.taches)):
            if Tache.afficherStatut(self.taches[i]) == "A faire":
                print(Tache.afficherTache(self.taches[i]))
        print("Taches terminées : ")
        for j in range(len(self.taches)):
            if Tache.afficherStatut(self.taches[j]) == "Terminée":
                print(Tache.afficherTache(self.taches[j]))

if __name__ == "__main__":
    todo1 = Tache("a","blabla")
    todo2 = Tache("b","bloblo")
    todo3 = Tache("c","blehbleh")
    todo4 = Tache("d","blublu")
    todolist = ListeDeTaches()
    todolist.ajouterTache(todo1)
    todolist.ajouterTache(todo2)
    todolist.ajouterTache(todo3)
    todolist.ajouterTache(todo4)
    todolist.supprimerTache(todo2)
    print(todolist.afficherListe())
    todolist.marquerCommeFinie(todo3)
    print(todolist.filterListe())