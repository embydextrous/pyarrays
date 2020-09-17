def check(s1, s2):
    a = s1 + s1
    return a[2:len(s1)+2] == s2 or a[len(s1) - 2: 2 * len(s1) - 2] == s2

s1 = "amazon"
s2 = "azonam"

print check(s1, s2)