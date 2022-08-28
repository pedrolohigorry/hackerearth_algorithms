x, y, s, t = map(int, input().split())

res = 0

# With doble loop we go to every point after coordinates x and y
# and use range function to limit values of x and y
for i in range(x,x+s+1):
    for j in range(y,y+s+1):
        # Each move in the i direction and in the j direction takes 1 second.
        # The following condition takes into account how far the frog can go. 
        if i + j <= t:
            res += 1


print(res)
