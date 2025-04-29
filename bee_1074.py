cont = int(input())
while cont > 0:
    N = int(input())
    if N > 0:
        n = 'POSITIVE'
    elif N < 0:
        n = 'NEGATIVE'
    if N == 0:
        print('NULL')
    elif N % 2 == 0:
        print(f'EVEN {n}')
    else:
        print(f'ODD {n}')
    cont -= 1