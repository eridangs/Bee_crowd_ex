def gera(n):
    m = [[0]*n for _ in range(n)]
    a = n
    meio = n//2
    q1 = n//3
    fimq1 = n - q1

# diagonais
    for i in range(n):
        m[i][i] = 2
    for i in range(a):
        m[a-1][i] = 3
        a -= 1
# diagonais

    for i in range(q1,fimq1):
        for j in range(q1,fimq1):
            m[i][j] = 1
    
    m[meio][meio] = 4

    return m
#--------------------------------------
def imprime(m):
    for i in range(len(m)):
        for j in range(len(m)):
            print(f'{m[i][j]}',end='')
        print()
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