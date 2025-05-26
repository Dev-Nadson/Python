#Classes -> Atributos(Características) e Metódos(Funções)

class Peoples:
    def __init__(self, Name, Age): #Atributos Padrão
        self.Name = Name
        self.Age = Age

people1 = Peoples("José","21")
print(people1.Name)