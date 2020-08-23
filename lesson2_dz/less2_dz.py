import math

def y(n):
    # return n / ((math.factorial(n))**(1/n))
    return math.e/((2*math.pi*n)**(1/n))

eps = 10**(-7)
mult  = 10
n = 1

while True:
    if y(n+ 1) - y(n) < eps:
        print(y(n))
        break
    else:
        n *= mult