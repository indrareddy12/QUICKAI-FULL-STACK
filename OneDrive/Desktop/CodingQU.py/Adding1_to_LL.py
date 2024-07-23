class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def add_one_recursive(node):
    # Base case: if the node is None, return a carry of 1
    if not node:
        return 1

    # Recursively call the function for the next node
    carry = add_one_recursive(node.next)

    # Add the carry to the current node's value       
    new_val = node.val + carry
    node.val = new_val % 10
    carry = new_val // 10

    return carry

def add_one(head):
    # Call the recursive function starting from the head
    carry = add_one_recursive(head)

    # If there's a carry left after processing all nodes, add a new node at the front
    if carry:
        new_head = ListNode(carry)
        new_head.next = head
        head = new_head

    return head
def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

def create_list(numbers):
    if not numbers:
        return None
    head = ListNode(numbers[0])
    current = head
    for number in numbers[1:]:
        current.next = ListNode(number)
        current = current.next
    return head
# Create a linked list for the number 129 (stored as 1 -> 2 -> 9)
numbers = [1, 2, 9]
head = create_list(numbers)

print("Original list:")
print_list(head)

# Add 1 to the number represented by the linked list
head = add_one(head)

print("List after adding 1:")
print_list(head)
