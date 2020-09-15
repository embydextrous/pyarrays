def minimumRotationString(s):
    a = s + s
    n = len(s)
    cmi = 0
    for i in range(1, n):
        for j in range(n):
            if a[cmi + j] > a[i + j]:
                cmi = i
                break
            elif a[cmi + j] < a[i+j]:
                break
    return a[cmi:cmi+n]

s = "GEEKSFORGEEKS"
print minimumRotationString(s)
