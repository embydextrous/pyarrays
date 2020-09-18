def minRotationsToGetSameString(s):
    a = s + s
    n = len(s)
    for i in range(1, n + 1):
        if a[i:i+n] == s:
            return i
    return len(s)


s = "abcabc"
print minRotationsToGetSameString(s)
