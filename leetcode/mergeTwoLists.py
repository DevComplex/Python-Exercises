class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

def mergeTwoLists(l1, l2):
    if l1 == None and l2 == None:
        return None
    if l1 == None:
        return l2
    if l2 == None:
        return l1

    head = ListNode(0)

    curr = head

    while l1 or l2:
        if l1 and l2:
            if l1.val > l2.val:
                curr.next = l2
                l2 = l2.next
            else:
                curr.next = l1
                l1 = l1.next
        elif l1:
            curr.next = l1
            l1 = l1.next
        elif l2:
            curr.next = l2
            l2 = l2.next

        curr = curr.next

    return head.next

    