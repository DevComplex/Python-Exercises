def postorderHelper(n, output):
    for child in n.children:
        postorderHelper(child, output)

    output.append(n.val)

def postorder(root):
    if root == None:
        return

    output = []

    postorderHelper(root, output)

    return output