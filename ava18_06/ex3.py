def transposta(matriz,m,n):
    T = [[0]*m for _ in range(n)]

    for i in range(m):
        for j in range(n):
            T[j][i] = matriz[i][j]
    return T
#------------------------------------------------------------

def imprime(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            print(f'{M[i][j]}',end=' ')
        print()

#------------------------------------------

def main():
    m, n = map(int,input().split())
    Ma = []
    for i in range(m):
        Ma.append(list(map(int,input().split())))
    T = transposta(Ma,m,n)
    imprime(T)

main()