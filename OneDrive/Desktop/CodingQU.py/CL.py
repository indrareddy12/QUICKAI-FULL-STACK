class CircularNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = CircularNode(data)
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = CircularNode(data)
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            new_node.next = self.head
            self.head = new_node
            current.next = self.head

    def delete(self, data):
        if self.is_empty():
            return

        current = self.head
        prev = None

        while True:
            if current.data == data:
                if prev is not None:
                    prev.next = current.next
                else:
                    if current.next == self.head:
                        self.head = None
                    else:
                        self.head = current.next
                        current_tail = self.head
                        while current_tail.next != current:
                            current_tail = current_tail.next
                        current_tail.next = self.head
                return

            prev = current
            current = current.next

            if current == self.head:
                break

    def __repr__(self):
        nodes = []
        if self.is_empty():
            return "List is empty"
        
        current = self.head
        while True:
            nodes.append(str(current.data))
            current = current.next
            if current == self.head:
                break
        return " -> ".join(nodes) + " -> (head)"



# Create a circular linked list
cll = CircularLinkedList()

# Append elements
cll.append(1)
cll.append(2)
cll.append(3)
cll.append(4)
print("List after appending 1, 2, 3, 4:", cll)  # Output: 1 -> 2 -> 3 -> 4 -> (head)

# Prepend an element
cll.prepend(0)
print("List after prepending 0:", cll)  # Output: 0 -> 1 -> 2 -> 3 -> 4 -> (head)

# Delete an element
cll.delete(3)
print("List after deleting 3:", cll)  # Output: 0 -> 1 -> 2 -> 4 -> (head)

# Delete the head
cll.delete(0)
print("List after deleting head (0):", cll)  # Output: 1 -> 2 -> 4 -> (head)

# Delete the tail
cll.delete(4)
print("List after deleting tail (4):", cll)  # Output: 1 -> 2 -> (head)

# Attempt to delete a non-existent element
cll.delete(5)
print("List after attempting to delete non-existent element (5):", cll)  # Output: 1 -> 2 -> (head)

# Delete the remaining elements
cll.delete(1)
cll.delete(2)
print("List after deleting all elements:", cll)  # Output: List is empty
