from linked_list import LinkedList

# Create a new linked list
ll = LinkedList()

# Insert elements at the end
print("Inserting elements at the end: 10, 20, 30, 40")
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.insert_at_end(40)

print("Linked List:")
ll.display()

# Insert at the beginning
print("\nInserting 5 at the beginning:")
ll.insert_at_beginning(5)
ll.display()

# Insert at a specific position
print("\nInserting 25 at position 3:")
ll.insert_at_position(25, 3)
ll.display()

# Get length
print(f"\nLength of linked list: {ll.get_length()}")

# Search for an element
print(f"\nSearching for 25: Found at position {ll.search(25)}")
print(f"Searching for 100: Found at position {ll.search(100)}")

# Delete at the beginning
print("\nDeleting element at the beginning:")
ll.delete_at_beginning()
ll.display()

# Delete at the end
print("\nDeleting element at the end:")
ll.delete_at_end()
ll.display()

# Delete at a specific position
print("\nDeleting element at position 2:")
ll.delete_at_position(2)
ll.display()

# Reverse the linked list
print("\nReversing the linked list:")
ll.reverse()
ll.display()

# Check if list is empty
print(f"\nIs the linked list empty? {ll.is_empty()}")

# Create another linked list and test edge cases
print("\n--- Testing Edge Cases ---")
ll2 = LinkedList()
print("Empty list:")
ll2.display()
print(f"Length of empty list: {ll2.get_length()}")
print(f"Is empty? {ll2.is_empty()}")

ll2.insert_at_end(100)
print("\nAfter inserting 100:")
ll2.display()
