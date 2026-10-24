from collections import deque

from original import Node, draw_tree, add_edges
# Функція для генерації кольорів від темного до світлого
def get_color_gradient(n):
    colors = []
    for i in range(n):
        intensity = int(255 * (i / n))
        color = f"#{intensity:02x}{intensity:02x}{240:02x}"
        colors.append(color)
    return colors

# Функція для збереження початкових кольорів вузлів дерева
def save_tree_colors(root):
    colors = {}
    def traverse(node):
        if node:
            colors[node.id] = node.color
            traverse(node.left)
            traverse(node.right)
    traverse(root)
    return colors

# Функція для відновлення початкових кольорів вузлів дерева
def restore_tree_colors(root, colors):
    def traverse(node):
        if node:
            node.color = colors[node.id]
            traverse(node.left)
            traverse(node.right)
    traverse(root)

# Функція для візуалізації обходу дерева
def visualize_tree_traversal(root, traversal_type):
    visited = set()
    order = []
    colors = []

    def dfs(node):
        if node:
            visited.add(node)
            order.append(node)
            colors.append(next(color_gen))
            draw_tree_step()
            dfs(node.left)
            dfs(node.right)

    def bfs(node):
        queue = deque([node])
        while queue:
            current = queue.popleft()
            if current and current not in visited:
                visited.add(current)
                order.append(current)
                colors.append(next(color_gen))
                draw_tree_step()
                queue.append(current.left)
                queue.append(current.right)

    # Функція для візуалізації кожного кроку обходу дерева
    def draw_tree_step():
        for idx, node in enumerate(order):
            node.color = colors[idx]
        draw_tree(root, title=f"{traversal_type.upper()} Step {len(order)}")

    # Генерація градієнту кольорів для кожного кроку обходу
    color_gen = iter(get_color_gradient(len([node for node in traverse_nodes(root)])))

    if traversal_type == "dfs":
        dfs(root)
    elif traversal_type == "bfs":
        bfs(root)
    else:
        raise ValueError("Invalid traversal type. Use 'dfs' or 'bfs'.")

# Функція для обходу всіх вузлів дерева
def traverse_nodes(root):
    if root:
        yield root
        yield from traverse_nodes(root.left)
        yield from traverse_nodes(root.right)