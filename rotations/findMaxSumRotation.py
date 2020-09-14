def findMax(a):
    sum = 0
    n = len(a)
    for i in a:
        sum += i
    rotationSum = 0
    for i in range(n):
        rotationSum += i * a[i]
    maxRotationSum = rotationSum
    for i in range(n-1):
        rotationSum = rotationSum + sum - n * a[n-1-i]
        maxRotationSum = max(maxRotationSum, rotationSum)
    return maxRotationSum

a = [6, 0, 1, 2, 3, 4, 5]
print findMax(a)