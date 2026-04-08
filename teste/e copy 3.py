# 3. Ordenação Personalizada

v = list(map(int, input().split()))
vpar = []
vimpar = []

for i in range(0, len(v)):
    if v[i] % 2 == 0:
        vpar.append(v[i])
    else:
        vimpar.append(v[i])

for i in range(len(vpar)):
    for j in range(i + 1, len(vpar)):
        if vpar[j] < vpar[i]:
            vpar[i], vpar[j] = vpar[j], vpar[i]

for i in range(len(vimpar)):
    for j in range(i + 1, len(vimpar)):
        if vimpar[i] < vimpar[j]:
            vimpar[i], vimpar[j] = vimpar[j], vimpar[i]

v = vpar + vimpar
print(v)