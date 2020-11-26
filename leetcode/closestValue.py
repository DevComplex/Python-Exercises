def closestValueHelper(n, target, solution):
    if n == None:
        return

    if abs(n.val - target) < abs(solution[0] - target):
        solution[0] = n.val

    if target > n.val:
        closestValueHelper(n.right, target, solution)
    else:
        closestValueHelper(n.left, target, solution)

def closestValue(root, target):
    if root == None:
        return None

    solution = [float('inf')]
    
    closestValueHelper(root, target, solution)

    return solution[0]
