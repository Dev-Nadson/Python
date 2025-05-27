import os
def Create(type):
    i = 0
    CharacterString = []
    while True:
        i += 1
        nome = input(f"Enter the name of {i}º {type}: ")
        vida = input(f"Enter the life of {i}º {type}: ")
        dano = input(f"Enter the damage of {i}º {type}: ")
        character = {'Name': nome, 'Life': vida, 'Damage': dano}
        CharacterString.append(character)
        ctrl = int(input("Enter any number to continue, or press 1 to stop: "))  
        if ctrl == 1:
            break
    return CharacterString

def ShowChar(CharacterString, type):
    print(f"\n{type} Data\n")
    for i, key in enumerate(CharacterString):
        print(f"{i+1}º {type} : ")
        print(f"  Name : {key['Name']}")
        print(f"  Life : {key['Life']}")
        print(f"  Damage : {key['Damage']}")

os.system('cls')
print("Wellcome to the entity creator!")
type = input("Enter the type of entity or enter 1 to stop: ")
CharacterS = Create(type)
ShowChar(CharacterS, type)
control = input("\nDo you want to continue creating entities? Enter 1 to stop: ")
while control != "1":
    type = input("Enter the type of entity: ")
    CharacterS += Create(type)
    ShowChar(CharacterS, type)
    control = input("\nDo you want to continue creating entities? Enter 1 to stop: ")
print(f"{CharacterS}")