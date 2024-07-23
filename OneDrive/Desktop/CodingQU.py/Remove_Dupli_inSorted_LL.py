class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = Node(data)
    
    def remove_duplicates(self):
        current = self.head
        while current and current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Example usage:
ll = LinkedList()
ll.append(1)
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(3)
ll.append(4)
ll.append(4)
ll.append(4)
ll.append(5)
print("Original list:")
ll.print_list()  # Output: 1 -> 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 4 -> 5 -> None
ll.remove_duplicates()
print("List after removing duplicates:")
ll.print_list()  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> None
