class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create():
    x = int(input("Enter Ticket Number (-1 for no node): "))

    if x == -1:
        return None

    root = Node(x)

    print(f"Enter left of {x}")
    root.left = create()

    print(f"Enter right of {x}")
    root.right = create()

    return root


class Stack:
    def __init__(self):
        self.TOP = -1
        self.st = [0] * 100

    def push(self, x):
        self.TOP += 1
        self.st[self.TOP] = x

    def pop(self):
        x = self.st[self.TOP]
        self.TOP -= 1
        return x


def inorder(root):
    s = Stack()

    while root is not None or s.TOP != -1:

        while root is not None:
            s.push(root)
            root = root.left

        root = s.pop()
        print(root.data, end=" ")

        root = root.right


root = create()

print("\nTicket Numbers in Ascending Order:")
inorder(root)