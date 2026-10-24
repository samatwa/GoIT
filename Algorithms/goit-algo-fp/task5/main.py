from original import Node, draw_tree, add_edges
from visual import visualize_tree_traversal, save_tree_colors, restore_tree_colors

def main():
    # Створення дерева
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    # Збереження початкового стану дерева
    original_colors = save_tree_colors(root)

    # Відображення початкового дерева
    draw_tree(root, title="Original Tree")

    # Візуалізація обходу у глибину
    visualize_tree_traversal(root, traversal_type="dfs")

    # Відновлення початкового стану дерева
    restore_tree_colors(root, original_colors)

    # Відображення дерева після відновлення
    draw_tree(root, title="Restored Original Tree")

    # Візуалізація обходу у ширину
    visualize_tree_traversal(root, traversal_type="bfs")

if __name__ == "__main__":
    main()