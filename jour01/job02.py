class Operation:
    def __init__(self,nombre1=1,nombre2=2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
    
    def __repr__(self):
        return f"Le nombre1 est {self.nombre1}\nLe nombre2 est {self.nombre2}"

