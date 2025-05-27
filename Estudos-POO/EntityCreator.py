class Characters:
    def __init__(self, Name, Life, Damage):
        self.Name = Name
        self.Life = Life
        self.Damage = Damage

All_Data = []
while True:
    Name = input("Enter the name of the character: ")
    if Name == "-1":
        break
    Life = input("Enter the life of the character")
    Damage = input("Enter the damage of the character")
    character = Characters(Name, Life, Damage)
    character = character.Name, character.Life, character.Damage
    All_Data.append(character)

print(All_Data)
with open ("./Estudos-POO/Creatures.txt", "a") as Data:
    for i in All_Data:
        Data.write(str(i))