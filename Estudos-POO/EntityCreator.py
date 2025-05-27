class Characters:
    def __init__(self, Name, Life, Damage):
        self.Name = Name
        self.Life = Life
        self.Damage = Damage

    def __str__(self):
        return f"Name: {self.Name}, Life: {self.Life}, Damage: {self.Damage}\n" #Formata o obj como string

    def Export(character):
        with open ("./Estudos-POO/Creatures.txt", "a") as Data:
            Data.write(str(character))

while True:
    Name = input("Enter the name of the character: ")
    if Name == "-1":
        break
    Life = input("Enter the life of the character: ")
    Damage = input("Enter the damage of the character: ")
    character = Characters(Name, Life, Damage)
    Characters.Export(character)