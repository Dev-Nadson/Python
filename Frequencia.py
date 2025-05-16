from collections import Counter
print("--- This algorithm counts the most frequent number in a list ---")
Frq = input("Enter the list: ").split(",") #Split ignora as vírgulas
List = list(Frq)
Cont = Counter(List)
frequency = Cont.most_common(1) #Retorna uma Tupla ex:. '1': 4 -Número 1 quatro vezes-
print(f"The most frequent number is: {frequency[0][0]}") #Aqui pega o primeiro valor