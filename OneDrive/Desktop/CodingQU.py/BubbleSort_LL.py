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

def bubble_sort(head):
    if not head or not head.next:
        return

    swapped = True
    while swapped:
        current = head
        swapped = False
        while current.next:
            if current.data > current.next.data:
                # Swap data of current node and next node
                current.data, current.next.data = current.next.data, current.data
                swapped = True
            current = current.next

# Example usage
ll = LinkedList()
ll.append(5)
ll.append(3)
ll.append(8)
ll.append(4)
ll.append(2)

print("Original List:")
ll.print_list()

# Sort the linked list using bubble sort
bubble_sort(ll.head)

print("Sorted List:")
ll.print_list()
