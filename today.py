l1 = [2, 7, 1, 5, 10]

for x in range(0, 1):
    min = tuple()
    sum = 0
    for i in l1:
        sum += (i - x)**2
    if sum < min[0]:
        min = (sum, float(x/10))
