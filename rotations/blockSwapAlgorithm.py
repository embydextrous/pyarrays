def leftRotate(arr, k):
    if k % len(arr) == 0:
        return
    leftRotateUtil(arr, 0, len(arr) - 1, k, True)

def leftRotateUtil(arr, start, end, k, fixedRight):
    if start >= end:
        return
    l = end - start + 1
    if fixedRight:
        i, j = k, l - k
    else:
        j, i = k, l - k
    if i < j:
        swap(arr, start, end - i + 1, i)
        leftRotateUtil(arr, start, end - i, i, True)
    elif i > j:
        swap(arr, start, end - j + 1, j)
        leftRotateUtil(arr, start + j, end, j, False)
    else:
        swap(arr, start, start + i, i)

def swap(arr, x1, x2, k):
    while k > 0:
        arr[x1], arr[x2] = arr[x2], arr[x1]
        x1 += 1
        x2 += 1
        k -= 1

arr = [1,2,3,4,5,6,7]
leftRotate(arr, 1)
print arr