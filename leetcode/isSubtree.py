import hashlib

class TreeNode(object):
    self __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def hash(x):
    m = hashlib.sha256()
    m.update(str(x).encode('utf-8'))
    return m.hexdigest()

def merkle(n):
    if n == None:
        return "@"

    l = merkle(n.left)
    r = merkle(n.right)
    h = hash(l + str(n.val) + r)
    n.h = h
    return h

def dfs(s, t):
    if s == None:
        return False

    if s.h == t.h:
        return True

    return dfs(s.left, t) or dfs(s.right, t)

def isSubtree(s, t):
    merkle(s)
    merkle(t)

    return dfs(s, t)
