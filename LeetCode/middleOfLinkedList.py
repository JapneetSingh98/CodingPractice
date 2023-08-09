# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def helper(self, leader, middle, count):
        if leader.next == None:
            return middle
        if count % 2 == 0:
            return self.helper(leader.next, middle.next, count+1)
        else:
            return self.helper(leader.next, middle, count+1)

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.helper(head, head, 0)