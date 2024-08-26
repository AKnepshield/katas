from src.record_collection import RecordCollection


def test_add_record():
    collection = RecordCollection()
    record = collection.add_record("The Smiths", "Louder Than Bombs")
    expected_record = {"artist": "The Smiths", "title": "Louder Than Bombs"}
    assert expected_record == record
