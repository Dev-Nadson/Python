def MediaNotas(nota01, nota02):
    media = ((nota01 + nota02) / 2)

    if media >= 3 and media < 7:
        print(f"Sua média foi: {media}, será nescessário fazer a prova final.")
        NotaProvaFinal = int(input("Insira a nota da prova final: "))
        return "Aprovado" if (media + NotaProvaFinal) >= 5 else "Reprovado"
    
    return f"Aprovado, sua média foi: {media}" if media >= 7 else f"Reprovado, sua média foi: {media}"

def CalcAlturas(Alturas):
    total = 0
    maior = Alturas[0]
    menor = Alturas[0]

    for i in Alturas:
        if i > maior:
            maior = i
        if i < menor:
            menor = i

        total = total + i
    media = total / 10

    return f"A média é {media}, o maior número é {maior} e o menor número é {menor}"

print("--- Sistema de Notas ---")
nota01 = int(input("Insira a primeira nota: "))
nota02 = int(input("Insira a segunda nota: "))
print(MediaNotas(nota01, nota02))

print("--- Sistema de Altura ---")
Alturas = []

for i in range(10):
    altura = float(input(f"Insira a altura do {i+1} aluno (em metros): "))
    Alturas.append(altura)

print(CalcAlturas(Alturas))