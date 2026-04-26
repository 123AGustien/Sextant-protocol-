class EventLog:
    """
simulsimulation/graph_view.py
    """

    def __init__(self):
        self.events = []

    def record(self, event_type, node_name, message, source=None):
        self.events.append({
            "type": event_type,
            "node": node_name,
            "message": message,
            "source": source
        })

    def get_all(self):
        return self.events

    def clear(self):
        self.events = []
