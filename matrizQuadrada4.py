while True:
    try:
        def geraM(n):
            M = [[0]*n for _ in range(n)]

            return M

        def imprime(M,n):
            for i in range(n):
                for j in range(n):
                    print(f'{M[i][j]}',end='')
                print()

        def main():
            n = int(input())
            matriz = geraM(n)
            imprime(matriz,n)

        main()

    except EOFError:
        break