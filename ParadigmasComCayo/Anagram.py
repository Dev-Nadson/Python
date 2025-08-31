import os
def isAnagram(word):
    listWord = list(word)
    ReverseWord = listWord[::-1]
    return "É palindromo" if listWord == ReverseWord else "Não é um palìndormo"

def isLegalAge(idade):
    if idade >= 18:
        return "Você pode entrar!"
    else:
        guardian = input("Você está acompanhado do responsável? ")
        return "Pocê pode entrar!" if guardian in ("s", "S", "sim", "SIM") else "Você NÃO pode entrar!"
    
def changeList(list):
    list[0] = "kiwi"
    list.append("laranja")
    list.insert(1, "limao")
    list.remove("banana")
    return list

os.system('clear')
word = input("Insira a palavra para ver se é Palíndromo: ")
print(f"{isAnagram(word)}\n")

idade = int(input("Qual a sua idade? Responda apenas com números: "))
print(f"{isLegalAge(idade)}\n")

list = ["maca", "banana", "careja"]
print(f"Sua lista: {list}")
print(f"O segundo item da sua lista: {list[1]}")
print(f"A lista alterada: {changeList(list)}\n")
