def geraM(n):
    M = [[0]* n for _ in range(n)]
    
    for i in range(n):
        k = 1
        for j in range(i,n):
            M[i][j] = M[j][i] = k
            k += 1

    return M

def imprime(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if j == len(matriz[0]) - 1:
                print(f"{matriz[i][j]:>3}", end="")
            else:
                print(f"{matriz[i][j]:>3}", end=" ")
        print()
    print()
    
def main():
    n = int(input())
    while n != 0:
        matriz = geraM(n)
        imprime(matriz)
        n = int(input())

main()