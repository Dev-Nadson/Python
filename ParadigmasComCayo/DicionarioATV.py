def PrintSeparado(dic):
    for chave, valor in dic.items():
        return f"{chave} + {valor}"
    

pessoa = {
    'nome': "Marcos Vinicius Guilherme Bryan Araújo",
    'CPF': "193.335.669-37",
    'RG': "32.872.935-8"
}

print(f"{pessoa} \n")
PrintSeparado(pessoa)
