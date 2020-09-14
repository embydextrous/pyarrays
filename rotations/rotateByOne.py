def rotateByOne(a):
    n = len(a)
    x = a[n-1]
    for i in range(n - 1):
        a[n-1-i] = a[n-2-i]
    a[0] = x

a = [1, 2, 3, 4, 5]
print a
rotateByOne(a)
print a
rotateByOne(a)
print a
rotateByOne(a)
print a