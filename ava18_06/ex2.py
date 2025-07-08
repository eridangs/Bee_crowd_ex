
def gerarM(n):
    M = [ [0] * n for _ in range(n)]
    val = n**2

    for i in range(n):
        if i % 2 == 0:
            for k in range(n):
                M[i][k] = val
                val -= 1
        else:
            for k in range(n-1,-1,-1):
                M[i][k] = val
                val -= 1
    
    return M

#------------------------------------------

def imprime(M,n):
    for i in range(n):
        for j in range(n):
            print(f'{M[i][j]}',end='\t')
        print()

#------------------------------------------

def main():
    n = int(input())
    M = gerarM(n)
    imprime(M,n)

main()