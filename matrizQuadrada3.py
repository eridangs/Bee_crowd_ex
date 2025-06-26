def geraM(n):
    M = [[0]* n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            valor = 2 ** (j+i)
            M[i][j] = valor

    return M
    
def imprime(M,n):
    T = len(str(M[n-1][n-1]))
    for i in range(len(M)):
        for j in range(len(M)):
            if j == len(M) - 1:
                print(f'{M[i][j]:>{T}}',end='')
            else:
                print(f'{M[i][j]:>{T}}',end=' ')
        print()
    print()

def main():
    n = int(input())
    while n != 0:
        matriz = geraM(n)
        imprime(matriz,n)
        n = int(input())

main()