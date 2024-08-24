from src.record_collection import RecordCollection


def test_add_record():
    collection = RecordCollection()

    record = collection.add_record("Background Music", "AN")

    expected_record = {"title": "Background Music", "artist": "AN"}

    assert expected_record == record


def test_get_record_by_title():
    collection = RecordCollection()
    record = collection.add_record("Background Music", "AN")
    expected_record = {"title": "Background Music", "artist": "AN"}

    assert expected_record == record


def test_get_record_collection():
    collection = RecordCollection()
    collection.add_record("Walking Wires", "High Vis")
    collection.add_record("Blending", "High Vis")

    returned_collection = collection.get_record_collection()

    expected_collection = [
        {"title": "Walking Wires", "artist": "High Vis"},
        {"title": "Blending", "artist": "High Vis"},
    ]
