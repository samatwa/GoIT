class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)

def find_min_value_node(root):
    current = root
    while current.left:
        current = current.left
    return current.val

def find_max_value_node(root):
    current = root
    while current.right:
        current = current.right
    return current.val

def calculate_sum_values(root):
    if root is None:
        return 0
    else:
        return root.val + calculate_sum_values(root.left) + calculate_sum_values(root.right)