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
def is_palindrome(head):
    if not head or not head.next:
        return True

    # Step 1: Find the middle of the linked list
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half of the list
    prev = None
    curr = slow
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    # Step 3: Compare the two halves
    first_half = head
    second_half = prev
    while second_half:
        if first_half.data != second_half.data:
            return False
        first_half = first_half.next
        second_half = second_half.next

    return True
# Create a linked list
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(2)
ll.append(1)

print("Original List:")
ll.print_list()

# Check if the linked list is a palindrome
print("Is Palindrome:", is_palindrome(ll.head))
