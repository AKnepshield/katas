from src.record_collection import RecordCollection


def test_add_record():
    # arrange
    collection = RecordCollection()
    # act
    record = collection.add_record("AN", "AN")
    # assert
    expected_record = {"title": "AN", "artist": "AN"}
    assert expected_record == record
