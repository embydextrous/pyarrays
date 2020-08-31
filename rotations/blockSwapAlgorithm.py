def leftRotate(arr, k):
    length = len(arr)
    i = k
    j = length - k
    while i != j:
        if i < j:
            swap(arr, k-i, i+j-k, i)
            j -= i
        else:
            swap(arr, k-i, k, j)
            i -= j
    swap(arr, k - i, k, i)

def swap(arr, x1, x2, k):
    while k > 0:
        arr[x1], arr[x2] = arr[x2], arr[x1]
        x1 += 1
        x2 += 1
        k -= 1

arr = [1,2,3,4,5,6,7]
leftRotate(arr, 3)
print arr