class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def peek(self):
        return self.head.data if self.head else None

    def is_empty(self):
        return self.size == 0
    
    def enqueue(self, data):
        n = Node(data)

        if self.is_empty():
            self.head = self.tail = n
        else:
            n.prev = self.tail
            self.tail.next = n
            self.tail = n

        self.size += 1

    def dequeue(self):
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