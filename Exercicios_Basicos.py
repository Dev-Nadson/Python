def Multiplication():
    a = int(input("Enter the desired multiplication table: "))
    for i in range(1, 11):
        print(f"{a} * {i} = {a * i}")
        
def Palindrome():        
    word = input("insert a word: ")
    lista = list(word)
    lista.reverse()
    reverse_word = "".join(lista)

    if word == reverse_word:
        print("It's a palindrome")
    else:
        print("Isn't a palindrome")

def NamesList():
    Names=[]

    Name = input("Insert the names, and write 'end' to stop: ")
    while Name != "end":    
        Names.append(Name) #Adiciona no fim da lista
        Name = input("Insert the names, and write 'end' to stop: ")

    Names.insert(0, "ADM") #Adiciona no início da lista
    for i, Name in enumerate(Names): #Name = item, Names = List
        print(f"{i}: {Name}")

    rmv = input("Do you want to remove some name? \nanswer with 'yes' or 'no': ")
    if rmv == "yes":
        Removed_Name = input("Enter the name to be removed: ")
        while Removed_Name not in Names:
            print("That name isn't in the list, enter again.")
            Removed_Name = input("Enter the name to be removed: ")
        Names.remove(Removed_Name)
        Names = list(Names)
        print("\nUpdated list:")
        for i, Name in enumerate(Names): #Name = item, Names = List
            print(f"{i}: {Name}")        
    else:
        print("ok")
    change = input("Do you want to change some name? \nanswer with 'yes' or 'no': ")
    if change == "yes":
        i = int(input("Enter the index position of the name: "))
        Names[i] = input("Enter the new name: ") 
        print("\nUpdated list:") 
        for i, Name in enumerate(Names): #Name = item, Names = List
            print(f"{i}: {Name}")   
    else:
        print("ok")     


def error():
    print("Invalid option.")

opcoes = {
    1: Multiplication,
    2: Palindrome,
    3: NamesList
}

print("1. Multiplication Table \n2. Palindrome Test \n3. Names List")
Op = int(input("Insert the option: "))
opcoes.get(Op, error)()