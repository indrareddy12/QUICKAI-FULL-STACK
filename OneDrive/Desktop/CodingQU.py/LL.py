class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if self.is_empty():
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
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
        return " -> ".join(nodes)

# Example usage
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
print("List after appending 1, 2, 3:", ll)  # Output: 1 -> 2 -> 3

ll.prepend(0)
print("List after prepending 0:", ll)  # Output: 0 -> 1 -> 2 -> 3

print("Find 2:", ll.find(2))  # Output: True
print("Find 4:", ll.find(4))  # Output: False

ll.delete(2)
print("List after deleting 2:", ll)  # Output: 0 -> 1 -> 3

print("Is the list empty?", ll.is_empty())  # Output: False
print("Final list:", ll)  # Output: 0 -> 1 -> 3



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_recursive(self, head, data, position):
        if position == 0:
            new_node = Node(data)
            new_node.next = head
            return new_node
        if head is None:
            return None
        head.next = self.insert_recursive(head.next, data, position - 1)
        return head
    
    def insert(self, data, position):
        self.head = self.insert_recursive(self.head, data, position)
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Example usage:
ll = LinkedList()
ll.insert(1, 0)  # Insert 1 at position 0
ll.insert(2, 1)  # Insert 2 at position 1
ll.insert(3, 2)  # Insert 3 at position 2
ll.insert(4, 1)  # Insert 4 at position 1
ll.print_list()  # Output: 1 -> 4 -> 2 -> 3 -> None
