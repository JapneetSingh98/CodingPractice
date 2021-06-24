
# Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

# Ex.
# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]

def merge(l1, l2):                              # cur1      # cur2      # head       # current      # current.next
    cur1 = l1                                   # 1L
    cur2 = l2                                               # 1R

    if l1.val <= l2.val:
        head = l1                                                       # 1L
        cur1 = cur1.next                        # 2L
    else:
        head = l2
        cur2 = cur2.next
    
    current = head                                                                  # 1L            # 2L

    while cur1 != None or cur2 != None:
        if cur1.val <= cur2.val:
            current.next = cur1                 
            cur1 = cur1.next                    # 4L
            current = current.next                                                  # 2L
        else:
            current.next = cur2                                                                     # 1R
            cur2 = cur2.next                                # 3R
            current = current.next                                                  # 1R

    if cur1 == None:
        current.next = cur2
    else:
        current.next = cur1

    return head