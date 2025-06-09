e = int(input())#num na mao esquerda
d = int(input())#num na mao direita
if e != d and d >=0 and e >=0 and e <= 5 and e <= 5:
    if e > d:
        r = e + d
    else:
        r = (d - e) * 2

    print(r)