def gerarM(n):
    M = [[0] * n for _ in range(n) ]
    valor = 1
    li = ci = 0
    lf = cf = n - 1


    for camada in range(n // 2 + 1):

        #borda superior
        for j in range(ci, cf + 1):
            print(f'M{li}{j}')
            M[li][j] = valor
            valor += 1

        # borda direita
        for k in range(li + 1, lf + 1):
            print(f'M{k}{cf}')
            M[k][cf] =  valor
            valor += 1
        
        # borda inferior
        for l in range(cf - 1, ci - 1, -1):
            print(f'M{lf}{l}')
            M[lf][l] = valor
            valor += 1

        #borda esquerda
        for m in range(lf - 1, li, -1):
            print(f'M{m}{ci}')
            M[m][ci] = valor
            valor += 1

        li += 1
        ci += 1
        lf -= 1
        cf -= 1

    return M
#------------------------------------------

def imprime(M,n):
    T = len(str(n*n))
    for i in range(n):
        for j in range(n):
            if  j == len(M) - 1:
                print(f'{M[i][j]:>{T}}',end='')
            else:
                print(f'{M[i][j]:>{T}}',end=' ')
        print()

#------------------------------------------

def main():
    n = int(input())
    M = gerarM(n)
    imprime(M,n)

main()