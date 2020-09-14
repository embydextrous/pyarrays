def findMinimumElement(a):
    pivot = findPivot(a, 0, len(a) - 1)
    return a[pivot + 1]

def findPivot(a, l, r):
    if l > r:
        return -1
    mid = (l+r)/2
    if mid < r and a[mid+1] < a[mid]:
        return mid
    if mid > l and a[mid-1] > a[mid]:
        return mid - 1
    if a[l] >= a[mid]:
        return findPivot(a, l, mid - 1)
    return findPivot(a, mid + 1, r)

a = [1, 2, 3, 4, 5, 6, 7, 8]
print findMinimumElement(a)
a = [6, 7, 8, 1, 2, 3, 4, 5]
print findMinimumElement(a)