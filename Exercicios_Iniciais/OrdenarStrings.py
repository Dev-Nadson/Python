def Order(numbers):
    List = list(numbers)
    ord = sorted(List)
    return ord

numbers = (input("Enter the numbers: "))
List = Order(numbers)
print(List)