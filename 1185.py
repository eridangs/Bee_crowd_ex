def calcula(op,matriz):
    coluna = 10
    soma = 0


    for i in range(len(matriz)):

        for j in range(len(matriz[0])):
            if j <= coluna:
                # print(f'matriz[{i}][{j}]: ',matriz[i][j])
                soma+= matriz[i][j]
        
        coluna -= 1

    if op == "M":
        soma /= 66

    return soma

# def imprime(matriz):
#     for i in range(len(matriz)):
#         for j in range(len(matriz[0])):
#             print(matriz[i][j], end="\t")
#         print()

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