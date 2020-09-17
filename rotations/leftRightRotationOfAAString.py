def leftRotation(s, k):
    a = s + s
    return a[k:k+len(s)]


def rightRotation(s, k):
    a = s + s
    return a[len(s) - k: 2 * len(s) - k]


s = "GEEKSFORGEEKS"
print leftRotation(s, 4)
print rightRotation(s, 4)