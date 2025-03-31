n = int(input())
print(n)
c100 = n//100
n = n - (c100 * 100)
c50 = n //50
n = n - (c50 * 50)
c20 = n//20
n = n - (c20 * 20)
c10 = n //10
n = n - (c10 * 10)
c5 = n //5
n = n - (c5 * 5)
c2 = n//2
n = n - (c2 * 2)
c1 = n/1
n = n - (c1 * 1)
print(f'{c100} nota(s) de R$ 100,00\n{c50} nota(s) de R$ 50,00\n{c20} nota(s) de R$ 20,00\n{c10} nota(s) de R$ 10,00\n{c5} nota(s) de R$ 5,00\n{c2} nota(s) de R$ 2,00\n{c1} nota(s) de R$ 1,00')