'''
Given an array arr that has numbers appearing twice or once.
The task is to identify numbers that occurred only once in the array.

Note: Duplicates appear side by side every time. Might be few numbers can occur one time and just assume this is a 
right rotating array (just say an array can rotate k times towards right). 
Order of the elements in the output doesn't matter.

Examples:

Input: arr[] = { 7, 7, 8, 8, 9, 1, 1, 4, 2, 2 }
Output: 9 4

Input: arr[] = {-9, -8, 4, 4, 5, 5, -1}
Output: -9 -8 -1
'''
def printOnceOccuringElement(a):
    n = len(a)
    i = 0
    if n > 1 and a[0] == a[n-1]:
        print a[0],
        i += 1
    while i < n - 1:
        if a[i] == a[i+1]:
            print a[i],
            i += 2
        else:
            i += 1

a = [7, 8, 8, 9, 1, 1, 4, 2, 2, 7]
printOnceOccuringElement(a)
