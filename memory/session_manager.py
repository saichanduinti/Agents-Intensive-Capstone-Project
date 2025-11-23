class SessionManager:
    def __init__(self):
        self.state = {}
        self.history = []

    def update(self, key, value):
        self.state[key] = value
        self.history.append({"key": key, "value": value})

    def get(self, key):
        return self.state.get(key, None)

session_manager = SessionManager()
