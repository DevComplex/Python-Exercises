def comesBefore(before, after, weights):
    i = 0

    while i < min(len(before), len(after)):
        index1 = ord(before[i]) - ord('a')
        index2 = ord(after[i]) - ord('a')

        if weights[index1] < weights[index2]:
            return True
        if weights[index1] > weights[index2]:
            return False
            
        i += 1

    return len(before) <= len(after)


def isAlienSorted(words, order):
    weights = [0] * 26

    for i, letter in enumerate(order):
        index = ord(letter) - ord('a')
        weights[index] = i

    for i in range(len(words) - 1):
        if not comesBefore(words[i], words[i + 1], weights):
            return False

    return True