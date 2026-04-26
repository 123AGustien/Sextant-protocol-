class RiskEngine:
    """
    Calculates node criticality and system risk exposure.
    """

    def __init__(self, engine, log):
        self.engine = engine
        self.log = log

    def node_failure_impact(self, node_id):
        """
        Count how many nodes are affected if this node fails.
        """

        visited = set()
        stack = [node_id]

        while stack:
            current = stack.pop()

            if current in visited:
                continue

            visited.add(current)

            children = self.engine.dependencies.get(current, [])
            stack.extend(children)

        # exclude root node itself
        return len(visited) - 1

    def compute_risk_scores(self):
        """
        Assign risk score to each node.
        """

        scores = {}

        all_nodes = set(self.engine.dependencies.keys())

        for children in self.engine.dependencies.values():
            all_nodes.update(children)

        for node in all_nodes:
            scores[node] = self.node_failure_impact(node)

        return scores

    def most_critical_nodes(self, top_n=3):
        """
        Return highest risk nodes.
        """

        scores = self.compute_risk_scores()

        sorted_nodes = sorted(
            scores.items(),
            key=lambda x: x[1],
            reverse=True
        )

        return sorted_nodes[:top_n]
