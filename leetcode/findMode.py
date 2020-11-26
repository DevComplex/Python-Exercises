import collections

def findModeHelper(n, count, mode):
    if n == None:
        return

    count[n.val] += 1
    mode[0] = max(mode[0], count[n.val])
    findModeHelper(n.left, count, mode)
    findModeHelper(n.right, count, mode)

def findMode(root):
    count = collections.defaultdict(int)
    mode = [0]
    output = []

    findModeHelper(root, count, mode)

    for value, occurence in count.items():
        if occurence == mode[0]:
            output.append(value)

    return output
