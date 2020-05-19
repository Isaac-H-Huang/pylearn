def findMinMax(list):
    min = list[0]
    max = list[0]
    for i in list[1:]:
        if min > i:
            min = i
        if max < i:
            max = i
    return [min, max]

print(findMinMax([7]))
print(findMinMax([7,9]))
print(findMinMax([7, 1, 3, 5, 11, 9]))
