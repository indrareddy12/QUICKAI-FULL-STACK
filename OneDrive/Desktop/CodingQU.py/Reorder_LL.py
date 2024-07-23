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
def reorder_list(head):
    if not head or not head.next:
        return head

    # Step 1: Find the middle of the linked list
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half of the list
    prev, curr = None, slow
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    # Step 3: Merge the two halves
    first, second = head, prev
    while second.next:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2

    return head
# Create a linked list
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

print("Original List:")
ll.print_list()

# Reorder the linked list
reorder_list(ll.head)

print("Reordered List:")
ll.print_list()
