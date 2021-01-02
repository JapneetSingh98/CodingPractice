""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
    return helper(root, float("-inf"), float("inf"))
        
def helper(node, low, high):
    leftSide = rightSide = True
    if node.data <= low or node.data >= high:
        return False
    if node.left == None and node.right == None:
        return True
    if node.left != None:
        leftSide = helper(node.left, low, node.data)
    if node.right != None:
        rightSide = helper(node.right, node.data, high)
        
    return (leftSide and rightSide)
