""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
    return checkBSThelper(root, -float('inf'), float('inf'))
    
def checkBSThelper(root, min, max):
    if root.left == None and root.right == None:
        return True
    elif root.left == None:
        if root.right.data <= root.data or root.right.data > max:
            return False
        else:
            return checkBSThelper(root.right, root.data, max)
    elif root.right == None:
        if root.left.data >= root.data or root.left.data < min:
            return False
        else:
            return checkBSThelper(root.left, min, root.data)
    else:
        if root.right.data <= root.data or root.left.data >= root.data or root.right.data > max or root.left.data < min:
            return False
        else:
            return checkBSThelper(root.right, root.data, max) and checkBSThelper(root.left, min, root.data)
