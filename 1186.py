def calcula(op,matriz):
    collumn = 11
    soma = 0


    for linha in range(1,len(matriz)):

        for coluna in range(len(matriz[0])):
            if coluna >= collumn:

                # print(f'matriz[{linha}][{coluna}]: ',matriz[linha][coluna])
                soma+= matriz[linha][coluna]

        collumn -= 1

    if op == "M":
        soma /= 66

    return soma

def main():
    op = input()
    
    coluna = 12
    matriz = [[0]* coluna for _ in range(coluna)]

    # leitura da matriz
    for i in range(coluna): #linhas
        for j in range(coluna): #colunas
            matriz[i][j] = float(input())
    r = calcula(op,matriz)
    print(f'{r:.1f}')

main()