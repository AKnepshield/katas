class RecordCollection:

    def __init__(self):
        self.record_collection = []

    def add_record(self, title, artist):
        record = {"title": title, "artist": artist}
        self.record_collection.append(record)
        return record
