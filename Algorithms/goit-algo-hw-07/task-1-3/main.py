from node import Node, insert, calculate_sum_values, find_max_value_node, find_min_value_node


def main():

    # Test
    root = Node(5)
    root = insert(root, 3)
    root = insert(root, 8)
    root = insert(root, 4)
    root = insert(root, 1)
    root = insert(root, 6)
    root = insert(root, 10)
    root = insert(root, 26)
    root = insert(root, 12)
    root = insert(root, 48)
    root = insert(root, 0)

    minimum = find_min_value_node(root)
    print(f"The minimum value in the tree is {minimum}.")

    maximum = find_max_value_node(root)
    print(f"The maximum value in the tree is {maximum}.")

    sum_values = calculate_sum_values(root)
    print(f"The sum of values in the tree is {sum_values}.")


if __name__ == "__main__":
    main()
