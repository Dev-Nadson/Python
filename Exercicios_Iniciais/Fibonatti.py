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
  