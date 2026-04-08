# 5. Maior Subsequência Crescente

v = list(map(int, input().split()))

msequencia = 1

count = 1

for i in range(len(v)):
    if i == 0: continue
    if v[i] > v[i-1]:
        count+=1
    else:
        if count > msequencia:
            msequencia = count
        count = 1

print(msequencia)