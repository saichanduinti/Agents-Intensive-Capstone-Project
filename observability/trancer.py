import uuid
import datetime

class Tracer:
    def __init__(self):
        self.traces = []

    def trace(self, agent_name: str, action: str, metadata=None):
        record = {
            "id": str(uuid.uuid4()),
            "timestamp": datetime.datetime.now().isoformat(),
            "agent": agent_name,
            "action": action,
            "metadata": metadata or {}
        }
        self.traces.append(record)
        return record

tracer = Tracer()
