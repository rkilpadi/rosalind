# Given: An int n and an adjacency list corresponding to a graph on n nodes with no cycles
# Return: The minimum number of edges that can be added to the graph to produce a tree
def min_edges(n, edges):
    # node with n nodes has n-1 edges
    return n - 1 - len(edges)


if __name__ == "__main__":
    with open('../data/rosalind_tree.txt', 'r') as data:
        lines = data.readlines()
        print(min_edges(int(lines.pop(0)), lines))
