import sys

def checkSortedAndRotated(a):
    minEle = sys.maxint
    n = len(a)
    minIndex = -1
    for i in range(n):
        if a[i] < minEle:
            minEle = a[i]
            minIndex = i
    if minIndex == 0:
        return False
    for i in range(minIndex + 1, n - 1):
        if a[i] > a[i+1]:
            return False
    for i in range(minIndex-1):
        if a[i] > a[i+1]:
            return False
    return True

a = [6, 7, 8, 1, 2, 3, 4, 5]
print checkSortedAndRotated(a)
a = [1, 2, 3, 4, 5, 6, 7, 8]
print checkSortedAndRotated(a)
a = [8, 1, 2, 3, 4, 4, 3, 5]
print checkSortedAndRotated(a)
