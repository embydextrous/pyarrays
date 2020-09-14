def splitAndAdd(a, k):
    n = len(a)
    if k >= n - 1:
        return
    reverse(a, 0, k - 1)
    reverse(a, k, n - 1)
    reverse(a, 0, n - 1)

def reverse(a, l, r):
    while l < r:
        a[l], a[r], l, r = a[r], a[l], l + 1, r - 1

a = [1, 2, 3, 4, 5]
splitAndAdd(a, 2)
print a
