import networkx as nx
from task_1 import G


# DFS за допогою бібліотеки networkx
dfs_tree = nx.dfs_tree(G, source='A')
print(f"DFS tree: {list(dfs_tree.edges())}") 
print()

# BFS за допогою бібліотеки networkx
bfs_tree = nx.bfs_tree(G, source='A')
print(f"BFS tree: {list(bfs_tree.edges())}")  