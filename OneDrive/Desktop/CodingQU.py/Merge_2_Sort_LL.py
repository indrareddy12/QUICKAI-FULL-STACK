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
def merge_sorted_lists(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1

    # Determine the head of the merged list
    if l1.data < l2.data:
        merged_head = l1
        l1 = l1.next
    else:
        merged_head = l2
        l2 = l2.next

    # Use current to track the end of the merged list
    current = merged_head

    # Traverse both lists
    while l1 and l2:
        if l1.data < l2.data:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    # Append remaining nodes, if any
    if l1:
        current.next = l1
    if l2:
        current.next = l2

    return merged_head


# Create two sorted linked lists
ll1 = LinkedList()
ll1.append(1)
ll1.append(3)
ll1.append(5)

ll2 = LinkedList()
ll2.append(2)
ll2.append(4)
ll2.append(6)

# Print the original lists
print("List 1:")
ll1.print_list()

print("List 2:")
ll2.print_list()

# Merge the lists
merged_head = merge_sorted_lists(ll1.head, ll2.head)
merged_list = LinkedList()
merged_list.head = merged_head

# Print the merged list
print("Merged list:")
merged_list.print_list()
