
# core/dependency_graph.py

class Node:
    def __init__(self, name):
        self.name = name
        self.state = "OK"
        self.dependents = []


class DependencyGraph:
    """
    Represents system dependency relationships.
    """

    def __init__(self):
        self.nodes = {}

    def add_node(self, node_name):
        if node_name not in self.nodes:
            self.nodes[node_name] = Node(node_name)

    def add_dependency(self, from_node, to_node):
        self.add_node(from_node)
        self.add_node(to_node)

        self.nodes[from_node].dependents.append(self.nodes[to_node])

    def get_node(self, node_name):
        return self.nodes.get(node_name)

    def reset(self):
        for node in self.nodes.values():
            node.state = "OK"
