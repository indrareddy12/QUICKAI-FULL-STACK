class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTreeToDLL:
    def __init__(self):
        self.head = None
        self.prev = None

    def inorder_traversal(self, root):
        if root is None:
            return

        # Recursively convert the left subtree
        self.inorder_traversal(root.left)

        # Convert the current node
        if self.prev is None:
            # This condition is true for the leftmost node
            self.head = root
        else:
            # Adjust the pointers
            root.left = self.prev
            self.prev.right = root

        # Mark this node as previous for the next node
        self.prev = root

        # Recursively convert the right subtree
        self.inorder_traversal(root.right)

    def convert_to_dll(self, root):
        self.inorder_traversal(root)
        return self.head

# Helper function to print the DLL
def print_dll(head):
    current = head
    while current:
        print(current.value, end=" <-> " if current.right else "\n")
        current = current.right

# Example usage:
if __name__ == "__main__":
    # Create a binary tree
    root = Node(10)
    root.left = Node(12)
    root.right = Node(15)
    root.left.left = Node(25)
    root.left.right = Node(30)
    root.right.left = Node(36)

    # Convert to DLL
    converter = BinaryTreeToDLL()
    head = converter.convert_to_dll(root)

    # Print the DLL
    print_dll(head)
