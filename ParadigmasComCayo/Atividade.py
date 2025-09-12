def Numbers(num): #feito!
    list = []
    maior = num
    menor = num
    while num != 0:
        list.append(num)
        if maior < num:
            maior = num
        if menor > num:
            menor = num
        num = int(input("Digite o próximo número: "))
    return f"A quantidade de números lidos foi:{len(list)}\nO maior é: {maior}\nO menor é: {menor}\nA média é: {sum(list)/len(list)}"

def Names():
    peoples = {}
    ages = []
    names = []
    while True:
        name = input("Digite um nome ou '0' para encerrar: ")
        if name == '0':
            break
        age = int(input("Digite a idade: "))

        ages.append(age)
        names.append(name)

    for age in ages:
        if age >= 18:
            print(names[ages.index(age)])

    return f"A média de idade do grupo é: {sum(ages)/len(ages)}\nO nome mais velho é: {names[ages.index(max(ages))]} e a idade é: {max(ages)}"

def CircleArea(radius): 
    pass

def Fatorial(num): #feito!
    return num if num in (0, 1) else "Erro" if num < 0 else num * Fatorial(num - 1) 

def Fibonatty():
    a = 1
    b = 0
    c = 0
    print("Esse algoritmo irá calcular quantas casas da sequência de fibonatti você pedir")
    i = int(input("Digite um número: "))

    if i <= 0:
        print("Número inválido")
    for x in range(i):
        c = a + b
        print(c, end=" ")
        b = a
        a = c
  
def Operations():
    pass

def RollDice():
    pass

def DivisionWithExeptions():
    pass

def module():
    pass

def ManagementSystem():
    pass

# num = int(input("Digite um número:"))
# print(Numbers(num))

print(Names())

# num = int(input("Digite um número para receber o fatorial: "))
# print(Fatorial(num))


