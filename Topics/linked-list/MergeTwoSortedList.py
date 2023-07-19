"""
    Merge two sorted linked lists and return it as a sorted list. 
    The list should be made by splicing together the nodes of the first two lists.

    Example:-

    Input: l1 = [1,2,4], l2 = [1,3,4]
    Output: [1,1,2,3,4,4]

    Input: l1 = [], l2 = [0]
    Output: [0]

"""


def mergeTwoLists(self, l1, l2):
    dummy = ListNode()
    tail = dummy

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next

        tail = tail.next

    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2

    return dummy.next
