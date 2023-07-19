"""
    Given the head of a singly linked list, reverse the list, and return the reversed list.

    Example:-

    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]

    Input: head = [1,2]
    Output: [2,1]

    Input: head = []
    Output: []

"""


def reverseList(self, head):
    # Iterative
    prev, curr = None, head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

    # Recursive
    if not head:
        return None

    newHead = head
    if head.next:
        newHead = self.reverseList(head.next)
        head.next.next = head
    head.next = None

    return newHead
