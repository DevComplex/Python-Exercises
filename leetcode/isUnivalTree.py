def isUnivalTreeHelper(root, val):
    if root == None:
        return True
    if root.val != val:
        return False
    return isUnivalTreeHelper(root.left, val) and isUnivalTreeHelper(root.right, val)

def isUnivalTree(root):
    if root == None:
        return True
    return isUnivalTreeHelper(root, root.val)