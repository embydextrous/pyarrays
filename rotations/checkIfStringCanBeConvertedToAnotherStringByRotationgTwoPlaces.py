def check(s1, s2):
    a = s1 + s1
    return a[2:len(s1)+2] == s2 or a[len(s1) - 2: 2 * len(s1) - 2] == s2

def checkD(s1, s2, d):
    a = s1 + s1
    return a[d:len(s1) + d] == s2 or a[len(s1) - d: 2 * len(s1) - d] == s2

s1 = "amazon"
s2 = "azonam"

s3 = "abcdefg"
s4 = "cdefgab"

print check(s1, s2)
print checkD(s3, s4, 2)