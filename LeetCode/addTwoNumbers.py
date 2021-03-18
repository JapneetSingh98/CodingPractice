# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addHelper(self, l1: ListNode, l2: ListNode, carry):
        if (l1 == None and l2 == None):
            if (carry == 0):
                return None
            else:
                l1 = ListNode(carry, None)
                return l1
        
        elif (l1 == None):
            l1 = ListNode(l2.val, None)
            if (l1.val + carry > 9):
                l1.val = l1.val + carry - 10
                carry = 1
            else:
                l1.val = l1.val + carry
                carry = 0
            l1.next = self.addHelper(l1.next, l2.next, carry)
            return l1
        
        elif (l2 == None):
            if (l1.val + carry > 9):
                l1.val = l1.val + carry - 10
                carry = 1
            else:
                l1.val = l1.val + carry
                carry = 0
            l1.next = self.addHelper(l1.next, None, carry)
            return l1
        
        else:
            if (l1.val + l2.val + carry > 9):
                l1.val = l1.val + l2.val + carry - 10
                carry = 1
            else:
                l1.val = l1.val + l2.val + carry
                carry = 0
            l1.next = self.addHelper(l1.next, l2.next, carry)
            return l1
            
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.addHelper(l1, l2, 0)