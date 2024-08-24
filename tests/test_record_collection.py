from src.record_collection import RecordCollection


def test_add_record():
    collection = RecordCollection()

    record = collection.add_record("Background Music", "AN")

    expected_record = {"title": "Background Music", "artist": "AN"}

    assert expected_record == record


def test_get_record_by_title():
    collection = RecordCollection()
    record = collection.add_record("Background Music", "AN")

    record = collection.get_record_by_title("Background Music")

    expected_record = {"title": "Background Music", "artist": "AN"}

    assert expected_record == record
