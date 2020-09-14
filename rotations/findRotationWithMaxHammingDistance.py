def findRotation(a):
    n = len(a)
    b = a + a
    maxHammingDistance = 0
    index = 0
    for i in range(1, n):
        count = 0
        for j in range(i, i + n):
            if b[j] != a[j-i]:
                count += 1
        if count > maxHammingDistance:
            maxHammingDistance = count
            index = i
    return (maxHammingDistance, b[index:index+n])



a = [1, 1, 2, 1, 2]
print findRotation(a)