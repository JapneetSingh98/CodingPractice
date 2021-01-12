# Your task is to complete this function
# function should return an integer denoting the required answer
def evalTree(root):
    # Code here
    if root.data == '+':
        return int(evalTree(root.left) + evalTree(root.right))
    elif root.data == '-':
        return int(evalTree(root.left) - evalTree(root.right))
    elif root.data == '*':
        return int(evalTree(root.left) * evalTree(root.right))
    elif root.data == '/':
        return int(evalTree(root.left) / evalTree(root.right))
    else:
        return int(root.data)




#{ 
#  Driver Code Starts
class node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

def isExp(s):
    if s=="+" or s=="-" or s=="*" or s=="/":
        return True
    return False

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = input().strip().split()
        q = []
        p = 0
        root = node(arr[p])
        q.append(root)
        p = 1
        while q!=[]:
            f = q.pop(0)
            if isExp(f.data):
                l = node(arr[p])
                p+=1
                r = node(arr[p])
                p+=1
                f.left = l
                f.right = r
                q.append(l)
                q.append(r)
            
        # inorder(root)
        # print ''
        print(evalTree(root))


# } Driver Code Ends