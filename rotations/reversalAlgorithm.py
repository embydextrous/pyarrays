def leftRotate(arr, k):
    length = len(arr)
    k %= length
    reverse(arr, 0, k - 1)
    reverse(arr, k, length - 1)
    reverse(arr, 0, length - 1)
    return arr

def rightRotate(arr, k):
    length = len(arr)
    k %= length
    reverse(arr, 0, length - 1)
    reverse(arr, k, length - 1)
    reverse(arr, 0, k - 1)
    return arr


def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

arr = [1,2,3,4,5,6,7]
k = 2
print arr
rightRotate(arr, 2)
print arr