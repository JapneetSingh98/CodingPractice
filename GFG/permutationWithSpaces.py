#User function Template for python3

class Solution:
    
    def helper (self, S, index, output):
        if index >= len(S):
            return output

        if S not in output:
            output.append(S)
        
        withSpace = S[0:index] + " " + S[index:]
        
        if withSpace not in output:
            output.append(withSpace)
            
        output = self.helper(S, index+1, output)
        output = self.helper(withSpace, index+2, output)
        return output
        
    def permutation (self, S):
        # code here
        index = 1
        output = [S]
        result = self.helper(S, index, output)
        result.sort()
        return result





#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        S = input()
        ans = ob.permutation(S);
        write = "";
        for i in ans:
            write += "(" + i + ")"
        print(write)


# } Driver Code Ends