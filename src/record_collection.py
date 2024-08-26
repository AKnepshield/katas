class RecordCollection:
    def __init__(self):
        self.record_collection = []

    def add_record(self, artist, title):
        record = {"artist": artist, "title": title}
        self.record_collection.append(record)
        return record
