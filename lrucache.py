class Node:
    def __init__(self, data):
        self.next = self.prev = None
        self.data = data

class LRUCache:
    def __init__(self, max_capacity, **kargs):
        self.head = self.tail = None
        self.memory = {}
        self.max_capacity = max_capacity
        self.current_size = 0

        if ("values" in kargs):
            for value in kargs["values"]:
                self.add(value)

    def __add_end(self, node):
        if self.head == None and self.tail == None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def __len__(self):
        return self.current_size

    def __remove(self, node):
        if node == self.head and node == self.tail:
            self.head = self.tail = None
        elif node == self.head:
            self.head = self.head.next
            self.head.prev = None
        elif node == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

    def add(self, data):
        key = data[0]

        if self.current_size == self.max_capacity:
            k, v = self.head.data
            del self.memory[k]
            self.__remove(self.head)
        elif key in self.memory:
            self.__remove(self.memory[key])
        else:
            self.current_size += 1

        new_node = Node(data)
        
        self.memory[key] = new_node

        self.__add_end(new_node)

    def get(self, key):
        if key not in self.memory:
            return None

        node = self.memory[key]
        k, v = node.data

        self.__remove(node)
        self.__add_end(node)

        return v

def main():
    VALUE_RANGE = (1, 100)
    CACHE_MAX_CAPACITY = 5

    values = [(i, i + 1) for i in range(*VALUE_RANGE)]
    cache = LRUCache(CACHE_MAX_CAPACITY, values=values)

    for i in range(*VALUE_RANGE):
        print(cache.get(i))

if __name__ == "__main__":
    main()