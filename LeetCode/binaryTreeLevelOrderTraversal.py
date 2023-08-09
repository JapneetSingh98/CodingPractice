# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []

        output = []
        queue = [root, "end"]
        curLevel = []
        while len(queue) > 0:
            if queue[0] == "end":
                if len(queue) == 1:
                    output.append(curLevel)
                    return output
                else:
                    queue.append("end")
                output.append(curLevel)
                curLevel = []
                queue.pop(0)
            else:
                if queue[0].left != None:
                    queue.append(queue[0].left)
                if queue[0].right != None:
                    queue.append(queue[0].right)
                curLevel.append(queue.pop(0).val)