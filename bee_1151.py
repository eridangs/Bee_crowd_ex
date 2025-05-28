n = int(input())
fibonacci = 0
guarda = 1
for f in range(n):
    print(fibonacci,end=' ')
    fibonacci, guarda = guarda, fibonacci + guarda