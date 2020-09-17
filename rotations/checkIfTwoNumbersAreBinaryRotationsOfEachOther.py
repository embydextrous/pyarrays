def checkIfBinaryRotation(a, b):
    x = a | a << 32
    while x >= b:
        print "{0:b}".format(x)
        if x & 0xffffffff == b:
            return True
        x >>= 1
    return False

b = 122
a = 2147483678

print checkIfBinaryRotation(a, b)