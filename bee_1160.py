T = int(input())
for t in range(T):
    pA, pB, g1, g2 = map(float,input().split())
    pA = int(pA)
    pB = int(pB)
    anos = 0

    while pA <= pB:
        pA *= g1
        if g2 == 0:
            pB = pB
        else:
            pB *= g2
        anos += 1
        print(pA,pB)
    print(pA,pB)