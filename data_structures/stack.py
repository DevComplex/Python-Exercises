class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def top(self):
        return self.top.val if self.top else None

    def push(self, data):
        n = Node(data)

        if self.is_empty():
            self.top = n
        else:
            self.top.next = n
            n.prev = self.top
            self.top = n

        self.size += 1

    def pop(self):
        if self.is_empty():
            return None

        n_to_remove = self.top
        self.top = self.top.prev

        if self.top:
            self.top.next = None

        self.size -= 1

        return n_to_remove.data