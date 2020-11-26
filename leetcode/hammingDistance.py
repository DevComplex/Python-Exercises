def hammingDistance(x, y):
    distance = 0

    while x > 0 or y > 0:
        xBit = x & 1
        yBit = y & 1
        distance += xBit ^ yBit
        x = x >> 1
        y = y >> 1

    return distance

print(hammingDistance(1, 3))