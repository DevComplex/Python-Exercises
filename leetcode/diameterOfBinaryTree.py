def diameterOfBinaryTreeHelper(root, solution):
    if root == None:
        return 0

    left = diameterOfBinaryTree(root.left, solution)
    right = diameterOfBinaryTree(root.right, solution)
    solution[0] = max(left + right, solution[0])
    return max(left, right) + 1

def diameterOfBinaryTree(root):
    solution = [0]
    diameterOfBinaryTreeHelper(root, solution)
    return solution[0]