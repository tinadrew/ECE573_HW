#https://stackoverflow.com/questions/31186801/testing-weighted-quick-union-algorithm

class QuickUnion_Lazy:
    def __init__(self, nodes):
        self.array = [num for num in range(nodes)]

    # Follows parent pointers to actual root
    def root(self, parent):
        while parent != self.array[parent]:
            parent = self.array[parent]
        return parent

    # Joins two nodes into a component
    def union(self, first_node, second_node):
        self.array[first_node] = self.array[second_node]

    # Checks if two nodes are in the same component
    def connected(self, first_node, second_node):
        return self.root(first_node) == self.root(second_node)
