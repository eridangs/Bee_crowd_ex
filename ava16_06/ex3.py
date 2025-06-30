def descobreM(M):
    positivo = 0
    negativo = 0
    n = len(M)

    for i in range(n):
        a = M[i][i]
        if a > 0:
            positivo += 1
        elif a < 0:
            negativo += 1
        
        j = n - 1 - i
        
        if j != i: #apenas a posição não pode ser igual, o elemento pode ser igual
            b = M[i][j]
            if b > 0:
                positivo += 1
            elif b < 0:
                negativo += 1

    return positivo,negativo

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
    p, n = descobreM(M)
    print(f'{p}\n{n}')

main()