# integration_adapter.py

from core.engine import DependencyGraph  # your existing system
from grid_resilience.grid_nodes import GridNetwork, GridNode
from grid_resilience.failure_propagation import FailurePropagationEngine
from grid_resilience.resilience_engine import ResilienceEngine


class GridIntegrationAdapter:
    def __init__(self):
        self.core_graph = DependencyGraph()
        self.grid_network = GridNetwork()
        self.failure_engine = FailurePropagationEngine(self.grid_network)
        self.resilience_engine = ResilienceEngine(self.grid_network)

    # ----------------------------
    # Map core nodes → grid nodes
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
    # Sync dependency graph → grid dependencies
    # ----------------------------
    def build_dependencies(self, edges):
        for edge in edges:
            self.failure_engine.add_dependency(
                edge["from"],
                edge["to"]
            )

    # ----------------------------
    # Run full simulation
    # ----------------------------
    def run_simulation(self, load_map, failure_start=None):
        # 1. Apply load
        self.grid_network.simulate_load(load_map)

        # 2. Trigger failure (if any)
        if failure_start:
            self.failure_engine.simulate_failure_chain(failure_start)

        # 3. Compute resilience
        return self.resilience_engine.system_health_report()
