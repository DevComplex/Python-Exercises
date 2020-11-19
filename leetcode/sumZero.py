def sumZero(n):
    if n == 1:
        return [0]

    total = 0
    output = []

    for i in range(1, n):
        output.append(i)
        total += i

    output.append(-total)

    return output

print(sumZero(2))
