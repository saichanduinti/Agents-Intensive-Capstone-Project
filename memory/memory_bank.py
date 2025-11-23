class MemoryBank:
    def __init__(self):
        self.records = []

    def store(self, key: str, value):
        self.records.append({"key": key, "value": value})

    def search(self, keyword: str):
        return [
            record for record in self.records
            if keyword.lower() in str(record["value"]).lower()
        ]

memory_bank = MemoryBank()
