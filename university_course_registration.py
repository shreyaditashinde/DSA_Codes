# Case Study 16: University Course Registration
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

    # Delete a node by value
    def delete(self, data):
        if self.head is None:
            print("Course list is empty!")
            return
        if self.head.data == data:
            self.head = self.head.next
            print(f"Course {data} deleted successfully.")
            return
        temp = self.head
        while temp.next:
            if temp.next.data == data:
                temp.next = temp.next.next
                print(f"Course {data} deleted successfully.")
                return
            temp = temp.next
        print(f"Course {data} not found!")

    # Display Linked List
    def display(self):
        if self.head is None:
            print("Course list is empty!")
            return
        temp = self.head
        print("Courses in Linked List:")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Example usage


courses = LinkedList()

# Create linked list with Python → Java → C++ → AI
courses.insert("Python")
courses.insert("Java")
courses.insert("C++")
courses.insert("AI")

# Display initial courses
courses.display()

# Delete Java
courses.delete("Java")

# Insert Cloud Computing
courses.insert("Cloud Computing")

# Display updated course list
courses.display()
