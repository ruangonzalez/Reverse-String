def inverte_string(string):
    inverted_string = ""
    
    for i in range(len(string) - 1, -1, -1):
        inverted_string += string[i]  
    return inverted_string

entrada = input("Digite uma string: ")
if entrada:  
    resultado = inverte_string(entrada)
    print("String invertida:", resultado)
else:
    print("A string de entrada está vazia.")