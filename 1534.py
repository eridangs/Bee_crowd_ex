def gera(n):
    m = [[3]*n for _ in range(n)]
    a = n
    meio = n//2

# diagonais


    for i in range(n):
        m[i][i] = 1

    for i in range(a):
        m[a-1][i] = 2
        a -= 1
# diagonais

    return m

#--------------------------------------

def imprime(m):
    for i in range(len(m)):
        for j in range(len(m)):
            print(f'{m[i][j]}',end='')
        print()

#--------------------------------------

def main():
    while True:
        try:
            n = int(input())
            m = gera(n)
            imprime(m)
        except EOFError:
            break

main()