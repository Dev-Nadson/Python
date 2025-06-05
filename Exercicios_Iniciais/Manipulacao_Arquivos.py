adress = "./ArquivosManipulacao/exemplo_02.txt"
def read(): #Modo Leitura
    with open(adress, "r", encoding="utf-8") as archive:
        txt = archive.readlines()
    for index, content in enumerate(txt):
        print(f"{index}. {content}", end="")

def write(): #Modo Escrita, cria ou substitui arquvios
    with open(adress, "w", encoding="utf-8") as archive:
        archive.write("Testando a escrita")
    with open(adress, "r", encoding="utf-8") as archive:   
        txt = archive.read()
        print(txt)

def apend(): #Modo Adição, atualiza o arquvio
    with open(adress, "r", encoding="utf-8") as archive:
        txt = archive.readlines()
    for index, content in enumerate(txt):
        print(f"{index}. {content}", end="")
    with open(adress, "a", encoding="utf-8") as archive:
        archive.write("\nLinha 2")
    with open(adress, "r", encoding="utf-8") as archive:
        txt = archive.readlines()
    for content in txt:
        print(f"{content}")