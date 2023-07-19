"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:-
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Input: l1 = [0], l2 = [0]
Output: [0]

"""
def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    a = l1 
    b = l2 
    arr1 = []
    arr2 = []

    while a:
        arr1.append(a.val)
        a = a.next

    while b:
        arr2.append(b.val)
        b = b.next

    arr1.reverse()
    arr2.reverse()
        
    # Converting list to strings
    inta = int("".join(str(x) for x in arr1)) 
    intb = int("".join(str(x) for x in arr2))

    # Performing addition - the answer we wanted
    c = list(str(inta + intb))

    # Assign last digit to new ListNode which represents the head of returned LL
    head = l3 = ListNode(c.pop())

    c.reverse()

    # Traverse remaining digits, assigning each to new ListNode
    for i in c:
        l3.next = ListNode(i)
        l3 = l3.next

    return head 