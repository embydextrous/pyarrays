'''
https://www.geeksforgeeks.org/find-element-given-index-number-rotations/
'''
def findElement(a, ranges, index):
    for r in ranges[::-1]:
        left, right = r[0], r[1]
        if index >= left and index <= right:
            if index == left:
                index = right
            else:
                index -= 1
        print index
    return a[index]

a = [1, 2, 3, 4, 5]
ranges = [[0, 2], [0, 3]]
index = 1
print findElement(a, ranges, index)