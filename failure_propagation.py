# failure_propagation.py

class FailurePropagationEngine:
    def __init__(self, network):
        self.network = network
        self.dependencies = {}  # A → B relationships

    def add_dependency(self, from_node, to_node):
        if from_node not in self.dependencies:
            self.dependencies[from_node] = []
        self.dependencies[from_node].append(to_node)

    def trigger_failure(self, node_id):
        node = self.network.get_node(node_id)
        if node:
            node.fail()
            self._cascade(node_id)

    def _cascade(self, node_id):
        if node_id not in self.dependencies:
            return

        for dependent in self.dependencies[node_id]:
            dep_node = self.network.get_node(dependent)
            if dep_node and dep_node.status != "FAILED":
                dep_node.fail()
                self._cascade(dependent)

    def simulate_failure_chain(self, start_node):
        self.trigger_failure(start_node)
