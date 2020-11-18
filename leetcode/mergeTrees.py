def mergeTrees(self, t1, t2):
    if t1 == None and t2 == None:
        return None
    if t1 == None:
        return t2
    if t2 == None:
        return t1
        
    node = TreeNode(t1.val + t2.val)
    node.left = self.mergeTrees(t1.left, t2.left)
    node.right = self.mergeTrees(t1.right, t2.right)
    return node