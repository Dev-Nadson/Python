dic = {
    "a":"1",
    "b":"2",
    "c":"3",
    "d": "4",
    "e": "5"
}
word = input("Enter the word to criptograph: ")
new_w = ""
l1 = list(word)
for i in l1:
    if i in dic:
        new_w += dic[i]

print("".join(new_w))