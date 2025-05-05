n = int(input())
operacao = True
pi = 4
for i in range(n+1):
    if i >= 3 and i % 2 != 0:
        if operacao == True:
            pi -= 4/i
            operacao = False
        else:
            pi += 4/i
            operacao = True
print(f"{pi:.4f}")