class DoublyNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return str(self.data)
    
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = DoublyNode(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend(self, data):
        new_node = DoublyNode(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, data):
        if self.is_empty():
            return

        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
                return
            current = current.next

    def find(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return " <-> ".join(nodes)
    
    
# Create a doubly linked list
dll = DoublyLinkedList()

# Append elements
dll.append(1)
dll.append(2)
dll.append(3)
print("Doubly list after appending 1, 2, 3:", dll)

# Prepend elements
dll.prepend(0)
print("Doubly list after prepending 0:", dll)

# Find elements
print("Find 2:", dll.find(2))
print("Find 4:", dll.find(4))

# Delete elements
dll.delete(2)
print("Doubly list after deleting 2:", dll)

# Check if list is empty
print("Is the doubly list empty?", dll.is_empty())

# Print the final list
print("Final doubly list:", dll)

