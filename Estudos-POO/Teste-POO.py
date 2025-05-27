#Classes -> Atributos(Características) e Metódos(Funções)

class Peoples:
    def __init__(self, Name, Age): #Atributos Padrão
        self.Name = Name
        self.Age = Age
    
    def __str__(self):
        return f"{self.Name},{self.Age}"

print(Peoples("llaal", "12"))