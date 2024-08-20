class RecordCollection:
    def __init__(self):
        self.records = []

    def add_record(self, title, artist):
        record = {"title": title, "artist": artist}
        collection = self.records.append(record)
        return collection
