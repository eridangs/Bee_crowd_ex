a,b,c = map(float,input().split())
maior = 0
if a >= b and a >= c:
    maior = a
    a = maior
    b = b
    c = c
elif b > a and b > c:
    maior = b
    b = a
    c = c
    a = maior
elif c >= a and c >=b:
    maior = c
    c = a
    b = b
    a = maior
if a>=b+c:
    print('NAO FORMA TRIANGULO')
else:
    a **= 2
    b **= 2
    c **= 2
    if a == b + c:
        print('TRIANGULO RETANGULO')
    elif a == b == c:
        print('TRIANGULO ACUTANGULO\nTRIANGULO EQUILATERO')
    elif a > (b + c):
        print('TRIANGULO OBTUSANGULO')
        if a == b or a == c or b == c:
            print('TRIANGULO ISOSCELES')
    elif a < (b + c):
        print('TRIANGULO ACUTANGULO')
        if a == b or a == c or b == c:
            print('TRIANGULO ISOSCELES')