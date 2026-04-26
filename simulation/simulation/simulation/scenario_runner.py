
from grid_nodes import Node
from failure_propagation import propagate_failure
from resilience_engine import compute_resilience
from simulation.event_log import EventLog


class SimulationRunner:
    """
    Unified execution engine for Sextant Protocol.
    """

    def __init__(self):
        self.nodes = []
        self.log = EventLog()

    def load_nodes(self, nodes):
        self.nodes = nodes

    def trigger_event(self, root_node):
        """
        Start failure cascade from a single node.
        """
        self.log.record("TRIGGER", root_node.name, "Root failure triggered")
        propagate_failure(root_node)

    def evaluate_system(self):
        """
        Compute final system resilience after simulation.
        """
        score = compute_resilience(self.nodes)
        self.log.record("RESULT", "SYSTEM", f"Resilience score: {score}")
        return score

    def run(self, nodes, root_node):
        """
        SAFE ENTRY POINT
        """
        self.load_nodes(nodes)
        self.trigger_event(root_node)
        return self.evaluate_system()
