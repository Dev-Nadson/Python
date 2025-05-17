# a = int(input("Digite um número: "))
# fatorial = 1

# for i in range(a, 1, -1):
#     fatorial *= i

# print("O fatorial de", a, "é:", fatorial)

dic = {
    "a":"1",
    "b":"2",
    "c":"3",
    "d": "4",
    "e": "5"
}
word = input("Enter the word to criptografe: ")
new_w = ""
l1 = list(word)
for i in l1:
    if i in dic:
        new_w += dic[i]

print("".join(new_w))