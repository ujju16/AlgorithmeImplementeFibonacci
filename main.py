""" Suite de Fibonacci """

n = int(input("Entrer un entier supérieur à 1: "))

fibo = [0]*(n+1)
fibo[0] = 0
fibo[1] = 1

for i in range(2, n+1):
  fibo[i] = fibo[i-1] + fibo[i-2]

