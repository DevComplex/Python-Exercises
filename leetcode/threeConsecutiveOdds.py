def threeConsecutiveOdds(arr):
    if len(arr) < 3:
        return False

    odds = 0

    for i in range(3):
        if arr[i] % 2 == 1:
            odds += 1

    if odds == 3:
        return True

    for i in range(3, len(arr)):
        if arr[i - 3] % 2 == 1:
            odds -= 1

        if arr[i] % 2 == 1:
            odds += 1

        if odds == 3:
            return True

    return False