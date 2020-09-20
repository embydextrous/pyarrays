def findLargestPairSum(a):
    p, q = max(a[0], a[1]), min(a[0], a[1])
    for i in range(2, len(a)):
        if a[i] >= p:
            p, q = a[i], p
        elif a[i] > q:
            q = a[i]
    return p + q

a = [12, 34, 10, 6, 40]
print findLargestPairSum(a)