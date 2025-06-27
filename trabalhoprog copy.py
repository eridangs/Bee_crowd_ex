#Lara Eridan Genes Santiago e Emily Vitória
def matrizX1(M:list,L:list):
    n = len(M)

    for i in range(1, n): #a partir da coluna 1/ zerar primeira linha até o final
        l = L[i-1]
        for j in range(len(M)): # percorre as linhas
            #print(f'M[{j}][{i}] = {M[j][i]} - {l} * {M[j][i-1]}')
            M[j][i] -= l * M[j][0]
    
    return M

#-------------------------------------------------------

def matrizX2(M):
    for i in range(1,len(M)): #(1,n-1) linhas

        Betas = descobrirbeta(M,i)
        if Betas == 0:
            return 0
        
        posicao = 0

        for j in range(i+1,len(M)):# colunas
            B = Betas[posicao]
            #print(f'Beta {posicao}:{B:.2f} =  {M[i][j]:.2f} / {M[i][i]:.2f}')

            for k in range(i,len(M)): #percorrer as linhas de baixo
                M[k][j] -= B * M[k][i]
                #print(f'M[{k}][{j}] = {M[k][j]:.2f} -  {B:.2f} * {M[k][i]:.2f}')

            posicao += 1

    return M

#------------------------------------------------------------

def descobrirbeta(M, i):
    Betas = []
    # β = a{i,j} / a{i,i}
    for j in range(i + 1, len(M)):
        if M[i][i] == 0:
            return 0
        beta = M[i][j] / M[i][i]
        Betas.append(beta)
    return Betas

#-------------------------------------------------------

def descobrirlambda(M): #metodo do professor
    Lambdas = []
    for j in range(1,len(M)):
        #rint(f'L = {M[0][j]}/{M[0][0]}')
        if M[0][0] == 0:
            return 0
        L = M[0][j]/M[0][0]
        Lambdas.append(L)
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
    if L == 0:
        print('Divisao por zero.')
        return
        
    M = matrizX1(M,L) # Zerar primeira linha
    M = matrizX2(M) #Zerar linhas seguintes
    if M == 0:
        print('Divisao por zero.')
        return
    else:
        imprime(M)
    #matrizY(M,L)
   
main()

#if j == len(M)-1:
#print(f'{M[i][j]}',end=("\t"))
#-------------------------------------------------------

# def descobrirbeta(M):
#     Betas = []
#     for i in range(1,len(M)):
#         for j in range(2,len(M)):
#             B = M[i][j] / M[i][j-1]
#             Betas.append(B)
#     print(Betas)

#     return Betas


# def matrizY(M:list,L:list):
#     coluna = 0
#     Ediagonal = []
#     for i in range(1,len(M)):
#         for j in range(len(M)):
#             if j <= coluna:
#                 Ediagonal.append(M[i][j])
#                 M[i][j] = 0

#         coluna += 1
#     print()
#     print(Ediagonal)

#---------------------------------------------