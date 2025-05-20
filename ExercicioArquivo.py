from collections import Counter

ContChar = 0
ContWord = 0
cont = []
TextFull = []

with open ("C:/Users/Ana Julia/Desktop/PRO-git/Python/ArquivosManipulacao/exemplo_03.txt", "r", encoding="utf-8") as arquivo:
    txt = arquivo.readlines()

for i in range(len(txt)):
    NewText = list(txt[i].split())
    if "\n" in NewText:
        NewText.remove("\n")
    print(NewText)
    for char in NewText:
        ContChar += len(char)
    TextFull += NewText

ContWord += len(TextFull)
cont = Counter(TextFull)
cont = cont.most_common(1)

print("The text is: \n")
for i in txt:
    if "\n" in i:
        i = i.replace("\n", " ")
    print(f'{i}')

print(f"\nThe number of words: {ContWord}")
print(f"The number of characters: {ContChar}")
print(f'The most frequent word is "{cont[0][0]}" appearing "{cont[0][1]}" times')