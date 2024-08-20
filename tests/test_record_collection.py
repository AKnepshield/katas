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


def test_get_records():
    collection = RecordCollection()
    records = collection.get_records()
    assert records == []


def test_get_records_with_one_record():
    collection = RecordCollection()
    title = "Hear Nothing See Nothing Say Nothing"
    artist = "Discharge"
    record = collection.add_record(title, artist)
    records = collection.get_records()
    assert len(records) == 1
    assert records == [record]
