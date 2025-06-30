def descobrirMaior(M):
    maior = M[0][0]

    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] > maior:
                maior = M[i][j]

    return maior

#--------------------------------------------

def lerM(m):
    M = []

    for i in range(m):
        n = list(map(int,input().split()))
        M.append(n)
    return M

#--------------------------------------------

def main():
    linha, coluna = map(int,input().split())
    M = lerM(linha)
    maior = descobrirMaior(M)
    print(maior)

main()