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
def detect_cycle_start(head):
    if not head:
        return None

    slow = head
    fast = head

    # Detect if there is a cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            # Cycle detected, find the cycle length
            cycle_length = find_cycle_length(slow)
            # Find the start of the cycle
            return find_cycle_start(head, cycle_length)

    return None

def find_cycle_length(meeting_point):
    current = meeting_point
    length = 0

    while True:
        current = current.next
        length += 1
        if current == meeting_point:
            break

    return length

def find_cycle_start(head, cycle_length):
    pointer1 = head
    pointer2 = head

    # Move pointer2 ahead by the length of the cycle
    for _ in range(cycle_length):
        pointer2 = pointer2.next

    # Move both pointers one step at a time until they meet
    while pointer1 != pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next

    return pointer1
# Create a linked list
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

# Introduce a cycle: 5 -> 3
head = ll.head
node1 = head.next
node2 = node1.next
node3 = node2.next
node4 = node3.next
node4.next = node2  # Creating the cycle

# Find the start of the cycle
cycle_start_node = detect_cycle_start(ll.head)
if cycle_start_node:
    print("Cycle starts at node with data:", cycle_start_node.data)  # Output: 3
else:
    print("No cycle detected.")

# Create another linked list without a cycle
ll2 = LinkedList()
ll2.append(1)
ll2.append(2)
ll2.append(3)
ll2.append(4)
ll2.append(5)

# Find the start of the cycle
cycle_start_node = detect_cycle_start(ll2.head)
if cycle_start_node:
    print("Cycle starts at node with data:", cycle_start_node.data)
else:
    print("No cycle detected.")  # Output: No cycle detected.
