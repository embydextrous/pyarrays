def pairSum(a, s):
    n = len(a)
    pivot = findPivot(a, 0, n)
    l = pivot + 1
    r = pivot
    while l != r:
        print l, r, a[l] + a[r]
        if a[l] + a[r] == s:
            return (l, r)
        if a[l] + a[r] < s:
            l = (l + 1) % n
        else:
            r = (r - 1) % n

def findPivot(a, l, r):
    if l > r:
        return -1
    mid = (l+r)/2
    if mid < r and a[mid] > a[mid+1]:
        return mid
    if mid > l and a[mid-1] > a[mid]:
        return mid - 1
    if a[l] >= a[mid]:
        return findPivot(a, l, mid - 1)
    return findPivot(a, mid + 1, r)


a = [6, 7, 8, 1, 2, 3, 4, 5]
print(pairSum(a, 4))