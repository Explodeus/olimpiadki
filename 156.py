import math

n,k = map(int, input().split())

if k > n:
    print(0)
else:
    print(math.factorial(n)**2 // math.factorial(n - k)**2 // math.factorial(k))