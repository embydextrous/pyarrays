def oddAndEvenRotation(n):
    odd = even = 0
    while n > 0:
        if (n % 10) & 1 == 1:
            odd += 1
        else:
            even += 1
        n /= 10
    return (odd, even)

print oddAndEvenRotation(361876128)