class Metrics:
    def __init__(self):
        self.rows_processed = 0
        self.errors = 0
        self.pipeline_time = 0.0

    def increment_rows(self, count):
        self.rows_processed += count

    def increment_errors(self):
        self.errors += 1

metrics = Metrics()
