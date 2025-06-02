def descobre(l:list):
    m = l[0]
    M = l[0]
    for i in range(len(l)):
        if l[i] < m:
            m = l[i]
        elif l[i] > M:
            M = l[i]
    return m,M

def main():
    numbers = list(map(int,input().split()))
    m,M = descobre(numbers)
    print(f'Menor = {m}\nMaior = {M}')

main()