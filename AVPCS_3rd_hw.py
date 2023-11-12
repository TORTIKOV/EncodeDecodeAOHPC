import networkx as nx
import matplotlib.pyplot as plt

# Define the test examples with their respective edges
test_examples = [
    {
        'title': 'Test Example 3',
        'edges': [(1, 2), (2, 3), (3, 4), (4, 5), (1, 3), (1, 4), (1, 5), (2, 4), (2, 5), (3, 5)]
    },
    # Add more test examples in a similar format
    # ...

]

# Iterate through the test examples
for example in test_examples:
    title = example['title']
    edges = example['edges']

    # Create a graph using NetworkX
    G = nx.Graph()
    G.add_edges_from(edges)

    # Plot the original graph
    plt.figure(figsize=(8, 6))
    nx.draw(G, with_labels=True, font_weight='bold', node_color='lightblue', edge_color='gray', width=2)
    plt.title(f'{title} - Original Graph')
    plt.show()

    # Use Kruskal's algorithm to find the minimum spanning tree (acyclic)
    mst_kruskal = nx.minimum_spanning_tree(G, algorithm='kruskal')

    # Plot the acyclic tree using Kruskal's algorithm
    plt.figure(figsize=(8, 6))
    nx.draw(mst_kruskal, with_labels=True, font_weight='bold', node_color='lightgreen', edge_color='green', width=2)
    plt.title(f'{title} - Acyclic Tree (Kruskal)')
    plt.show()

    # Uncomment the below lines to visualize the acyclic tree using Prim's algorithm
    # mst_prim = nx.minimum_spanning_tree(G, algorithm='prim')
    # plt.figure(figsize=(8, 6))
    # nx.draw(mst_prim, with_labels=True, font_weight='bold', node_color='lightgreen', edge_color='green', width=2)
    # plt.title(f'{title} - Acyclic Tree (Prim)')
    # plt.show()
