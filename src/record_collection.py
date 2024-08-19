class RecordCollection:

    def __init__(self):
        self.records = []

    def add_record(self, title, artist):
        record = {"title": title, "artist": artist}
        self.records.append(record)
