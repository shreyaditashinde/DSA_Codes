class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create():
    x = int(input("Enter the Employee ID (-1 for no node): "))

    if x == -1:
        return None

    root = Node(x)

    print(f"Enter left of {x}")
    root.left = create()

    print(f"Enter right of {x}")
    root.right = create()

    return root


def postorder(temp):
    if temp is not None:
        postorder(temp.left)
        postorder(temp.right)
        print(temp.data, end=" ")


root = create()

print("\nPostorder Traversal:")
postorder(root)