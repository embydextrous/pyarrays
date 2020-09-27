def generateAllRotations(n):
    k = n
    d = 0
    while k > 0:
        k /= 10
        d += 1
    result = set()
    for j in range(1, d):
        result.add(n / (10 ** j) + (n % (10 ** j)) * (10 ** (d-j)))
    return result

print generateAllRotations(1200)