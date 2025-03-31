a, b, c, d = map(int,input().split())
if b>c:
    if d>a:
        if c+d > a+b:
            if c>0 and d>0:
                if a%2 == 0:
                    print('Valores aceitos')
                else:
                    print('Valores nao aceitos')
            else:
                print('Valores nao aceitos')
        else:
                    print('Valores nao aceitos')
    else:
                    print('Valores nao aceitos')                
else:
    print('Valores nao aceitos')