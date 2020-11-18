class Solution(object):
    def rangeSumBSTHelper(self, n, low, high, total):
        if n == None:
            return
        
        if n.val >= low and n.val <= high:
            total[0] += n.val
            
        self.rangeSumBSTHelper(n.left, low, high, total)
        self.rangeSumBSTHelper(n.right, low, high, total)
    
    def rangeSumBST(self, root, low, high):
        if root == None:
            return 0
        
        total = [0]
        
        self.rangeSumBSTHelper(root, low, high, total)
        
        return total[0]