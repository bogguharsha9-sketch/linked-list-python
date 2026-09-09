class Node:
    """A node in the linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """A singly linked list implementation"""
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        """Insert a node at the beginning of the linked list"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_end(self, data):
        """Insert a node at the end of the linked list"""
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def insert_at_position(self, data, position):
        """Insert a node at a specific position (0-indexed)"""
        if position < 0:
            print("Position must be non-negative")
            return
        
        new_node = Node(data)
        
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        count = 0
        
        while current and count < position - 1:
            current = current.next
            count += 1
        
        if not current:
            print("Position out of range")
            return
        
        new_node.next = current.next
        current.next = new_node
    
    def delete_at_beginning(self):
        """Delete the node at the beginning"""
        if not self.head:
            print("List is empty")
            return
        
        self.head = self.head.next
    
    def delete_at_end(self):
        """Delete the node at the end"""
        if not self.head:
            print("List is empty")
            return
        
        if not self.head.next:
            self.head = None
            return
        
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None
    
    def delete_at_position(self, position):
        """Delete a node at a specific position (0-indexed)"""
        if position < 0 or not self.head:
            print("Invalid position or empty list")
            return
        
        if position == 0:
            self.head = self.head.next
            return
        
        current = self.head
        count = 0
        
        while current.next and count < position - 1:
            current = current.next
            count += 1
        
        if not current.next:
            print("Position out of range")
            return
        
        current.next = current.next.next
    
    def search(self, data):
        """Search for a node with specific data"""
        current = self.head
        position = 0
        
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        
        return -1
    
    def display(self):
        """Display all elements in the linked list"""
        elements = []
        current = self.head
        
        while current:
            elements.append(str(current.data))
            current = current.next
        
        if elements:
            print(" -> ".join(elements) + " -> None")
        else:
            print("None")
    
    def reverse(self):
        """Reverse the linked list"""
        prev = None
        current = self.head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev
    
    def get_length(self):
        """Get the length of the linked list"""
        count = 0
        current = self.head
        
        while current:
            count += 1
            current = current.next
        
        return count
    
    def is_empty(self):
        """Check if the linked list is empty"""
        return self.head is None
