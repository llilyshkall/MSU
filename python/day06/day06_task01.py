uneven = {'a', 'e', 'i', 'o', 'u', 'y'}
even = {'a', 'e', 'i', 'o', 'u', 'y'}
i = 1
while s := input():
    if i == 1:
        for item in s:
            if item not in uneven:
                uneven.add(item)
    if i == 0:
        for item in s:
            if item not in even:
                even.add(item)
    if i == 0:
        i = 1
    else:
        i = 0

if len(uneven) > len(even):
    print("Mumbo")
else:
    print("Jumbo")
