class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def pop_left(self):
        if self.is_empty():
            return None

        n_to_remove = self.head

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

        self.size -= 1

        return n_to_remove.data

    def pop_right(self):
        if self.is_empty():
            return None

        n_to_remove = self.tail

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        self.size -= 1

        return n_to_remove.data

    def push_left(self, data):
        n = Node(data)

        if self.is_empty():
            self.head = self.tail = n
        else:
            self.head.prev = n
            n.next = self.head
            self.head = n

        self.size += 1

    def push_right(self, data):
        n = Node(data)

        if self.is_empty():
            self.head = self.tail = n
        else:
            self.tail.next = n
            n.prev = self.tail
            self.tail = n

        self.size += 1
