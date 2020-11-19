def isAlphaNumeric(ch):
    return (ch >= "0" and ch <= "9") or (ch >= "a" and ch <= "z") or (ch >= "A" and ch <= "Z")

def isPalindrome(s):
    lo = 0
    hi = len(s) - 1

    while lo < hi:
        if not isAlphaNumeric(s[lo]):
            lo += 1
        elif not isAlphaNumeric(s[hi]):
            hi -= 1
        elif s[lo].lower() != s[hi].lower():
            return False
        else:
            lo += 1
            hi -= 1

    return True

s = "A man, a plan, a canal: Panama"

print(isPalindrome(s))