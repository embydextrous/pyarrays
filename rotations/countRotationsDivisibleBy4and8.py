def rotationsDivisibleBy4(n):
    count = 0
    s = str(n)
    l = len(s)
    for i in range(l):
        num = 10 * int(s[i]) + int(s[(i+1) % l])
        if num % 4 == 0:
            count += 1
    return count

def rotationsDivisibleBy8(n):
    count = 0
    s = str(n)
    l = len(s)
    for i in range(l):
        num = 100 * int(s[i]) + 10 * int(s[(i+1) % l]) + int(s[(i+2) % l])
        if num % 8 == 0:
            count += 1
    return count

n = 43292816
print rotationsDivisibleBy4(n)
print rotationsDivisibleBy8(n)