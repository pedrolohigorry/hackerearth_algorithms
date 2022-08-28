### Solved using Calculus.
### We define the function f(x,y) = a*x**2+b*y**2  which is the total cost
### as a function of both x and y
### But x + y = n, so y = n - x
### Thus f(x) = a*x**2 + b*(n-x)**2 which now has 1 variable
### The minimum is found using Calculus techniques (derivatives)
### which is x_min = 2*b*n/(2*a+2*b)
### So we just compute the total cost rounding this minimum

t = int(input())

while t != 0:
    n, a, b = map(int, input().split())
    minimum = 2*b*n/(2*a+2*b)
    minimum = round(minimum)
    total = a * minimum **2 + b * (n-minimum) **2
    print(total)
    t -= 1
