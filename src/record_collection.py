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

    def get_record_collection(self):
        return self.record_collection

    def remove_record_by_title(self, title):
        for record in self.record_collection:
            if record["title"] == title:
                self.record_collection.remove(record)
                return self.record_collection

    def count_records(self):
        return len(self.record_collection)

    def list_unique_artists(self):
        artists = set()
        for record in self.record_collection:
            artists.add(record["artist"])
        return list(artists)
