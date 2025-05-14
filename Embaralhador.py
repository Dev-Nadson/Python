import random

word = input("Insira a palavra: ")
lista = []
new_word = ""

tam = len(word)
key = random.randint(0, tam)

for i in range(tam):
    lista.append(word[i]) #Transforma a string em lista facilitando a modificação

random.shuffle(lista)

for i in range(tam):
    new_word += lista[i] #Transforma a lista em string

print(new_word)
