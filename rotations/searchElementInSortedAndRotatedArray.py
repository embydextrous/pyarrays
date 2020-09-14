def search(a, key):
    pivot = findPivot(a, 0, len(a) - 1)
    if pivot == -1: # array is not rotated at all
        return binarySearch(a, 0, len(a) - 1, key)
    if a[pivot] == key:
        return pivot
    if a[0] <= key:
        return binarySearch(a, 0, pivot - 1, key)
    return binarySearch(a, pivot + 1, len(a) - 1, key)


def findPivot(a, l, r):
    if l > r:
        return -1
    mid = (l + r) / 2
    if mid < r and a[mid + 1] < a[mid]:
        return mid
    if mid > l and a[mid - 1] > a[mid]:
        return mid - 1
    if a[l] >= a[mid]:
        return findPivot(a, l, mid - 1)
    return findPivot(a, mid + 1, r)

def binarySearch(a, l, r, key):
    if l > r:
        return -1
    mid = (l + r) / 2
    if a[mid] == key:
        return mid
    if a[mid] < key:
        return binarySearch(a, mid + 1, r, key)
    return binarySearch(a, l, mid - 1, key)
    

a = [6, 7, 8, 1, 2, 3, 4, 5]
for i in range(0, 10):
    print search(a, i)