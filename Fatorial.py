a = int(input("Digite um número: "))
fatorial = 1

for i in range(a, 0, -1):
    fatorial = fatorial * i

print("O fatorial de", a, "é:", fatorial)
