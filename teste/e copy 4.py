# 4. Validador de Parênteses

entrada = input()
entrada = list(entrada)
parenteses = []

for i in range(len(entrada)):
    if len(parenteses) > 0 and entrada[i] == ")" and parenteses[-1] == "(":
        parenteses.pop()
        
    elif entrada[i] == "(" or entrada[i] == ")":
        parenteses.append(entrada[i])

if len(parenteses) == 0:
    print("válido")
else:
    print("inválido")