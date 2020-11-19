import math

def getDigits(N):
    digits = []

    while (N > 0):
        digit = N % 10
        digits.append(digit)
        N = N // 10
        
    return digits

def getTotal(digits):
    K = len(digits)
    total = 0

    for digit in digits:
        total += int(math.pow(digit, K))

    return total

def isArmstrong(N):
    digits = getDigits(N)
    total = getTotal(digits)
    return total == N

print(isArmstrong(153))