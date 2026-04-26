
from grid_nodes import Node
from failure_propagation import FailurePropagationEngine
from resilience_engine import compute_resilience
from simulation.event_log import EventLog


class SimulationRunner:
    """
    Unified execution engine for Sextant Protocol.
    """

    def __init__(self):
        self.nodes = []
        self.log = EventLog()
        self.engine = None

    def load_nodes(self, nodes):
        self.nodes = nodes

    def trigger_event(self, root_node):
        """
        Start failure cascade from a single node.
        """
        if self.engine:
            self.engine.simulate_failure_chain(root_node)

    def evaluate_system(self):
        """
        Compute final system resilience after simulation.
        """
        return compute_resilience(self.nodes)

    def run(self, nodes, root_node):
        """
        SAFE ENTRY POINT (fixed + complete version)
        """

        # 1. Load nodes
        self.load_nodes(nodes)

        # 2. Build engine with logging
        self.engine = FailurePropagationEngine(
            network=self,
            log=self.log
        )

        # 3. Run simulation
        self.trigger_event(root_node)

        # 4. Evaluate result
        result = self.evaluate_system()

        # 5. Return full report
        return {
            "resilience": result,
            "events": self.log.get_all()
        }
