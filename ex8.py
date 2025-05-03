n = int(input())
enesimo = 1
for i in range(n+1):
    if i > 1:
        enesimo += 1/i
print(f'{enesimo:.4f}')