def getMin(A):
    minNum = float('inf')

    for num in A:
        minNum = min(minNum, num)

    return minNum

def getSumOfDigits(num):
    digitsSum = 0

    while num > 0:
        digit = num % 10
        digitsSum += digit
        num = num // 10

    return digitsSum

def sumOfDigits(A):
    minNum = getMin(A)
    digitsSum = getSumOfDigits(minNum)

    if digitsSum % 2 == 0:
        return 1

    return 0

A = [99,77,33,66,55]

print(sumOfDigits(A))