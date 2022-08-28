n = int(input())
a = list(map(int, input().split()))
m = int(input())
c = list(map(int, input().split()))

# Calculate all possible values of numbers of B
temp = []
for number_c in c:
    for number_a in a:
        temp.append(number_c - number_a)

# For every possible value of B in temp, check if the sum with every
# number of A is actually in C. If so, then add it to B.
b = set()
for number in temp:
    is_in = True
    for number_a in a:
        suma = number + number_a
        if suma not in c:
            is_in = False
    if is_in == True:
        b.add(number)

# The set is not sorted, so we sort it first
b_list = list(b)
b_list.sort()

print(*b_list, sep=" ")
