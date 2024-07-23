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
def find_middle(head):
    if not head:
        return None

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow
# Create a linked list
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

# Print the linked list
ll.print_list()

# Find the middle element
middle_node = find_middle(ll.head)
if middle_node:
    print("The middle element is:", middle_node.data)  # Output: 3
else:
    print("The linked list is empty.")

# Create another linked list with an even number of elements
ll2 = LinkedList()
ll2.append(1)
ll2.append(2)
ll2.append(3)
ll2.append(4)
ll2.append(5)
ll2.append(6)

# Print the linked list
ll2.print_list()

# Find the middle element
middle_node = find_middle(ll2.head)
if middle_node:
    print("The middle element is:", middle_node.data)  # Output: 4
else:
    print("The linked list is empty.")
