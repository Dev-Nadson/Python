Nomes = []
Vidas = []
Danos = []
NomesMb = []
VidasMb = []
DanosMb = []
Personagem = {
    'nome': Nomes,
    'vida': Vidas,
    'dano': Danos
}
Mobs = {
    'nome': NomesMb,
    'vida': VidasMb,
    'dano': DanosMb
}

def Personagens():
    control = 0 #Para inicializar o while
    i = 0
    while control != 1:
        i += 1
        nome = input(f"Insira o nome do {i}º Personagem: ")
        vida = input(f"Insira a vida do {i}º Personagem: ")
        dano = input(f"Insira o dano do {i}º Personagem: ")
        Nomes.append(nome)
        Vidas.append(vida)
        Danos.append(dano)
        control = int(input("Insira qualquer número para continuar ou 1 Para finalizar: "))

def MOBS():
    control = 0 #Para inicializar o while
    i = 0
    while control != 1:
        i += 1
        nome = input(f"Insira o nome do {i}º Mob: ")
        vida = input(f"Insira a vida do {i}º Mob: ")
        dano = input(f"Insira o dano do {i}º Mob: ")
        NomesMb.append(nome)
        VidasMb.append(vida)
        DanosMb.append(dano)
        control = int(input("Insira qualquer número para continuar ou 1 Para finalizar: "))

def ShowInfoChar():
    print("\nDados dos Personagens\n")
    for i in range(len(Nomes)):
        print(f"Personagem {i+1}º: ")
        print(f"  Nome : {Personagem['nome'][i]}")
        print(f"  Vida : {Personagem['vida'][i]}") #Primeiro a chave depois o índice
        print(f"  Dano : {Personagem['dano'][i]}")

def ShowInfoMobs():
    print("\nDados dos Mobs\n")
    for n in range(len(Nomes)):
        print(f"Mob {n+1}º: ")
        print(f"  Nome : {Mobs['nome'][n]}")
        print(f"  Vida : {Mobs['vida'][n]}") #Primeiro a chave depois o índice
        print(f"  Dano : {Mobs['dano'][n]}")

Personagens()
ShowInfoChar()
MOBS()
ShowInfoMobs()
