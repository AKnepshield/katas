from src.record_collection import RecordCollection


def test_add_record():
    collection = RecordCollection()
    record = collection.add_record("The Smiths", "Louder Than Bombs")
    expected_record = {"artist": "The Smiths", "title": "Louder Than Bombs"}
    assert expected_record == record


def test_get_record_by_title():
    # Arrange
    collection = RecordCollection()
    collection.add_record("The Smiths", "Hatful Of Hollow")
    # Act
    retrieved_record = collection.get_record_by_title("Hatful Of Hollow")
    expected_record = {"artist": "The Smiths", "title": "Hatful Of Hollow"}
    # Assert
    assert retrieved_record == expected_record
