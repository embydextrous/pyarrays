def sortBitonicArray(a):
    n = len(a)
    pivot = findPivot(a, 0, n - 1)
    if pivot != -1:
        reverse(a, 0, pivot)
        reverse(a, pivot + 1, n - 1)
        reverse(a, 0, n - 1)


def reverse(a, l, r):
    while l < r:
        a[l], a[r] = a[r], a[l]
        l += 1
        r -= 1
    

def findPivot(a, l, r):
    if l > r:
        return -1
    mid = l + (r - l) / 2
    if mid > l and a[mid-1] > a[mid]:
        return mid - 1
    if mid < r and a[mid] > a[mid+1]:
        return mid
    if a[l] >= a[mid]:
        return findPivot(a, l, mid - 1)
    return findPivot(a, mid + 1, r)

a = [6, 7, 8, 1, 2, 3, 4, 5]
sortBitonicArray(a)
print a