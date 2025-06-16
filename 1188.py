def calcula(op,matriz):
    collumn = 5
    line = 7
    soma = 0
    cont = 0
    for linha in range(7,12):

        for coluna in range(collumn,line):
            #print(f'matriz[{linha}][{coluna}]: ',matriz[linha][coluna])
            soma+= matriz[linha][coluna]
            cont += 1
        
        collumn -= 1
        line += 1
        
        

    if op == "M":
        soma /= cont

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