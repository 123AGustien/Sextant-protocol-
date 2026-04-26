class FailurePropagationEngine:
    def __init__(self, network, log=None):
        self.network = network
        self.dependencies = {}  # A → B relationships
        self.log = log

    def add_dependency(self, from_node, to_node):
        if from_node not in self.dependencies:
            self.dependencies[from_node] = []
        self.dependencies[from_node].append(to_node)

    def trigger_failure(self, node_id):
        node = self.network.get_node(node_id)

        if node:
            node.fail()

            if self.log:
                self.log.record("FAIL", node_id, "Initial failure triggered")

            self._cascade(node_id)

    def _cascade(self, node_id):
        if node_id not in self.dependencies:
            return

        for dependent in self.dependencies[node_id]:
            dep_node = self.network.get_node(dependent)

            if dep_node and dep_node.status != "FAILED":
                dep_node.fail()

                if self.log:
                    self.log.record(
                        "CASCADE",
                        dependent,
                        f"Failed due to dependency from {node_id}"
                    )

                self._cascade(dependent)

    def simulate_failure_chain(self, start_node):
        if self.log:
            self.log.record("START", start_node, "Simulation started")

        self.trigger_failure(start_node)

        if self.log:
            self.log.record("END", start_node, "Simulation finished")
