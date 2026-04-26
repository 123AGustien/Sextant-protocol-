from grid_nodes import Node
from failure_propagation import propagate_failure
from resilience_engine import compute_resilience


class SimulationRunner:
    """
    Unified execution engine for Sextant Protocol.
    """

    def __init__(self):
        self.nodes = []

    def load_nodes(self, nodes):
        self.nodes = nodes

    def trigger_event(self, root_node):
        """
        Start failure cascade from a single node.
        """
        propagate_failure(root_node)

    def evaluate_system(self):
        """
        Compute final system resilience after simulation.
        """
        return compute_resilience(self.nodes)

    def run(self, nodes, root_node):
        """
        SAFE ENTRY POINT (fixed version)
        """

        # Ensure system is loaded for consistency
        self.load_nodes(nodes)

        # Trigger cascade
        self.trigger_event(root_node)

        # Evaluate result
        return self.evaluate_system()
