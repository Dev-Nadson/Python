import os
os.system('cls')
print("--- This algorithm checks if two words are palindromes ---")
word1 = input("Enter the first word: ").lower()
word2 = input("Enter the second word: ").lower()

w1 = list(word1)
w2 = list(word2)
cont = 0
for i in w1:
    if i in w2:
        cont += 1
if cont == len(w1) and len(w1) == len(w2):
    print("Is a palindrome")
else:
    print("Isn't a palindrome")