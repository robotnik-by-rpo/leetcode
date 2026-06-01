def isPalindrome(self, x: int) -> bool:
    oper = -1 if x < 0 else 1
    if oper == -1:
        return False
    rests = []
    while x != 0:
        rests.append(x%10)
        x //= 10
    orig = rests.copy()
    orig.reverse()   
    return orig == rests

print(1,isPalindrome(1))
print(121, isPalindrome(121))
print(-121, isPalindrome(-121))
print(10, isPalindrome(10))
print(0,isPalindrome(0))