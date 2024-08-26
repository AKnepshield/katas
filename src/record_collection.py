class RecordCollection:
    def __init__(self):
        self.record_collection = []

    def add_record(self, artist, title):
        record = {"artist": artist, "title": title}
        self.record_collection.append(record)
        return record

    def get_record_by_title(self, title):
        for record in self.record_collection:
            if record["title"] == title:
                return record
        return None
