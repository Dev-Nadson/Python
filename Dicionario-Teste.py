Nomes = []
Vidas = []
Danos = []
i = 0
nome = "a" #Para inicializar o while
while nome != "end":
    i += 1
    nome = input(f"Insira o nome do {i}º Personagem: ")
    Nomes.append(nome)
    vida = input(f"Insira a vida do {i}º Personagem: ")
    Vidas.append(vida)
    dano = input(f"Insira o dano do {i}º Personagem: ")
    Danos.append(dano)

Personagem = {
    'nome': Nomes,
    'vida': Vidas,
    'dano': Danos
}

# Mobs = [
#     {'nome': 'zumbi', 'vida': '2', 'dano': '10',},
#     {'nome': 'esqueleto', 'vida': '7', 'dano': '7',},
#     {'nome': 'clown', 'vida': '10', 'dano': '15',}
# ]

print("Os dados do personagem são:", Personagem)
# print(f"Os Mobs são: \n{Mobs[0]['nome']}\n{Mobs[1]}\n{Mobs[2]} ")