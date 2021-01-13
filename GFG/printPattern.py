#code

global output
output = []

def helper(N, curNum, reverse):
    output.append(curNum)
    if curNum == N and len(output) > 1:
        return output
    else:
        if reverse or curNum <= 0:
            reverse = True
            return helper(N, curNum+5, reverse)
        else:
            return helper(N, curNum-5, reverse)

if __name__=="__main__":
    t = int(input())
    for i in range(t):
        N = int(input())
        reverse = False
        output = []
        output = helper(N, N, reverse)
        op = ""
        for i in output:
            op = op + " " + str(i)
        print(op[1:])