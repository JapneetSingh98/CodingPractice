# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0

        def helper(curNode):
            nonlocal maxDiameter
            if curNode.left == None and curNode.right == None:
                return 0
            elif curNode.left == None:
                rightHeight = helper(curNode.right)
                if 1 + rightHeight > maxDiameter:
                    maxDiameter = 1 + rightHeight
                return 1 + rightHeight
            elif curNode.right == None:
                leftHeight = helper(curNode.left)
                if 1 + leftHeight > maxDiameter:
                    maxDiameter = 1 + leftHeight
                return 1 + leftHeight
            else:
                leftHeight = helper(curNode.left)
                rightHeight = helper(curNode.right)
                if 2 + leftHeight + rightHeight > maxDiameter:
                    maxDiameter = 2 + leftHeight + rightHeight
                return 1 + max(leftHeight, rightHeight)

        helper(root)
        return maxDiameter