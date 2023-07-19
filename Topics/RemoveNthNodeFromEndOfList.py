"""
    Given the head of a linked list, remove the nth node from the end of the list and return its head.
    
    Example:-

    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]

    Input: head = [1], n = 1
    Output: []

    Input: head = [1,2], n = 1
    Output: [1]

"""


def removeNthFromEnd(self, head, n):
    # Will use two pointer technique

    left = right = head
    for i in range(n):
        right = right.next

    if not right:
        return head.next

    while right.next:
        left = left.next
        right = right.next

    left.next = left.next.next
    return head
