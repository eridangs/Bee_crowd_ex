def muda(matriz):
    
    meio = int(len(matriz) // 2)


    for linha in range(1,len(matriz-1)): #borda da linha nao muda
        for coluna in range(1,len(matriz-1)): #borda da coluna não muda

            
                matriz[linha][coluna] += 1


def imprime(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            print(matriz[i][j], end="\t")
        print()


def main():
    while True:
        ordem = int(input())
        if ordem == 0:
            break

        matriz = [[1]* ordem for _ in range(ordem)]
        if ordem > 2:
            muda(matriz)

        imprime(matriz)
        

main()