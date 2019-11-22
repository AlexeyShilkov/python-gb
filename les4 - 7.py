from math import factorial

def fibo_gen(n):
    i = 0
    for n in range(1,n):
        m = factorial(n)
        if n >= 15:
            break
        yield m

for i in fibo_gen(19):
    print(i)

