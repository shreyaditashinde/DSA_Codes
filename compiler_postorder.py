class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create():
    x = input("Enter node value (-1 for no node): ")

    if x == "-1":
        return None

    root = Node(x)

    print("Enter left of", x)
    root.left = create()

    print("Enter right of", x)
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


def postorder(root):
    if root is None:
        return

    s1 = Stack()
    s2 = Stack()

    s1.push(root)

    while s1.TOP != -1:
        temp = s1.pop()
        s2.push(temp)

        if temp.left is not None:
            s1.push(temp.left)

        if temp.right is not None:
            s1.push(temp.right)

    while s2.TOP != -1:
        print(s2.pop().data, end=" ")


root = create()

print("\nPostfix Expression:")
postorder(root)