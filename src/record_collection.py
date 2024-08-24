class RecordCollection:

    def __init__(self):
        self.record_collection = []

    def add_record(self, title, artist):
        record = {"title": title, "artist": artist}
        self.record_collection.append(record)
        return record

    def get_record_by_title(self, title):
        for record in self.record_collection:
            if record["title"] == title:
                return record
        return None

    def get_record_collection(self):
        return self.record_collection

    def remove_record_by_title(self, title):
        for record in self.record_collection:
            if record["title"] == title:
                self.record_collection.remove(record)
                return record
        return None
