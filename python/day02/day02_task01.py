sum = max = int(input())
while (item := int(input())) != 0:
    if item > 0:
        if sum < 0:
            sum = item
        else:
            sum += item
    elif sum < item:
        sum = item
    else:
        sum += item
    if sum > max:
        max = sum
    print(sum, max)

print(max)
