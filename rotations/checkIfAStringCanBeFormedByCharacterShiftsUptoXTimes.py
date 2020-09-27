'''
Given an integer X and two strings S1 and S2, the task is to check that string S1 can be 
converted to the string S2 by shifting characters circular clockwise atmost X times.
 
    Input: S1 = "abcd", S2 = "dddd", X = 3 
    Output: Yes 
    Explanation: 
    Given string S1 can be converted to string S2 as- 
    Character "a" - Shift 3 times - "d" 
    Character "b" - Shift 2 times - "d" 
    Character "c" - Shift 1 times - "d" 
    Character "d" - Shift 0 times - "d"
    Input: S1 = "you", S2 = "ara", X = 6 
    Output: Yes 
    Explanation: 
    Given string S1 can be converted to string S2 as - 
    Character "y" - Circular Shift 2 times - "a" 
    Character "o" - Shift 3 times - "r" 
    Character "u" - Circular Shift 6 times - "a" 
'''
def check(s1, s2, x):
    n = len(s1)
    s1 = s1.lower()
    s2 = s2.lower()
    for i in range(n):
        d = ord('z') - ord('a') + 1
        p = ((ord(s1[i]) + x - ord('a')) % d) + ord('a')
        if p < ord(s2[i]):
            return False
    return True

s1 = "you"
s2 = "arb"
print check(s1, s2, 6)
