class RecordCollection:
    def __init__(self):
        self.records = []

    def add_record(self, title, artist):
        record = {"title": title, "artist": artist}
        self.records.append(record)
        return record

    def get_records(self):
        return self.records
