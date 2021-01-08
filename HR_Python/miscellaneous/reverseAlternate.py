import math 
  
# Link list node  
class Node:  
    def __init__(self, data):  
        self.data = data  
        self.next = None
    
def pushFront(curHead, val):
    newHead = Node(val)
    newHead.next = curHead
    return newHead

def altReverse(node, k, rev):
    startOfTail = None
    if rev:
        stack = []
        curNode = node
        for i in range(k):
            startOfTail = curNode.next
            curNode.next = None
            stack.append(curNode)
            curNode = startOfTail
        startOfHead = stack[-1]
        curNode = startOfHead

        for i in range(k-1):
            del stack[-1]
            curNode.next = stack[-1]
            curNode = stack[-1]
        del stack[-1]
    else:
        startOfHead = node
        curNode = startOfHead
        for i in range(k-1):
            curNode = curNode.next
        startOfTail = curNode.next
    if startOfTail != None:
        curNode.next = altReverse(startOfTail, k, not rev)
    else:
        curNode.next = None
    return startOfHead

def printList(node):
    arr = []
    while node != None:
        arr.append(node.data)
        node = node.next
    print(arr)

if __name__ =='__main__':
    head = None

    n = int(input("How many numbers? "))

    head = None

    for i in range(n):
        prompt = "Number " + str(i+1) + ": "
        val = int(input(prompt))
        head = pushFront(head, val)

    k = int(input("What is k? "))

    printList(head)
    head = altReverse(head, k, True)
    printList(head)