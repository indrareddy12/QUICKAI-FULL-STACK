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
def rotate_list(head, k):
    if not head or k == 0:
        return head

    # Step 1: Find the length of the linked list
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1

    # Step 2: Connect the last node to the head to make it circular
    tail.next = head

    # Step 3: Find the new head and new tail
    k = k % length  # In case k is greater than the length of the list
    steps_to_new_head = length - k
    new_tail = head
    for _ in range(steps_to_new_head - 1):
        new_tail = new_tail.next
    new_head = new_tail.next

    # Step 4: Break the circular link
    new_tail.next = None

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

# Rotate the linked list by 2 positions
ll.head = rotate_list(ll.head, 2)

print("List After Rotation by 2 Positions:")
ll.print_list()
