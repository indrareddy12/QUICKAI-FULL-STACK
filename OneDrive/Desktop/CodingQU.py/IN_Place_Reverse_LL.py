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
def reverse_in_place(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next  # Save next node
        curr.next = prev       # Reverse the current node's pointer
        prev = curr            # Move prev and curr one step forward
        curr = next_node
    return prev  # New head of the reversed list
# Create a linked list
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

print("Original List:")
ll.print_list()

# Reverse the linked list in place
ll.head = reverse_in_place(ll.head)

print("Reversed List:")
ll.print_list()
