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

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def reverse(self):
        self.head = reverse_recursive(self.head)
def reverse_recursive(node):
    # Base case: if the list is empty or has only one node
    if node is None or node.next is None:
        return node

    # Recursive case: reverse the rest of the list
    new_head = reverse_recursive(node.next)

    # Reversing the pointers
    node.next.next = node
    node.next = None

    return new_head
# Create a linked list
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

print("Original List:")
ll.print_list()

# Reverse the linked list using recursion
ll.reverse()

print("Reversed List:")
ll.print_list()
