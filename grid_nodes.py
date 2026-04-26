# grid_nodes.py

class GridNode:
    def __init__(self, node_id, node_type, capacity_mw):
        self.node_id = node_id
        self.node_type = node_type  # substation, transformer, feeder, renewable
        self.capacity_mw = capacity_mw
        self.status = "OK"
        self.load_mw = 0

    def apply_load(self, load):
        self.load_mw = load
        if self.load_mw > self.capacity_mw:
            self.status = "OVERLOADED"
        else:
            self.status = "OK"

    def fail(self):
        self.status = "FAILED"
        self.load_mw = 0


class GridNetwork:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node: GridNode):
        self.nodes[node.node_id] = node

    def get_node(self, node_id):
        return self.nodes.get(node_id)

    def simulate_load(self, load_map):
        for node_id, load in load_map.items():
            if node_id in self.nodes:
                self.nodes[node_id].apply_load(load)

    def failed_nodes(self):
        return [n for n in self.nodes.values() if n.status == "FAILED"]
