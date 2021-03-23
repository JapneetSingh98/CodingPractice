# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        cur = head
        
        while cur != None:
            if cur.next == None:
                break
            else:
                temp = cur.next.val
                cur.next.val = cur.val
                cur.val = temp
                cur = cur.next.next
                
        return head