# integration_adapter.py

from core.engine import DependencyGraph
from grid_resilience.grid_nodes import GridNetwork, GridNode
from grid_resilience.failure_propagation import FailurePropagationEngine
from grid_resilience.resilience_engine import ResilienceEngine


class GridIntegrationAdapter:
    """
    Integration layer between:
    - Core dependency model
    - Grid simulation model
    - Failure propagation engine
    - Resilience analytics engine
    """

    def __init__(self):
        self.core_graph = DependencyGraph()
        self.grid_network = GridNetwork()
        self.failure_engine = FailurePropagationEngine(self.grid_network)
        self.resilience_engine = ResilienceEngine(self.grid_network)

    # ----------------------------
    # Map abstract system → physical grid nodes
    # ----------------------------
    def map_core_to_grid(self, core_nodes):
        for node in core_nodes:
            grid_node = GridNode(
                node_id=node["id"],
                node_type=node.get("type", "substation"),
                capacity_mw=node.get("capacity", 100)
            )
            self.grid_network.add_node(grid_node)

    # ----------------------------
    # Build dependency relationships
    # ----------------------------
    def build_dependencies(self, edges):
        for edge in edges:
            self.failure_engine.add_dependency(
                edge["from"],
                edge["to"]
            )

    # ----------------------------
    # Execute simulation scenario
    # ----------------------------
    def run_simulation(self, load_map, failure_start=None):
        """
        Executes a full deterministic scenario:
        1. Load application
        2. Optional failure propagation
        3. Resilience evaluation
        """

        # Step 1: Apply grid load conditions
        self.grid_network.simulate_load(load_map)

        # Step 2: Trigger cascading failure (if provided)
        if failure_start:
            self.failure_engine.simulate_failure_chain(failure_start)

        # Step 3: Return resilience analytics output
        return self.resilience_engine.system_health_report()
