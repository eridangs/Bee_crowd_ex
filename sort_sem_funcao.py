a,b,c = map(int,input().split())
maior = 0
menor = 0
medio = 0
if a >= b and a >= c:
    maior = a
    if b <= a and b > c:
        medio = b
        menor = c
    elif c > b or c == a:
        medio = c
        menor = b
elif b > a and b > c:
    maior = b
    if a <= b and a >=c:
        medio = a
        menor = c
    elif c <= b and c >a:
        medio = c
        menor = a
elif c >= a and c >=b:
    maior = c
    if a <= c and a >= b:
        medio = a
        menor = b
    elif b <= c and b >= a:
        medio = b
        menor = a
print(f'{menor}\n{medio}\n{maior}\n\n{a}\n{b}\n{c}')