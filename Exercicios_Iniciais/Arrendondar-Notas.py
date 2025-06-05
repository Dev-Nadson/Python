
Notas = []
Notas_Arredondadas = []

print("Digite -1 para finalizar o processo.")
Nota = int(input("Digite as notas: "))

while Nota != -1:
    Notas.append(Nota)
    Nota = int(input("digite as notas: "))

for n in Notas:
    if n < 40:
        Notas_Arredondadas.append(n)
    else:
        Nota_round = n
        cont = 0
        while Nota_round % 5 != 0:
            Nota_round += 1
            cont += 1 
        if cont <= 3:   
            Notas_Arredondadas.append(Nota_round)
        else:
            Notas_Arredondadas.append(n)
  
print(f"As notas arredondadas são: {Notas_Arredondadas}")