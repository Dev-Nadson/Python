def Even(n1, n2):
    for a in range(n1, (n2+1)):
        if a % 2 == 0:
            Numbers.append(a)

Numbers = []
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
Even(n1, n2)
print(Numbers)
print(len(Numbers))