t = int(input())
while t != 0:
    n = int(input())
    array = list(map(int, input().split()))
    if n == 0 or n == 1:
        print(0)
    if n == 2 or n ==3:
        max1 = max(array)
        min1 = min(array)
        weigh = max1 - min1
        print(weigh)
    if n >= 4:
        max1 = max(array)
        min1 = min(array)
        array.remove(max1)
        array.remove(min1)
        max2 = max(array)
        min2 = min(array)
        weigh1 = max1 - min1
        weigh2 = max2 - min2
        total = weigh1 + weigh2
        print(total)

    t -= 1
