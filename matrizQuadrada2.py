def geraM(n):
    matriz = [[0]* n for _ in range(n)]

    ci = 0 # linha inicial e coluna inicial
    lf = cf = n - 1 # linha final e coluna final
    for i in range(n):
        for j in range(i,n):
            matriz[j][i] = j-i+1
            matriz[i][j] = j-i+1
            #print(f'matriz[{i}][{j}] {matriz[i][j]}\nmatriz[{j}][{i}] {matriz[j][i]}')
        # li = 1
        # for lin in range(valormatriz,valormatriz+1):
        #     for linha in range(len(matriz)):
        #         matriz[lin][linha] = li
        #     li += 1
        #     for colu in range(len(matriz)):
        #         matriz[colu][lin] = li
            
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
    n = 1
    while n != 0:
        n = int(input())

        matriz = geraM(n)

        imprime(matriz)

main()