def mdc(a, b):
    def div(num):
        div = []
        for i in range(1, num+1):
            if num % i == 0:   
                div.append((num / i))
        return div
    return f"Os divisores de {a} são: {div(a)} e os divisores de {b} são: {div(b)}"

for i in range(3):
    a = int(input(f"Digite o {i+1}º número: "))
    b = int(input(f"Digite o {i+1}º número: "))
    print(mdc(a, b))