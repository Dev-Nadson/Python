def read(): #Modo Leitura
    with open("C:/Users/Ana Julia/Desktop/PRO-git/Python/ArquivosManipulacao/exemplo_01.txt", "r", encoding="utf-8") as archive:
        txt = archive.readlines()
    for index, content in enumerate(txt):
        print(f"{index}. {content}", end="")

def write(): #Modo Escrita, cria ou substitui arquvios
    with open("C:/Users/Ana Julia/Desktop/PRO-git/Python/ArquivosManipulacao/exemplo_02.txt", "w", encoding="utf-8") as archive:
        archive.write("Testando a escrita")
    with open("C:/Users/Ana Julia/Desktop/PRO-git/Python/ArquivosManipulacao/exemplo_02.txt", "r", encoding="utf-8") as archive:   
        txt = archive.read()
        print(txt)

def apend(): #Modo Adição, atualiza o arquvio
    with open("C:/Users/Ana Julia/Desktop/PRO-git/Python/ArquivosManipulacao/exemplo_03.txt", "r", encoding="utf-8") as archive:
        txt = archive.readlines()
    for index, content in enumerate(txt):
        print(f"{index}. {content}", end="")
    with open("C:/Users/Ana Julia/Desktop/PRO-git/Python/ArquivosManipulacao/exemplo_03.txt", "a", encoding="utf-8") as archive:
        archive.write("\nLinha 2")
    with open("C:/Users/Ana Julia/Desktop/PRO-git/Python/ArquivosManipulacao/exemplo_03.txt", "r", encoding="utf-8") as archive:
        txt = archive.readlines()
    for content in txt:
        print(f"{content}")

apend()
        