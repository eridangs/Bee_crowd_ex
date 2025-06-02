conjunto = list(map(int,input()))
soma = conjunto[0]

totalconjuntos = 2 ** len(conjunto)
i = 0
while i <= len(conjunto):
    sub = conjunto[i]
    if sub > soma:
        soma = sub
    if i == len(conjunto):
        i = 0
        sub = conjunto[i] + conjunto[i+1]
    i += 1
    # if conjunto[0] + conjunto[1] + conjunto[2] > soma:
    #     soma = 
    #SOMAR TODOS OS POSITIVOS   