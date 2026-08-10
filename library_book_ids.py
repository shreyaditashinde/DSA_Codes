# Case Study 3: Library Book ID

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at end
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Display Linked List
    def display(self):
        if self.head is None:
            print("Linked List is empty!")
            return
        temp = self.head
        print("Library Book IDs in Linked List:")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Example usage


library_books = LinkedList()

# Create linked list with B101, B102, B103
library_books.insert("B101")
library_books.insert("B102")
library_books.insert("B103")

# Insert B104 and B105
library_books.insert("B104")
library_books.insert("B105")

# Display final linked list
library_books.display()
