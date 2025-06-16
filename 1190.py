def calcula(op,matriz):
    collumn = 11
    soma = 0
    cont = 0
    decrescente = True

    for linha in range(1,11):
        if collumn == 6:
            decrescente = False
            collumn = 7


        for coluna in range(collumn,12):
            #print(f'matriz[{linha}][{coluna}]: ',matriz[linha][coluna])
            soma+= matriz[linha][coluna]
            cont += 1
        
        if decrescente:
            collumn -= 1
        else:
            collumn += 1
        
        

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