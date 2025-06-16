def calcula(op,matriz):
    collumn = 1
    soma = 0
    cont = 0
    crescente = True

    for linha in range(1,11):
        if collumn == 6:
            crescente = False
            collumn = 5


        for coluna in range(0,collumn):
            #print(f'matriz[{linha}][{coluna}]: ',matriz[linha][coluna])
            soma+= matriz[linha][coluna]
            cont += 1
        
        if crescente:
            collumn += 1
        else:
            collumn -= 1
        
        

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