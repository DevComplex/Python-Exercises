class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head, val):
    if head == None:
        return None

    h = ListNode(0)
    prev = h
    h.next = curr
    curr = head

    while curr:
        if curr.val == val:
            prev.next = curr.next
        else:
            prev = curr

        curr = curr.next

    return h.next