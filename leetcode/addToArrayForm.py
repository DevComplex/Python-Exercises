def getDigits(num):
    if num == 0:
        return [0]

    digits = []

    while num > 0:
        digit = num % 10
        digits.append(digit)
        num = num // 10

    return digits[::-1]


def addToArrayForm(A, K):
    arrayForm = getDigits(K)

    i = len(A) - 1
    j = len(arrayForm) - 1

    carry = 0

    output = []

    while i >= 0 or j >= 0:
        x = A[i] if i >= 0 else 0
        y = arrayForm[j] if j >= 0 else 0
        carry += x + y
        digit = carry % 10
        output.append(digit)
        carry = carry // 10

        i -= 1
        j -= 1

    if carry > 0:
        output.append(carry)

    return output[::-1]

A = [9,9,9,9,9,9,9,9,9,9]
K = 1

print(addToArrayForm(A, K))