def mostrarMaior(numeros:list, vezes_repetidos:list, maiorquantiarepetida:int):
    mostrar = []
    for i in range(len(vezes_repetidos)):
        if vezes_repetidos[i] == maiorquantiarepetida:
            mostrar.append(numeros[i])

    for i in mostrar:
        print(i)

#---------------------------------------------------------

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

                        if numero == numerocomparado:
                            repetiu += 1

                vezesrepetido.append(repetiu)
            if repetiu > maisrepetiu:
                maisrepetiu = repetiu

    return repetidos, vezesrepetido, maisrepetiu

#------------------------------------------------------------

def geraM(m):
    M = []

    for i in range(m):
        n = list(map(int,input().split()))
        M.append(n)
    
    return M

#------------------------------------------------------------

def main():
    ordem = int(input())
    M = geraM(ordem)
    numeros, vezes_cada, maior = descobreM(M)
    mostrarMaior(numeros,vezes_cada,maior)

main()