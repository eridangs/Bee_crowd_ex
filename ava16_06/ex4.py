def descobreM(M):
    n = len(M)
    maisrepetiu = 0
    repetidos = []
    vezesrepetido = []

    for i in range(n): #linhas inteiras
        for j in range(n):
            numero = M[i][j]
            if numero not in repetidos:
                repetidos.append(numero)
                repetiu = 0
                for k in range(n):
                    for l in range(n):
                        numerocomparado = M[k][l]
                        print(f'numero: {numero} é igual a {numerocomparado}?')

                        if numero == numerocomparado:
                            repetiu += 1
                            print(f'sim: {repetiu}')

                print(f'quantas vezes {numero} repetiu: {repetiu}')
                vezesrepetido.append(repetiu)
            if repetiu > maisrepetiu:
                maisrepetiu = repetiu
                
    print(f'mais vezes repetido = {maisrepetiu}')
    print(repetidos)
    print(vezesrepetido)

    return 0

#-------------------------------------------

def geraM(m):
    M = []

    for i in range(m):
        n = list(map(int,input().split()))
        M.append(n)
    
    return M

#---------------------------------------------

def main():
    ordem = int(input())
    M = geraM(ordem)
    p = descobreM(M)
    print(f'{p}')

main()
        # for j in range(n):
        #     for k in range(n): #confirmação interna
        #         print(f'{M[j][k]} == {repete}\n')
        #         if M[j][k] == repete:
        #             repetiu += 1
        #             print(f'quantas vezes repetiu: {repetiu}')

        #     print(f'antes: {maisrepetiu}\n')

        #     if repetiu > maisrepetiu:
        #         maisrepetiu = repetiu
        #         print(f'depois: {maisrepetiu}\n')