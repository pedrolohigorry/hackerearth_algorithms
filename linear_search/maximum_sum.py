n = int(input())
array = list(map(int, input().split()))

maximum_sum = 0
numbers = 0
maximum_negative = array[0]

# If we have positive and negative numbers, then only positive numbers
# actually add to the maximum sum.
# If there are only negative numbers, then the biggest negative number
# is the only element that gives us the maximum sum.
for number in array:
    if number >= 0: # The zeros add to the maximum numbers of elements
        maximum_sum += number
        numbers += 1
    elif abs(maximum_negative) > abs(number):
        maximum_negative = number

if numbers != 0:
    print(maximum_sum, numbers)
else:
    print(maximum_negative, 1)
