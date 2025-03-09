from temperature import Temperature

class Node:
    """
    Node class to be used in the linked list implementation of the stack.
    """
    def __init__(self, data):
        """Initialize a node with data and a pointer to the next node."""
        self.data = data
        self.next = None

class CircularStack:
    """
    Circular stack class using a linked list with a maximum size of 5 elements.
    """
    MAX_SIZE = 5

    def __init__(self):
        """Initialize the stack with an empty state."""
        self.top = None
        self.size = 0

    def push(self, temp_obj):
        """Add a new Temperature object to the stack, replacing the oldest entry if full."""
        new_node = Node(temp_obj)

        if self.is_empty():
            self.top = new_node
            new_node.next = self.top  # Circular reference
        elif self.size < self.MAX_SIZE:
            new_node.next = self.top.next
            self.top.next = new_node
            self.top = new_node
        else:  # Stack is full, replace the oldest
            new_node.next = self.top.next.next
            self.top.next = new_node
            self.top = new_node

        if self.size < self.MAX_SIZE:
            self.size += 1

    def pop(self):
        """Remove the oldest entry from the stack."""
        if self.is_empty():
            return None
        if self.size == 1:
            data = self.top.data
            self.top = None
            self.size = 0
            return data

        oldest = self.top.next
        self.top.next = oldest.next
        self.size -= 1
        return oldest.data

    def peek(self):
        """Return the most recent temperature entry without removing it."""
        return None if self.is_empty() else self.top.data

    def print_stack(self):
        """Print all stored readings in order from oldest to newest."""
        if self.is_empty():
            print("Stack is empty.")
            return

        current = self.top.next  # Oldest element
        for _ in range(self.size):
            print(current.data)
            current = current.next

    def is_empty(self):
        """Return True if the stack is empty, otherwise False."""
        return self.top is None