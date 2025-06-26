#Lara Eridan Genes Santiago e Emily Vitória
def matrizX(M):
    coluna = 1
    Adiagonal = []
    for i in range(len(M)-1):
        for j in range(len(M[0])):
            if j >= coluna:
                Adiagonal.append(M[i][j])
                M[i][j] = 0
        coluna += 1
    print()
    print(Adiagonal)

#---------------------------------------------

def matrizY(M):
    coluna = 0
    Ediagonal = []
    for i in range(1,len(M)):
        for j in range(len(M)):
            if j <= coluna:
                Ediagonal.append(M[i][j])
                M[i][j] = 0

        coluna += 1
    print()
    print(Ediagonal)

#---------------------------------------------

def descobrirlambda(M):
    Lambdas = []
    for j in range(1,len(M)):
        L = M[0][j]/M[0][0]
        Lambdas.append(L)
    print()
    print(Lambdas)
    return Lambdas

#-----------------------------------------------

def lerM(n):
    M = [[''] * n for i in range(n)]
    for i in range(n):
        linha = list(map(float,input().split()))
        for j in range(n):
            M[i][j] = linha[j]
    return M

# ----------------------------------------------

def imprime(M):
    for i in range(len(M)):
        for j in range(len(M)):
            print(f'{M[i][j]:.2f}',end=("\t"))
        print()

#----------------------------------------------

def main():
    n = int(input())
    M = lerM(n)
    L = descobrirlambda(M)
    matrizX(M)
    matrizY(M)
    imprime(M)
   

main()

#if j == len(M)-1:
#print(f'{M[i][j]}',end=("\t"))