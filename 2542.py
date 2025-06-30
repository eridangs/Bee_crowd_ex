def selecionar(M, L, cartaM, cartaL, col):
    cartaM -= 1
    cartaL -= 1
    col -= 1

    resultM = M[cartaM][col]
    resultL = L[cartaL][col]

    if resultM > resultL:
        print('Marcos')
    elif resultL > resultM:
        print('Leonardo')
    else:
        print('Empate')


#--------------------------------------------------

def atributos(M, L):
    Marcos = []
    Leonardo = []

    for i in range(M):
        line = list(map(int, (input().split())))
        Marcos.append(line)

    for i in range(L):
        line = list(map(int, (input().split())))
        Leonardo.append(line)

    return Marcos, Leonardo

#--------------------------------------------------

def main():
    while True:
        try:
            
            n = int(input())
            cartasM, cartasL = map(int,input().split())
            M, L = atributos(cartasM, cartasL)
            cartaM, cartaL = map(int,input().split())
            col = int(input())
            selecionar(M, L, cartaM, cartaL, col)

        except EOFError:
            break

main()