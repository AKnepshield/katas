from src.record_collection import RecordCollection


def test_add_record():
    collection = RecordCollection()
    title = "Hear Nothing See Nothing Say Nothing"
    artist = "Discharge"
    collection.add_record(title, artist)
    assert len(collection.records) == 1
    record = collection.records[0]
    assert record["artist"] == artist
    assert record["title"] == title
