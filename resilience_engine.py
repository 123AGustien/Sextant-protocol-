# resilience_engine.py

class ResilienceEngine:
    def __init__(self, network):
        self.network = network

    def compute_stability_score(self):
        total = len(self.network.nodes)
        failed = len(self.network.failed_nodes())

        if total == 0:
            return 0

        score = (total - failed) / total
        return round(score, 4)

    def system_health_report(self):
        report = {
            "total_nodes": len(self.network.nodes),
            "failed_nodes": len(self.network.failed_nodes()),
            "stability_score": self.compute_stability_score()
        }
        return report

    def risk_level(self):
        score = self.compute_stability_score()

        if score > 0.8:
            return "LOW_RISK"
        elif score > 0.5:
            return "MEDIUM_RISK"
        else:
            return "HIGH_RISK"
