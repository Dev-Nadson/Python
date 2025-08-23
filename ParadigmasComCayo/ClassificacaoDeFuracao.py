def classificar(velocidade):
    classificacoes = {
        "Tempestade fraca": range(0, 62),
        "Tempestade tropical": range(62, 119),
        "Furacão de categoria 1": range(119, 154),
        "Furacão de categoria 2": range(154, 178),
        "Furacão de categoria 3": range(178, 210),
        "Furacão de categoria 4": range(210, 250)
    }

    for tipo, Velocidades in classificacoes.items():
        if velocidade in Velocidades: 
            return tipo
    
    return "Velocidade inválida" if velocidade < 0 else "Furacão de categoria 5"

velocidade = int(input("Insira a velocidade do vento durante a tesmpestade: "))
print(f"Classificação: {classificar(velocidade)}")