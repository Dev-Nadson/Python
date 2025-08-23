def operations(num1, num2):
    print(f"A soma dos dois é: {num1 + num2}")
    print(f"A subtração do segundo pelo primeiro é: {num2 - num1}")
    print(f"O produto dos dois é: {num1 * num2}")
    print(f"A divisão do primeiro pelo segundo é: {num1 / num2}")
    print(f"{num1} é maior que {num2}" if num1 > num2 else f"O {num2} é maior que {num1}")

def parORimpar(num3):
    return "Impar" if num3 % 2 != 0 else "Par"

def Fatorial(num4):
    return num4 if num4 in (0, 1) else "Erro" if num4 < 0 else num4 * Fatorial(num4 - 1)

def FemOrMasc(gender):
    return "F - Feminino" if gender in ("F", "f") else "M - Masculino" if gender in ("M", "m") else "Genêro Inválido"

def TempConversor():
    return None

num1 = int(input("Insira o número 1: "))
num2 = int(input("Insira o número 2: "))
operations(num1,num2)

num3 = int(input("Insira o terceiro número: "))
print(parORimpar(num3))

num4 = int(input("Insira um número para receber o fatorial: "))
print(Fatorial(num4))

gender = input("insira o gênero F ou M: ")
print(FemOrMasc(gender))