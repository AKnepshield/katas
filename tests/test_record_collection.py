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


def test_get_record_collection():
    # Arrange
    collection = RecordCollection()
    collection.add_record("The Smiths", "Hatful Of Hollow")
    collection.add_record("The Smiths", "The Queen Is Dead")
    collection.add_record("The Smiths", "Strangeways, Here We Come")
    # Act
    record_collection = collection.get_record_collection()
    # Assert
    expected_collection = [
        {"artist": "The Smiths", "title": "Hatful Of Hollow"},
        {"artist": "The Smiths", "title": "The Queen Is Dead"},
        {"artist": "The Smiths", "title": "Strangeways, Here We Come"},
    ]
    assert expected_collection == record_collection


def test_remove_record_by_title():
    # Arrange
    collection = RecordCollection()
    collection.add_record("The Smiths", "Hatful Of Hollow")
    collection.add_record("The Smiths", "The Queen Is Dead")
    collection.add_record("The Smiths", "Strangeways, Here We Come")

    # Act
    record_to_remove = collection.remove_record_by_title("Hatful Of Hollow")
    current_collection = collection.get_record_collection()
    expected_removed_record = {"artist": "The Smiths", "title": "Hatful Of Hollow"}
    current_collection_without_record = [
        {"artist": "The Smiths", "title": "The Queen Is Dead"},
        {"artist": "The Smiths", "title": "Strangeways, Here We Come"},
    ]
    # Assert
    assert expected_removed_record == record_to_remove
    assert current_collection_without_record == current_collection
