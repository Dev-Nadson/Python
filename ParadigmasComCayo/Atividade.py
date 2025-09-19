import math
import random

def Numbers(num): 
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
    ages = []
    names = []
    maiores18 = []
    menores15 = []
    while True:
        name = input("Digite um nome ou '0' para encerrar: ")
        if name == '0':
            break
        age = int(input("Digite a idade: "))

        ages.append(age)
        names.append(name)

        if age >= 18:
            maiores18.append(name)
        if age < 15:
            menores15.append(name)

    return f"""
A média de idade do grupo é: {sum(ages)/len(ages)}
O nome mais velho é: {names[ages.index(max(ages))]} e a idade é: {max(ages)}
Maiores de 18: {maiores18}
Menores de 15: {menores15}
"""

def CircleArea(radius): 
    return math.pi * (radius**2)

def Fatorial(num): 
    if num < 0:
        return "Erro"
    if num in (0, 1):
        return 1
    return num * Fatorial(num - 1) 

def Fibonatty():
    def fib(n):
        if n <= 1:
            return n
        return fib(n-1) + fib(n-2)

    while True:
        i = int(input("Digite um número ou um menor que um para encerrar: "))
        if i <= 0:
            break
        print(f"O {i}º termo da sequência de Fibonacci é: {fib(i)}")

def Operations():
    raiz = math.sqrt(144)
    logaritmo = math.log(10)
    cosseno = math.cos(math.radians(60))
    return f"Raiz quadrada de 144: {raiz}\nLogaritmo natural de 10: {logaritmo}\nCosseno de 60 graus: {cosseno}"

def RollDice():
    lancamentos = [random.randint(1, 6) for vezes in range(10)]
    lancamentos.sort(reverse=True)
    repeticoes = {}
    for n in lancamentos:
        repeticoes[n] = repeticoes.get(n, 0) + 1
    print(f"Lançamentos: {lancamentos}")
    for num, qtdeVezes in repeticoes.items():
        if qtdeVezes > 1:
            print(f"O número {num} apareceu {qtdeVezes} vezes")

def DivisionWithExeptions():
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print(f"O resultado da divisão é: {num1/num2}")
        except ZeroDivisionError:
            print("Erro: Não é possível dividir por zero.")
        opcao = input("Deseja realizar outra operação? (s/n): ")
        if opcao in ("n", "N"):
            break

def Module():
    def check_number(n):
        div = []
        primo = True
        if n < 2:
            primo = False
        else:
            for i in range(1, n+1):
                if n % i == 0:
                    div.append(i)
                if len(div) > 2:
                    primo = False
                    break
        isPar = "par" if n % 2 == 0 else "ímpar"
        return f"O número {n} é {isPar} e {'primo' if primo else 'não primo'}"
    
    for vezes in range(5):
        n = int(input(f"Digite o {vezes+1}º número de 5: "))
        print(check_number(n))

def ManagementSystem():
    estudantes = {}

    def cadastrar():
        matricula = input("Digite a matrícula: ")
        nome = input("Digite o nome: ")
        curso = input("Digite o curso: ")
        estudantes[matricula] = {"nome": nome, "curso": curso}
        print("Estudante cadastrado com sucesso!")

    def atualizar():
        matricula = input("Digite a matrícula do estudante a atualizar: ")
        if matricula in estudantes:
            nome = input("Digite o novo nome: ")
            curso = input("Digite o novo curso: ")
            estudantes[matricula] = {"nome": nome, "curso": curso}
            print("Dados atualizados com sucesso!")
        else:
            print("Matrícula não encontrada.")

    def excluir():
        matricula = input("Digite a matrícula do estudante a excluir: ")
        if matricula in estudantes:
            del estudantes[matricula]
            print("Estudante excluído com sucesso!")
        else:
            print("Matrícula não encontrada.")

    def listar():
        for matricula, dados in estudantes.items():
            print(f"Matrícula: {matricula}, Nome: {dados['nome']}, Curso: {dados['curso']}")

    while True:
        print("\nMenu:")
        print("1 - Cadastrar estudante")
        print("2 - Atualizar estudante")
        print("3 - Excluir estudante")
        print("4 - Listar estudantes")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            atualizar()
        elif opcao == "3":
            excluir()
        elif opcao == "4":
            listar()
        elif opcao == "5":
            break
        else:
            print("Opção inválida.")


while True:
    print("""
-------- MENU PRINCIPAL --------
1 - Números 
2 - Nomes e idades 
3 - Área do círculo 
4 - Fatorial 
5 - Fibonacci 
6 - Operações com math 
7 - Lançar dados 
8 - Divisão com exceções 
9 - Módulo par/ímpar/primo 
10 - Sistema de gerenciamento
0 - Sair
--------------------------------
""")

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            num = int(input("Digite o primeiro número: "))
            print(Numbers(num))
        case "2":
            print(Names())
        case "3":
            for vezes in range(3):
                raio = int(input(f"Digite o {vezes+1}º raio: "))
                print(f"A área é: {CircleArea(raio)}")
        case "4":
            num = int(input("Digite um número: "))
            print(Fatorial(num))
        case "5":
            Fibonatty()
        case "6":
            print(Operations())
        case "7":
            RollDice()
        case "8":
            DivisionWithExeptions()
        case "9":
            Module()
        case "10":
            ManagementSystem()
        case "0":
            print("Programa Encerrado")
            break
        case _:
            print("Opção inválida. Tente novamente.")