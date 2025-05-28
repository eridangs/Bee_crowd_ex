T = int(input())
for t in range(T):
    pA, pB, g1, g2 = map(float,input().split())
    anos = 0

    while pA <= pB:
        if anos > 100:
            pA = pB + 1
        pA += pA*(g1/100)
        pA//= 1
        if g2 == 0:
            pB = pB
        else:
            pB += pB*(g2/100)
            pB//= 1
        anos += 1
    pA = int(pA)
    pB = int(pB)
    if anos > 100:
        print("Mais de 1 seculo.")
    else:
        print(anos," anos.")