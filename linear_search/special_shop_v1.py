## This version can't complete all testcases on time.
## See version 2 in this repo for another approach that solves
## all testcases much more efficiently

import numpy as np
t = int(input())

while t != 0:
    n, a, b = map(int, input().split())
    ## Compute all test cases using "brute force"
    X = np.arange(n+1)
    X2 = np.square(X)
    Y2 = np.flip(X2)
    total = a * X2 + b * Y2
    print(np.min(total))
    t -= 1
