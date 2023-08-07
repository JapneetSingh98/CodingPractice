class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        def findPathToLongest(node, ignore=None):
            # reached leaf
            if node.val == ignore:
                # print("hi")
                return []

            if node.left == None and node.right == None:
                return [node.val]

            # node only has right child
            elif node.left == None:
                path = findPathToLongest(node.right, ignore)
                path.append(node.val)
                return path

            # node only has left child
            elif node.right == None:
                path = findPathToLongest(node.left, ignore)
                path.append(node.val)
                return path

            # node has 2 children
            else:
                leftPath = findPathToLongest(node.left, ignore)
                leftPath.append(node.val)
                rightPath = findPathToLongest(node.right, ignore)
                rightPath.append(node.val)
                if len(leftPath) > len(rightPath):
                    return leftPath
                else:
                    return rightPath

        output = []
        longestPath = findPathToLongest(root)
        # print(longestPath)

        for query in queries:
            if query in longestPath:
                # print(findPathToLongest(root, query))
                output.append(len(findPathToLongest(root, query)) - 1)
            else:
                output.append(len(longestPath) - 1)

        return output