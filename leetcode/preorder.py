def preorderHelper(n, output):
    output.append(n.val)

    for child in n.children:
        preorderHelper(child, output)

def preorder(root):
    if root == None:
        return

    output = []

    preorderHelper(root, output)

    return output