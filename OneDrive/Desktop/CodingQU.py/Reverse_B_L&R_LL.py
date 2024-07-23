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
def reverse_between(head, left, right):
    if not head or left == right:
        return head

    dummy = Node(0)
    dummy.next = head
    prev = dummy

    # Move prev to the node before the left position
    for _ in range(left - 1):
        prev = prev.next

    # Reverse the sublist
    curr = prev.next
    next_node = curr.next
    for _ in range(right - left):
        curr.next = next_node.next
        next_node.next = prev.next
        prev.next = next_node
        next_node = curr.next

    return dummy.next
# Create a linked list
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

print("Original List:")
ll.print_list()

# Reverse the sublist between positions 2 and 4
ll.head = reverse_between(ll.head, 2, 4)

print("List After Reversing Between Positions 2 and 4:")
ll.print_list()
