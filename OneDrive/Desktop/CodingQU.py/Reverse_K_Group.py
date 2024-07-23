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
def reverse_k_group(head, k):
    if not head or k == 1:
        return head

    # Step 1: Determine the length of the linked list
    length = 0
    current = head
    while current:
        length += 1
        current = current.next

    # Step 2: Initialize pointers
    dummy = Node(0)
    dummy.next = head
    prev_group_end = dummy

    while length >= k:
        current = prev_group_end.next
        next_group_start = current.next
        prev = prev_group_end
        for _ in range(k):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        next_node = prev_group_end.next
        prev_group_end.next = prev
        next_node.next = current
        prev_group_end = next_node

        length -= k

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

# Reverse the linked list in groups of 3
ll.head = reverse_k_group(ll.head, 3)

print("List After Reversing in Groups of 3:")
ll.print_list()
