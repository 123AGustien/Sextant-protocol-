
# core/engine.py

from core.dependency_graph import DependencyGraph

class SimulationEngine:
    """
    Deterministic execution engine for dependency-based system simulation.
    Designed for reproducible runs (sandbox-grade validation).
    """

    def __init__(self):
        self.graph = DependencyGraph()
        self.state_log = []

    def add_node(self, node):
        self.graph.add_node(node)

    def add_dependency(self, from_node, to_node):
        self.graph.add_dependency(from_node, to_node)

    def run_simulation(self, trigger_node):
        """
        Executes deterministic failure propagation simulation.
        """
        self.state_log = []

        visited = set()
        queue = [trigger_node]

        while queue:
            current = queue.pop(0)

            if current in visited:
                continue

            visited.add(current)

            node = self.graph.get_node(current)
            if node:
                node.state = "FAIL"
                self.state_log.append(f"{current} -> FAIL")

                for child in node.dependents:
                    queue.append(child.name)

        return {
            "status": "completed",
            "log": self.state_log
        }
