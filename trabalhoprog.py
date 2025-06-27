#Emily Vitória de Souza Oliveira e Lara Eridan Genes Santiago - SI 2025


def matrizX1(M:list,L:list):
    n = len(M)

    for i in range(1, n):
        l = L[i-1]
        for j in range(len(M)):
            M[j][i] -= l * M[j][0]
    
    return M

#-------------------------------------------------------

def matrizX2(M):
    coeficienteB = []
    for i in range(1,len(M)):
        posicao = 0
        Betas = descobrirbeta(M,i)

        if Betas == 0:
            return 0,0
        
        for j in range(i+1,len(M)):
            B = Betas[posicao]

            if not B in coeficienteB:
                coeficienteB.append(B)

            for k in range(i,len(M)):
                M[k][j] -= B * M[k][i]
            posicao += 1

    return M, coeficienteB

#------------------------------------------------------------

def descobrirbeta(M, i):
    Betas = []
    for j in range(i + 1, len(M)):
        if M[i][i] == 0:
            return 0
        
        beta = M[i][j] / M[i][i]
        Betas.append(beta)
    return Betas

#-------------------------------------------------------

def descobrirlambda(M):
    Lambdas = []
    for j in range(1,len(M)):
        if M[0][0] == 0:
            return 0
        
        L = M[0][j]/M[0][0]
        Lambdas.append(L)
    return Lambdas

#------------------------------------------------------

def matrizY(M:list,L:list,B:list) -> list:
    coefientes = L + B
    C = len(coefientes)
    T = 0
    n = len(M)
    coluna = 1
    My = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(1,n):
            My[i][i] = 1 # diagonal = 1

            if j >= coluna and T != C:
                My[i][j] = coefientes[T]
                T += 1
        coluna += 1
    return My

#------------------------------------------------------

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
    print()

#----------------------------------------------

def main():
    n = int(input()) # Receber ordem da matriz
    M = lerM(n) # Preencher matriz
    L = descobrirlambda(M)
    if L == 0: # Lambda
        print('Divisao por zero.')
        return
        
    X = matrizX1(M,L) # Zerar primeira linha da matriz X
    X, B = matrizX2(X) #Zerar linhas seguintes
    if X == 0:
        print('Divisao por zero.')
        return
    
    imprime(X)
    Y = matrizY(X,L,B) # Criar matriz Y
    imprime(Y)
#-------------------------------------------------

main()