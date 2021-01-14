"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def helper(head, visited):
    if head == None:
        return False
    if head in visited:
        return True
    visited.append(head)
    return helper(head.next, visited)

def has_cycle(head):
    visited = []
    return helper(head, visited)
    

