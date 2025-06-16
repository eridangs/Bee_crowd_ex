l = int(input())
opereracao = input()
matriz = []
coluna = 12
row = 12
linha = []
result = 0

for i in range(row):
    for j in range(coluna):
        valor = float(input())
        linha.append(valor)
    matriz.append(linha)
    linha = []

for i in range(row): #entra na linha
    for j in range(coluna): #entra na coluna da linha
        if j == l:
            result += matriz[i][j]

if opereracao == "M":
    result /= 12

print(f'{result:.1f}')