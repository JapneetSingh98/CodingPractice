class Solution:
    def simplifyPath(self, path: str) -> str:
        pathArr = path.split('/')
        stack = []
        
        for item in pathArr:
            if item == '' or item == '.':
                continue
            elif item == '..':
                if len(stack) >= 1:
                    stack.pop(-1)
            else:
                stack.append(item)
            
            print(stack)
            
        if len(stack) == 0:
            return '/'
        
        output = ''
        for item in stack:
            output = output + '/' + item
            
        return output