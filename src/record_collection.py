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

    def remove_record(self, title):
        for record in self.record_collection:
            if record["title"] == title:
                self.record_collection.remove(record)
                return record

    def count_records(self):
        return len(self.record_collection)

    def list_unique_artists(self):
        artists = []
        for record in self.record_collection:
            if record["artist"] not in artists:
                artists.append(record["artist"])
        return artists
