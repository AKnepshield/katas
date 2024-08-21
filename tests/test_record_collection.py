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

    actual_record_collection = collection.get_records()

    record_collection_length = len(actual_record_collection)
    expected_record_collection = [{"title": title, "artist": artist}]
    assert record_collection_length == 1
    assert expected_record_collection == actual_record_collection


def test_get_record_with_title():
    collection = RecordCollection()
    title = "Hear Nothing See Nothing Say Nothing"
    artist = "Discharge"
    record = collection.add_record(title, artist)

    record_by_title = collection.get_record(title)

    assert record_by_title == record


def test_get_record_with_empty_collection():
    collection = RecordCollection()

    record = collection.get_record("test title")

    assert record == None
