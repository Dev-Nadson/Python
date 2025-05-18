a = int(input("Digite um número: "))
fatorial = 1

for i in range(a, 1, -1):
    fatorial *= i

print("O fatorial de", a, "é:", fatorial)
