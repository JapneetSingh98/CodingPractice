"""
Given the head of a singly linked list, group all the nodes with even indices together followed by the nodes with odd indices, and return the reordered list.


Note that the relative order inside both the even and odd groups should remain as it was in the input.


Example 1:
Input: head = [0, 1, 2, 3, 4]
Output: [0, 2, 4, 1, 3]
"""


def separate(l1):

    headEven = l1                                                           # 0, 2, 4 -> 1, 3
    backEven = headEven

    if l1 != None:
        l1 = l1.next   
    else:
        return headEven       

    headOdd = l1                                                            # 1, 3
    backOdd = headOdd
    if l1 != None:
        l1 = l1.next   
    else:
        return headEven   

    isEven = True
    while l1 != None:
        if isEven:
            backEven.next = newNode(l1.val)
            backEven = backEven.next
            l1 = l1.next
        else:
            backOdd.next = newNode(l1.val)
            backOdd = backOdd.next
            l1 = l1.next
        isEven = !isEven

    backEven.next = headOdd
    return headEven