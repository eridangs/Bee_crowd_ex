def descobre(v1,v2):
    i = 0
    p = 0
    while i < len(v1):
        p += v1[i] * v2[i]
        i += 1
    return p

def main():
    v1 = list(map(float,input().split()))
    v2 = list(map(float,input().split()))
    P = descobre(v1,v2)
    print(f'{P:.4f}')

main()