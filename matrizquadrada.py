def gera(n):
    #bordas das linhas e colunas mudam
    matriz = [[1]* n for _ in range(n)]

    li = ci = 0 # linha inicial e coluna inicial
    lf = cf = n - 1 # linha final e coluna final

    for valor_interno in range(1,(n + 1) // 2 + 1): # vai contemplar todos os numeros diferentes que a matriz terá

        for j in range(ci, cf + 1): 

            matriz[li][j] = matriz[lf][j] = valor_interno #cima e baixo

        for i in range(li + 1,lf):
            matriz[i][ci] = matriz[i][cf] = valor_interno #esquerda e direita

        li += 1
        ci += 1
        lf -= 1
        cf -= 1

    return matriz
        


def imprime(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if j != len(matriz[0]) - 1:
                print(f"{matriz[i][j]:3}", end=" ")
            else:
                print(f"{matriz[i][j]:3}", end="")
        print()
    print()


def main():
    while True:
        n = int(input())
        if n == 0:
            break

        matriz = gera(n)

        imprime(matriz)
        

main()