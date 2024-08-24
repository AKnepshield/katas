from src.record_collection import RecordCollection


def test_add_record():
    collection = RecordCollection()

    record = collection.add_record("Background Music", "AN")

    expected_record = {"title": "Background Music", "artist": "AN"}

    assert expected_record == record
