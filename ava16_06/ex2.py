def somaL(L):
    soma = 0
    for i in L:
        soma += i

    return soma

#--------------------------------------------

def somaM(M):
    maiorlinha = []

    for i in range(len(M)):
        maior = M[i][0]
        for j in range(len(M[0])):
            if M[i][j] > maior:
                maior = M[i][j]
        maiorlinha.append(maior)

    return maiorlinha

#--------------------------------------------

def lerM(m):
    M = []
    
    for i in range(m):
        coluna = list(map(int,input().split()))
        M.append(coluna)

    return M

#--------------------------------------------

def main():
    linha = int(input())
    coluna = int(input())
    M = lerM(linha)
    linhas = somaM(M)
    soma = somaL(linhas)
    print(soma)

main()