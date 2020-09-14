def findRotation(a, k):
    n = len(a)
    for i in range(k, k + n):
        print a[i % n],

a = [1, 2, 3, 4, 5]
findRotation(a, 3)