import sys

def minMove(a):
    miniMove = sys.maxint

    for target in a:
        count = 0
        for s in a:
            b = s + s
            for i in range(len(target)):
                if b[i:i+len(target)] == target:
                    print i
                    count += i
                    break

        if count < miniMove:
            miniMove = count
    return miniMove

a = ["xzzwo", "zwoxz", "zzwox", "xzzwo"]
print minMove(a)

                